# Import all required modules
from utils import (display_menu, display_array_menu, display_linked_list_menu,
                 display_stack_menu, display_queue_menu, display_binary_tree_menu)
from linear_ds.Array import Array
from linear_ds.LinkedList import LinkedList
from linear_ds.Stack import Stack
from linear_ds.Queue import Queue
from hierarchical_ds.BinaryTree import BinaryTree

def main():
    # Initialize data structures
    arr = None
    linked_list = None
    stack = None
    queue = None
    binary_tree = None
    
    while True:
        choice = display_menu()
        
        # Main Menu
        if choice == '1':  # Array
            arr = handle_array(arr)
        elif choice == '2':  # Linked List
            linked_list = handle_linked_list(linked_list)
        elif choice == '3':  # Stack
            stack = handle_stack(stack)
        elif choice == '4':  # Queue
            queue = handle_queue(queue)
        elif choice == '5':  # Binary Tree
            binary_tree = handle_binary_tree(binary_tree)
        elif choice == '6':  # Exit
            print("Thank you for using the Data Structures Toolkit!")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_array(arr):
    while True:
        choice = display_array_menu()
        
        if choice == '0':  # Return to main menu
            return arr
            
        # Create array if not exists for other operations
        if arr is None and choice != '1':
            print("Please create an array first.")
            continue
            
        if choice == '1':  # Create an Empty Array
            arr = Array()  # Use default size of 5
            arr.create_array()
            print("Empty array created successfully with default size of 5.")
            
        elif choice == '2':  # Insert elements
            element = input("Enter element to insert: ")
            # Try to convert to appropriate type
            try:
                element = int(element)
            except ValueError:
                try:
                    element = float(element)
                except ValueError:
                    pass  # Keep as string
                    
            success, message = arr.insert(element)
            print(message)
            
        elif choice == '3':  # Delete an element
            element = input("Enter element to delete: ")
            # Try to convert to appropriate type
            try:
                element = int(element)
            except ValueError:
                try:
                    element = float(element)
                except ValueError:
                    pass  # Keep as string
                    
            success, message = arr.delete(element)
            print(message)
            
        elif choice == '4':  # Sort ascending
            sorted_arr = arr.sort_asc()
            print("Array sorted in ascending order:")
            print(sorted_arr)
            
        elif choice == '5':  # Sort descending
            sorted_arr = arr.sort_desc()
            print("Array sorted in descending order:")
            print(sorted_arr)
            
        else:
            print("Invalid choice. Please try again.")
            
    return arr

def handle_linked_list(linked_list):
    while True:
        choice = display_linked_list_menu()
        
        if choice == '0':  # Return to main menu
            return linked_list
            
        # Create linked list if not exists for other operations
        if linked_list is None and choice != '1':
            print("Please create a linked list first.")
            continue
            
        if choice == '1':  # Create an Empty Linked List
            linked_list = LinkedList()
            linked_list.create_linked_list()
            print("Empty linked list created successfully.")
            
        elif choice == '2':  # Insert elements
            element = input("Enter element to insert: ")
            # Try to convert to appropriate type
            try:
                element = int(element)
            except ValueError:
                try:
                    element = float(element)
                except ValueError:
                    pass  # Keep as string
                    
            linked_list.insert(element)
            print("Element inserted successfully.")
            
        elif choice == '3':  # Delete an element
            element = input("Enter element to delete: ")
            # Try to convert to appropriate type
            try:
                element = int(element)
            except ValueError:
                try:
                    element = float(element)
                except ValueError:
                    pass  # Keep as string
                    
            success, message = linked_list.delete(element)
            print(message)
            
        elif choice == '4':  # Reverse
            linked_list.reverse()
            print("Linked list reversed successfully.")
            print("Reversed list:", linked_list.display())
            
        elif choice == '5':  # Remove duplicates
            linked_list.remove_duplicates()
            print("Duplicates removed successfully.")
            print("List after removing duplicates:", linked_list.display())
            
        elif choice == '6':  # Display
            print(linked_list.display())
            
        else:
            print("Invalid choice. Please try again.")
            
    return linked_list

