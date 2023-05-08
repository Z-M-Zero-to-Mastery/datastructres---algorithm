
#  QUESTION : 1

# def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

# def remove_by_value(self, data):
    # Remove first node that contains data

#  QUESTION : 2

# Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. That way you can iterate in forward and backward direction. Your node class will look this this,
# class Node:
    # def __init__(self, data=None, next=None, prev=None):
        # self.data = data
        # self.next = next
        # self.prev = prev

# Add following new methods,

# def print_forward(self):
    # This method prints list in forward direction. Use node.next

# def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

# ****************************************************************************************************************

# QUESTION : 1

# ****************************************************************************************************************
# Solution 

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head

        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)  
                itr.next = node
                break
                
            itr = itr.next       

    def remove_by_value(self, data):

        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next            



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()
