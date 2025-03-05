class Stack:
    def __init__(self, size=5):
        # TODO: Initialize empty stack
        # - Create array to store elements
        # - Track top index
        # - Set maximum size
        self.stackSize = size
        self.stackElements = [None] * size
        self.stackTop = -1  # Top points to -1 when stack is empty

    def create_stack(self):
        # TODO: Reset stack to empty state
        # - Reset elements array
        # - Reset top index
        self.stackElements = [None] * self.stackSize
        self.stackTop = -1
        return True

    def push(self, element):
        # TODO: Push element onto stack
        # - Check for stack overflow
        # - Increment top index
        # - Add element at top
        
        # Check for stack overflow
        if self.stackTop == self.stackSize - 1:
            return False, "STACK OVERFLOW"
            
        # Increment top and add element
        self.stackTop += 1
        self.stackElements[self.stackTop] = element
        return True, "Element pushed successfully"

    def pop(self):
        # TODO: Remove and return top element
        # - Check for stack underflow
        # - Get top element
        # - Decrement top index
        
        # Check for stack underflow
        if self.stackTop == -1:
            return None, "STACK UNDERFLOW"
            
        # Get top element
        element = self.stackElements[self.stackTop]
        
        # Set the position to None and decrement top
        self.stackElements[self.stackTop] = None
        self.stackTop -= 1
        
        return element, "Element popped successfully"

    def modify(self, index, new_value):
        # TODO: Modify element at specific position
        # - Check if index is valid
        # - Update element at index
        
        # Check if index is valid (0 to stackTop)
        if index < 0 or index > self.stackTop:
            return False, "Invalid index"
            
        # Update element at index
        self.stackElements[index] = new_value
        return True, "Element modified successfully"

    def display(self):
        # TODO: Create string representation of stack
        # - Handle empty stack case
        # - Create list of elements from bottom to top
        
        if self.stackTop == -1:
            return "Empty stack"
            
        elements = []
        # Display from bottom to top
        i = 0
        while i <= self.stackTop:
            elements.append(str(self.stackElements[i]))
            i += 1
            
        return " -> ".join(elements) + " (Top)"