def handle_stack(stack):
    while True:
        choice = display_stack_menu()
        
        if choice == '0':  # Return to main menu
            return stack
            
        # Create stack if not exists for other operations
        if stack is None and choice != '1':
            print("Please create a stack first.")
            continue
            
        if choice == '1':  # Create an Empty Stack
            stack = Stack()  # Use default size of 5
            stack.create_stack()
            print("Empty stack created successfully with default size of 5.")
            
        elif choice == '2':  # Push
            element = input("Enter element to push: ")
            # Try to convert to appropriate type
            try:
                element = int(element)
            except ValueError:
                try:
                    element = float(element)
                except ValueError:
                    pass  # Keep as string
                    
            success, message = stack.push(element)
            print(message)
            
        elif choice == '3':  # Pop
            element, message = stack.pop()
            if element is not None:
                print(f"Popped element: {element}")
            print(message)
            
        elif choice == '4':  # Modify
            try:
                index = int(input("Enter index to modify: "))
                element = input("Enter new value: ")
                # Try to convert to appropriate type
                try:
                    element = int(element)
                except ValueError:
                    try:
                        element = float(element)
                    except ValueError:
                        pass  # Keep as string
                        
                success, message = stack.modify(index, element)
                print(message)
            except ValueError:
                print("Index must be an integer.")
            
        elif choice == '5':  # Display
            print(stack.display())
            
        else:
            print("Invalid choice. Please try again.")
            
    return stack

def handle_queue(queue):
    while True:
        choice = display_queue_menu()
        
        if choice == '0':  # Return to main menu
            return queue
            
        # Create queue if not exists for other operations
        if queue is None and choice != '1':
            print("Please create a queue first.")
            continue
            
        if choice == '1':  # Create an Empty Queue
            queue = Queue()  # Use default size of 5
            queue.create_queue()
            print("Empty queue created successfully with default size of 5.")
            
        elif choice == '2':  # Enqueue
            element = input("Enter element to enqueue: ")
            # Try to convert to appropriate type
            try:
                element = int(element)
            except ValueError:
                try:
                    element = float(element)
                except ValueError:
                    pass  # Keep as string
                    
            success, message = queue.enqueue(element)
            print(message)
            
        elif choice == '3':  # Dequeue
            element, message = queue.dequeue()
            if element is not None:
                print(f"Dequeued element: {element}")
            print(message)
            
        elif choice == '4':  # Check front
            element, index, message = queue.check_front()
            if element is not None:
                print(f"Front element: {element}, Index: {index}")
            print(message)
            
        elif choice == '5':  # Check rear
            element, index, message = queue.check_rear()
            if element is not None:
                print(f"Rear element: {element}, Index: {index}")
            print(message)
            
        elif choice == '6':  # Display
            print(queue.display())
            
        else:
            print("Invalid choice. Please try again.")
            
    return queue

def handle_binary_tree(binary_tree):
    while True:
        choice = display_binary_tree_menu()
        
        if choice == '0':  # Return to main menu
            return binary_tree
            
        # Create binary tree if not exists for other operations
        if binary_tree is None and choice != '1':
            print("Please create a binary tree first.")
            continue
            
        if choice == '1':  # Create an Empty Binary Tree
            binary_tree = BinaryTree()
            binary_tree.create_binary_tree()
            print("Empty binary tree created successfully.")
            
        elif choice == '2':  # Insert
            element = input("Enter element to insert: ")
            # Try to convert to appropriate type
            try:
                element = int(element)
            except ValueError:
                try:
                    element = float(element)
                except ValueError:
                    pass  # Keep as string
                    
            binary_tree.insert(element)
            print("Element inserted successfully.")
            
        elif choice == '3':  # Delete
            element = input("Enter element to delete: ")
            # Try to convert to appropriate type
            try:
                element = int(element)
            except ValueError:
                try:
                    element = float(element)
                except ValueError:
                    pass  # Keep as string
                    
            success, message = binary_tree.delete(element)
            print(message)
            
        elif choice == '4':  # Display inorder
            print(binary_tree.display_binary_tree())
            
        elif choice == '5':  # Display tree structure
            print(binary_tree.display_tree_structure())
            
        else:
            print("Invalid choice. Please try again.")
            
    return binary_tree

if __name__ == "__main__":
    main()