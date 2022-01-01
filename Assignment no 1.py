#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = '''Twinkle, twinkle, little star, 
   How I wonder what you are! '''
b = '''Up above the world so high, 
         Like a diamond in the sky. '''
print(a,b,a,sep=('\n'))


# In[2]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[3]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[ ]:


from math import pi

r = float(input ("Enter radius of circle : "))

print ("Area of the circle is: " + str(pi * r**2))


# In[ ]:


fname = input("Input your First Name : ")

lname = input("Input your Last Name : ")

print ("Hello " + lname + " " + fname)

print ("Hello " + lname + " " + fname)


# In[ ]:


# This program adds two numbers provided by the user
 
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
 
# Add two numbers
sum = float(num1) + float(num2)
 
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# In[ ]:





# In[ ]:





# In[ ]:




