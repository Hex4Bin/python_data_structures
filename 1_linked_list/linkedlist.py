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

    def reverse_iter(self):
        """
        Reverse the LinkedList (iterative method).
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.get_root()
        previous = None
        while current:
            next_node = current.get_next()
            current.set_next(previous)
            previous = current
            current = next_node
        self.__root = previous

    def reverse_recursive(self):
        """
        Reverse the LinkedList (recursive method).
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        def _reverse_recursive(current, previous):
            """ Helper method for recursion. """
            if not current:
                return previous
            else:
                next_node = current.get_next()
                current.set_next(previous)
                previous = current
                current = next_node
                return _reverse_recursive(current, previous)

        self.__root = _reverse_recursive(current=self.__root, previous=None)
