package assignment1;

import java.util.Arrays;

public class Sorting 
{	
	private static int count;
	/**
	 * Sorts the specified array of integers using the selection
	 * sort algorithm.
	 *
	 * @param data the array to be sorted
	 */
	public static <T extends Comparable<T>> 
	void selectionSort(T[] data)
	{
		int min;
		T temp;
		count=0;

		for (int index = 0; index < data.length - 1; index++)
		{
			min = index;
			for (int scan = index + 1; scan < data.length; scan++) 
			{				
				count++;
				if (data[scan].compareTo(data[min]) < 0) 
				{
					min = scan;
				}
			}
			swap(data, min, index);
		}
	}

	/**
	 * Swaps to elements in an array. Used by various sorting algorithms.
	 * 
	 * @param data   the array in which the elements are swapped
	 * @param index1 the index of the first element to be swapped
	 * @param index2 the index of the second element to be swapped
	 */
	private static <T extends Comparable<T>> 
	void swap(T[] data, int index1, int index2)
	{
		T temp = data[index1];
		data[index1] = data[index2];
		data[index2] = temp;
	}

	/**
	 * Sorts the specified array of objects using an insertion
	 * sort algorithm.
	 *
	 * @param data the array to be sorted
	 */
	public static <T extends Comparable<T>> 
	void insertionSort(T[] data)
	{
		count=0;
		for (int index = 1; index < data.length; index++)
		{
			
			T key = data[index];
			int position = index;
			

			// shift larger values to the right 
			while (position > 0 && data[position-1].compareTo(key) > 0)
			{
				data[position] = data[position - 1];
				position--;
				count++;
				
			}

			data[position] = key;			
		}
	}

	/**
	 * Sorts the specified array of objects using a bubble sort
	 * algorithm.
	 *
	 * @param data the array to be sorted
	 */
	public static <T extends Comparable<T>> 
	void bubbleSort(T[] data)
	{
		int position, scan;
		count=0;

		for (position =  data.length - 1; position >= 0; position--)
		{
			for (scan = 0; scan <= position - 1; scan++)
			{
				count++;
				if (data[scan].compareTo(data[scan + 1]) > 0) 
				{
					
					swap(data, scan, scan + 1);
					
				}
			}
		}
	}

	/**
	 * Sorts the specified array of objects using the quick sort algorithm.
	 * 
	 * @param data the array to be sorted
	 */
	public static <T extends Comparable<T>> 
	void quickSort(T[] data)
	{
		count=0;
		quickSort(data, 0, data.length - 1);
	}

	/**
	 * Recursively sorts a range of objects in the specified array using the
	 * quick sort algorithm. 
	 * 
	 * @param data the array to be sorted
	 * @param min  the minimum index in the range to be sorted
	 * @param max  the maximum index in the range to be sorted
	 */
	private static <T extends Comparable<T>> 
	void quickSort(T[] data, int min, int max)
	{
		if (min < max)
		{
			// create partitions
			int indexofpartition = partition(data, min, max);
			// sort the left partition (lower values)
			quickSort(data, min, indexofpartition - 1);
			count++;
			// sort the right partition (higher values)
			quickSort(data, indexofpartition + 1, max);
			count++;
		}
	}

	/**
	 * Used by the quick sort algorithm to find the partition.
	 * 
	 * @param data the array to be sorted
	 * @param min  the minimum index in the range to be sorted
	 * @param max  the maximum index in the range to be sorted
	 */
	private static <T extends Comparable<T>> 
	int partition(T[] data, int min, int max)
	{
		
		T partitionelement;
		int left, right;
		int middle = (min + max) / 2;

		// use the middle data value as the partition element
		partitionelement = data[middle];
		
		// move it out of the way for now
		swap(data, middle, min);

		left = min;
		right = max;

		while (left < right)
		{
			
			// search for an element that is > the partition element
			while (left < right && data[left].compareTo(partitionelement) <= 0)
			{
				left++;
				count++;
			}

			// search for an element that is < the partition element
			while (data[right].compareTo(partitionelement) > 0) 
			{
				right--;
				count++;

			}

			// swap the elements
			if (left < right)
				swap(data, left, right);
			
		}

		// move the partition element into place
		swap(data, min, right);

		return right;
	}
	
	/**
	 * Sorts the specified array of objects using the merge sort
	 * algorithm.
	 *
	 * @param data the array to be sorted
	 */
	public static <T extends Comparable<T>>
	void mergeSort(T[] data)
	{
		count=0;
		mergeSort(data, 0, data.length - 1);
	}

	/**
	 * Recursively sorts a range of objects in the specified array using the
	 * merge sort algorithm.
	 *
	 * @param data the array to be sorted
	 * @param min  the index of the first element 
	 * @param max  the index of the last element
	 */
	private static <T extends Comparable<T>>
	void mergeSort(T[] data, int min, int max)
	{
		if (min < max)
		{
			int mid = (min + max) / 2;
			mergeSort(data, min, mid);
			mergeSort(data, mid+1, max);
			merge(data, min, mid, max);
		}
	}

