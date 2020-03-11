class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to head, if head == none, LL empty
        self.head = None
        self.tail = None 
    # reference to the head of the list
    # reference to the tail of the list
    def add_to_head(self, value):
        # create new Node with value
        new_node = Node(value)
         # update pointer new node --> Head
        new_node.set_next(self.head)
       
        if self.head is None and self.tail is None:
            self.head = new_node 
            self.tail = new_node
        else:
            # mark new Node as head (list with one or more nodes)
             self.head = new_node
            
    def add_to_tail(self, value):
        # create new Node with value 
        new_node = Node(value)

        #update next pointer of old tail
        self.tail.set_next(new_node)

        if self.head is None and self.tail is None:
            self.head = new_node 
            self.tail = new_node
        else:
            # mark new Node as tail (list with one or more nodes)
            self.tail = new_node
        

    def remove_head(self):
        # Special Case 1: remove from Empty LL--> nothing should happen 
        if self.head is None and self.tail is None:
            return "Empty"
        # Special Case 2:Remove from LinkedList with one or two elements 
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        #general 
        else: 
            # New head = old head's next Node (this auto-removes it)
            self.head = self.head.get_next()


    # STRETCH
    def insert_at(self, value, position):
        pass
    def contains(self, value):
        #Need pointer to temporary node (start at the head)
        cur_node = self.head
        while(cur_node.get_next() is not None):
            # do stuff? 
            # advance and move to next
            cur_node = cur_node.get_next()
            pass
        pass