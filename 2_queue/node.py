class Node:
    """
    This Node class contains the necessary properties, which are:
    - name
    - phone
    - next
    """

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.__next = None

    def set_next(self, node):
        """ Set the next element of the node. """
        if isinstance(node, Node) or node is None:
            self.__next = node
        else:
            raise TypeError("The 'next' node must be of type Node or None.")

    def get_next(self):
        """ Get the next element of the node. """
        return self.__next

    def print_details(self):
        """ Print the details of the node. """
        print(f"{self.name} ({self.phone})")
