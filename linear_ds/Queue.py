class Queue:
    def __init__(self, size=5):
        # TODO: Initialize empty queue
        # - Create array to store elements
        # - Track front and rear indices
        # - Set maximum size and current count
        self.queueSize = size
        self.queueElements = [None] * size
        self.queueFront = -1  # Index of front element
        self.queueRear = -1   # Index of rear element
        self.queueCount = 0   # Number of elements in queue

    def create_queue(self):
        # TODO: Reset queue to empty state
        # - Reset elements array
        # - Reset front, rear and count
        self.queueElements = [None] * self.queueSize
        self.queueFront = -1
        self.queueRear = -1
        self.queueCount = 0
        return True

    def enqueue(self, element):
        # TODO: Add element to rear of queue
        # - Check data type consistency
        # - Check if queue is full
        # - Update rear index
        # - Add element at rear
        
        # Check data type consistency if queue is not empty
        if self.queueCount > 0:
            # Find the first non-None element to check type
            i = self.queueFront
            firstElement = self.queueElements[i]
            
            # Check if element type matches existing elements
            if type(element) != type(firstElement):
                return False, f"Type mismatch. Expected {type(firstElement).__name__}, got {type(element).__name__}"
        
        # Check if queue is full
        if self.queueCount == self.queueSize:
            return False, "Queue is full"
            
        # If queue is empty, set front to 0
        if self.queueFront == -1:
            self.queueFront = 0
            
        # Update rear (circular implementation)
        self.queueRear = (self.queueRear + 1) % self.queueSize
        
        # Add element at rear
        self.queueElements[self.queueRear] = element
        self.queueCount += 1
        
        return True, "Element enqueued successfully"

    def dequeue(self):
        # TODO: Remove and return front element
        # - Check if queue is empty
        # - Get front element
        # - Update front index
        
        # Check if queue is empty
        if self.queueCount == 0:
            return None, "Queue is empty"
            
        # Get front element
        element = self.queueElements[self.queueFront]
        
        # Clear the position
        self.queueElements[self.queueFront] = None
        
        # Update front (circular implementation)
        if self.queueFront == self.queueRear:
            # Last element being removed
            self.queueFront = -1
            self.queueRear = -1
        else:
            self.queueFront = (self.queueFront + 1) % self.queueSize
            
        self.queueCount -= 1
        
        return element, "Element dequeued successfully"

    def check_front(self):
        # TODO: Return front element without removing
        # - Check if queue is empty
        # - Return front element and its index
        
        # Check if queue is empty
        if self.queueCount == 0:
            return None, -1, "Queue is empty"
            
        return self.queueElements[self.queueFront], self.queueFront, "Front element"

    def check_rear(self):
        # TODO: Return rear element without removing
        # - Check if queue is empty
        # - Return rear element and its index
        
        # Check if queue is empty
        if self.queueCount == 0:
            return None, -1, "Queue is empty"
            
        return self.queueElements[self.queueRear], self.queueRear, "Rear element"

    def display(self):
        # TODO: Create string representation of queue
        # - Handle empty queue case
        # - Create list of elements from front to rear
        
        if self.queueCount == 0:
            return "Empty queue"
            
        elements = []
        
        # Start from front and go to rear (handling circular queue)
        i = self.queueFront
        count = 0
        
        while count < self.queueCount:
            elements.append(str(self.queueElements[i]))
            i = (i + 1) % self.queueSize
            count += 1
            
        return "Front [" + " -> ".join(elements) + "] Rear"