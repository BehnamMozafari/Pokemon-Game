"""
    Array-based implementation of SortedList ADT.
    Items to store should be of time ListItem.
"""

from referential_array import ArrayR
from sorted_list import *
from pokemon import Charmander, Bulbasaur, Squirtle

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev and Graeme Gange'
__docformat__ = 'reStructuredText'

class ArraySortedList(SortedList[T]):
    """ SortedList ADT implemented with arrays. """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """ ArraySortedList object initialiser. """

        # first, calling the basic initialiser
        SortedList.__init__(self)

        # initialising the internal array
        size = max(self.MIN_CAPACITY, max_capacity)
        self.array = ArrayR(size)

    def reset(self):
        """ Reset the list. """
        SortedList.__init__(self)

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        return self.array[index]

    def __setitem__(self, index: int, item: ListItem) -> None:
        """ Magic method. Insert the item at a given position,
            if possible (!). Shift the following elements to the right.
        """
        if self.is_empty() or \
                (index == 0 and item.key <= self[index].key) or \
                (index == len(self) and self[index - 1].key <= item.key) or \
                (index > 0 and self[index - 1].key <= item.key <= self[index].key):

            if self.is_full():
                self._resize()

            self._shuffle_right(index)
            self.array[index] = item
        else:
            # the list isn't empty and the item's position is wrong wrt. its neighbourghs
            raise IndexError('Element should be inserted in sorted order')

    def __contains__(self, item: ListItem):
        """ Checks if value is in the list. """
        for i in range(len(self)):
            if self.array[i] == item:
                return True
        return False

    def _shuffle_right(self, index: int) -> None:
        """ Shuffle items to the right up to a given position. """
        for i in range(len(self), index, -1):
            self.array[i] = self.array[i - 1]

    def _shuffle_left(self, index: int) -> None:
        """ Shuffle items starting at a given position to the left. """
        for i in range(index, len(self)):
            self.array[i] = self.array[i + 1]

    def _resize(self) -> None:
        """ Resize the list. """
        # doubling the size of our list
        new_array = ArrayR(2 * len(self.array))

        # copying the contents
        for i in range(self.length):
            new_array[i] = self.array[i]

        # referring to the new array
        self.array = new_array

    def delete_at_index(self, index: int) -> ListItem:
        """ Delete item at a given position. """
        if index >= len(self):
            raise IndexError('No such index in the list')
        item = self.array[index]
        self.length -= 1
        self._shuffle_left(index)
        return item

    def index(self, item: ListItem) -> int:
        """ Find the position of a given item in the list. """
        pos = self._index_to_add(item)
        if pos < len(self) and self[pos] == item:
            return pos
        raise ValueError('item not in list')

    def is_full(self):
        """ Check if the list is full. """
        return len(self) >= len(self.array)

    def add(self, item: ListItem) -> None:
        """ Add new element to the list. """
        if self.is_full():
            self._resize()

        # find where to place it
        position = self._index_to_add(item)

        self[position] = item
        self.length += 1

    def _index_to_add(self, item: ListItem) -> int:
        """ Find the position where the new item should be placed. """
        low = 0
        high = len(self) - 1

        while low <= high:
            mid = (low + high) // 2
            if self[mid].key < item.key:
                low = mid + 1
            elif self[mid].key > item.key:
                high = mid - 1
            else:
                return mid

        return low

    def poke_reorder(self, criterion: str) -> None:
        """sorts list in non-increasing order, if two elements have the same value, they are arranged in the order
        Charmander, Bulbasaur, Squirtle.
        :pre: List is not empty
        :param criterion: criterion used to sort list
        :raises Exception: If the list is empty
        :complexity:
        """
        if self.is_empty():
            raise Exception("Sorted List is empty")

        # adding all items from sorted list to arrays based on pokemon name, updating key
        charm = []
        bulb = []
        squir = []
        miss = []
        length = len(self)
        num_battled = 0
        missingno_in_team = 0
        for i in range(length):
            # checking if all pokemon have battled
            if not self[i].value.get_name() == 'MissingNo':
                num_battled += self[i].value.get_battled()

            if criterion == 'lvl':
                self[i].key = self[i].value.get_level()
            elif criterion == 'hp':
                self[i].key = self[i].value.get_hp()
            elif criterion == 'atk':
                self[i].key = self[i].value.get_attack()
            elif criterion == 'def':
                self[i].key = self[i].value.get_defence()
            elif criterion == 'spd':
                self[i].key = self[i].value.get_speed()

            if self[i].value.get_name() == 'Charmander':
                charm.append(self[i])
            elif self[i].value.get_name() == 'Bulbasaur':
                bulb.append(self[i])
            elif self[i].value.get_name() == 'Squirtle':
                squir.append(self[i])
        # adding missingno
        if missingno_in_team:
            for i in range(length):
                if self[i].value.get_name() == 'MissingNo':
                    if num_battled < length - 1:
                        self[i].key = 1
                    miss.append(self[i])
        # create arr
        arr = miss + squir + bulb + charm
        # sorting arr in non-decreasing order
        for i in range(1, length):
            current = arr[i]
            j = i - 1
            while j >= 0 and arr[j].key > current.key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j+1] = current
        # deleting all items from sorted list
        for i in range(length):
            self.delete_at_index(0)
        # adding items from arr to sorted list
        for i in range(length):
            self.array[i] = arr[i]
            self.length += 1
