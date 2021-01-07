import java.util.ArrayList;

/**
 * Represents a queue using an array list
 */

public class QueueArrayList<T> implements QueueADT<T> {
	private ArrayList<T> queue;
	private int front;
	private int back;
	
	/**
	 * Creates an empty array list
	 */
	
	QueueArrayList()
	{
		queue = new ArrayList<T>();
		front=0;
		back=0;
	}
	
	/**
	 * Adds an element to the back in FIFO manner
	 * @param element the number to be added to the back of the list
	 */
	
	public void enqueue(T element)
	{
		queue.add(back, element);
		back++;
	}
	
	/**
	 * Removes the first element from the front of the list
	 */
	
	public T dequeue()
	{		
		back--;
		return queue.remove(front);
	}
	
	/**
	 * Returns the first element of the queue(the front) without removing it
	 * @return the first element of the queue without removing it
	 */
	
	public T first()
	{
		return queue.get(front);
	}
	
	/**
	 * Returns the boolean value if the queue is empty(no elements in it)
	 * @return the boolean value if the stack is empty or not
	 */
	
	public boolean isEmpty()
	{
		return queue.isEmpty();
	}
	
	/**
	 * Returns the current number of elements in the queue
	 * @return the number of elements of the queue
	 */
	
	public  int size()
	{
		return queue.size();
	}
	
	/**
	 * Returns the string representation of the queue
	 * @return the string representation of the queue
	 */
	
	public String toString()
	{
		String s="";
		for(int i=front;i<queue.size();i++)
			s+=queue.get(i) + " ";
		return s;
	}
	public static void main(String[] args) {
		QueueArrayList<Integer> queue = new QueueArrayList<Integer>();
		System.out.println("The queue is empty: "+queue.isEmpty());
		queue.enqueue(5);
		queue.enqueue(2);
		queue.enqueue(5);
		queue.enqueue(5);
		System.out.println("There are "+queue.size()+" elements in the queue");
		System.out.println("The queue is: "+queue.toString());
		queue.enqueue(5);
		queue.enqueue(5);
		System.out.println("There are "+queue.size()+" elements in the queue");
		System.out.println("The queue is: "+queue.toString());
		queue.dequeue();
		queue.dequeue();
		System.out.println("There are "+queue.size()+" elements in the queue");
		System.out.println("The queue is: "+queue.toString());
		System.out.println("The queue is empty: "+queue.isEmpty());
		System.out.println("The front of the queue is: "+queue.first());
	}
}