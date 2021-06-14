class LinkedList:
    """ Our linked list """

    def __init__(self):
        self.__root = None

    def get_root(self):
        """ Gives back the root of the linked list. """
        return self.__root

    def add_start_to_list(self, node):
        """ Adds a new element to the beginning of the list. """
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def remove_end_from_list(self):
        """ Removes an element from the end of the list. """
        marker = self.__root

        if not marker.get_next():
            self.__root = None
            return marker

        while marker:
            following_node = marker.get_next()
            if not following_node.get_next():
                marker.set_next(None)
                return following_node
            marker = marker.get_next()

        raise LookupError("The list is empty!")

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
        raise LookupError(f"Name {name} not found in the linked list.")

    def size(self):
        """ Prints out the size of the list. """
        marker = self.__root
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count
