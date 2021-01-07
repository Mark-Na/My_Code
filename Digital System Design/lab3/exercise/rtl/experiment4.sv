/*
Copyright by Henry Ko and Nicola Nicolici
Department of Electrical and Computer Engineering
McMaster University
Ontario, Canada
*/

`timescale 1ns/100ps
`ifndef DISABLE_DEFAULT_NET
`default_nettype none
`endif

module experiment4 (
		/////// board clocks                      ////////////
		input logic CLOCK_50_I,                   // 50 MHz clock

		/////// switches                          ////////////
		input logic[17:0] SWITCH_I,               // toggle switches

		/////// VGA interface                     ////////////
		output logic VGA_CLOCK_O,                 // VGA clock
		output logic VGA_HSYNC_O,                 // VGA H_SYNC
		output logic VGA_VSYNC_O,                 // VGA V_SYNC
		output logic VGA_BLANK_O,                 // VGA BLANK
		output logic VGA_SYNC_O,                  // VGA SYNC
		output logic[7:0] VGA_RED_O,              // VGA red
		output logic[7:0] VGA_GREEN_O,            // VGA green
		output logic[7:0] VGA_BLUE_O,              // VGA blue

		/////// PS2                               ////////////
		input logic PS2_DATA_I,                   // PS2 data
		input logic PS2_CLOCK_I                   // PS2 clock
);

