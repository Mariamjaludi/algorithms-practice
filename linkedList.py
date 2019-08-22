#A simple Python program for traversal of a linked list

# Node class
class Node:
    # constructor to initialize the node object
    def __init__(self, data=None):
      self.data = data # Assign data
      self.next = None # Initialize next as null

class LinkedList:
    # constructor to initialize the linked list object
    def __init__(self, head=None):
      self.head = head # Initialize head as null when list is created without a node

    # method to insert a node at the beginning of a linked list
    def insert(self, data):
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

    # method to insert a node at the end of a linked list
    def insertAtTail(self, data):
      new_node = Node(data)
      current = self.head
      while current.next != None:
        current = current.next
      current.next = new_node

    # method to find the length of a linked list
    def length(self):
      current = self.head
      count = 0
      if current != None:
        count += 1
        while current.next != None:
          count += 1
          current = current.next
      return count

    # method to find a specific node in a linked list
    def search(self, data):
      current = self.head
      while current:
        if current.data == data:
          return current
        else:
          current = current.next
      return None

    # method to delete a specific node in a linked list
    def delete(self, data):
      current = self.head
      while current:
        if current.data == data:
          current.data = current.next.data
          current.next = current.next.next
        else:
          current = current.next

    # method to reverse a linked list
    def reverse(self):
        previous = None
        current = self.head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous

    # method to stringify the linked list
    def __str__(self):
      node = self.head
      output = ""
      while node:
        output += str(node.data) + " "
        node = node.next
      return output
