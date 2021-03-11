import sympy as sp
import math as mt


def get_exp (n,p):
	
	if (n%p != 0):
		return 0
	
	else:
		return 1 + get_exp(n/p , p)


def get_Mobius(n):
	
	if (n == 1):
		return 1
	
	else:
		allpri= list(sp.primerange(1 , n+1))
		l=len(allpri)
		
		exp = allpri
		for i in range (0,l):
			exp[i]=get_exp(n , allpri[i])
			
		k=0
		for i in range(0,l):
			if(exp[i] != 0):
				k=k+1
		
		for j in range(0,l):
			if(exp[j] != 0 and exp[j] != 1):
				break

		if(j == l-1):
			return (-1)**k
		else:
			return 0



def get_Euler_Totient(n):
	
	if (n == 1):
		return 1
	
	else:
		phi = 0
		for i in range (1,n):
			if( mt.gcd(i,n) == 1):
				phi = phi + 1
		return phi
		


m = input("Enter a positive integer to calculate \u03BC and \u03A6: ")
n = int(m)

mu = get_Mobius(n)
phi = get_Euler_Totient(n)

print("\u03BC(" + m + ") = " + str(mu))
print("\u03A6(" + m + ") = " + str(phi))