	/**
	 * Merges two sorted subarrays of the specified array.
	 *
	 * @param data the array to be sorted
	 * @param first the beginning index of the first subarray 
	 * @param mid the ending index for the first subarray
	 * @param last the ending index of the second subarray
	 */
	@SuppressWarnings("unchecked")
	private static <T extends Comparable<T>>
	void merge(T[] data, int first, int mid, int last)
	{
		T[] temp = (T[])(new Comparable[data.length]);

		int first1 = first, last1 = mid;  // endpoints of first subarray
		int first2 = mid + 1, last2 = last;  // endpoints of second subarray
		int index = first1;  // next index open in temp array

		//  Copy smaller item from each subarray into temp until one
		//  of the subarrays is exhausted
		while (first1 <= last1 && first2 <= last2)
		{
			if (data[first1].compareTo(data[first2]) < 0)
			{
				temp[index] = data[first1];
				first1++;
				count++;
			}
			else
			{
				temp[index] = data[first2];
				first2++;
				count++;
			}
			index++;
			
		}

		//  Copy remaining elements from first subarray, if any
		while (first1 <= last1)
		{
			temp[index] = data[first1];
			first1++;
			index++;
			
		}

		//  Copy remaining elements from second subarray, if any
		while (first2 <= last2)
		{
			temp[index] = data[first2];
			first2++;
			index++;
			
		}

		//  Copy merged data into original array
		for (index = first; index <= last; index++)
			data[index] = temp[index];
	}
	
	public static int getCount() 
	{
		return count;
	}
	
