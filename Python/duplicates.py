# given array of len n containing elements 0 - n-1
# find whether or not it returns a duplicate

arr1 = [1, 2, 5, 3, 4, 0]
arr2 = [1, 1, 1, 1, 1, 2]
arr3 = [0, 1, 2, 3, 3, 4]
arr4 = [2, 4, 3, 5, 1, 0]

def findDuplicate(arr):
	for i in range(len(arr)):
		while i != arr[i]:
			val = arr[i]
			arr[i], arr[val] = arr[val], arr[i]

			if arr[i] == arr[val]:
				return True

	return False

def angle_between_hour_min(h, m):
	assert 0 <= h <= 23
	assert 0 <= m <= 59

	if h >= 12:
		h -= 12

	new_hr = (m/60 + h) * 30

	new_min = m/60 * 360

	angle = new_min - new_hr

	if angle > 180:
		angle = 360 - angle
	if angle < 0:
		angle = 360 + angle
		
	return angle


def tests():
	assert findDuplicate(arr1) == False
	assert findDuplicate(arr2) == True
	assert findDuplicate(arr3) == True
	assert findDuplicate(arr4) == False

	print("All tests passing")


if __name__=="__main__":
	#tests()

	print(angle_between_hour_min(12, 30))
	print(angle_between_hour_min(3, 30))
	print(angle_between_hour_min(9, 0))





	