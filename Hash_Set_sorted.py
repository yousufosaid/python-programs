
# pylint: disable=protected-access

# Imports
# Use any appropriate data structure here.
from Sorted_List_array import Sorted_List

# Constants
SEP = '-' * 40
new_slot = Sorted_List

class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, capacity):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size capacity.
        Use: hs = Hash_Set(capacity)
        -------------------------------------------------------
        Parameter:
            capacity - size of initial table in Hash Set  (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._capacity = capacity
        self._table = []
        self._count = 0

        # Define the empty table.
        for _ in range(self._capacity):
            self._table.append(new_slot())

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """

        hk = hash(key) % self._capacity
        slot = self._table[hk]
        return slot


    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """

        slot = self._find_slot(key)
        
        return key in slot


    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """

        slot = self._find_slot(value)

        if value in slot:
            inserted = False
        else:
            inserted = True
            slot.insert(value)
            self._count += 1

            if self._count > (self._LOAD_FACTOR * self._capacity):
                self._rehash()
        return inserted


    def find(self, key):
        """
        ---------------------------------------------------------
        Returns a copy of the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """

        slot = self._find_slot(key)
        value = slot.find(key)
        return value



    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """

        slot = self._find_slot(key)
        value = slot.remove(key)

        if value is not None:
            self._count -= 1
        return value


    def _rehash(self):
        """
        ---------------------------------------------------------
        Creates a new larger table in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        temp_table = self._table
        # Increase the number of slots and define them.
        self._capacity = self._capacity * 2 + 1
        self._table = []

        for _ in range(self._capacity):
            self._table.append(new_slot())

        # Copy old data to new slots.
        while len(temp_table) > 0:
            old_slot = temp_table.pop(0)

            while not old_slot.is_empty():
                value = old_slot.remove_front()
                slot = self._find_slot(value)
                slot.insert(value)
        return


    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two hash sets are identical.
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
             target - another hash set (Hash_Set)
        Returns:
            identical - True if this hash set contains the same values
                as other in the same order, otherwise returns False.
        -------------------------------------------------------
        """

        is_identical = True
        i = 0

        while is_identical and i < len(self._table):
            is_identical = self._table[i].is_identical(target._table[i])
            i += 1
        return is_identical



    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        
        print()
        for slot_num in range(self._capacity):
            print('========================================')
            print('Slot {}'.format(slot_num))
            for value in self._table[slot_num]:
                print(value)
        return


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slot. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item

