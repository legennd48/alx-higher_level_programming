#!/usr/bin/python3

'''Define classes for a singly-linked list.'''


class Node:
    '''Defines a node in a singly-linked list.'''

    def __init__(self, data, next_node=None):
        ''' Instantiation a new Node.
        Args:
            data (int): data of the new Node.
            next_node (Node): The next node.
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Retrieves the data.'''
        return (self.__data)

    @data.setter
    def data(self, value):
        ''' sets the value of node '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''Retrieves the next_node of the Node.'''
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''Represent a singly-linked list.'''

    def __init__(self):
        '''Initalize a new SinglyLinkedList.'''
        self.__head = None

    def sorted_insert(self, value):
        '''Insert a new Node to the SinglyLinkedList.

        Args:
            value (Node): new Node value.
        '''
        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new

        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new

        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        '''Define the print()'''
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
