"""
1. Write a tester program that counts and displays the number of iterations 
    of the following loop: 
    
    while problemSize > 0:
        problemSize = problemSize // 2
​
​
2. Run the program you created in Exercise 1 using problem sizes of 
    1000, 2000, 4000, 10,000, and 100,000. As the problem size doubles 
    or increases by a factor of 10, what happens to the number of iterations?
​
​
3. The difference between the results of two calls of the function time.time() 
    is an elapsed time. Because the operating system might use the CPU for part 
    of this time, the elapsed time might not reflect the actual time that a 
    Python code segment uses the CPU. Browse the Python documentation for an 
    alternative way of recording the processing time, and describe how this 
    would be done.
​
"""

"""
1. Assume that each of the following expressions indicates the number of 
operations performed by an algorithm for a problem size of n. Point out 
the dominant term of each algorithm and use big-O notation to classify it. 
​
    a. 2^n - 4n^2 + 5n   O(2^n)
    b. 3n^2 + 6          O(n^2)
    c. n^3 + n^2 - n     O(n^3)
​
2. For problem size n, algorithms A and B perform n^2 and (1/2)n^2 + (1/2)n 
instructions, respectively. Which algorithm does more work? Are there particular 
problem sizes for which one algorithm performs significantly better than the 
other? Are there particular problem sizes for which both algorithms perform 
approximately the same amount of work?

They are the same b/c the dominant portion is the same with n^2. There is no 
performance advantage of one over the other.
​
3. At what point does an n^4 algorithm begin to perform better than a 2^n algorithm?

when n = 17
"""

"""
1. Suppose that a list contains the values 20, 44, 48, 55, 62, 66, 74, 88, 93, 99 
at index positions 0 through 9. Trace the values of the variables left, right, and 
midpoint in a binary search of this list for the target value 90. Repeat for the 
target value 44.
​
​
2(challenge). The method that’s usually used to look up an entry in a phone book is not 
exactly the same as a binary search because, when using a phone book, you don’t always go 
to the midpoint of the sublist being searched. Instead, you estimate the position of the 
target based on the alphabetical position of the first letter of the person’s last name. 
For example, when you are looking up a number for “Smith,” you look toward the middle of 
the second half of the phone book first, instead of in the middle of the entire book. 
Suggest a modification of the binary search algorithm that emulates this strategy for a 
list of names. Is its computational complexity any better than that of the standard 
binary search? 
​
"""
"""
1. Which configuration of data in a list causes the smallest number of exchanges 
in a selection sort? Which configuration of data causes the largest number of 
exchanges?
Ascending vs descending order
Sorted vs unsorted
​
 2. Explain the role that the number of data exchanges plays in the analysis of 
 selection sort and bubble sort. What role, if any, does the size of the data 
 objects play?

 Both of the strategies have a big-O of O(n^2) there for the size of n has a quadratic 
 effect on the exchanges
​
 3. Explain why the modified bubble sort still exhibits O(n^2) behavior on average.
 Because the modification checks to see if it had to swap anything allowing it to 
 end earlier. However, on average it will still have to do at least half the iterations
 of the outer loop
​
 4. Explain why insertion sort works well on partially sorted lists. 
 
"""