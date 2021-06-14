class Node:
    """
    This Node class contains the necessary properties, which are:
    - data
    - value
    """

    def __init__(self, data, value):
        self.data = data
        self.value = value
        self.__left = None
        self.__right = None

    def set_right(self, node):
        """ Set the right-next element of the node. """
        if isinstance(node, Node) or node is None:
            self.__right = node
        else:
            raise TypeError("The 'right' node must be of type Node or None.")

    def set_left(self, node):
        """ Set the left-next element of the node. """
        if isinstance(node, Node) or node is None:
            self.__left = node
        else:
            raise TypeError("The 'left' node must be of type Node or None.")

    def get_right(self):
        """ Get the right-next element of the node. """
        return self.__right

    def get_left(self):
        """ Get the left-next element of the node. """
        return self.__left

    def print_details(self):
        """ Print the details of the node. """
        print(f"{self.value}: {self.data}")
