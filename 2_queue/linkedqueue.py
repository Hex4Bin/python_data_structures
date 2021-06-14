from linkedlist import LinkedList


class LinkedQueue:
    """
    This class is a queue wrapper around a LinkedList.
    This means that methods like `add_to_list_start` should now be called `push`, for example.
    """

    def __init__(self):
        self.__linked_list = LinkedList()

    def push(self, node):
        """ Same as LinkedList's add_start_to_list method. """
        self.__linked_list.add_start_to_list(node)

    def pop(self):
        """ Same as LinkedList's remove_end_from_list method. """
        return self.__linked_list.remove_end_from_list()

    def find(self, name):
        """ Same as LinkedList's find method. """
        return self.__linked_list.find(name)

    def print_details(self):
        """ Same as LinkedList's print_list method. """
        self.__linked_list.print_list()

    def __len__(self):
        """ Same as LinkedList's size method. """
        return self.__linked_list.size()
