class Array:
    def __init__(self, size=5):
        # TODO: Initialize array with given size
        # - Create empty list with None values
        # - Track current number of elements
        # - Track data type of elements for type checking
        self.arrSize = size  # Max size ng array
        self.arrElements = [None] * size  # Actual elements
        self.arrCount = 0  # Current number of elements
        self.arrDataType = None  # Track data type of elements

    def create_array(self):
        # TODO: Reset array to empty state
        # - Initialize elements to None
        # - Reset count and data type
        self.arrElements = [None] * self.arrSize
        self.arrCount = 0
        self.arrDataType = None
        return self.arrElements

    def insert(self, element):
        # TODO: Insert element into array
        # - Check if array is full, resize if needed
        # - Check data type consistency
        # - Add element to next available position
        
        # Check kung may data type na ang array
        if self.arrCount > 0 and self.arrDataType is not None:
            # Check kung pareho ang data type
            if type(element) != self.arrDataType:
                return False, f"Type mismatch. Expected {self.arrDataType.__name__}, got {type(element).__name__}"
        else:
            # Set data type kung wala pa
            self.arrDataType = type(element)
        
        # Check kung puno na ang array
        if self.arrCount >= self.arrSize:
            # Increase size by 1
            self.arrSize += 1
            tempElements = [None] * self.arrSize
            
            # Copy existing elements
            i = 0
            while i < self.arrCount:
                tempElements[i] = self.arrElements[i]
                i += 1
                
            self.arrElements = tempElements
        
        # Insert element
        self.arrElements[self.arrCount] = element
        self.arrCount += 1
        return True, "Element inserted successfully"

    def delete(self, element):
        # TODO: Delete element from array
        # - Search for element
        # - Shift elements to fill gap
        # - Check if element exists before deletion
        
        found = False
        position = -1
        
        # Find element position
        i = 0
        while i < self.arrCount:
            if self.arrElements[i] == element:
                found = True
                position = i
                break
            i += 1
        
        if not found:
            return False, "Element not found in array"
        
        # Shift elements to fill gap
        i = position
        while i < self.arrCount - 1:
            self.arrElements[i] = self.arrElements[i + 1]
            i += 1
        
        # Set last element to None
        self.arrElements[self.arrCount - 1] = None
        self.arrCount -= 1
        
        # Reset data type if array is now empty
        if self.arrCount == 0:
            self.arrDataType = None
            
        return True, "Element deleted successfully"

    def sort_asc(self):
        # TODO: Sort array in ascending order
        # - Implement bubble sort algorithm
        # - Return sorted copy of array
        
        if self.arrCount <= 1:
            return self.arrElements[:self.arrCount]
        
        # Create a copy to sort
        sorted_arr = [None] * self.arrCount
        i = 0
        while i < self.arrCount:
            sorted_arr[i] = self.arrElements[i]
            i += 1
        
        # Bubble sort algorithm
        i = 0
        while i < self.arrCount:
            j = 0
            while j < self.arrCount - i - 1:
                if sorted_arr[j] > sorted_arr[j + 1]:
                    # Swap elements
                    temp = sorted_arr[j]
                    sorted_arr[j] = sorted_arr[j + 1]
                    sorted_arr[j + 1] = temp
                j += 1
            i += 1
            
        return sorted_arr

    def sort_desc(self):
        # TODO: Sort array in descending order
        # - Implement bubble sort algorithm
        # - Return sorted copy of array
        
        if self.arrCount <= 1:
            return self.arrElements[:self.arrCount]
        
        # Create a copy to sort
        sorted_arr = [None] * self.arrCount
        i = 0
        while i < self.arrCount:
            sorted_arr[i] = self.arrElements[i]
            i += 1
        
        # Bubble sort algorithm for descending order
        i = 0
        while i < self.arrCount:
            j = 0
            while j < self.arrCount - i - 1:
                if sorted_arr[j] < sorted_arr[j + 1]:
                    # Swap elements
                    temp = sorted_arr[j]
                    sorted_arr[j] = sorted_arr[j + 1]
                    sorted_arr[j + 1] = temp
                j += 1
            i += 1
            
        return sorted_arr