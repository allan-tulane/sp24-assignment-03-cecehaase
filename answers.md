# CMPS 2200 Assignment 3
## Answers

**Name:**_______Cece Haase__


Place all written answers from `assignment-03.md` here for easier grading.

1a.
   To solve this in greedy scheduler the value of 2^k that is less than or equal to N would be subtracted from N until N equals 0, for each subtraction the coin count would increase by one
1b. The largest optimal coin is being utilized in subtraction, so the least amount of coins will be used
1c. 
Work = O(logn) Span=O(logn)
2a
Suppose N=12 and there are denominations of 6, 5, and 1. In this case one 6 coin would be chosen then a 5 and a 1 to total to 10. In this case 3 coins are selected, but the optimal choice is 2 6 coins. 
2b This falls into optimal substructure since it uses the least amount of coins to total to the needed N value
2c
With dynamic programming we can solve this through creating a table n (money) * k (coins) filled in with each possible soultion of coins to equal the money. With a bottom up implementation the table would start with the least amount of money and most coins then work its way up. Work= O(n*k) Span=O(n)


   