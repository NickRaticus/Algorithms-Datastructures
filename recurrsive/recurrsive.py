import array
from asyncio.windows_events import NULL
from importlib.machinery import SOURCE_SUFFIXES
from mimetypes import init
from msilib import MSIMODIFY_MERGE
from multiprocessing import Value, current_process
import os
from pickle import FALSE
import random
from re import S
import string
from xml.etree.ElementTree import TreeBuilder, tostring
import math

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

        value = fibbonaci(n - 1) + fibbonaci(n - 2)
    fibonacci_cache[n] = value
    return value


# def recursive_folders(path):
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
# recursive_folders("C:\\Users\\Niklas\\Downloads\\Skema-PDF-New-DB\\Skema-PDF-New-DB\\skemawpf")
def sortedarray():
    value = []
    for i in range(500):
        print("test")
        value.append(i)
    return value


sortedlist = sortedarray()

bigger = False
smaller = False


def binarysearch(list, high, target, low):
    if high >= low:
        mid = low + (high - low) // 2
        if mid == target:
            print("test1")
            return mid

        elif mid > target:
            return binarysearch(list, mid, target, low)
        elif mid < target:
            return binarysearch(list, high, target, mid)


print(
    binarysearch(
        sortedlist,
        len(sortedlist),
        40,
        0,
    )
)


def InsertInSortedArray(arraysorted, element, current, workarray):
    if element < len(arraysorted):
        if element == current:
            workarray += [element]
            value = workarray[current]
            print(len(workarray) - 2)
            if workarray[len(workarray) - 2] == element:
                InsertInSortedArray(arraysorted, element, current + 1, workarray)

            InsertInSortedArray(arraysorted, element, current, workarray)
        else:
            workarray += [arraysorted[current]]
            InsertInSortedArray(arraysorted, element, current + 1, workarray)

    elif element >= len(arraysorted):
        arraysorted += [element]
        return arraysorted
    return workarray


array2 = []


def InsertInArrayBinary(arraysorted, element, current, workarray):

    index = (binarysearch(arraysorted, len(arraysorted), element, 0,)- 1)
    if index == current:
        workarray += [element]
        InsertInArrayBinary(arraysorted, element, current + 1, workarray)
    elif current >= len(arraysorted) - 1:
        workarray += [arraysorted[-1]]
        return
    elif index < current:
        workarray += [arraysorted[current]]
        InsertInArrayBinary(arraysorted, element, current + 1, workarray)
    elif index > current:
        workarray += arraysorted[0:element]
        InsertInArrayBinary(arraysorted, element, element - 1, workarray)


InsertInArrayBinary(sortedlist, 37, 0, array2)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def backwards_traversal(data):
        data = data.prev

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
            print(self.Tail.data)
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
        self.root = None

    def search(self, Value, current):
        if self.root == None:
            return
        else:
            if current.value == Value:

                return current
            else:
                if current.value >= Value:
                    current = current.left
                    return self.search(Value, current)
                elif current.value < Value:
                    current = current.right
                    return self.search(Value, current)

    def PrintStructure(self, current, treelist):
        if self.root == None:
            return
        if current.left != None:
            parent = current.parent
            if parent == None:
                            treelist.append(f"({current.value} 'parent':None)")
            else:
             treelist.append(f"({current.value} 'parent':{parent.value})")
            treelist.append(("left"))
            self.PrintStructure(current.left, treelist)
            if current.right != None:
                parent = current.parent
                if parent == None:
                            treelist.append(f"({current.value} 'parent':None)")
                else:
                 treelist.append(f"({current.value} 'parent':{parent.value})")
                treelist.append(("right"))
                self.PrintStructure(current.right, treelist)
            return
        if current.right != None:
            parent = current.parent
            treelist.append(f"({current.value} 'parent':{parent.value})")
            treelist.append(("right"))
            self.PrintStructure(current.right, treelist)
            if current.left != None:
                parent = current.parent
                treelist.append(f"({current.value} 'parent':{parent.value})")
                treelist.append(("left"))
                self.PrintStructure(current.left, treelist)
            return
    def PrintTree(self, current, treelist):

        if self.root == None:
            return
        else:

            if current.left != None:
                self.PrintTree(current.left, treelist)
                if current.right != None:
                    treelist.append(current.value)
                    self.PrintTree(current.right, treelist)
                else:
                   treelist.append(current.value)
                return treelist

            if current.right != None:
                if current.left != None:
                    #treelist.append(current.value)
                    self.PrintTree(current.left, treelist)
                treelist.append(current.value)
                self.PrintTree(current.right, treelist)
                return treelist
            treelist.append(current.value)
            return treelist

    def pop(self, value):
        if self.root == None:
            return
        else:
            node = self.search(value, self.root)
            left = node.left
            right = node.right
            parent = node.parent
            if parent.left == node:
                parent.left = None
            if parent.right == node:
                parent.right = None

            node = None

            if left != None:
                left.parent = None
                self.push(left)
            if right != None:
                right.parent = None
                self.push(right)

    def push(self, Value):
        if self.root == None:
            node = TreeNode(Value)
            self.root = node
        else:
            current = self.root

            while current != None:
                if type(Value) == TreeNode:
                    node = Value
                    if current.value >= Value.value:
                        if current.left == None:
                            node.parent = current
                            parent = node.parent
                            parent.left = node
                            current.left = node
                            print(f"{Value}, Value")
                            return
                        else:
                            current = current.left
                    elif current.value < Value.value:
                        if current.right == None:

                            node.parent = current
                            parent = node.parent
                            parent.right = node
                            current.right = node
                            print(f"{Value.value}, Value")
                            return
                        else:
                            current = current.right
                else:
                    node = TreeNode(Value)
                    if current.value >= Value:
                        if current.left == None:
                            node.parent = current
                            current.left = node
                            print(f"{Value}, Value")
                            return
                        else:
                            current = current.left
                    elif current.value < Value:
                        if current.right == None:
                            node = TreeNode(Value)
                            node.parent = current
                            current.right = node
                            print(f"{Value}, Value")
                            return
                        else:
                            current = current.right
