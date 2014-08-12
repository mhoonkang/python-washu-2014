# sort by merge

# divide the input list into two lists(the first half and the last half of the input list)
# until the length of each list becomes less than or equal to 1.
def mergesort(unsorted):
    if len(unsorted) <= 1: 
      return unsorted
    middle = len(unsorted)/2
    first = mergesort(unsorted[:middle])
    last = mergesort(unsorted[middle:])
    
    return merge(first, last) # merge two split lists. 

def merge(first, last):
    i, j = 0, 0 # i is an index for the first half, j is an index for the second half.
    result = []
    while i<len(first) and j<len(last): # while the elements in the both of two lists are not exausted
        if first[i] <= last[j]:    # we compare the number of i in first list and j in the second list 
          result.append(first[i])  # then append smaller one to the new list 
          i+=1                     # then we compare the remaining number to new number by adding 1 
        else:                      # to the index of the list whose number was appended to the new list, 
          result.append(last[j])   # then do it again, again.....
          j+=1
    result += first[i:] # when all the elements are exhausted in either of the two lists, 
    result += last[j:]  # then we append the remaining numbers to the new list. 
    return result


# bubble sort
  
def bubblesort(unsorted):
   if len(unsorted) <= 1: return unsorted
   for i in range(len(unsorted)-1): # The greatest number will be stored in the last index
                                    # by running this whole code once. So we need to run this code
                                    # n times. (n=the number of elements in the list)
     for j in range( 1, len(unsorted) - i): # compare j-1th, jth number
       if unsorted[j-1] > unsorted[j]: # if jth number is greater than j-1th number
         temp = unsorted[j-1]          # then store j-1th number to temporary variable
         unsorted[j-1] = unsorted[j]   # store jth number in j-1th
         unsorted[j] = temp            # store j-1th number in jth. Do this n times.
   return unsorted

# quick sort (from www.pythonschoo.net)

def quicksort(unsorted): # this is a wrapper function.
    start = 0
    end = len(unsorted)-1
    return quick_sort(unsorted, start, end)
    
def quick_sort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quick_sort(myList, start, pivot-1)
        quick_sort(myList, pivot+1, end)
    return myList


def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right





