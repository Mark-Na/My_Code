//***************************************************************************************************************************************************
//HashTable.Java
//
//Mark Naguib T00651567
//COMP2231 Assignment 5 Question 3
//This application creates a hash table and tests most of the functions involved
//***************************************************************************************************************************************************
package jsjf;
import java.lang.Math;
import java.util.Arrays;

public class HashTable {
	private Integer[] table;
    private int size;
    private int keys;
    private double maxLoad;
    
    //referenced previous code that I had written before
    public HashTable()
    {
    	maxLoad = 0.8;
    	size = 31;
    	table = new Integer[size] ;
    	keys=0;
    }
    
    public void remove(Integer key) 
    {
    	Integer temp=-1;
    	
    	if(keys>0) 
    	{
    		for(int i=0;i<size;i++)
    		{
    			if(table[i].equals(key))
    			{
    				temp = table[i];
    				table[i]=null;
    				keys--;
    				return;
    			}
            
           
    		}
    		if (temp==-1)
    		{
    			System.out.println("key not in here");
    			return;
    		}

    	}
    	
    	
    }
    
    public void insert(String n)
    {
      int num = Integer.parseInt(n);
      int temp = Math.abs(num)%10000;
      int index = temp%size;
      if(table[index]==null)
      {
    	  table[index]=num;
    	  keys++;
    	  if(keys>size)
    		  resize();
    	  
      }
      
      else
      {
    	  rehash(n);
      }
    }
    // if the index is full the program tries the 
    protected void rehash(String n)
    {
    	String str = "";
    	String str1="";
    	for(int i=0; i<3; i++)
    	{
    		str += n.charAt(i);
    	}
    	for(int j=0; j<n.length(); j++)
    	{
    		str1 += n.charAt(j);
    	}
    	
    	int num = Integer.parseInt(str);
    	int element = Integer.parseInt(str1) ;
    	int index = num%size;
    	int indexF=0;
    	if(table[index]==null)
    	{
    		table[index]=num;
    		keys++;
    	}
    	else
    	{
    		boolean flag = true;
    		int j = 2;
    		while(flag)
    		{
    			indexF = index+j*index;
    			if(table[indexF]!=null)
    				j++;
    			else 
    			{
    				table[indexF]=element;
    				keys++;
    				break;
    			}
    		}
    	}
    }
    
    protected void resize()
    {
    	size = nextPrime(size);
    	table = Arrays.copyOf(table, size);//creates a new array of size the next prime number
    	return;
    }
    
    public double getLoad()
    {
        return (keys/size);
    }
    
    //referenced https://stackoverflow.com/questions/47407251/optimal-way-to-find-next-prime-number-java
    //parameter is put in and function returns the next prime after it
    public int nextPrime(int input){
    	  int counter;
    	  input++;   
    	  while(true){
    	    counter = 0;
    	    for(int i = 2; i <= Math.sqrt(input); i ++){
    	      if(input % i == 0)  counter++;
    	    }
    	    if(counter == 0)
    	      return input;
    	    else{
    	      input++;
    	      continue;
    	    }
    	  }
    	}
    
    public void printKeysAndIndexes()
    {
        for(int x=0;x<this.size;x++)
        {
        	if(table[x]!=null)
                {
                    System.out.println("The element: "+table[x]+ " is at index: "+ x);
                }
        }
    }
    
    public static void main(String[] args) 
	 {
    	HashTable table = new HashTable();
    	table.insert("123456789");
    	table.insert("123456799");
    	table.insert("123456798");
    	table.printKeysAndIndexes();
    	System.out.println("The table's current load is: "+table.getLoad());
        table.remove(123456789);
    	table.printKeysAndIndexes();
    	
	 }
}