sorted_list = []
unsorted_list = [2,5,1,46,6,8,2,9,10]
index_list = []
def sortingalgo(sorted_list, unsorted_list, current, current_index, index, index_list):
        if len(sorted_list) == len(unsorted_list)-1:
            sorted_list += [unsorted_list[-1]]
            
        elif unsorted_list[current_index] == unsorted_list[-1]:
            if sorted_list == []:

              sorted_list += [current]
              index_list += [index]
              sortingalgo(sorted_list,unsorted_list, unsorted_list[0], 0, index, index_list)
            else:
                  isthere = False
                  for i in index_list:
                      if i == index:
                            isthere = True
                            sortingalgo(sorted_list,unsorted_list, 50, 0, index, index_list)
                  if isthere == False:
                      sorted_list += [current]
                      index_list += [index]
                      sortingalgo(sorted_list,unsorted_list, unsorted_list[0], 0, index, index_list)


        elif current >= unsorted_list[current_index]:
            isthere = False
            for i in index_list:

                if i == current_index:
                    isthere = True
            if isthere == True:
                current_index = current_index+1
                
            else:
              index = current_index
              current = unsorted_list[current_index]
              current_index = current_index+1
            sortingalgo(sorted_list,unsorted_list, current, current_index, index, index_list)
        elif current < unsorted_list[current_index]:
            current_index = current_index+1
            sortingalgo(sorted_list,unsorted_list, current, current_index, index, index_list)
        

    #if unsorted_list[current_index] == unsorted_list[-1]:
    #    sorted_list += [current]
    #else:
    #    isthere = False
    #    for i in index_list:
    #        if i == unsorted_list[current_index]:
    #            isthere = True
    #            current_index = current_index+1
    #            sortingalgo(sorted_list,unsorted_list, current, current_index, index, index_list)
    #    if isthere == False:
    #        if unsorted_list[current_index] > sorted_list[current_index]:
    #          index_list += [current_index]
    #          current_index = current_index+1
    #          sorted_list += [unsorted_list[current_index]]
    #          sortingalgo(sorted_list,unsorted_list, current, current_index, index, index_list)

def insertinarray(unsorted_list, sorted_list, current_index, current):
    
    sortedlist1 = []
    sortedlist2 = []
    isinserted = False
            


def insertsortingalgo(sorted_list, unsorted_list, current, current_index, index, index_list):
    if len(unsorted_list) == current:
        insertsortingalgo(sorted_list,unsorted_list, current, current_index, index,index_list)
    if len(unsorted_list) == current_index:
        insertsortingalgo(sorted_list,unsorted_list, current, current_index, index,index_list)
 
    if current == 0:
        sorted_list = [2,5,1,46,6,8,2,9,10]
        current = current+1
        insertsortingalgo(sorted_list,unsorted_list, current, current_index, index,index_list)
    else:
            if sorted_list[current_index] > sorted_list[current]:
                current_index = current_index+1
                insertsortingalgo(sorted_list,unsorted_list, current, current_index, index, index_list)
            if sorted_list[current_index] <= sorted_list[current]:
                   currentitem = sorted_list[current]
                   isinserted = False
                   index = 0
                   
                   for i, value in enumerate(sorted_list):
                       if value >= sorted_list[current] and isinserted == False:
                           isinserted = True
                           index = i
                           if i == current:
                               break

                           sorted_list[i] = unsorted_list[current]
                           if i >= index and i != current:
                            isin = False
                            for a in index_list:
                                   if a == i and i != current:
                                       isin = True
                            if isin == False:
                              if i == len(unsorted_list)-1:
                                 sorted_list += [unsorted_list[i]]
                                 break
                              else:
                                  if sorted_list[i+1] == unsorted_list[i]:
                                     unsorted_list = sorted_list[0:index_list[-1]+1]+unsorted_list[index_list[-1]+1:]
                                     sorted_list[i+1] = sorted_list[i]
                                     index_list = []
                                  else:
                                   sorted_list[i+1] = unsorted_list[i]
                                   index_list += [current]

                       elif isinserted == True and i > current:
                           break
                       elif i > index and i != current and isinserted == True:
                           isin = False
                           for a in index_list:
                                   if a == i and i != current:
                                       isin = True
                           if isin == False:
                            if i == len(unsorted_list)-1:
                                sorted_list += [unsorted_list[i]]
                                break
                            else:
                             sorted_list[i+1] = unsorted_list[i]
                           
                   
                   current_index = current_index+1
                   current = current+1
                    
                   insertsortingalgo(sorted_list, unsorted_list,current, current_index, index,index_list)
