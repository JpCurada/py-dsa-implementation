import streamlit as st
import sys
import os
from datetime import datetime

# Add the repository directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the data structure classes
from linear_ds.Array import Array
from linear_ds.LinkedList import LinkedList
from linear_ds.Stack import Stack
from linear_ds.Queue import Queue
from hierarchical_ds.BinaryTree import BinaryTree

# Set page title and configuration
st.set_page_config(
    page_title="Data Structures Toolkit",
    page_icon=":material/analytics:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add some custom CSS to make the app look nice
st.markdown("""
    <style>
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .error-message {
        background-color: #f8d7da;
        color: #721c24;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .warning-message {
        background-color: #fff3cd;
        color: #856404;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .linked-list-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        overflow-x: auto;
        padding: 10px 0;
    }
    .linked-list-node {
        border: 2px solid #4e8df5;
        border-radius: 5px;
        padding: 10px;
        text-align: center;
        background-color: #e6f0ff;
        width: 80px;
        min-width: 80px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 5px;
    }
    .linked-list-arrow {
        color: #4e8df5;
        font-size: 20px;
        margin: 0 5px;
    }
    </style>
    """, unsafe_allow_html=True)

def success_message(message):
    st.markdown(f'<div class="success-message">{message}</div>', unsafe_allow_html=True)
    
def error_message(message):
    st.markdown(f'<div class="error-message">{message}</div>', unsafe_allow_html=True)
    
def warning_message(message):
    st.markdown(f'<div class="warning-message">{message}</div>', unsafe_allow_html=True)

# Initialize session state for data structures if not already initialized
if 'array' not in st.session_state:
    st.session_state.array = None
    
if 'linked_list' not in st.session_state:
    st.session_state.linked_list = None
    
if 'stack' not in st.session_state:
    st.session_state.stack = None
    
if 'queue' not in st.session_state:
    st.session_state.queue = None
    
if 'binary_tree' not in st.session_state:
    st.session_state.binary_tree = None

# Initialize message history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to convert input to appropriate type
def convert_input(value):
    # Try to convert to int
    try:
        return int(value)
    except ValueError:
        # Try to convert to float
        try:
            return float(value)
        except ValueError:
            # Keep as string
            return value

# Main App Layout
st.title("Data Structures Toolkit")
st.write("Machine Problem 1 - COSC 203 Design and Analysis of Algorithms")
st.caption("By: John Paul Curada of BS CS 2-5")

# navigation tabs for each data structure
tabs = st.tabs(["Array", "Linked List", "Stack", "Queue", "Binary Search Tree"])

# Array Tab
with tabs[0]:    
    col1, col2 = st.columns([3, 1])
    
    with col2:
        st.subheader("Operations")
        if st.button("Create Empty Array", key="create_array"):
            st.session_state.array = Array()
            st.session_state.array.create_array()
            success_message("Empty array created successfully with default size of 5.")
            st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": "Empty array created"})
        
        # Only show these operations if array exists
        if st.session_state.array is not None:
            element_input = st.text_input("Element value:", key="array_element")
            
            if st.button("Insert Element", key="insert_array"):
                if element_input:
                    element = convert_input(element_input)
                    success, message = st.session_state.array.insert(element)
                    if success:
                        success_message(message)
                    else:
                        error_message(message)
                    st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": f"Insert attempt: {message}"})
                else:
                    warning_message("Please enter an element value")
            
            if st.button("Delete Element", key="delete_array"):
                if element_input:
                    element = convert_input(element_input)
                    success, message = st.session_state.array.delete(element)
                    if success:
                        success_message(message)
                    else:
                        error_message(message)
                    st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": f"Delete attempt: {message}"})
                else:
                    warning_message("Please enter an element value")
            
            if st.button("Sort (Ascending)", key="sort_asc"):
                sorted_arr = st.session_state.array.sort_asc()
                
                # Actually update the array elements to match sorted order
                i = 0
                while i < st.session_state.array.arrCount:
                    st.session_state.array.arrElements[i] = sorted_arr[i]
                    i += 1
                    
                success_message("Array sorted in ascending order")
                st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": "Array sorted in ascending order"})
            
            if st.button("Sort (Descending)", key="sort_desc"):
                sorted_arr = st.session_state.array.sort_desc()
                
                # Actually update the array elements to match sorted order
                i = 0
                while i < st.session_state.array.arrCount:
                    st.session_state.array.arrElements[i] = sorted_arr[i]
                    i += 1
                    
                success_message("Array sorted in descending order")
                st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": "Array sorted in descending order"})
    
    with col1:
        st.subheader("Visualization")
        if st.session_state.array is not None:
            # Create a more visual representation of the array
            elements = []
            i = 0
            while i < st.session_state.array.arrSize:
                if i < st.session_state.array.arrCount:
                    elements.append(st.session_state.array.arrElements[i])
                else:
                    elements.append(None)
                i += 1
                
            # Display the array state
            st.write(f"**Current Array (Size: {st.session_state.array.arrSize}, Count: {st.session_state.array.arrCount})**")
            
            # Create a more visual representation
            cols = st.columns(len(elements))
            for i, (col, element) in enumerate(zip(cols, elements)):
                with col:
                    if element is not None:
                        st.markdown(f"""
                        <div style="border: 2px solid #4e8df5; border-radius: 5px; padding: 10px; text-align: center; background-color: #e6f0ff;">
                            <span style="font-weight: bold;">{element}</span>
                            <hr style="margin: 5px 0;">
                            <span style="color: gray; font-size: 0.8em;">Index: {i}</span>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="border: 1px dashed #cccccc; border-radius: 5px; padding: 10px; text-align: center; background-color: #f8f9fa;">
                            <span style="color: #cccccc;">Empty</span>
                            <hr style="margin: 5px 0;">
                            <span style="color: gray; font-size: 0.8em;">Index: {i}</span>
                        </div>
                        """, unsafe_allow_html=True)
            
            # Display sorted arrays if they exist
            sorted_asc = st.session_state.array.sort_asc()
            sorted_desc = st.session_state.array.sort_desc()
            
        else:
            st.info("Please create an array first to visualize it.")

# Linked List Tab
with tabs[1]:    
    col1, col2 = st.columns([3, 1])
    
    with col2:
        st.subheader("Operations")
        if st.button("Create Empty Linked List", key="create_list"):
            st.session_state.linked_list = LinkedList()
            st.session_state.linked_list.create_linked_list()
            # Add a flag to track if the list is reversed or not
            st.session_state.is_list_reversed = False
            success_message("Empty linked list created successfully.")
            st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": "Empty linked list created"})
        
        # Only show these operations if linked list exists
        if st.session_state.linked_list is not None:
            element_input = st.text_input("Element value:", key="list_element")
            
            if st.button("Insert Element", key="insert_list"):
                if element_input:
                    element = convert_input(element_input)
                    st.session_state.linked_list.insert(element)
                    success_message("Element inserted successfully.")
                    st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": f"Element {element} inserted into linked list"})
                else:
                    warning_message("Please enter an element value")
            
            if st.button("Delete Element", key="delete_list"):
                if element_input:
                    element = convert_input(element_input)
                    success, message = st.session_state.linked_list.delete(element)
                    if success:
                        success_message(message)
                    else:
                        error_message(message)
                    st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": f"Delete attempt: {message}"})
                else:
                    warning_message("Please enter an element value")
            
            if st.button("Reverse Linked List", key="reverse_list"):
                st.session_state.linked_list.reverse()
                # Toggle the reversed flag when the list is reversed
                if 'is_list_reversed' not in st.session_state:
                    st.session_state.is_list_reversed = False
                st.session_state.is_list_reversed = not st.session_state.is_list_reversed
                success_message("Linked list reversed successfully.")
                st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": "Linked list reversed"})
            
            if st.button("Remove Duplicates", key="remove_dups"):
                st.session_state.linked_list.remove_duplicates()
                success_message("Duplicates removed successfully.")
                st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": "Duplicates removed from linked list"})
    
    with col1:
        st.subheader("Visualization")
        if st.session_state.linked_list is not None:
            if st.session_state.linked_list.head is None:
                st.info("The linked list is currently empty.")
            else:
                # Get all nodes for visualization
                nodes = []
                current = st.session_state.linked_list.head
                while current is not None:
                    nodes.append(current.data)
                    current = current.next
                
                # Display the linked list
                st.write(f"**Current Linked List (Size: {st.session_state.linked_list.size})**")
                
                # Check if the list is reversed
                is_reversed = False
                if 'is_list_reversed' in st.session_state:
                    is_reversed = st.session_state.is_list_reversed
                
                st.write(f"**Direction: {'Reversed' if is_reversed else 'Normal'}**")
                
                # Create a horizontal visual representation
                html_content = '<div class="linked-list-container">'
                
                if is_reversed:
                    # Reversed visualization (right to left)
                    # Fix the null pointer HTML to avoid rendering issues
                    html_content = '<div class="linked-list-container">'
                    html_content += '<div class="linked-list-arrow" style="margin-right: 5px;">null &larr;</div>'
                    
                    for i, node in enumerate(nodes):
                        html_content += f'<div class="linked-list-node"><span style="font-weight: bold;">{node}</span></div>'
                        
                        if i < len(nodes) - 1:
                            html_content += '<div class="linked-list-arrow">&larr;</div>'
                else:
                    # Normal visualization (left to right)
                    html_content = '<div class="linked-list-container">'
                    for i, node in enumerate(nodes):
                        html_content += f'<div class="linked-list-node"><span style="font-weight: bold;">{node}</span></div>'
                        
                        if i < len(nodes) - 1:
                            html_content += '<div class="linked-list-arrow">&rarr;</div>'
                        else:
                            html_content += '<div class="linked-list-arrow">&rarr; null</div>'

                html_content += '</div>'
                
                st.markdown(html_content, unsafe_allow_html=True)
        else:
            st.info("Please create a linked list first to visualize it.")

# Stack Tab
with tabs[2]:    
    col1, col2 = st.columns([3, 1])
    
    with col2:
        st.subheader("Operations")
        if st.button("Create Empty Stack", key="create_stack"):
            st.session_state.stack = Stack()
            st.session_state.stack.create_stack()
            success_message("Empty stack created successfully with default size of 5.")
            st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": "Empty stack created"})
        
        # Only show these operations if stack exists
        if st.session_state.stack is not None:
            element_input = st.text_input("Element value:", key="stack_element")
            
            if st.button("Push Element", key="push_stack"):
                if element_input:
                    element = convert_input(element_input)
                    success, message = st.session_state.stack.push(element)
                    if success:
                        success_message(message)
                    else:
                        error_message(message)
                    st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": f"Push attempt: {message}"})
                else:
                    warning_message("Please enter an element value")
            
            if st.button("Pop Element", key="pop_stack"):
                element, message = st.session_state.stack.pop()
                if element is not None:
                    success_message(f"Popped element: {element}")
                else:
                    error_message(message)
                st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": f"Pop attempt: {message}"})
            
            # Modify element
            modify_col1, modify_col2 = st.columns(2)
            with modify_col1:
                index_input = st.text_input("Index:", key="stack_index")
            with modify_col2:
                new_value_input = st.text_input("New Value:", key="stack_new_value")
                
            if st.button("Modify Element", key="modify_stack"):
                if index_input and new_value_input:
                    try:
                        index = int(index_input)
                        new_value = convert_input(new_value_input)
                        success, message = st.session_state.stack.modify(index, new_value)
                        if success:
                            success_message(message)
                        else:
                            error_message(message)
                        st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": f"Modify attempt: {message}"})
                    except ValueError:
                        error_message("Index must be an integer.")
                else:
                    warning_message("Please enter both index and new value")
    
    with col1:
        st.subheader("Visualization")
        if st.session_state.stack is not None:
            # Display stack information
            st.write(f"**Current Stack (Size: {st.session_state.stack.stackSize}, Top: {st.session_state.stack.stackTop})**")
            
            if st.session_state.stack.stackTop == -1:
                st.info("The stack is currently empty.")
            else:
                # Create a more visual representation of the stack
                st.write("**Stack Elements (Bottom to Top)**")
                
                # Get elements for display
                elements = []
                i = 0
                while i <= st.session_state.stack.stackTop:
                    elements.append(st.session_state.stack.stackElements[i])
                    i += 1
                
                # Display in reverse order (top to bottom)
                for i, element in enumerate(reversed(elements)):
                    position = len(elements) - i - 1
                    is_top = position == st.session_state.stack.stackTop
                    
                    bg_color = "#e6f0ff"
                    border_color = "#4e8df5"
                    
                    if is_top:
                        bg_color = "#4e8df5"
                        border_color = "#0051a8"
                        
                    st.markdown(f"""
                    <div style="
                        border: 2px solid {border_color}; 
                        border-radius: 5px; 
                        padding: 15px; 
                        margin-bottom: 5px; 
                        text-align: center; 
                        background-color: {bg_color}; 
                        color: {'white' if is_top else 'black'};
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    ">
                        <span style="font-weight: bold; font-size: 1.1em;">{element}</span>
                        <span style="margin-left: 10px; font-size: 0.8em;">
                            {f"← TOP (Index: {position})" if is_top else f"(Index: {position})"}
                        </span>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("Please create a stack first to visualize it.")

# Queue Tab
with tabs[3]:    
    col1, col2 = st.columns([3, 1])
    
    with col2:
        st.subheader("Operations")
        if st.button("Create Empty Queue", key="create_queue"):
            st.session_state.queue = Queue()
            st.session_state.queue.create_queue()
            success_message("Empty queue created successfully with default size of 5.")
            st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": "Empty queue created"})
        
        # Only show these operations if queue exists
        if st.session_state.queue is not None:
            element_input = st.text_input("Element value:", key="queue_element")
            
            if st.button("Enqueue Element", key="enqueue"):
                if element_input:
                    element = convert_input(element_input)
                    success, message = st.session_state.queue.enqueue(element)
                    if success:
                        success_message(message)
                    else:
                        error_message(message)
                    st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": f"Enqueue attempt: {message}"})
                else:
                    warning_message("Please enter an element value")
            
            if st.button("Dequeue Element", key="dequeue"):
                element, message = st.session_state.queue.dequeue()
                if element is not None:
                    success_message(f"Dequeued element: {element}")
                else:
                    error_message(message)
                st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": f"Dequeue attempt: {message}"})
            
            if st.button("Check Front", key="check_front"):
                element, index, message = st.session_state.queue.check_front()
                if element is not None:
                    success_message(f"Front element: {element}, Index: {index}")
                else:
                    error_message(message)
            
            if st.button("Check Rear", key="check_rear"):
                element, index, message = st.session_state.queue.check_rear()
                if element is not None:
                    success_message(f"Rear element: {element}, Index: {index}")
                else:
                    error_message(message)
    
    with col1:
        st.subheader("Visualization")
        if st.session_state.queue is not None:
            # Display queue information
            st.write(f"**Current Queue (Size: {st.session_state.queue.queueSize}, Count: {st.session_state.queue.queueCount})**")
            st.write(f"**Front Index: {st.session_state.queue.queueFront}, Rear Index: {st.session_state.queue.queueRear}**")
            
            if st.session_state.queue.queueCount == 0:
                st.info("The queue is currently empty.")
            else:
                # Create a more visual representation of the queue
                st.write("**Queue Elements (Front to Rear)**")
                
                # Get elements for display
                elements = []
                i = st.session_state.queue.queueFront
                count = 0
                
                while count < st.session_state.queue.queueCount:
                    elements.append((i, st.session_state.queue.queueElements[i]))
                    i = (i + 1) % st.session_state.queue.queueSize
                    count += 1
                
                # Display horizontally
                cols = st.columns(len(elements))
                
                for idx, (col, (i, element)) in enumerate(zip(cols, elements)):
                    with col:
                        is_front = i == st.session_state.queue.queueFront
                        is_rear = i == st.session_state.queue.queueRear
                        
                        label = ""
                        border_color = "#4e8df5"
                        bg_color = "#e6f0ff"
                        text_color = "black"
                        
                        if is_front and is_rear:
                            label = "FRONT & REAR"
                            border_color = "#9c27b0"
                            bg_color = "#e1bee7"
                        elif is_front:
                            label = "FRONT"
                            border_color = "#4caf50"
                            bg_color = "#c8e6c9"
                        elif is_rear:
                            label = "REAR"
                            border_color = "#f44336"
                            bg_color = "#ffcdd2"
                        
                        st.markdown(f"""
                        <div style="
                            border: 2px solid {border_color}; 
                            border-radius: 5px; 
                            padding: 10px; 
                            text-align: center; 
                            background-color: {bg_color};
                            color: {text_color};
                            height: 100px;
                            display: flex;
                            flex-direction: column;
                            justify-content: space-between;
                        ">
                            <div style="font-weight: bold; font-size: 0.8em;">{label}</div>
                            <div style="font-weight: bold; font-size: 1.2em;">{element}</div>
                            <div style="color: gray; font-size: 0.7em;">Index: {i}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Display directed arrow
                if len(elements) > 1:
                    st.markdown("""
                    <div style="
                        display: flex;
                        justify-content: center;
                        margin-top: 10px;
                    ">
                        <div style="
                            background-color: #4e8df5;
                            height: 2px;
                            width: 80%;
                            position: relative;
                        ">
                            <div style="
                                position: absolute;
                                right: -10px;
                                top: -4px;
                                width: 0;
                                height: 0;
                                border-top: 5px solid transparent;
                                border-left: 10px solid #4e8df5;
                                border-bottom: 5px solid transparent;
                            "></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("Please create a queue first to visualize it.")

# Binary Search Tree Tab
# Binary Search Tree Tab section in main.py

# This code should be placed in the Binary Tree Tab section of main.py
with tabs[4]:    
    col1, col2 = st.columns([3, 1])
    
    with col2:
        st.subheader("Operations")
        if st.button("Create Empty Binary Tree", key="create_tree"):
            st.session_state.binary_tree = BinaryTree()
            st.session_state.binary_tree.create_binary_tree()
            success_message("Empty binary tree created successfully.")
            st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": "Empty binary tree created"})
        
        # Only show these operations if binary tree exists
        if st.session_state.binary_tree is not None:
            element_input = st.text_input("Element value:", key="tree_element")
            
            if st.button("Insert Element", key="insert_tree"):
                if element_input:
                    element = convert_input(element_input)
                    st.session_state.binary_tree.insert(element)
                    success_message("Element inserted successfully.")
                    st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": f"Element {element} inserted into binary tree"})
                else:
                    warning_message("Please enter an element value")
            
            if st.button("Delete Element", key="delete_tree"):
                if element_input:
                    element = convert_input(element_input)
                    success, message = st.session_state.binary_tree.delete(element)
                    if success:
                        success_message(message)
                    else:
                        error_message(message)
                    st.session_state.messages.append({"time": datetime.now().strftime("%H:%M:%S"), "message": f"Delete attempt: {message}"})
                else:
                    warning_message("Please enter an element value")
    
    with col1:
        st.subheader("Visualization")
        if st.session_state.binary_tree is not None:
            # Display inorder traversal
            inorder = st.session_state.binary_tree.display_binary_tree()
            if inorder == "Empty tree":
                st.info("The binary tree is currently empty.")
            else:
                st.write("**Inorder Traversal (Sorted Order)**")
                st.write(inorder)
                
                # Display preorder traversal
                preorder = st.session_state.binary_tree.display_preorder_traversal()
                st.write("**Preorder Traversal (Root, Left, Right)**")
                st.write(preorder)
                
                # Display postorder traversal
                postorder = st.session_state.binary_tree.display_postorder_traversal()
                st.write("**Postorder Traversal (Left, Right, Root)**")
                st.write(postorder)
                
                # Display tree structure
                st.write("**Tree Structure**")
                tree_structure = st.session_state.binary_tree.display_tree_structure()
                st.code(tree_structure)
        else:
            st.info("Please create a binary tree first to visualize it.")

# Activity Log at the bottom
with st.popover("Activity Log"):
    if st.session_state.messages:
        for msg in reversed(st.session_state.messages):
            st.write(f"[{msg['time']}] {msg['message']}")
    else:
        st.write("No activity yet.")

# Add a footer
st.markdown("""
---
<div style="text-align: center;">
    <p style="color: gray; font-size: 0.8em;">
        <a href="https://www.linkedin.com/in/jpcurada/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-Connect-blue.svg" alt="LinkedIn"></a>  <a href="https://github.com/JpCurada" target="_blank"><img src="https://img.shields.io/badge/GitHub-Follow-black.svg" alt="GitHub"></a>
    </p>
</div>
""", unsafe_allow_html=True)