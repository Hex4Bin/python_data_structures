from node import Node


class LinkedList:
    """ Our linked list """

    def __init__(self):
        self.__root = None

    def get_root(self):
        """ Gives back the root of the linked list. """
        return self.__root

    def add_to_list(self, node):
        """ Adds a new element to the beginning of the list. """
        if isinstance(node, Node):
            if self.__root != None:
                node.set_next(self.__root)
            self.__root = node
        else:
            raise TypeError("The added node must be of type Node.")

    def print_list(self):
        """ Prints out the elements of the list. """
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):
        """ Finds an exact element in the list. """
        marker = self.__root
        while marker:
            if marker.name == name:
                return marker
            marker = marker.get_next()
        raise LookupError("Can't find the name.")
