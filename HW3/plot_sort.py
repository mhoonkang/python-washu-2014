# simulation and drawing graphs
# to use this code, you should install matplotlib module.

from sort import *
import random
import timeit
import pylab as plt

# simulation
def sort_sim(n, iter): # n is the number of elements in the list, iter is the number of iteration.
  tm = []
  tb = []
  tq = []
  for i in range(iter): # do this loop 'iter' times
    sample = range(0,n)  
    unsorted = random.sample(sample, n) # randomly arrange n numbers
    T0 = timeit.Timer('mergesort(%s)'% unsorted, 'from __main__ import mergesort') # set timer for mergesort
    T1 = timeit.Timer('bubblesort(%s)'% unsorted, 'from __main__ import bubblesort') # set timer for bubblesort
    T2 = timeit.Timer('quicksort(%s)' % unsorted, 'from __main__ import quicksort') # set timer for quicksort
    tm.append(T0.timeit(number=1)) # append consumed time for excuting mergesort 
    tb.append(T1.timeit(number=1)) # append consumed time for excuting bubblesort
    tq.append(T2.timeit(number=1)) # append consumed time for excuting quicksort 
  return [sum(tm)/iter, sum(tb)/iter, sum(tq)/iter] # return average time for each sorting method

# plot graphs for average time consumed for each sort method from size 1 to n by iterating 'iter' times
def plot(n=500, iter=10):
  time_merge = [] # list where average times consumed in merge sort from size 1 to n to be stored
  time_bubble = [] # list where average times consumed in bubble sort from size 1 to n to be stored
  time_quick = [] # list where average times consumed in quick sort from size 1 to n to be stored
  for i in range(1,n+1): # for size n data
    mtime = sort_sim(i, iter)[0] # average time for merge sort
    btime = sort_sim(i, iter)[1] # average time for bubble sort    
    qtime = sort_sim(i, iter)[2] # average time for quick sort    
    time_merge.append(mtime) # append average time to the list
    time_bubble.append(btime)  
    time_quick.append(qtime)  
  plt.rcParams['legend.loc'] = 'best' # locate the legend to best location
  plt.plot(range(1,n+1), time_merge, label = "merge sort") # plot for merge sort
  plt.plot(range(1,n+1), time_bubble, label = "bubble sort") # plot for bubble sort
  plt.plot(range(1,n+1), time_quick, label = "quick sort") # plot for quick sort
  plt.xlabel("the number of elements") # x-axis label
  plt.ylabel("average times in seconds") # y-axis label
  plt.legend() # add legend
  plt.savefig('plot.png')  # save the figure

plot()