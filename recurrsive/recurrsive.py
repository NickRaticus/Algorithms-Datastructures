import array
from asyncio.windows_events import NULL
from mimetypes import init
from multiprocessing import Value
import os
from pickle import FALSE
import random
import string
from xml.etree.ElementTree import tostring
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(10))

fibonacci_cache = {}
def fibbonaci(n):
    print(f"{n},i")
    fiblist = []
    if n in fibonacci_cache:
        print(f"{n},a")
        return fibonacci_cache[n]
    if n == 1: 
        return 0
    if n == 2:
        return 1
    else:

        value = fibbonaci(n-1)+fibbonaci(n-2)
    fibonacci_cache[n] = value
    return value

#def recursive_folders(path):
#    dirs = os.listdir(path)
#    file_string = ""
#    for file in dirs:
#        if os.path.isfile(f"{path}\\{file}"):
#            print(file)
#            
#        if os.path.isdir(f"{path}\\{file}"):
#            print(file)
#            
#            recursive_folders(f"{path}\\{file}")
#recursive_folders("C:\\Users\\Niklas\\Downloads\\Skema-PDF-New-DB\\Skema-PDF-New-DB\\skemawpf")
def sortedarray():
    value = []
    for i in range(500):
        print("test")
        value.append(i)
    return value
sortedlist = sortedarray()

bigger=False
smaller=False
def binarysearch(list,high, target ,low ):
    if high >= low:
      mid = low + (high - low) // 2
      if mid == target:
          print("test1")
          return mid

      elif mid > target:
          return binarysearch(list, mid , target, low)
      elif mid < target:
          return binarysearch(list,high,target, mid)
print(binarysearch(sortedlist ,len(sortedlist), 40, 0,))


def InsertInSortedArray(arraysorted, element, current, workarray):
      if element < len(arraysorted):
          if element == current:
            workarray += [element]
            value = workarray[current]
            print(len(workarray)-2)
            if workarray[len(workarray)-2] == element :
                  InsertInSortedArray(arraysorted, element, current+1, workarray)
            
            InsertInSortedArray(arraysorted, element, current, workarray)
          else: 
              workarray += [arraysorted[current]]
              InsertInSortedArray(arraysorted, element, current+1, workarray)

      elif element >= len(arraysorted):
        arraysorted += [element]
        return arraysorted
      return workarray
array2 = []




def InsertInArrayBinary(arraysorted, element, current, workarray):

    index = (binarysearch(arraysorted ,len(arraysorted), element, 0,)-1)
    if index == current:
        workarray += [element]
        InsertInArrayBinary(arraysorted, element, current+1, workarray)
    elif current >= len(arraysorted)-1:
        workarray += [arraysorted[-1]]
        return
    elif index < current:
        workarray += [arraysorted[current]]
        InsertInArrayBinary(arraysorted, element, current+1, workarray)
    elif index > current:
        workarray += arraysorted[0:element]
        InsertInArrayBinary(arraysorted, element, element-1, workarray)

InsertInArrayBinary(sortedlist, 37, 0, array2)
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


    def backwards_traversal(data):
        data =  data.prev

        return data
class Lifo:
    def __init__(self):
        self.head = Node("head")
        self.size = 0


    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1 
    def pop(self):
        if self.size == 0:
            return None
        remove = self.head.next
        self.head.next = remove.next 
        self.size -= 1
        return remove.data
class LifoNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class Fifo:
    def __init__(self):
        self.head = None
        self.Tail = None
        self.size = 0
    def push(self, value):
        node = LifoNode(value)
        if self.size == 0:
            self.Tail = self.head = node
        else:
            
            self.Tail.next = node
            self.Tail = self.Tail.next
            
        self.size += 1
 
        
        
        
    def pop(self):
        if self.size == 0:
            return None
        remove = self.head
        self.head = remove.next
        self.size -= 1
        return remove.data
    def forward(self):
        values = []
        current = self.head
        while current != None:
            values.append(current.data)
            current = current.next
        print(values)
        return values

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.head = TreeNode(NULL)
        parent = self.head
fifo = Fifo()
for i in range(1, 10):
    fifo.push(i)
fifo.forward()
     