package jsjf;

import jsjf.exceptions.*;
import java.util.Arrays;

/**
 * An array implementation of a stack in which the bottom of the
 * stack is fixed at index 0.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class ArrayStack<T> implements StackADT<T>
{
	private final static int DEFAULT_CAPACITY = 100;

	private int top;  
	private T[] stack;

	/**
	 * Creates an empty stack using the default capacity.
	 */
	public ArrayStack()
	{
		this(DEFAULT_CAPACITY);
	}

	/**
	 * Creates an empty stack using the specified capacity.
	 * @param initialCapacity the initial size of the array 
	 */
	public ArrayStack(int initialCapacity)
	{
		top = -1;//start at -1 so that the top points at the actual top not the one above it
		stack = (T[])(new Object[initialCapacity]);
	}

	/**
	 * Adds the specified element to the top of this stack, expanding
	 * the capacity of the array if necessary.
	 * @param element generic element to be pushed onto stack
	 */
	public void push(T element)
	{		
		top++;
		
		if (top == stack.length) 
			expandCapacity();
		
		stack[top] = element;
		
	}

	/**
	 * Creates a new array to store the contents of this stack with
	 * twice the capacity of the old one.
	 */
	private void expandCapacity()
	{
		this.stack = Arrays.copyOf(stack, stack.length * 2);   
	}

	/**
	 * Removes the element at the top of this stack and returns a
	 * reference to it. 
	 * @return element removed from top of stack
	 * @throws EmptyCollectionException if stack is empty 
	 */
	public T pop() throws EmptyCollectionException
	{
		if (isEmpty())
			throw new EmptyCollectionException("stack");

		
		T result = stack[top];
		stack[top] = null; 
		top--;

		return result;
	}

	/**
	 * Returns a reference to the element at the top of this stack.
	 * The element is not removed from the stack.  
	 * @return element on top of stack
	 * @throws EmptyCollectionException if stack is empty
	 */
	public T peek() throws EmptyCollectionException
	{
		if (isEmpty())
			throw new EmptyCollectionException("stack");

		return stack[top];
	}

	/**
	 * Returns true if this stack is empty and false otherwise. 
	 * @return true if this stack is empty
	 */
	public boolean isEmpty()
	{
		return (top==-1);
	}

	/**
	 * Returns the number of elements in this stack.
	 * @return the number of elements in the stack
	 */
	public int size()
	{
		int size = top+1;
		return size;
	}

	/**
	 * Returns a string representation of this stack. 
	 * @return a string representation of the stack
	 */
	public String toString()
	{
		String str="";
		for(int i=top;i>=0;i--) {
			str+=stack[i]+" ";
		}
		return str;
			
	}
	
	public static void main(String[] args) {
		ArrayStack<Integer> stack = new ArrayStack<Integer>(5);
		System.out.println("The stack is empty: "+stack.isEmpty());
		stack.push(5);
		System.out.println("The stack is: " +stack.toString());
		stack.push(3);
		System.out.println("The stack is: " +stack.toString());
		stack.push(10);
		System.out.println("The stack is: " +stack.toString());
		stack.pop();
		System.out.println("The stack is: " +stack.toString());
		System.out.println("The stack has " + stack.size()+" elements");
		System.out.println("The top of the stack is: " +stack.peek());
		stack.push(5);
		stack.push(5);
		stack.push(5);
		stack.push(5);
		stack.push(5);
		System.out.println("The stack is: " +stack.toString());
		System.out.println("The stack has " + stack.size()+" elements");
	}
}

