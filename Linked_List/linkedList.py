# This file contains the Node class which is used to create nodes for the linked list
class Node:
    # This is the constructor for the Node class
    # It takes in the data to be stored in the node and the next node in the list
    def __init__(self, data, next= None):
        self.data = data
        self.next = next

# This is the LinkedList class
# It is used to create a linked list and perform operations on it 
# It contains a head node which points to the first node in the list 
class LinkedList:
    # This is the constructor for the LinkedList class
    # It initializes the head node to None 
    # It takes in the head node as a parameter 
    # If no head node is passed, it initializes the head node to None
    def __init__(self):
        # Initialize the head node to None 
        self.head = None

    # This method is used to insert a node at the beginning of the list 
    # It takes in the data to be stored in the node as a parameter 
    def insert_at_beginning(self, data):
        # Create a new node with the data passed in as a parameter 
        node = Node(data, self.head)
        # Set the head node to the new node 
        # This makes the new node the first node in the list
        self.head = node      

    # This method is used to print the linked list 
    # It takes in no parameters
    def print(self):

        # If the head node is None, the list is empty 
        if self.head is None:
            print("Linked List is empty")
            return

        # If the head node is not None, print the list 
        # Create an itr variable to iterate through the list, It starts at the head node
        itr = self.head
        # Create an empty string to store the list
        llstr = ""

        # Iterate through the list until the itr variable is None
        while itr:
            # Add the data in the current node to the string 
            # Add an arrow to the string to show the next node
            llstr += str(itr.data) + "--->"   
            # Set the itr variable to the next node in the list
            itr = itr.next
        # Print the string  
        print(llstr)   

    # This method is used to find the length of the linked list
    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count       

    # This method is used to insert a node at the end of the list
    def insert_at_end(self, data):
        # If the list is empty, set the head node to the new node
        if self.head is None:
            # Create a new node with the data passed in as a parameter
            self.head = Node(data, None)
            return
        # If the list is not empty, iterate through the list until the last node is reached
        itr = self.head
        # Iterate through the list until the itr variable is None
        while itr.next:
            itr = itr.next
        # Set the next node of the last node to the new node
        itr.next = Node(data, None)

    # This method is used to insert a node at a given index
    def insert_at(self, index, data):
        # If the index is less than 0 or greater than the length of the list, raise an exception
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        # If the index is 0, insert the node at the beginning of the list
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        # Iterate through the list until the index is reached 
        # eg : 1->2->3->4->5->None
        # If we want to insert a node at index 2 (at 3), we iterate through the list until the count is equal to 1
        while itr:
            # If th count is equal to the index-1, insert the node at the given index
            # ie, if the count is 1 and the index we want to insert the node at is 2, then the index-1 is 1 
            # It will take the previous node as the current node and insert the new node after it
            # ie, 1->2->3->4->5->None
            if count == index-1:
                # It will be at element 2
                # It will create a new node and the parameter passed are data of the new node and next node of the current node(ie, the node at the given index)
                #  And data which we want to insert will be 6 so Node(6, 3) where 3 is the next node of the current node(2)
                node = Node(data, itr.next)
                # And set the next node of the current node to the new node
                # And the itr.next will be 6 for the current node(2)
                itr.next = node
                # And the output will be 1->2->6->3->4->5->None
                break

        itr = itr.next
        count += 1

    # This method is used to remove a node at a given index  
    def remove_at(self, index):
        # If the index is less than 0 or greater than the length of the list, raise an exception
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        # If the index is 0, ie the first node, remove the first node
        if index == 0:
            # Then we will set the head node to the next node which will be None or the next node of the current node
            # ie, 1->2->3->4->5->None
            # Then we will set the head node to 2
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        # Iterate through the list until the index is reached
        while itr:
            # If the count is equal to the index-1, remove the node at the given index
            if count == index-1:
                # ie, 1->2->3->4->5->None
                # If we want to remove the node at index 2 (ie, 3), we iterate through the list until the count is equal to 1
                # We will set the next node of the current node to the next node of the next node of the current node
                # ie, if we are at 2,and we will set the next node of 2 as the next node of 3 which is 4
                itr.next = itr.next.next
                # And the output will be 1->2->4->5->None
                break

        itr = itr.next
        count += 1

    # This method is used to insert a list of values into the linked list
    def insert_values(self, data_list):
        # Delete the existing nodes in the linked list
        self.head = None
        # Iterate through the list of values and insert each value into the linked list
        for data in data_list:
            # Insert the value at the end of the linked list
            self.insert_at_end(data)


# if __name__ == '__main__':
ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.insert_at(1,"blueberry")
ll.remove_at(2)
ll.print()
ll.insert_values([45,7,12,567,99])
ll.insert_at_end(67)
ll.print()
