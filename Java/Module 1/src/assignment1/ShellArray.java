package assignment1;
import java.util.Random;

public class ShellArray 
{
	private int gap;
	private static int [] values;
	
	public ShellArray(int size) 
	{
		Random rand = new Random();
		values = new int[size];
		gap = size/2;
		for(int i=0; i<size; i++) 
		{
			values[i]=rand.nextInt(10);
		}
		
	}
	//I had done a shell sort before in class so there are similarities(citing myself)
	public void ShellSort() 
	{
		int length = values.length;
		int i=0;
		int j=0;
		for (gap=length/2; gap > 0; gap /= 2) 
		{  
		  for (i = gap; i < length; i += 1) 
		  {
			  int temp = values[i]; 		                
		      for (j = i; j >= gap && values[j - gap] > temp; j -= gap)//sorting the sublists 
		    	  values[j] =values[j - gap]; 
		      values[j] = temp; 
		  } 
		  System.out.println(gap +" sublist(s):"+ toString());
		 } 
	} 
	
	public String toString()
	{
		String str ="";
		for(int i=0;i<values.length;i++)
		{
			str += values[i]+" ";
		}
		return str;
	}
	
	public static void main(String args[]) 
    { 
       ShellArray x = new ShellArray(9);
       System.out.println("This is the array to be sorted:"+ x.toString());
       x.ShellSort();
    }
	
	

}
