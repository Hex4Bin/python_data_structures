from linkedlist import LinkedList


class LinkedStack:
    """
    This class is a stack wrapper around a LinkedList.
    This means that methods like `add_to_list_start` should now be called `push`, for example.
    """

    def __init__(self):
        self.__linked_list = LinkedList()

    def push(self, node):
        """ Same as LinkedList's add_start_to_list method. """
        self.__linked_list.add_start_to_list(node)

    def pop(self):
        """ Same as LinkedList's remove_start_from_list method. """
        return self.__linked_list.remove_start_from_list()

    def find(self, text):
        """ Same as LinkedList's find method. """
        return self.__linked_list.find(text)

    def print_details(self):
        """ Same as LinkedList's print_list method. """
        self.__linked_list.print_list()

    def __len__(self):
        """ Same as LinkedList's size method. """
        return self.__linked_list.size()
