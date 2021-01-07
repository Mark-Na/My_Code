package jsjf;
import jsjf.exceptions.*;

/**
 * CircularArrayQueue represents an array implementation of a queue in 
 * which the indexes for the front and rear of the queue circle back to 0
 * when they reach the end of the array.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class CircularArrayQueue<T> implements QueueADT<T>
{
	private final static int DEFAULT_CAPACITY = 100;
	private int front, rear, count;
	private T[] queue; 

	/**
	 * Creates an empty queue using the specified capacity.
	 * @param initialCapacity the initial size of the circular array queue
	 */
	@SuppressWarnings("unchecked")
	public CircularArrayQueue(int initialCapacity)
	{
		front = rear = count = 0;
		queue = (T[]) (new Object[initialCapacity]);
	}

	/**
	 * Creates an empty queue using the default capacity.
	 */
	public CircularArrayQueue()
	{
		this(DEFAULT_CAPACITY);
	}    

	/**
	 * Adds the specified element to the rear of this queue, expanding
	 * the capacity of the queue array if necessary.
	 * @param element the element to add to the rear of the queue
	 */
	public void enqueue(T element)
	{
		if (count == queue.length) 
			expandCapacity();

		queue[rear] = element;
		rear = (rear + 1) % queue.length;

		count++;
	}
	
	/**
	 * Adds an element to the front of the queue
	 */
	public void enqueueF(T element) 
	{
		if(count==queue.length)
			expandCapacity();
		
		if(front==0) 
		{
			front=queue.length-1;
		}
		else
		{
			front--;
		}
		queue[front]=element;		
		count++;
	}

	/**
	 * Creates a new array to store the contents of this queue with
	 * twice the capacity of the old one.
	 */
	private void expandCapacity()
	{
		@SuppressWarnings("unchecked")
		T[] larger = (T[]) (new Object[queue.length * 2]);

		for (int scan = 0; scan < count; scan++)
		{
			larger[scan] = queue[front];
			front = (front + 1) % queue.length;
		}

		front = 0;
		rear = count;
		queue = larger;
	}

	/**
	 * Removes the element at the front of this queue and returns a
	 * reference to it. 
	 * @return the element removed from the front of the queue
	 * @throws EmptyCollectionException  if the queue is empty
	 */
	public T dequeue() throws EmptyCollectionException
	{
		if (isEmpty())
			throw new EmptyCollectionException("queue");

		T result = queue[front];
		queue[front] = null;
		front = (front + 1) % queue.length;

		count--;

		return result;
	}
	
	public T dequeueB() throws EmptyCollectionException
	{
		if (isEmpty())
			throw new EmptyCollectionException("queue");

		T result = queue[rear];
		queue[rear]=null;
		if(rear==0) 
		{
			rear=queue.length-1;
		}
		else
		{
			rear--;
		}

		count--;

		return result;
	}
	/** 
	 * Returns a reference to the element at the front of this queue.
	 * The element is not removed from the queue.  
	 * @return the first element in the queue
	 * @throws EmptyCollectionException if the queue is empty
	 */
	public T first() throws EmptyCollectionException
	{
		if(count==0) {
			throw new EmptyCollectionException("nothing in the queue");
		}
		
		else
		{
			return queue[front];
		}
	}

	/**
	 * Returns true if this queue is empty and false otherwise.
	 * @return true if this queue is empty 
	 */
	public boolean isEmpty()
	{
		return(count==0);
	}

	/**
	 * Returns the number of elements currently in this queue.
	 * @return the size of the queue
	 */
	public int size()
	{
		return count;
	}

	/**
	 * Returns a string representation of this queue. 
	 * @return the string representation of the queue
	 */
	public String toString()
	{
		String str="";
		int x=front;
		for(int i=0;i<count;i++) {
			if(x==count) {//if x is at the last index of the array, I want it to go back to index 0 and go from there
				str+=queue[x]+" ";
				x=0;
			}
			else {
				str+=queue[x]+" ";
				x++;
			}
		}
		return str;
	}
	
	public static void main(String[] args) {
		CircularArrayQueue<Integer> queue = new CircularArrayQueue<Integer>(5);
		System.out.println("The queue is empty: "+queue.isEmpty());
		queue.enqueue(5);
		queue.enqueueF(2);
		queue.enqueue(5);
		queue.enqueueF(5);
		System.out.println("There are " + queue.size()+ " elements");
		System.out.println("The queue is: "+ queue.toString());
		queue.enqueue(5);
		queue.enqueue(5);
		System.out.println("There are " + queue.size()+ " elements");
		System.out.println("The queue is: "+ queue.toString());
		queue.dequeue();
		queue.dequeueB();
		System.out.println("There are " + queue.size()+ " elements");
		System.out.println("The queue is: "+ queue.toString());
		System.out.println("The queue is empty: "+queue.isEmpty());
		System.out.println("The first element is: "+queue.first());
	}
}
