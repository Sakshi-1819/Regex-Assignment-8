#!/usr/bin/env python
# coding: utf-8

# # Q1.Given an array of integers and a number, perform left rotations on the array.

# In[1]:


def rotate(arr,n):
    x=arr[n-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1];
    arr[0] = x

arr=[1,2,3,4,5]
n = len(arr)
print("Given array is")
for i in range(0,n):
    print(arr[i],end=" ")
rotate(arr,n)

print("\nRotated array is")
for i in range(0,n):
    print(arr[i], end=" ")


# # Q2.Arrange the array elements so that all negative numbers appears before all positive numbers.

# In[5]:


def rearrange(arr, n):

    j=0
    for i in range(0,n):
        if(arr[i]<0):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j=j+1
    print(arr)
arr=[-12,11,-13,-5,6,-7,5,-3,-6]
n=len(arr)
rearrange(arr, n)


# # Q3.Given an array of positive and negative numbers arrange them in an alteenate fashion such that every positive number is followed by negative.

# In[2]:


def rearrange(arr, n):

    arr.sort()
    i, j = 1, 1
    while j < n:
        if arr[j] > 0:
            break
        j += 1

    while (arr[i] < 0) and (j < n):

        arr[i], arr[j] = arr[j], arr[i]
        i += 2
        j += 1

    return (arr)

arr = [-2,3,4,-1]

ans = rearrange(arr, len(arr))
for num in ans:
    print(num, end=" ")


# In[3]:


def rearrange(arr, n):

    arr.sort()
    i, j = 1, 1
    while j < n:
        if arr[j] > 0:
            break
        j += 1

    while (arr[i] < 0) and (j < n):

        arr[i], arr[j] = arr[j], arr[i]
        i += 2
        j += 1

    return (arr)

arr = [-2,3,1]

ans = rearrange(arr, len(arr))
for num in ans:
    print(num, end=" ")


# In[4]:


def rearrange(arr, n):

    arr.sort()
    i, j = 1, 1
    while j < n:
        if arr[j] > 0:
            break
        j += 1

    while (arr[i] < 0) and (j < n):

        arr[i], arr[j] = arr[j], arr[i]
        i += 2
        j += 1

    return (arr)

arr = [-5,3,4,5,-6,-2,8,9,-1,-4]

ans = rearrange(arr, len(arr))
for num in ans:
    print(num, end=" ")


# # Q4. Program for Caesar Cipher in Python.

# In[6]:


def encrypt(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher
text = input("enter string: ")
s = int(input("enter the key: "))
print("original string: ", text)
print("after encryption: ", encrypt(text, s))

