#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random
import math

# This function will say if the passed variable is prime number or not
def computeprime(n):
    if n%2==0:return False
    for i in range(2,n//2+1):
    	if(n%i==0):
    		return False
    return True

# This function implements the Euclidian algorithm to find H.C.F.  or GCD of two numbers
def computeHCF(x, y):
	while y:
		x, y = y, x % y
	return x

# creating a list of prime numbers between range 100 to 200, since larger the prime number more it is secured
prime_list=[x for x in range(105,200,2) if computeprime(x)]

# selecting two random  prime nummbers from the list
p = random.choice(prime_list)
q = random.choice(prime_list)

print("the two large prime numbers selected are %d,%d"%(p,q))

# calculating the product of selected prime numbers and euler's totient 
n = p*q # menghitung nilai RSA modulus
phi = (p-1)*(q-1)

print("the product of two selected prime numbers and euler's totient are : %d, %d"%(n,phi))

#generating public key t should be greater than 1 and less than n
gen_key = True
while gen_key:

	e = random.randint(2,n-1) # Menginput nilai public key
	if computeHCF(e,phi) ==1 :
		gen_key = False
		print("the encryption(public) key generated is %d" %e)


# generating private key
gen_key1 = True
while gen_key1:
	d = random.randint(2,100000) # Menginput nilai private key
	if (d*e)% phi == 1:
		gen_key1 = False
		print("the decryption(private) key generated is %d" %d)


#encryption activity, ord() is built in func which gives ascii number of each caharcter
x = input("enter the data to encrypt :") # Menginput string pada x
cryp_text = []
for i in range(len(x)):
	m = ord(x[i])
	c = (m**e)%n
	cryp_text.append(c)
print("the encrypted data is :")
print(cryp_text)

# Decryption activity, chr(ascii) will give the plain text 
plain_text = ""
for j in cryp_text :
	pt = (j**d)%n
	plain_text +=chr(pt)
print("the decrypted data is : " + plain_text)




# In[ ]:




