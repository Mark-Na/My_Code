//***************************************************************************************************************************************************
//LinkedBinarySearchTree.Java
//
//Mark Naguib T00651567
//COMP2231 Assignment 4 Question 2
//This application creates a binary search tree using linked lists and tests all the various methods
//edited the original file
//***************************************************************************************************************************************************
package jsjf;

import jsjf.exceptions.*;
import java.util.ArrayList;

/**
 * LinkedBinarySearchTree implements the BinarySearchTreeADT interface 
 * with links.
 * 
 * @author Java Foundations
 * @version 4.0
 */
//referenced class file given to us(source file)
public class LinkedBinarySearchTree<T> extends LinkedBinaryTree<T>
implements BinarySearchTreeADT<T>
{
	/**
	 * Creates an empty binary search tree.
	 */
	public LinkedBinarySearchTree() 
	{
		super();
	}

	/**
	 * Creates a binary search with the specified element as its root.
	 *
	 * @param element the element that will be the root of the new binary
	 *        search tree
	 */
	public LinkedBinarySearchTree(T element) 
	{
		super(element);

		if (!(element instanceof Comparable))
			throw new NonComparableElementException("LinkedBinarySearchTree");
	}

	/**
	 * Adds the specified object to the binary search tree in the
	 * appropriate position according to its natural order.  Note that
	 * equal elements are added to the right.
	 *
	 * @param element the element to be added to the binary search tree
	 */
	public void addElement(T element) 
	{
		if (!(element instanceof Comparable))
			throw new NonComparableElementException("LinkedBinarySearchTree");

		Comparable<T> comparableElement = (Comparable<T>)element;

		if (isEmpty())
			root = new BinaryTreeNode<T>(element);
		else 
		{
			if (comparableElement.compareTo(root.getElement()) < 0)
			{
				if (root.getLeft() == null) 
					this.getRootNode().setLeft(new BinaryTreeNode<T>(element));
				else
					addElement(element, root.getLeft());
			}
			else
			{
				if (root.getRight() == null) 
					this.getRootNode().setRight(new BinaryTreeNode<T>(element));
				else
					addElement(element, root.getRight());
			}
		}
		modCount++;
	}

	/**
	 * Adds the specified object to the binary search tree in the
	 * appropriate position according to its natural order.  Note that
	 * equal elements are added to the right.
	 *
	 * @param element the element to be added to the binary search tree
	 */
	private void addElement(T element, BinaryTreeNode<T> node) 
	{
		Comparable<T> comparableElement = (Comparable<T>)element;

		if (comparableElement.compareTo(node.getElement()) < 0)
		{
			if (node.getLeft() == null) 
				node.setLeft(new BinaryTreeNode<T>(element));
			else
				addElement(element, node.getLeft());
		}
		else
		{
			if (node.getRight() == null) 
				node.setRight(new BinaryTreeNode<T>(element));
			else
				addElement(element, node.getRight());
		}
	}

	/**
	 * Removes the first element that matches the specified target
	 * element from the binary search tree and returns a reference to
	 * it.  Throws a ElementNotFoundException if the specified target
	 * element is not found in the binary search tree.
	 *
	 * @param targetElement the element being sought in the binary search tree
	 * @throws ElementNotFoundException if the target element is not found
	 */
	public T removeElement(T targetElement)
			throws ElementNotFoundException 
	{
		T result = null;

		if (isEmpty())
			throw new ElementNotFoundException("LinkedBinarySearchTree");
		else
		{
			BinaryTreeNode<T> parent = null;
			if (((Comparable<T>)targetElement).equals(root.element)) 
			{
				result =  root.element;
				BinaryTreeNode<T> temp = replacement(root);
				if (temp == null)
					root = null;
				else 
				{
					root.element = temp.element;
					root.setRight(temp.right);
					root.setLeft(temp.left);
				}

				modCount--;
			}
			else 
			{                
				parent = root;
				if (((Comparable<T>)targetElement).compareTo(root.element) < 0)
					result = removeElement(targetElement, root.getLeft(), parent);
				else
					result = removeElement(targetElement, root.getRight(), parent);
			}
		}

		return result;
	}

	/**
	 * Removes the first element that matches the specified target
	 * element from the binary search tree and returns a reference to
	 * it.  Throws a ElementNotFoundException if the specified target
	 * element is not found in the binary search tree.
	 *
	 * @param targetElement the element being sought in the binary search tree
	 * @param node the node from which to search
	 * @param parent the parent of the node from which to search
	 * @throws ElementNotFoundException if the target element is not found
	 */
	private T removeElement(T targetElement, BinaryTreeNode<T> node, BinaryTreeNode<T> parent)
			throws ElementNotFoundException 
	{
		T result = null;

		if (node == null)
			throw new ElementNotFoundException("LinkedBinarySearchTree");
		else
		{
			if (((Comparable<T>)targetElement).equals(node.element)) 
			{
				result =  node.element;
				BinaryTreeNode<T> temp = replacement(node);
				if (parent.right == node)
					parent.right = temp;
				else 
					parent.left = temp;

				modCount--;
			}
			else 
			{                
				parent = node;
				if (((Comparable<T>)targetElement).compareTo(node.element) < 0)
					result = removeElement(targetElement, node.getLeft(), parent);
				else
					result = removeElement(targetElement, node.getRight(), parent);
			}
		}

		return result;
	}

	/**
	 * Returns a reference to a node that will replace the one
	 * specified for removal. In the case where the removed node has 
	 * two children, the inorder successor is used as its replacement.
	 *
	 * @param node the node to be removed
	 * @return a reference to the replacing node
	 */
	private BinaryTreeNode<T> replacement(BinaryTreeNode<T> node) 
	{
		BinaryTreeNode<T> result = null;

		if ((node.left == null) && (node.right == null))
			result = null;

		else if ((node.left != null) && (node.right == null))
			result = node.left;

		else if ((node.left == null) && (node.right != null))
			result = node.right;

		else
		{
			BinaryTreeNode<T> current = node.right;
			BinaryTreeNode<T> parent = node;

			while (current.left != null)
			{
				parent = current;
				current = current.left;
			}

			current.left = node.left;
			if (node.right != current)
			{
				parent.left = current.right;
				current.right = node.right;
			}

			result = current;
		}

		return result;
	}

	/**
	 * Removes elements that match the specified target element from 
	 * the binary search tree. Throws a ElementNotFoundException if 
	 * the specified target element is not found in this tree.
	 *
	 * @param targetElement the element being sought in the binary search tree
	 * @throws ElementNotFoundException if the target element is not found
	 */
	public void removeAllOccurrences(T targetElement)
			throws ElementNotFoundException 
	{
		removeElement(targetElement);

		try
		{
			while (contains((T)targetElement))
				removeElement(targetElement);
		}

		catch (Exception ElementNotFoundException)
		{
		}
	}

	/**
	 * Removes the node with the least value from the binary search
	 * tree and returns a reference to its element. Throws an
	 * EmptyCollectionException if this tree is empty. 
	 *
	 * @return a reference to the node with the least value
	 * @throws EmptyCollectionException if the tree is empty
	 */
	public T removeMin() throws EmptyCollectionException 
	{
		T result = null;

		if (isEmpty())
			throw new EmptyCollectionException("LinkedBinarySearchTree");
		else 
		{
			if (root.left == null) 
			{
				result = root.element;
				root = root.right;
			}
			else 
			{
				BinaryTreeNode<T> parent = root;
				BinaryTreeNode<T> current = root.left;
				while (current.left != null) 
				{
					parent = current;
					current = current.left;
				}
				result =  current.element;
				parent.left = current.right;
			}

			modCount--;
		}

		return result;
	}

	/**
	 * Removes the node with the highest value from the binary
	 * search tree and returns a reference to its element. Throws an
	 * EmptyCollectionException if this tree is empty. 
	 *
	 * @return a reference to the node with the highest value
	 * @throws EmptyCollectionException if the tree is empty
	 */
	//edited
	//removes the right most variable in the tree as it is the larges
	public T removeMax() throws EmptyCollectionException 
	{
		T result = null;

		if (isEmpty())
			throw new EmptyCollectionException("LinkedBinarySearchTree");
		else 
		{
			if (root.right == null) 
			{
				result = root.element;
				root = root.left;
			}
			else 
			{
				BinaryTreeNode<T> parent = root;
				BinaryTreeNode<T> current = root.right;
				while (current.right != null) 
				{
					parent = current;
					current = current.right;
				}
				result =  current.element;
				parent.right = current.left;
			}

			modCount--;
		}

		return result;
		
	}

	/**
	 * Returns the element with the least value in the binary search
	 * tree. It does not remove the node from the binary search tree. 
	 * Throws an EmptyCollectionException if this tree is empty.
	 *
	 * @return the element with the least value
	 * @throws EmptyCollectionException if the tree is empty
	 */
	//edited
	//travels to the left most value in the tree as it is the smallest and does not remove it
	public T findMin() throws EmptyCollectionException 
	{
		T min = null;

		if (isEmpty())
			throw new EmptyCollectionException("Tree is empty");
		else 
		{
			if (root.left == null) 
			{
				min = root.element;
			}
			else 
			{
				BinaryTreeNode<T> current = root;
				while (current.left != null) 
				{
					current = current.left;
				}
				min =  current.element;
			}

		}

		return min;
	}

	/**
	 * Returns the element with the highest value in the binary
	 * search tree. It does not remove the node from the binary
	 * search tree. Throws an EmptyCollectionException if this 
	 * tree is empty.
	 *
	 * @return the element with the highest value
	 * @throws EmptyCollectionException if the tree is empty
	 */
	//edited
	//travels to the right most value and does not remove it
	public T findMax() throws EmptyCollectionException 
	{
		T max = null;

		if (isEmpty())
			throw new EmptyCollectionException("Tree is empty");
		else 
		{
			if (root.right == null) 
			{
				max = root.element;
			}
			else 
			{
				BinaryTreeNode<T> current = root;
				while (current.right != null) 
				{
					current = current.right;
				}
				max =  current.element;
			}
		}

		return max;
	}

	/**
	 * Returns the left subtree of the root of this tree.
	 *
	 * @return a link to the left subtree of the tree
	 */
	//edited
	public LinkedBinarySearchTree<T> getLeft()
	{
		if (root==null) 
			throw new EmptyCollectionException("Tree is empty");
		//did not know how to do this
		LinkedBinarySearchTree<T> left = new LinkedBinarySearchTree<T>();
		return left;
	}

	/**
	 * Returns the right subtree of the root of this tree.
	 *
	 * @return a link to the right subtree of the tree
	 */
	//edited
	public LinkedBinarySearchTree<T> getRight()
	{
		if (root==null) 
			throw new EmptyCollectionException("Tree is empty");
		
		LinkedBinarySearchTree<T> right= new LinkedBinarySearchTree<T>();
		//did not know how to do this
		return right;
	}
	//edited
	//stores the binary tree into an array list recursively
	//https://www.quora.com/How-do-I-save-a-binary-tree-to-an-array-of-in-order-traversal
	private ArrayList<T> arr= new ArrayList<T>(size());
	private int index;
	public ArrayList<T> inOrderArray(BinaryTreeNode<T> root) throws EmptyCollectionException
	{
		if(root==null)
			throw new EmptyCollectionException("Tree is empty");
		inOrderArray(root.left);//puts in the left element first
		arr.add(index++, root.element);//puts in the root element
		inOrderArray(root.right);//puts in the right element		
		return arr;		
	}
	
	//edited
	//creates a tree from the sorted array list
	//https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/
    public BinaryTreeNode<T> balance(T[] arr, BinaryTreeNode<T> root,int i) 
    {  
        if (i < arr.length) { 
            BinaryTreeNode<T> temp = new BinaryTreeNode<T>(arr[i]); 
            root = temp;//make the root the first element of the array  
            root.left = balance(arr, root.left,2*i+1);//2i + 1 is the index for the left child so this puts in the left children 
            root.right = balance(arr, root.right,2*i+2); //2i+2 is the index for the right child so this puts in the right children
        } 
        return root; 
    } 
}

