# Data Structures Toolkit with Python

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.42.0-red)](https://streamlit.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/jpcurada/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/JpCurada)

A comprehensive data structures implementation toolkit created as part of the COSC 203 Design and Analysis of Algorithms course. This project implements fundamental data structures including Arrays, Linked Lists, Stacks, Queues, and Binary Search Trees with interactive visualization.

## Features

### Array Operations
- Create empty arrays with customizable size
- Insert and delete elements
- Sort in ascending and descending order
- Visual representation with indices

### Linked List Operations
- Create empty linked lists
- Insert and delete elements
- Reverse the linked list
- Remove duplicates
- Visual node-based representation

### Stack Operations
- Create empty stacks with customizable size
- Push and pop elements
- Handle overflow and underflow conditions
- Modify specific elements
- Visual representation showing the top element

### Queue Operations
- Create empty queues with customizable size
- Enqueue and dequeue elements
- Check front and rear elements
- Circular queue implementation
- Visual representation showing front and rear

### Binary Search Tree Operations
- Create empty binary search trees
- Insert and delete elements
- Traversal visualization
- Tree structure display

## Installation and Usage

1. Clone the repository:
```bash
git clone https://github.com/YourUsername/data-structures-toolkit.git
cd data-structures-toolkit
```

2. Install the required dependencies:
```bash
pip install streamlit
```

3. Run the application:
```bash
streamlit run main.py
```

4. Access the web interface at `http://localhost:8501`

## Project Structure

```
jpcurada-py-dsa-implementation/
├── README.md
├── main.py                   # Main application file (Streamlit UI)
├── utils.py                  # Utility functions
├── hierarchical_ds/
│   └── BinaryTree.py         # Binary Search Tree implementation
└── linear_ds/
    ├── Array.py              # Array implementation
    ├── LinkedList.py         # Linked List implementation
    ├── Queue.py              # Queue implementation
    └── Stack.py              # Stack implementation
```

## Implementation Details

All data structures are implemented from scratch without using Python's built-in data structure methods. The code follows educational best practices to demonstrate the underlying concepts:

- **Arrays**: Implemented with dynamic resizing and type checking
- **Linked Lists**: Pointer-based implementation with node traversal
- **Stacks**: Last-In-First-Out (LIFO) structure with overflow detection
- **Queues**: First-In-First-Out (FIFO) structure with circular implementation
- **Binary Search Trees**: Hierarchical structure with proper insertion and deletion logic

## Course Information

- **Course**: COSC 203 Design and Analysis of Algorithms
- **Assignment**: Machine Problem 1
- **Author**: John Paul Curada (BS CS 2-5)

## Acknowledgments

- Prof. Chris Piamonte 