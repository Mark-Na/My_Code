import java.util.LinkedList;
/**
 * Represents a queue as a linked list
 */
public class QueueLinkedList<T> implements QueueADT<T> {
	private LinkedList<T> queue;
	
	/**
	 * Creates an empty linked list
	 */
	
	QueueLinkedList()
	{
		queue = new LinkedList<T>();
	}
	
	/**
	 * Adds an element to the back in FIFO manner
	 * @param element the item to be added to the back of the list
	 */
	
	public void enqueue(T element)
	{
		queue.addLast(element);
	}
	
	/**
	 * Removes the first element from the front of the list
	 */
	
	public T dequeue()
	{
		return queue.remove();
	}
	
	/**
	 * Gets the first element of the queue(the front) without removing it
	 */
	
	public T first()
	{
		return queue.getFirst();
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
		return queue.toString();
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
