package jsjf;

import jsjf.exceptions.*;
import java.util.Iterator;

/**
 * Represents a linked implementation of a stack.
 *
 * @author Java Foundations
 * @version 4.0
 */
public class LinkedStack<T> implements StackADT<T>
{
    private int count;
    private LinearNode<T> top;

    /**
     * Creates an empty stack.
     */
    public LinkedStack()
    {
        count = 0;
        top = null;
    }

    /**
     * Adds the specified element to the top of this stack.
     * @param element element to be pushed on stack
     */
    @SuppressWarnings("unused")
	public void push(T element)
    {
    	LinearNode<T> temp = new LinearNode<T>(element);
        temp.setNext(top);
        top = temp;
        
        
        if(count>=5) //arbitrary max number of values in the stack
        { 
        	LinearNode<T> current = top;//to get the last node
        	LinearNode<T> previous = new LinearNode<T>(null);// to get the second last node to make it the last node
        	while(current.getNext()!=null)
        	{
        		previous = current;
        		current = current.getNext();
        	}
            previous.setNext(null);//sets the last node to null to get rid of it to make the second last node the last one        
        	count--;
        }                
        count++;
        
    }

    /**
     * Removes the element at the top of this stack and returns a
     * reference to it.
     * @return element from top of stack
     * @throws EmptyCollectionException if the stack is empty
     */
    public T pop() throws EmptyCollectionException
    {
        if (isEmpty())
            throw new EmptyCollectionException("stack");

        T result = top.getElement();
        top = top.getNext();
        count--;

        return result;
    }

    /**
     * Returns a reference to the element at the top of this stack.
     * The element is not removed from the stack.
     * @return element on top of stack
     * @throws EmptyCollectionException if the stack is empty
     */
    public T peek() throws EmptyCollectionException
    {
        if (isEmpty())
            throw new EmptyCollectionException("stack");

        return top.getElement();
    }

    /**
     * Returns true if this stack is empty and false otherwise.
     * @return true if stack is empty
     */
    public boolean isEmpty()
    {
        return (count == 0);
    }

    /**
     * Returns the number of elements in this stack.
     * @return number of elements in the stack
     */
    public int size()
    {
        return count;
    }

    /**
     * Returns a string representation of this stack.
     * @return string representation of the stack
     */
    public String toString()
    {
        String result = "";
        LinearNode<T> current = top;

        while (current != null)
        {
            result = result + current.getElement() + " ";
            current = current.getNext();
        }

        return result;
    }
    
    public static void main(String[] args) {
    	LinkedStack<Integer> stack = new LinkedStack<Integer>();
		System.out.println("The stack is empty: "+stack.isEmpty());
		stack.push(5);
		System.out.println("The stack is: "+ stack.toString());
		stack.push(3);
		System.out.println("The stack is: "+ stack.toString());
		stack.push(10);
		System.out.println("The stack is: "+ stack.toString());
		stack.pop();
		System.out.println("The stack is: "+ stack.toString());
		System.out.println("The stack has "+ stack.size()+" elements");
		System.out.println("The top of the stack is: " + stack.peek());
		stack.push(5);
		stack.push(4);
		stack.push(3);
		stack.push(2);
		stack.push(1);
		System.out.println("The stack is: "+ stack.toString());
		System.out.println("The stack has "+ stack.size()+" elements");
    }
}
