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

    def remove_start_from_list(self):
        """ Removes an element from the end of the list. """
        if not (result := self.__root):
            raise RuntimeError(
                "Tried to remove from the list but it was already empty!")
        self.__root = self.__root.get_next()
        return result

    def print_list(self):
        """ Prints out the elements of the list. """
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, text):
        """ Finds an exact element in the list. """
        marker = self.__root
        while marker:
            if marker.text == text:
                return marker
            marker = marker.get_next()
        raise LookupError(
            f"Node with text {text} was not found in the linked list!")

    def size(self):
        """ Prints out the size of the list. """
        marker = self.__root
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count
