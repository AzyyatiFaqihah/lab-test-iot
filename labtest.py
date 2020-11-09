#!/usr/bin/env python
# coding: utf-8

# In[64]:


number = input("Enter a number :")
newnumber = int(number)
binary = bin(newnumber)
print("binary : ", binary)
print("there are ", binary.count("1"), "bits with value 1" )


# In[81]:


letter = input("Write a simple sentence: ")
maxletter = len(letter);
print("Most letter in the sentence is : ", maxletter)


# In[78]:


word = input("Write a sentence: ")
numberofword = len(word.split())
print("There are ", numberofword, "word in the sentence")


# In[104]:


def multiply_by_three(x):
    return x*3

def subtract_numbers(j,k):
    return j-k
    
augmented_multiply_by_three(10) = print_arguments(multiply_by_three)
x = augmented_multiply_by_three(10)
print("Arguments are: ", x)
augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3,4)


# In[107]:


def multiply_output(y):
    return y
def multiply_by_five(x):
    return x * 5
    augmented_multiply_by_five = multiply_output(multiply_by_five)
    x = augmented_multiply_by_five(10)
    print(x)


# In[ ]:




