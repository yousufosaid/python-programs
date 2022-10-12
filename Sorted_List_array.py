"""
-------------------------------------------------------
Array version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164
__updated__ = "2022-02-10"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: target = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a sorted list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in source.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in source.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Index of beginning of subarray to search.
        low = 0
        # Index of end of subarray to search.
        high = len(self._values) - 1

        while low <= high:
            # Find the middle of the current subarray.
            # (avoids overflow on large values vs (low + high)//2
            mid = (high - low) // 2 + low

            if self._values[mid] > value:
                # search the left subarray.
                high = mid - 1
            else:
                # Default: search the right subarray.
                low = mid + 1
        self._values.insert(low, value)
        return

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list.
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the index of the first occurrence of key in
                the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        # Index of beginning of subarray to search.
        low = 0
        # Index of end of subarray to search.
        high = len(self._values) - 1

        while low < high:
            # Find the middle of the current subarray.
            # (avoids overflow on large values vs (low + high)//2
            mid = (high - low) // 2 + low

            if self._values[mid] < key:
                # Search the right subarray.
                low = mid + 1
            else:
                # Default: search the left subarray.
                high = mid

        # Deferred test for equality.
        if low == high and self._values[low] == key:
            i = low
        else:
            i = -1
        return i

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in source
        that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = self._binary_search(key)

        if i > -1:
            value = self._values.pop(i)
        else:
            value = None
        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = self._binary_search(key)

        if i > -1:
            value = deepcopy(self._values[i])
        else:
            value = None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty list"

        value = deepcopy(self._values[0])
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in source.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        i = self._binary_search(key)
        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(Sorted_List) to len(Sorted_List) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = len(self._values)
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of source.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of source (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        value = deepcopy(self._values[i])
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        i = self._binary_search(key)
        return i > -1

    def max(self):
        """
        -------------------------------------------------------
        Returns the maximum value in source.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find maximum of an empty list"

        value = deepcopy(self._values[-1])
        return value

    def min(self):
        """
        -------------------------------------------------------
        Returns the minimum value in source.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot find minimum of an empty list"

        value = deepcopy(self._values[0])
        return value

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in source.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in source (int)
        -------------------------------------------------------
        """
        i = self._binary_search(key)
        n = len(self._values)

        if i == -1:
            number = 0
        else:
            # Because the list is sorted, all values with the same
            # key are lumped together.
            number = 1
            i += 1

            while i < n and self._values[i] == key:
                i += 1
                number += 1
        return number

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from source. Source contains one and only one
        of each value formerly present in source. The first occurrence
        of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        i = 1
        # Note that we must call len(self._values) within the loop because
        # the list may grow smaller as values are cleaned out.
        while i < len(self._values):

            if self._values[i] == self._values[i - 1]:
                self._values.pop(i)
            else:
                i = i + 1
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source with index i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
                args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], otherwise
                the last value in source, value is removed from source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with copies of values that appear
        in both source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert len(self._values) == 0, "Target list must be empty"

        i = 0
        j = 0

        while i < len(source1._values) and j < len(source2._values):

            if source1._values[i] < source2._values[j]:
                # Skip the value in source1
                i += 1
            elif source1._values[i] > source2._values[j]:
                # Skip the value in source2
                j += 1
            else:
                # Values are the same - add the value if target is empty
                # or have not already added the value
                if len(self._values) == 0 or self._values[-1] != source1._values[i]:
                    self._values.append(deepcopy(source1._values[i]))
                i += 1
                j += 1
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert len(self._values) == 0, "Target list must be empty"

        i = 0
        j = 0

        while i < len(source1._values) and j < len(source2._values):

            if source1._values[i] < source2._values[j]:
                value = source1._values[i]
                # Skip the value in source1
                i += 1
            elif source1._values[i] > source2._values[j]:
                value = source2._values[j]
                # Skip the value in source2
                j += 1
            else:
                value = source1._values[i]
                i += 1
                j += 1

            if len(self._values) == 0 or self._values[-1] != value:
                # Add the new value if target is empty
                # or have not already added the value
                self._values.append(deepcopy(value))

        for value in source1._values[i:]:
            # Append one copy of each of the remaining values from source1
            # to the target.
            if len(self._values) == 0 or self._values[-1] != value:
                self._values.append(deepcopy(value))

        for value in source2._values[j:]:
            # Append one copy of each of the remaining values from source1
            # to the target.
            if len(self._values) == 0 or self._values[-1] != value:
                self._values.append(deepcopy(value))
        return

    def remove_many(self, key):
        """
        ---------------------------------------------------------
        Removes all values that match key in source.
        Use: source.remove_many(key)
        ---------------------------------------------------------
        Parameters:
            key - the key to match (?)
        Returns:
            None
        ---------------------------------------------------------
        """
        # Find first location of key.
        i = self._binary_search(key)

        if i > -1:
            while i < len(self._values) and self._values[i] == key:
                self._values.pop(i)
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. target1 contains the even indexed
        elements, target2 contains the odd indexed elements.
        Order of target1 and target2 is not significant.
        source is empty after the function executes.
        (iterative version)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - the even indexed elements of the list (Sorted_List)
            target2 - the odd indexed elements of the list (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        even = True

        while len(self._values) > 0:

            if even:
                target1._values.append(self._values.pop(0))
            else:
                target2._values.append(self._values.pop(0))
            even = not even
        return target1, target2

    def split(self):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. source becomes empty.
        Use:  target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (Sorted_List)
            target2 - a new List with <= 50% of the original List (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        # Split
        middle = len(self._values) // 2 + len(self._values) % 2
        target1._values = self._values[:middle]
        target2._values = self._values[middle:]
        self._values = []
        return target1, target2

    def split_key(self, key):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains all values < key,
        target2 all values >= key. source becomes empty. source is
        empty at end.
        Use:  target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            target1 - a new Sorted List with values < key (Sorted_List)
            target2 - a new Sorted List with values >= key (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()

        if len(self._values) > 0:
            if key < self._values[0]:
                target2._values = self._values
            elif key > self._values[-1]:
                target1._values = self._values
            else:
                i = self._binary_search(key)

                if i == -1:
                    i = 0
                    while key > self._values[i]:
                        i += 1
                target1._values = self._values[:i]
                target2._values = self._values[i:]

            self._values = []
        return target1, target2

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Values are sorted.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert len(self._values) == 0, "Target list must be empty"

        while len(source1._values) > 0 and len(source2._values) > 0:

            if source1._values[0] <= source2._values[0]:
                self._values.append(source1._values.pop(0))
            else:
                self._values.append(source2._values.pop(0))

        while len(source1._values) > 0:
            self._values.append(source1._values.pop(0))

        while len(source2._values) > 0:
            self._values.append(source2._values.pop(0))
        return

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are is_identical, i.e. same values appear
        in the same locations in both lists. (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (Sorted_List)
        Returns:
            identical - True if source contains the same values as target
                in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        identical = False
        n = len(self._values)

        # Lists must be the same length to be is_identical.
        if len(target) == n:
            i = 0

            # Compare each element, stop when the elements are not the same
            # or the end of the list is reached.
            while i < n and self._values[i] == target._values[i]:
                i += 1

            if i == n:
                identical = True
        return identical

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first item in source.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty list"

        value = self._values.pop(0)
        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            value - the next value in source (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
