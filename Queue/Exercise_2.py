# write an program to print binary of a number using recursion

def binary(n):
    if n > 1:
        binary(n//2)
    print(n % 2, end = '')    

binary(10)    

# Output: 1010

# Write a program to print binary numbers from 1 to 10 using Queue

def generate_binary(n):
    from collections import deque
    q = deque()
    q.append('1')
    while n > 0:
        n -= 1
        # here s1 is the binary number and s2 is the binary number which is going to be appended in the queue 
        # s1 is the binary number which is going to be printed 
        # eg : s1 = 1, s2 = 10, s1 = 10, s2 = 11, s1 = 11, s2 = 100, s1 = 100, s2 = 101, s1 = 101, s2 = 110, s1 = 110, s2 = 111, s1 = 111, s2 = 1000, s1 = 1000, s2 = 1001, s1 = 1001, s2 = 1010 
        # here popLeft() is used to pop the left most element from the queue ie, queue contains 1 and 10, 1 is popped and printed and 10 is popped and 11 is appended to the queue
        s1 = q.popleft()
        print(s1)
        s2 = s1
        q.append(s1 + '0')
        q.append(s2 + '1')

generate_binary(10)