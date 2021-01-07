//***************************************************************************************************************************************************
//HeapSort.Java
//
//Mark Naguib T00651567
//COMP2231 Assignment 5 Question 1
//This application creates a heap and puts all the elements into an array and sorts it by looking at the parents and compares it to its children
//***************************************************************************************************************************************************
package jsjf;
import jsjf.ArrayHeap;

/**
 * HeapSort sorts a given array of Comparable objects using a heap.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class HeapSort<T>
{
	/**
	 * Sorts the specified array using a Heap
	 *
	 * @param data the data to be added to the heapsort
	 */
	public void heapSort(T[] data) 
	{
		ArrayHeap<T> heap = new ArrayHeap<T>();

		// copy the array into a heap 
		for (int i = 0; i < data.length; i++)
			heap.addElement(data[i]);
		
		int position1, scan1;
		//sorting the array by checking the parents compared to their children
		for (position1 =  data.length - 1; position1 > 0; position1--)
		{
			for (scan1 = 0; scan1 < position1-1; scan1++)
			{
				if((2*scan1+2)<=data.length)//to make sure the index does not go over the length
				{
					if ((((Integer) data[scan1]).compareTo((Integer) data[2*scan1+1]) > 0) ) //checks the left child
					{
					
						swap((Integer[]) data, scan1, 2*scan1 + 1);
					
					}
					if ((((Integer) data[scan1]).compareTo((Integer) data[2*scan1+2]) > 0)) //checks the right child
					{
					
						swap((Integer[]) data, scan1, 2*scan1 + 2);
					
					}
				}
			}
		}
		

		// place the sorted elements back into the array 
		int count = 0;
		while (!(heap.isEmpty()))
		{
			data[count] = heap.removeMin();
			count++;
		}
	}
	
	
	
	//from textbookJava Foundations Introduction to Program Design & Data Structures
	private static void swap(Integer[] data, int index1, int index2)
	{
		Integer temp = data[index1];
		data[index1]=data[index2];
		data[index2]=temp;
	}
	
	public static void main(String[] args) 
	 {
		Integer[] data = {34,45,3,87,65,32,1,12,17};
		HeapSort<Integer> heap = new HeapSort<Integer>();
		heap.heapSort(data);
		for(int i=0;i<data.length;i++)
		{
			System.out.println(data[i]);
		}
	 }
}