def insertionSortRecursive(arr,n): 
    # base case 
    if n<=1: 
        return
      
    # Sort first n-1 elements 
    insertionSortRecursive(arr,n-1) 
    '''Insert last element at its correct position 
        in sorted array.'''
    last = arr[n-1] 
    j = n-2
      
      # Move elements of arr[0..i-1], that are 
      # greater than key, to one position ahead 
      # of their current position  
    while (j>=0 and arr[j]>last): 
        arr[j+1] = arr[j] 
        j = j-1
  
    arr[j+1]=last             

insertionSortRecursive(unsorted_list, len(unsorted_list))
def bubblesort(unsorted_list, n, i, j):
        if unsorted_list[n] >= unsorted_list[n-1]:
            bubblesort(unsorted_list, n-1, i, j)

        else:
            if n != 0:
             unsorted_list[n], unsorted_list[n-1] = unsorted_list[n-1], unsorted_list[n]
            if n == 0:
                if j == i:
                    return unsorted_list
                else:
                  j = i
                  
                  bubblesort(unsorted_list, len(unsorted_list)-1,i,j)
            else:
                i=i+1
                bubblesort(unsorted_list, n-1, i,j)
def quicksort(sourcelist, output):
        if sourcelist == []:
            return
        pivot = [sourcelist[0]]
        j = 0
        i = 1
        right = []
        left = []
        while (j < len(sourcelist)-1):
            if pivot < [sourcelist[i]]:
                right += [sourcelist[i]]
                
                
                j = j+1
                i = i+1
            else:
                    output += [sourcelist[i]]
                    left += [sourcelist[i]]
                    j = j+1
                    i = i+1
        output += pivot

        
        quicksort(right, output)
def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)

class MinHeap:
    def __init__(self):
        self.root = None
    def search(self, Value, current):
        if self.root == None:
            return
        else:

            if Value == None:
                if current.right == None:

                    return current
                elif current.left == None:
                    return current
                else:

                   current_left = current.left
                   current_right = current.right
                   if current_left.left == None:
                       return self.search(Value, current.left)
                   elif current_right.right == None:
                       return self.search(Value, current.right)
                   else:
                        self.search(Value, current.left)
                        self.search(Value, current.right)
            elif Value != None:
              if current.value >= Value.value and Value != None:
                  #new_current = current.parent
                  #new_current.value = current.value
                  #current_parent = current.parent
                  #current_parent.left = current.left
                  #current_parent.right = current.right
                  #current, current.parent = current.parent, current
                  #current = current.parent
                  if current.left == Value:
                   current_left = Value.left
                   current.right, Value.right = Value.right, current.right
                   Value.left = current
                   current.left = current_left

                  else:
                   current_right = Value.right
                   current.left, Value.left, = Value.left, current.left
                   Value.right = current
                   current.right = current_right


                  Value.parent = current.parent
                  current.parent = Value
                  

                  return self.search(Value, current)
              elif current.value < Value.value and Value.value != None:
                  return current
            else:

                     return self.search(Value, current.left)
            if current.left == None or current.right == None or current.parent == None and Value.value != None:
                
                return current
                     
    def push(self, Value):
         if self.root == None:
          node = TreeNode(Value)
          self.root = node
         else: 
            new_node = TreeNode(Value)
            parent = self.search(None, self.root)
            if parent.right == None and Value <= parent.value:
                parent.right = new_node
            else:
                
                parent.left = new_node
            
            new_node.parent = parent

            node = self.search(new_node, parent)
            new_node.parent = node.parent

            if new_node.value <= node.value:
                node_right = node.right
                node.right = node_right.right
                node_left = node.left
                node_left.parent = new_node
                new_node.right = node
                node.left,new_node.left = new_node.left, node.left
                
                node.parent = new_node
                if new_node.parent == None:
                    self.root = new_node



             




heap = MinHeap()
heap.push(5)
heap.push(6)
heap.push(2)
heap.push(1)
heap.push(3)
merge_sort([2,5,3,1,6,8,2,9])
quicksort([2,5,3,1,6,8,2,9,10,46,9,3], [])        
bubblesort([2,5,3,1,6,8,2,9,10,46,9], len(unsorted_list)-1, 0, 0)
fifo = Fifo()
fifo.forward()
tree = Tree()
for i in range(1, 10):
    tree.push(i)
    tree.push(3)
    tree.push(4)
    print(i)
tree.pop(4)
tree.push(1)
treelist = []
treelist1 = []
tree.PrintTree(tree.root, treelist)
tree.PrintStructure(tree.root, treelist1)
print(treelist)
