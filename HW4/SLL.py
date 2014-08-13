class Node:
  def __init__(self, _value = None, _next = None):
    self.value = _value
    self.next = _next
  def __str__(self):
    return str(self.value)

 

class LinkedList: 
  def __init__(self, value = None): # O(1), best complexity
    if type(value) == int or type(value) == float or type(value) == long or value == None: #input type should be an integer, a number or a long.
      self.head = Node(value)
    else:   
      print "Input should be a number (either integer or float)"

  def length(self): #O(n), best complexity
    if self.head.value == None: # if list is empty, then return 0.
      return 0
    current_node = self.head
    i = 1
    while current_node.next != None: # the tail does not have pointer.
      i += 1                         # so, we can measure the length by counting the number of excution in this loop. 
      current_node = current_node.next
    return i
    
  def addNode(self, new_value):  #O, best complexity
    if type(new_value) == int or type(new_value) == float or type(new_value) == long:
       current_node = self.head
       if current_node.value == None: # if the list is empty, then add value to the first container.
         current_node.value = new_value
       else:
         while current_node.next != None: # find the last node
           current_node = current_node.next # and add value after the last node
         current_node.next = Node(new_value)
       
    else: 
       print "Input should be a number (either integer or float)"
 
  def addNodeAfter(self, new_value, after_node): # O(n), best complexity
    i = self.length()
    if type(after_node) is not int: return "Input should be an integer"
    if after_node > i or after_node < 0: return "Input should be an integer within [1,{0}]".format(i)
    if type(new_value) == int or type(new_value) == float or type(new_value) == long:
      current_node = self.head
      node_number = 1
      while node_number != after_node: # find the node specified by the input
          current_node = current_node.next
          node_number += 1
      current_node.next = Node(new_value, current_node.next) #add value after the node specified   
    else:
      print "Input should be a number (either integer or float)"


  def addNodeBefore(self, new_value, before_node): #O(n), best complexity
    i = self.length()
    if type(before_node) is not int: return "Input should be an integer"
    if before_node > i or before_node < 1: return "Input should be an integer within [1,{0}]".format(i)
    current_node = self.head
    node_number = 1
    if node_number == before_node: # in the case when the first node is specified,
      self.head = Node(new_value, current_node) # set the input value as the head 
    else:
      while node_number+1 != before_node: # find the node specified
        current_node = current_node.next
        node_number += 1
      current_node.next = Node(new_value, current_node.next) # add value before the node specified.

  def removeNode(self, node_to_remove): #O(n), best complexity
    current_node = self.head
    i = self.length()
    if type(node_to_remove) is not int: return "Input should be an integer"
    if node_to_remove > i or node_to_remove < 1: return "Input should be an integer within [1,{0}]".format(i)
    node_number = 1
    while node_number < i: # from the first node to the second last node, find the specified node.
      if node_number == node_to_remove: # if the node is specified
         current_node.value = current_node.next.value # replace the value with the next node's value
         current_node.next = current_node.next.next # and replace the pointer with the next node's pointer
      current_node = current_node.next
      node_number += 1
    if node_number == node_to_remove: # if the last one is specified
       counter = 1                    # we need to know location of the second last node
       current_node = self.head       # to get rid of its pointer(make it None).  
       while counter != node_number - 1:
         current_node = current_node.next
         counter += 1
       current_node.next = None

  def removeNodesByValue(self, value): #O(n^2), possibly not best complexity because of recursive function call
    current_node = self.head
    i = self.length()
    old_i = i # the length of the list before removing
    counter = 0
    node_number = 1
    while node_number <= i: # check whether all nodes have the same value and this value is specified
      if current_node.value == value:
         current_node = current_node.next
         counter += 1
      node_number += 1 
    if counter == i:  # if so, all nodes will be removed 
      self.head = Node() # this is done by setting the head as None
    else: # if not, check from the first node to last node whether the node has the value specified
      current_node = self.head 
      counter = 0
      node_number = 1
      while node_number <= i:
          if current_node.value == value: # if so, remove the node is removed
              self.removeNode(node_number)# by using removeNode function
          if current_node.value == value: # However, this method is limited in the case when next node also has the same value because
             counter += 1                 # removing node is done through replacing the node with the next node.
          i = self.length()               # So, there still remains the values we want to delete.  
          current_node = current_node.next# To solve this problem, we count how many values still exist. 
          node_number += 1
      if counter != 0:                    # if more than 0 values we want to remove exist in the list
          self.removeNodesByValue(value)  # do this function again to remove them. 
    if old_i == i:                        # If the length of the list didn't change, then we know that 
      return "No such value in the list"  # this function didn't remove anything. It means input is not in the list.


  def __str__(self): #O(n), best complexity
    current_node = self.head
    i = self.length()
    node_number = 1
    listOut = "[ "
    while node_number <= i:
      listOut += str(current_node) + " "
      current_node = current_node.next
      node_number += 1
    listOut += "]"
    return listOut

  def reverse(self): #O(n^2), possibly best complexity
    current_node = self.head
    i = self.length()
    node_number = 1
    while node_number <= i: # make mirror image of the list before the original list
      self.addNodeBefore(current_node.value, 1)
      current_node = current_node.next
      node_number += 1
    new_i = self.length()  # measure the length of the new list
    while new_i > i: # remove the nodes from the last to middle
      self.removeNode(new_i)
      new_i -= 1
 

# a = LinkedList(20)   
# print a.__str__()

# a = LinkedList()
# print a.__str__()

# a.addNode(1)
# print a.__str__()

# print a.length()

# print a.addNodeAfter(10,2)
# print a.__str__()

# a.addNodeAfter(10,1)
# print a.__str__()

# a.addNodeBefore(13,1)
# print a.__str__()

# print a.addNodeBefore(13,4)
# print a.__str__()

# a.removeNode(2)
# print a.__str__()

# a.removeNode(1)
# print a.__str__()

# print a.removeNode(3)
# print a.__str__()

# a.addNode(13)
# print a.__str__()

# a.removeNodesByValue(13)
# print a.__str__()

# a.addNode(10)
# print a.__str__()

# a.addNode(10)
# print a.__str__()

# a.addNode(10)
# print a.__str__()

# print a.removeNodesByValue(12)
# print a.__str__()

# a.removeNodesByValue(10)
# print a.__str__()

# a.addNode(52)
# a.addNode(4)
# a.addNode(13)
# a.addNode(32)
# a.addNode(2)
# a.addNode(89)
# a.addNode(42)
# a.addNode(22)
# a.addNode(16)

print a.__str__()

a.reverse()
print a.__str__()