	public static void main(String args[]) 
    { 
		Integer[] data1 = {1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
				20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
				30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 
				40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
				50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
				60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 
				70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 
				80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 
				90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 
				100};
		long startTime1 = System.nanoTime();//starts the timer
		selectionSort(data1);
		long endTime1 = System.nanoTime();//ends the timer
		long duration1= (endTime1 - startTime1);//finds the time it takes for the code to run
		
		for(int i=0;i<data1.length;i++)
			System.out.println(data1[i]);
		System.out.println(getCount());
		System.out.println(duration1);
		
		
		long startTime2 = System.nanoTime();
		insertionSort(Arrays.copyOf(data1, 100));
		long endTime2 = System.nanoTime();
		long duration2= (endTime2 - startTime2);		
		for(int i=0;i<Arrays.copyOf(data1, 100).length;i++)
			System.out.println(Arrays.copyOf(data1, 100)[i]);
		System.out.println(getCount());
		System.out.println(duration2);
		
		long startTime3 = System.nanoTime();
		bubbleSort(Arrays.copyOf(data1, 100));
		long endTime3 = System.nanoTime();
		long duration3= (endTime3 - startTime3);		
		for(int i=0;i<Arrays.copyOf(data1, 100).length;i++)
			System.out.println(Arrays.copyOf(data1,100)[i]);
		System.out.println(getCount());
		System.out.println(duration3);
		
		long startTime4 = System.nanoTime();
		quickSort(Arrays.copyOf(data1, 100));
		long endTime4 = System.nanoTime();
		long duration4= (endTime4 - startTime4);		
		for(int i=0;i<Arrays.copyOf(data1, 100).length;i++)
			System.out.println(Arrays.copyOf(data1, 100)[i]);
		System.out.println(getCount());
		System.out.println(duration4);
		
		long startTime5 = System.nanoTime();
		mergeSort(Arrays.copyOf(data1, 100));
		long endTime5 = System.nanoTime();
		long duration5= (endTime5 - startTime5);		
		for(int i=0;i<Arrays.copyOf(data1, 100).length;i++)
			System.out.println(Arrays.copyOf(data1, 100)[i]);
		System.out.println(getCount());
		System.out.println(duration5);
		
		Integer[] data2 = {5,2,4,6,1,3,2,6};
		long startTime6 = System.nanoTime();
		selectionSort(data2);
		long endTime6 = System.nanoTime();
		long duration6= (endTime6 - startTime6);
		
		for(int i=0;i<data2.length;i++)
			System.out.println(data2[i]);
		System.out.println(getCount());
		System.out.println(duration6);
		
		
		long startTime7 = System.nanoTime();
		insertionSort(Arrays.copyOf(data2, 8));
		long endTime7 = System.nanoTime();
		long duration7= (endTime7 - startTime7);		
		for(int i=0;i<Arrays.copyOf(data2, 8).length;i++)
			System.out.println(Arrays.copyOf(data2, 8)[i]);
		System.out.println(getCount());
		System.out.println(duration7);
		
		long startTime8 = System.nanoTime();
		bubbleSort(Arrays.copyOf(data2, 8));
		long endTime8 = System.nanoTime();
		long duration8= (endTime8 - startTime8);		
		for(int i=0;i<Arrays.copyOf(data2, 8).length;i++)
			System.out.println(Arrays.copyOf(data2, 8)[i]);
		System.out.println(getCount());
		System.out.println(duration8);
		
		long startTime9 = System.nanoTime();
		quickSort(Arrays.copyOf(data2, 8));
		long endTime9 = System.nanoTime();
		long duration9= (endTime9 - startTime9);		
		for(int i=0;i<Arrays.copyOf(data2, 8).length;i++)
			System.out.println(Arrays.copyOf(data2, 8)[i]);
		System.out.println(getCount());
		System.out.println(duration9);
		
		long startTime10 = System.nanoTime();
		mergeSort(Arrays.copyOf(data2, 8));
		long endTime10 = System.nanoTime();
		long duration10= (endTime10 - startTime10);		
		for(int i=0;i<Arrays.copyOf(data2, 8).length;i++)
			System.out.println(Arrays.copyOf(data2, 8)[i]);
		System.out.println(getCount());
		System.out.println(duration10);
		
		Integer[] data3 = {9,4,12,5,7,3,2,4,1,7,3,8,9,10,3,1,5,8,8,8,3,2,1};
		long startTime11 = System.nanoTime();
		selectionSort(data3);
		long endTime11 = System.nanoTime();
		long duration11= (endTime11 - startTime11);
		
		for(int i=0;i<data3.length;i++)
			System.out.println(data3[i]);
		System.out.println(getCount());
		System.out.println(duration11);
		
		
		long startTime12 = System.nanoTime();
		insertionSort(Arrays.copyOf(data3, 23));
		long endTime12 = System.nanoTime();
		long duration12= (endTime12 - startTime12);		
		for(int i=0;i<Arrays.copyOf(data3, 23).length;i++)
			System.out.println(Arrays.copyOf(data3, 23)[i]);
		System.out.println(getCount());
		System.out.println(duration12);
		
		long startTime13 = System.nanoTime();
		bubbleSort(Arrays.copyOf(data3, 23));
		long endTime13 = System.nanoTime();
		long duration13= (endTime13 - startTime13);		
		for(int i=0;i<Arrays.copyOf(data3, 23).length;i++)
			System.out.println(Arrays.copyOf(data3, 23)[i]);
		System.out.println(getCount());
		System.out.println(duration13);
		
		long startTime14 = System.nanoTime();
		quickSort(Arrays.copyOf(data3, 23));
		long endTime14 = System.nanoTime();
		long duration14= (endTime14 - startTime14);		
		for(int i=0;i<Arrays.copyOf(data3, 23).length;i++)
			System.out.println(Arrays.copyOf(data3, 23)[i]);
		System.out.println(getCount());
		System.out.println(duration14);
		
		long startTime15 = System.nanoTime();
		mergeSort(Arrays.copyOf(data3, 23));
		long endTime15 = System.nanoTime();
		long duration15= (endTime15 - startTime15);		
		for(int i=0;i<Arrays.copyOf(data3, 23).length;i++)
			System.out.println(Arrays.copyOf(data3, 23)[i]);
		System.out.println(getCount());
		System.out.println(duration15);
		
		Integer[] data4 = {1,2,3,4,5,6,7,8,9};
		long startTime16 = System.nanoTime();
		selectionSort(data4);
		long endTime16 = System.nanoTime();
		long duration16= (endTime16 - startTime16);
		
		for(int i=0;i<data4.length;i++)
			System.out.println(data4[i]);
		System.out.println(getCount());
		System.out.println(duration16);
		
		long startTime17 = System.nanoTime();
		insertionSort(Arrays.copyOf(data4, 9));
		long endTime17 = System.nanoTime();
		long duration17= (endTime17 - startTime17);		
		for(int i=0;i<Arrays.copyOf(data4, 9).length;i++)
			System.out.println(Arrays.copyOf(data4, 9)[i]);
		System.out.println(getCount());
		System.out.println(duration17);
		
		long startTime18 = System.nanoTime();
		bubbleSort(Arrays.copyOf(data4, 9));
		long endTime18 = System.nanoTime();
		long duration18= (endTime18 - startTime18);		
		for(int i=0;i<Arrays.copyOf(data4, 9).length;i++)
			System.out.println(Arrays.copyOf(data4, 9)[i]);
		System.out.println(getCount());
		System.out.println(duration18);
		
		long startTime19 = System.nanoTime();
		quickSort(Arrays.copyOf(data4, 9));
		long endTime19 = System.nanoTime();
		long duration19= (endTime19 - startTime19);		
		for(int i=0;i<Arrays.copyOf(data4, 9).length;i++)
			System.out.println(Arrays.copyOf(data4, 9)[i]);
		System.out.println(getCount());
		System.out.println(duration19);
		
		long startTime20 = System.nanoTime();
		mergeSort(Arrays.copyOf(data4, 9));
		long endTime20 = System.nanoTime();
		long duration20= (endTime20 - startTime20);		
		for(int i=0;i<Arrays.copyOf(data4, 9).length;i++)
			System.out.println(Arrays.copyOf(data4, 9)[i]);
		System.out.println(getCount());
		System.out.println(duration20);
	
		
		
		
    }

}
