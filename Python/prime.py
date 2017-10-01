import math

def isprime(n):
	if n<2:
		return False
	elif n == 2 or n == 3:
		return True
	else:
		return min([n % e for e in range(2, int(math.sqrt(n))+1)]) != 0


# returns a list of prime factors
def primefactors(n):
    fac = []
    d = 2
    while d**2 <= n:
        while n%d == 0:
            fac.append(d)
            n//=d
        d+=1

    if n > 1:
        fac.append(n)

    return fac


"""
return smallest x where the product of x's digits = n

input: 26
output: -1

input: 10
output: 25

input: 128 (2^7)
output: 288

"""
def findXnumber(n):

    fac = primefactors(n)

    q = [2,3,5,7,9]
    if len(set(fac) - set(q)) > 0:
        return -1

    nonmerge = [i for i in fac if i > 4]
    pre = [i for i in fac if i == 2 or i == 3]
    post = []

    while len(pre) > 1:
        if pre[-1] * pre[-2] < 10:
            val = pre[-1] * pre[-2]
            pre.pop()
            pre.pop()
            if val == 6 or val == 8 or val == 9:
                post.append(val)
            else:
                pre.append(val)
        
    lst = pre + post + nonmerge
    lst.sort()

    return ''.join([str(i) for i in lst])




def myPow(x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
            return myPow(x, n)
        
        if n == 0:
            return 1
        if n == 1:
            return x
            
        if n % 2 == 1:
            return x * myPow(x*x, (n-1)/2)
        else:
            return myPow(x*x, n/2) 


if __name__=="__main__":
	# print(isprime(234))
	# print(isprime(2344354523))
	# #print(isprime(234721234523462345921))

	# print(myPow(8.03241, 3))

    arr = [100, 26, 128, 216]
    for i in arr:
        print(i, findXnumber(i))

    #v = primefactors(278)
    #print(v)




