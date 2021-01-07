//***************************************************************************************************************************************************
//LinkedBinaryTree.Java
//
//Mark Naguib T00651567
//COMP2231 Assignment 4 Question 2
//This decision tree checks what role to play in a MOBA
//***************************************************************************************************************************************************
package jsjf;
import java.io.*;

public class RoleCheck {
	//asks questions to know what role is right for them in a MOBA 
	public static void main(String[] args) throws FileNotFoundException 
	{
		System.out.println("So, you want to play a MOBA.");

		DecisionTree expert = new DecisionTree("MOBA.txt");
		expert.evaluate();
		
	}

}
