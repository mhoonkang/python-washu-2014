# simulation and drawing graphs
# to use this code, you should install matplotlib module.

from sort import *
import random
import timeit
import pylab as plt

# simulation
def sort_sim(n, iter): # n is the number of elements in the list, iter is the number of iteration.
  sample = range(0,n)  
  unsorted = random.sample(sample, n) # randomly arrange n numbers
  T0 = timeit.Timer('mergesort(%s)'% unsorted, 'from __main__ import mergesort') # set timer for mergesort
  T1 = timeit.Timer('bubblesort(%s)'% unsorted, 'from __main__ import bubblesort') # set timer for bubblesort
  T2 = timeit.Timer('quicksort(%s)' % unsorted, 'from __main__ import quicksort') # set timer for quicksort
  tm = T0.timeit(number=iter) # record consumed time for excuting mergesort 'iter' times
  tb = T1.timeit(number=iter) # record consumed time for excuting bubblesort 'iter' times
  tq = T2.timeit(number=iter) # record consumed time for excuting quicksort 'iter' times
  return [tm, tb, tq]

# plot graphs for average time consumed for each sort method from size 1 to n by iterating 'iter' times
def plot(n=500, iter=10):
  time_merge = [] # list of average times consumed in merge sort from size 1 to n
  time_bubble = [] # list of average times consumed in bubble sort from size 1 to n
  time_quick = [] # list of average times consumed in quick sort from size 1 to n
  for i in range(n): # for size n data
    mtime = sort_sim(n, iter)[0] # total time for merge sort
    btime = sort_sim(n, iter)[1] # total time for bubble sort    
    qtime = sort_sim(n, iter)[2] # total time for quick sort    
    time_m = mtime/iter # then record the average time
    time_b = btime/iter
    time_q = qtime/iter
    time_merge.append(time_m) # append average time to the list
    time_bubble.append(time_b)  
    time_quick.append(time_q)  
  plt.rcParams['legend.loc'] = 'best' # locate the legend to best location
  plt.plot(range(1,n+1), time_merge, label = "merge sort") # plot for merge sort
  plt.plot(range(1,n+1), time_bubble, label = "bubble sort") # plot for bubble sort
  plt.plot(range(1,n+1), time_quick, label = "quick sort") # plot for quick sort
  plt.xlabel("the number of elements") # x-axis label
  plt.ylabel("average times in seconds") # y-axis label
  plt.legend() # add legend
  plt.savefig('plot.png')  # save the figure