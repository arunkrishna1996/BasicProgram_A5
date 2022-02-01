#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.	Write a Python Program to Find LCM?
a=int(input('enter num1\r'))
b=int(input('enter num 2\r'))
if a>b:
    greater=a
else:
    greater=b
while(True):
    if (greater%a==0) and (greater%b==0):
        LCM=greater
        break
    greater+=1
print('LCM of',a,'and',b,'is',LCM)


# In[10]:


#2.	Write a Python Program to Find HCF?
a=int(input('enter the number 1\r'))
b=int(input('enter the number 2\r'))
if a<b:
    lower=a
else:
    lower=b
for i in range(1,lower+1):
    if (a%i==0) and (b%i==0):
        HCF=i
print('HCF of ',a,'&',b,'is',HCF)


# In[4]:


#3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
a= int(input('enter a number\r'))
t1=a
t2=a
t3=a
l1=[]
l2=[]
l3=[]
while t1>0:
    c=t1%2
    l1.append(c)
    t1=t1//2
l1.reverse()
print('your binary is =',l1)
while t2>0:
    c1=t2%8
    l2.append(c1)
    t2=t2//8
l2.reverse()
print("octal number is",l2)
while t3>0:
    c2=t3%16
    l3.append(c2)
    t3=t3//16
l3.reverse()
print("hexa number is",l3)


# In[ ]:





# In[2]:


#4.	Write a Python Program To Find ASCII value of a character?
a=input("enter a character\r")
for i in a:
    print('ASCI Value of',i)
    print(ord(i))


# In[1]:


#5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
a1=int(input('enter num 1\r'))
a2=int(input('enter num 2\r '))
a3=input('enter the operation which you want to perform "add","sub","div","mult"')
if a3=='add':
    print('value equals',a1+a2)
if a3=='sub':
    print('value equals',a1-a2)
if a3=='div':
    print('value equals',a1/a2)
if a3=='mult':
    print('value equals',a1*a2)


# In[ ]:





# In[ ]:





# In[ ]:




