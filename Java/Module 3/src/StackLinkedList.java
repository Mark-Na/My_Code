import java.util.LinkedList;
import java.util.NoSuchElementException;
/**
 * Represents a stack as a linked list
 */
public class StackLinkedList<T> implements StackADT<T>{
	private LinkedList<T> stack;
	
	/**
	 * Makes an empty linked list
	 */
	
	StackLinkedList()
	{
		stack = new LinkedList<T>();
	}
	
	/**
	 * Puts an element at the top of the stack(front of the list)
	 * @param element is the item to be put at the top of the stack
	 */
	
	public void push(T element)
	{
		stack.push(element);
	}
	
	/**
	 * Removes the top element from the stack(front of the list)
	 */
	
	public T pop() throws NoSuchElementException
	{
		if(stack.isEmpty())
			throw new NoSuchElementException("stack");
		return stack.pop();
	}
	
	/**
	 * Returns the top element of the stack(front of the list)
	 */
	
	public T peek()
	{
		return stack.peek();
	}
	
	/**
	 * Returns the boolean value if the stack is empty or not(has no elements)
	 * @return the boolean value if the stack is empty
	 */
	
	public boolean isEmpty()
	{
		return stack.isEmpty();
	}
	
	/**
	 * Returns the number of elements in the stack
	 * @return the number of elements in the stack
	 */
	
	public int size()
	{
		return stack.size();
	}
	
	/**
	 * Returns the string representation of the stack
	 * @return the string representation of the stack
	 */
	
	public String toString() {
		String str = "";
		for(int i=stack.size();i>=0;i--)
			str+=stack.get(i)+" ";
		return str;
	}
	
	public static void main(String[] args) {
    	StackArrayList<Integer> stack = new StackArrayList<Integer>();
    	System.out.println("The stack is empty: "+stack.isEmpty());
		stack.push(5);
		System.out.println("The stack is: "+stack.toString());
		stack.push(3);
		System.out.println("The stack is: "+stack.toString());
		stack.push(10);
		System.out.println("The stack is: "+stack.toString());
		stack.pop();
		System.out.println("The stack is: "+stack.toString());
		System.out.println("There are "+stack.size()+" elements in the stack");
		System.out.println("The top of the stack is: "+stack.peek());
		stack.push(5);
		stack.push(4);
		stack.push(3);
		stack.push(2);
		stack.push(1);
		System.out.println("The stack is empty: "+stack.isEmpty());
		System.out.println("The stack is: "+stack.toString());
		System.out.println("There are "+stack.size()+" elements in the stack");
    }
		
	}
