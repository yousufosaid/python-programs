"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Yousuf Osaid
ID:      210793270
Email:   osai3270l@mylaurier.ca
__updated__ = "2022-01-18"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
# Constants

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    for element in source:
        queue.insert(element)
        
    
    source *= 0
        
def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(queue)):
        target.append(queue._values[i])
        
        
    for i in range (len(target)):
        queue.remove()
        
def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    for i in q:
        print(i)

    b= q.is_empty()
    print(f"is_empty: {b}")
    print()
    
    print(f"insert 10,22:")
    q.insert(10)
    q.insert(22)
    for i in q:
        print(i)
        
    value = q.remove()
    print(f"Value removed: {value}")
    for i in q:
        print(i)
    print()
    
    value = q.peek()
    print(f"Value peeked: {value}")
    print()
    
    length = len(q)
    print(f"Length of queue: {length}")
    
def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for element in source:
        pq.insert(element)
        
    source *= 0
    

    
    
def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    count = 0
    for element in pq:
        count += 1
        
    for i in range(count):
        value = pq.remove()
        target.append(value)
        
        

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    pq.insert(10)
    pq.insert(20)
    pq.insert(30)
    print("Insert 10,20 and 30:")
    for i in pq:
        print(i)
    
    print()
    
    print(f"is_empty t01: {pq.is_empty()}")
    print()
    
    
    print(f"Remove: {pq.remove()}")
    for i in pq:
        print(i)
    
    

    print(f"Peek: {pq.peek()}")
    return

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source)):
        llist.insert(i,source[i])
        
    source *= 0
    
    
def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    count = 0
    for element in llist:
        target.append(element)
        count += 1
        
    for i in range(count):
        llist.pop(-1)
        
def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    
    print(f"is_empty: {lst.is_empty()}")
    
    lst.insert(0, 10)
    lst.insert(1,20)
    print(f"Insert 10,20:")
    for i in lst:
        print(i)
        
    lst.remove(10)
    print(f"remove 10:")
    for i in lst:
        print(i)
    
    print(f"Count 20: {lst.count(20)}")
    
    lst.append(40)
    print("Append 40:")
    for i in lst:
        print(i)
        
    print(f"Index 20: {lst.index(20)}")
    
    print(f"find 20: {lst.find(20)}")
    
    print(f"Max: {lst.max()}")
    print(f"Min: {lst.min()}")
    
a=[]
list_test(a)