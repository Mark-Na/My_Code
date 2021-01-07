package jsjf;
import java.util.Stack;
import java.util.LinkedList;
import java.util.Queue;
public class Palindrome {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String word = "tacocat";
		Stack<Character> stack = new Stack<Character>();
		Queue<Character> queue = new LinkedList<Character>();
		for(int i=0; i<word.length();i++)
		{
			stack.push(word.charAt(i));//putting the string onto a stack
		}
		
		for(int j=0; j<word.length();j++)
		{
			queue.add(word.charAt(j));//putting the string onto a queue

		}
		
		String answer = "yes";
		while(stack.empty()==false)//to go through the whole string
		{
			if(queue.remove().equals(stack.pop()))//stack will pop it from back to front while queue will dequeue the string front to back to check if they are the exact same letters
					continue;
			else {
				answer="no";
				break;
			}
				
		}
		
		System.out.println("Is " + word + " a palindrome?: "+answer);
	}

}
