A = [5,4,3,2,1]
B = []
C = []

def move(n, source, target, auxiliary):
	if n > 0:
		#move n-1 disks out of the way onto auxiliary
		move(n-1, source, auxiliary, target)

		#move nth disk from source to target
		target.append(source.pop())

		print(A, B, C, "#########", sep='\n')

		#move n-1 disks from auxiliary back onto target
		move(n-1, auxiliary, target, source)

if __name__=="__main__":
	move(5, A, C, B)