`include "VGA_param.h"
parameter SCREEN_BORDER_OFFSET = 32;
parameter DEFAULT_MESSAGE_LINE = 280;
parameter DEFAULT_MESSAGE_START_COL = 360;
parameter KEYBOARD_MESSAGE_LINE = 320;
parameter KEYBOARD_MESSAGE_START_COL = 360;

logic resetn, enable;

logic [7:0] VGA_red, VGA_green, VGA_blue;
logic [9:0] pixel_X_pos;
logic [9:0] pixel_Y_pos;

logic [5:0] character_address;
logic rom_mux_output;

logic screen_border_on;

assign resetn = ~SWITCH_I[17];

logic [7:0] PS2_reg[14:0];
logic [7:0] PS2_code;
logic PS2_code_ready;
logic [3:0] data_counter;

logic PS2_code_ready_buf;
logic PS2_make_code;

logic [5:0]KEY;
logic [11:0]COUNTER;

// PS/2 controller
PS2_controller ps2_unit (
	.Clock_50(CLOCK_50_I),
	.Resetn(resetn),
	.PS2_clock(PS2_CLOCK_I),
	.PS2_data(PS2_DATA_I),
	.PS2_code(PS2_code),
	.PS2_code_ready(PS2_code_ready),
	.PS2_make_code(PS2_make_code)
);

// Putting the PS2 code into a register
always_ff @ (posedge CLOCK_50_I or negedge resetn) begin
	if (resetn == 1'b0) begin
		PS2_code_ready_buf <= 1'b0;
		data_counter <= 4'd0;
		PS2_reg[0]<= 8'd0;
		PS2_reg[1]<= 8'd0;
		PS2_reg[2]<= 8'd0;
		PS2_reg[3]<= 8'd0;
		PS2_reg[4]<= 8'd0;
		PS2_reg[5]<= 8'd0;
		PS2_reg[6]<= 8'd0;
		PS2_reg[7]<= 8'd0;
		PS2_reg[10]<= 8'd0;
		PS2_reg[11]<= 8'd0;
		PS2_reg[12]<= 8'd0;
		PS2_reg[13]<= 8'd0;
		PS2_reg[14]<= 8'd0;
	end else begin
		PS2_code_ready_buf <= PS2_code_ready;
		if (PS2_code_ready && ~PS2_code_ready_buf && PS2_make_code) begin
			if (data_counter < 4'd13) begin
				data_counter <= data_counter + 4'd1;
			end else begin
				data_counter <= 4'd0;
			end
			PS2_reg[14] <=PS2_reg[13];
			PS2_reg[13] <=PS2_reg[12];
			PS2_reg[12] <=PS2_reg[11];
			PS2_reg[11] <=PS2_reg[10];
			PS2_reg[10] <=PS2_reg[9];
			PS2_reg[9] <=PS2_reg[8];
			PS2_reg[8] <=PS2_reg[7];
			PS2_reg[7] <=PS2_reg[6];
			PS2_reg[6] <=PS2_reg[5];
			PS2_reg[5] <=PS2_reg[4];
			PS2_reg[4] <=PS2_reg[3];
			PS2_reg[3] <=PS2_reg[2];
			PS2_reg[2] <=PS2_reg[1];
			PS2_reg[1] <=PS2_reg[0];
			PS2_reg[0] <=PS2_code;
		end
	end
end


VGA_controller VGA_unit(
	.clock(CLOCK_50_I),
	.resetn(resetn),
	.enable(enable),

	.iRed(VGA_red),
	.iGreen(VGA_green),
	.iBlue(VGA_blue),
	.oCoord_X(pixel_X_pos),
	.oCoord_Y(pixel_Y_pos),
	
	// VGA Side
	.oVGA_R(VGA_RED_O),
	.oVGA_G(VGA_GREEN_O),
	.oVGA_B(VGA_BLUE_O),
	.oVGA_H_SYNC(VGA_HSYNC_O),
	.oVGA_V_SYNC(VGA_VSYNC_O),
	.oVGA_SYNC(VGA_SYNC_O),
	.oVGA_BLANK(VGA_BLANK_O)
);

logic [2:0] delay_X_pos;

always_ff @(posedge CLOCK_50_I or negedge resetn) begin
	if(!resetn) begin
		delay_X_pos[2:0] <= 3'd0;
	end else begin
		delay_X_pos[2:0] <= pixel_X_pos[2:0];
	end
end

// Character ROM
char_rom char_rom_unit (
	.Clock(CLOCK_50_I),
	.Character_address(character_address),
	.Font_row(pixel_Y_pos[2:0]),
	.Font_col(delay_X_pos[2:0]),
	.Rom_mux_output(rom_mux_output)
);

// this experiment is in the 800x600 @ 72 fps mode
assign enable = 1'b1;
assign VGA_CLOCK_O = ~CLOCK_50_I;

always_comb begin
	screen_border_on = 0;
	if (pixel_X_pos == SCREEN_BORDER_OFFSET || pixel_X_pos == H_SYNC_ACT-SCREEN_BORDER_OFFSET)
		if (pixel_Y_pos >= SCREEN_BORDER_OFFSET && pixel_Y_pos < V_SYNC_ACT-SCREEN_BORDER_OFFSET)
			screen_border_on = 1'b1;
	if (pixel_Y_pos == SCREEN_BORDER_OFFSET || pixel_Y_pos == V_SYNC_ACT-SCREEN_BORDER_OFFSET)
		if (pixel_X_pos >= SCREEN_BORDER_OFFSET && pixel_X_pos < H_SYNC_ACT-SCREEN_BORDER_OFFSET)
			screen_border_on = 1'b1;
end

// Display text
always_comb begin

	character_address = 6'o40; // Show space by default
	
	// 8 x 8 characters
	if (pixel_Y_pos[9:3] == ((DEFAULT_MESSAGE_LINE) >> 3) && COUNTER!=12'd0) begin
		// Reach the section where the text is displayed
		case (pixel_X_pos[9:3])
			(DEFAULT_MESSAGE_START_COL >> 3) +  0: character_address = 6'o13; // K
			(DEFAULT_MESSAGE_START_COL >> 3) +  1: character_address = 6'o05; // E
			(DEFAULT_MESSAGE_START_COL >> 3) +  2: character_address = 6'o31; // Y
			(DEFAULT_MESSAGE_START_COL >> 3) +  3: character_address = 6'o40; // space
			(DEFAULT_MESSAGE_START_COL >> 3) +  4: character_address = KEY; // KEY			
			(DEFAULT_MESSAGE_START_COL >> 3) +  5: character_address = 6'o40; // space
			(DEFAULT_MESSAGE_START_COL >> 3) +  6: character_address = 6'o20; // P
			(DEFAULT_MESSAGE_START_COL >> 3) +  7: character_address = 6'o22; // R
			(DEFAULT_MESSAGE_START_COL >> 3) +  8: character_address = 6'o05; // E
			(DEFAULT_MESSAGE_START_COL >> 3) +  9: character_address = 6'o23; // S
			(DEFAULT_MESSAGE_START_COL >> 3) + 10: character_address = 6'o23; // S		
			(DEFAULT_MESSAGE_START_COL >> 3) + 11: character_address = 6'o05; // E
			(DEFAULT_MESSAGE_START_COL >> 3) + 12: character_address = 6'o04; // D
			(DEFAULT_MESSAGE_START_COL >> 3) + 13: character_address = 6'o40; // space
			(DEFAULT_MESSAGE_START_COL >> 3) + 14: character_address = COUNTER [11:6]; // COUNTER [11:6]
			(DEFAULT_MESSAGE_START_COL >> 3) + 15: character_address = COUNTER [5:0]; // COUNTER [5:0]
			(DEFAULT_MESSAGE_START_COL >> 3) + 16: character_address = 6'o40; // space
			(DEFAULT_MESSAGE_START_COL >> 3) + 17: character_address = 6'o24; // T
			(DEFAULT_MESSAGE_START_COL >> 3) + 18: character_address = 6'o11; // I
			(DEFAULT_MESSAGE_START_COL >> 3) + 19: character_address = 6'o15; // M
			(DEFAULT_MESSAGE_START_COL >> 3) + 20: character_address = 6'o05; // E
			(DEFAULT_MESSAGE_START_COL >> 3) + 21: character_address = 6'o23; // S
			default: character_address = 6'o40; // space
		endcase
	end else if(pixel_Y_pos[9:3] == ((DEFAULT_MESSAGE_LINE) >> 3) && COUNTER ==12'd0) begin
		case (pixel_X_pos[9:3])
			(DEFAULT_MESSAGE_START_COL >> 3) +  0: character_address = 6'o16; // N 
			(DEFAULT_MESSAGE_START_COL >> 3) +  1: character_address = 6'o17; // O
			(DEFAULT_MESSAGE_START_COL >> 3) +  2: character_address = 6'o40; // space
			(DEFAULT_MESSAGE_START_COL >> 3) +  3: character_address = 6'o16; // N
			(DEFAULT_MESSAGE_START_COL >> 3) +  4: character_address = 6'o25; // U		
			(DEFAULT_MESSAGE_START_COL >> 3) +  5: character_address = 6'o15; // M
			(DEFAULT_MESSAGE_START_COL >> 3) +  6: character_address = 6'o40; // space
			(DEFAULT_MESSAGE_START_COL >> 3) +  7: character_address = 6'o13; // K
			(DEFAULT_MESSAGE_START_COL >> 3) +  8: character_address = 6'o05; // E
			(DEFAULT_MESSAGE_START_COL >> 3) +  9: character_address = 6'o31; // Y
			(DEFAULT_MESSAGE_START_COL >> 3) + 10: character_address = 6'o23; // S		
			(DEFAULT_MESSAGE_START_COL >> 3) + 11: character_address = 6'o40; // space
			(DEFAULT_MESSAGE_START_COL >> 3) + 12: character_address = 6'o20; // P
			(DEFAULT_MESSAGE_START_COL >> 3) + 13: character_address = 6'o22; // R
			(DEFAULT_MESSAGE_START_COL >> 3) + 14: character_address = 6'o05; // E
			(DEFAULT_MESSAGE_START_COL >> 3) + 15: character_address = 6'o23; // S
			(DEFAULT_MESSAGE_START_COL >> 3) + 16: character_address = 6'o23; // S
			(DEFAULT_MESSAGE_START_COL >> 3) + 17: character_address = 6'o05; // E
			(DEFAULT_MESSAGE_START_COL >> 3) + 18: character_address = 6'o04; // D
			default: character_address = 6'o40; // space
		endcase
	end

	// 8 x 8 characters
	if (pixel_Y_pos[9:3] == ((KEYBOARD_MESSAGE_LINE) >> 3)) begin
		// Reach the section where the text is displayed
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+14) begin
			case (PS2_reg[0])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+13) begin
			case (PS2_reg[1])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+12) begin
			case (PS2_reg[2])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+11) begin
			case (PS2_reg[3])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+10) begin
			case (PS2_reg[4])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+9) begin
			case (PS2_reg[5])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+8) begin
			case (PS2_reg[6])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+7) begin
			case (PS2_reg[7])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+6) begin
			case (PS2_reg[8])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+5) begin
			case (PS2_reg[9])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+4) begin
			case (PS2_reg[10])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+3) begin
			case (PS2_reg[11])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+2) begin
			case (PS2_reg[12])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+1) begin
			case (PS2_reg[13])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end 	
		if (pixel_X_pos[9:3] == (KEYBOARD_MESSAGE_START_COL >> 3)+0) begin
			case (PS2_reg[14])
				8'h45:   character_address = 6'o60; // 0
				8'h16:   character_address = 6'o61; // 1
				8'h1E:   character_address = 6'o62; // 2
				8'h26:   character_address = 6'o63; // 3
				8'h25:   character_address = 6'o64; // 4
				8'h2E:   character_address = 6'o65; // 5
				8'h36:   character_address = 6'o66; // 6
				8'h3D:   character_address = 6'o67; // 7
				8'h3E:   character_address = 6'o70; // 8
				8'h46:   character_address = 6'o71; // 9
				default: character_address = 6'o40; // space
			endcase
		end		
	end
end

//KEY AND COUNTER
always_comb begin
	logic [3:0] c,c0,c1,c2,c3,c4,c5,c6,c7,c8,c9;
	c0=4'd0;
	c1=4'd0;
	c2=4'd0;
	c3=4'd0;
	c4=4'd0;
	c5=4'd0;
	c6=4'd0;
	c7=4'd0;
	c8=4'd0;
	c9=4'd0;
	for(int i=0;i<15;i=i+1)begin
		if(PS2_reg[i]==8'h46) begin
			c9 = c9+4'd1;
		end else if(PS2_reg[i]==8'h3E) begin
			c8 = c8+4'd1;
		end else if(PS2_reg[i]==8'h3D) begin
			c7 = c7+4'd1;
		end else if(PS2_reg[i]==8'h36) begin
			c6 = c6+4'd1;
		end else if(PS2_reg[i]==8'h2E) begin
			c5 = c5+4'd1;
		end else if(PS2_reg[i]==8'h25) begin
			c4 = c4+4'd1;
		end else if(PS2_reg[i]==8'h26) begin
			c3 = c3+4'd1;
		end else if(PS2_reg[i]==8'h1E) begin
			c2 = c2+4'd1;
		end else if(PS2_reg[i]==8'h16) begin
			c1 = c1+4'd1;
		end else if(PS2_reg[i]==8'h45) begin
			c0 = c0+4'd1;
		end
	end
	if(c9>=c8 && c9 >=c7 && c9>=c6 && c9>=c5&& c9>=c4&& c9>=c3&& c9>=c2&& c9>=c1&& c9>=c0) begin
		c=c9;
		KEY=6'o71;
	end else if(c8 >=c7 && c8>=c6 && c8>=c5&& c8>=c4&& c8>=c3&& c8>=c2&& c8>=c1&& c8>=c0)begin
		c=c8;
		KEY=6'o70;
	end else if(c7>=c6 && c7>=c5&& c7>=c4&& c7>=c3&& c7>=c2&& c7>=c1&& c7>=c0)begin
		c=c7;
		KEY=6'o67;
	end else if(c6>=c5&& c6>=c4&& c6>=c3&& c6>=c2&& c6>=c1&& c6>=c0)begin
		c=c6;
		KEY=6'o66;
	end else if(c5>=c4&& c5>=c3&& c5>=c2&& c5>=c1&& c5>=c0)begin
		c=c5;
		KEY=6'o65;
	end else if(c4>=c3&& c4>=c2&& c4>=c1&& c4>=c0)begin
		c=c4;
		KEY=6'o64;
	end else if(c3>=c2&& c3>=c1&& c3>=c0)begin
		c=c3;
		KEY=6'o63;
	end else if(c2>=c1&& c2>=c0)begin
		c=c2;
		KEY=6'o62;
	end else if(c1>=c0)begin
		c=c1;
		KEY=6'o61;
	end else begin
		c = c0;
		KEY = 6'o60;
	end
	
	case(c)
		1: COUNTER={6'o40,6'o61};   //1
		2: COUNTER={6'o40,6'o62};   //2
		3: COUNTER={6'o40,6'o63};   //3
		4: COUNTER={6'o40,6'o64};   //4
		5: COUNTER={6'o40,6'o65};   //5
		6: COUNTER={6'o40,6'o66};   //6
		7: COUNTER={6'o40,6'o67};   //7
		8: COUNTER={6'o40,6'o70};   //8
		9: COUNTER={6'o40,6'o71};   //9
		10: COUNTER={6'o61,6'o60};  //10
		11: COUNTER={6'o61,6'o61};  //11
		12: COUNTER={6'o61,6'o62};  //12
		13: COUNTER={6'o61,6'o63};  //13
		14: COUNTER={6'o61,6'o64};  //14
		15: COUNTER={6'o61,6'o65};  //15
		default: COUNTER=12'd0;
	endcase
end


// RGB signals
always_comb begin
		VGA_red = 8'h00;
		VGA_green = 8'h00;
		VGA_blue = 8'h00;

		if (screen_border_on) begin
			// blue border
			VGA_blue = 8'hFF;
		end
		
		if (rom_mux_output) begin
			// yellow text
			VGA_red = 8'hFF;
			VGA_green = 8'hFF;
		end
end

endmodule

