#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - because n cubed in this instance is just a mathematical calculation so the function will be linear and run equally to its input


b) O(n^2) - because the for loop runs n times and the while loop runs n times, so together are a polynomial. The additional multiplying is 0(1) so I think it stays a polynomial expression.


c) O(2^n) - because the function uses recursion but no cache so it's exponential.

## Exercise II

input
------
takes building with n stories
need to determine where floor f is within the stories
need to be quickly solved because time = more broken eggs

Strategy
--------
consider two different sorting methods
1. linear O(n)
2. binary O(log n)

Proposition
------------
I would take into consideration the size of the data structure I would be searching through. Since a building tower isn't likely crazy amounts of stories, linear runtime is more efficient for this. I would choose the simple linear search function.

Algorithm
----------
Loop through the array

If index is equal to the target return the index

Otherwise return not found

runtime complexity
------------------
O(n)
