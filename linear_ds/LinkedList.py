class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # TODO: Initialize empty linked list
        # - Head node points to None initially
        # - Track size of linked list
        self.head = None
        self.size = 0

    def create_linked_list(self):
        # TODO: Reset linked list to empty state
        # - Set head to None
        # - Reset size counter
        self.head = None
        self.size = 0
        return True

    def insert(self, data):
        # TODO: Insert element at the end of linked list
        # - Create new node
        # - Traverse to end if not empty
        # - Add node at the end
        
        new_node = Node(data)
        
        # If list is empty, set new node as head
        if self.head is None:
            self.head = new_node
        else:
            # Traverse to the last node
            current = self.head
            while current.next is not None:
                current = current.next
            # Add new node at the end
            current.next = new_node
            
        self.size += 1
        return True

    def delete(self, data):
        # TODO: Delete first occurrence of element with matching data
        # - Handle empty list case
        # - Handle head node deletion case
        # - Traverse list to find element
        # - Update references to remove node
        
        if self.head is None:
            return False, "List is empty"
        
        # If head node contains the data to be deleted
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True, "Element deleted successfully"
        
        # Find the node before the one to be deleted
        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next
            
        # If data not found
        if current.next is None:
            return False, "Element not found in list"
            
        # Delete the node
        current.next = current.next.next
        self.size -= 1
        return True, "Element deleted successfully"

    def reverse(self):
        # TODO: Reverse the linked list
        # - Use three pointers technique
        # - Return new head of reversed list
        
        if self.head is None or self.head.next is None:
            # Empty list or single node - no need to reverse
            return self.head
            
        prev = None
        current = self.head
        next_node = None
        
        while current is not None:
            # Store next node
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move pointers forward
            prev = current
            current = next_node
            
        # Update head to the new start (previously the last node)
        self.head = prev
        return self.head

    def remove_duplicates(self):
        # TODO: Remove duplicate elements from linked list
        # - Use nested loops to check for duplicates
        # - Skip duplicate nodes by updating references
        
        if self.head is None or self.head.next is None:
            # Empty list or single node - no duplicates to remove
            return True
            
        current = self.head
        
        # For each node, check all subsequent nodes for duplicates
        while current is not None:
            runner = current
            
            # Check for duplicates of current node
            while runner.next is not None:
                if runner.next.data == current.data:
                    # Found duplicate, skip it in the list
                    runner.next = runner.next.next
                    self.size -= 1
                else:
                    # Move to next node
                    runner = runner.next
                    
            # Move to next unique node
            current = current.next
            
        return True

    def display(self):
        # TODO: Create string representation of linked list
        # - Traverse list and append each value to output
        # - Handle empty list case
        
        if self.head is None:
            return "Empty linked list"
            
        elements = []
        current = self.head
        
        while current is not None:
            elements.append(str(current.data))
            current = current.next
            
        return " -> ".join(elements)