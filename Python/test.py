

def isPattern(mystr, pattern, d):
    if len(pattern) == 1:
        # if we find a new pattern, or an old pattern matches what we already have in our dic
        if pattern not in d or d[pattern] == mystr:
            d[pattern] = mystr
            # check no duplicate patterns
            return len(d.values()) == len(set(d.values))
        return False

    maxMatchLen = len(mystr) - len(pattern) + 1
    for i in range(1,maxMatchLen+1):
        proposedMatch = mystr[:i]

        # optimization
        # if the pattern is already in our dict but it doesn't match skip it
        if pattern[0] in d and d[pattern[0]] != proposedMatch:
            continue

        d[pattern[0]] = proposedMatch

        ret = isPattern(mystr[i:], pattern[1:], d)

        if ret == True:
            return True
        if pattern[0] in d:
            del d[pattern[0]]

    return False



def testPattern():
    pat1 = "abba"
    s1 = "redbluebluered"
    # should return true
    
    pat1 = "aaaa"
    s1 = "redbluebluered"
    # should return false
    
    pat1 = "abcdb"
    s1 = "tobeornottobe"
    # should return true
    
    pat1 = "ababb"
    s1 = "tobeornottobe"
    # should return false
    
    pat1 = "aaa"
    s1 = "raiseraysraze"
    # should return false
    
    pat1 = "abcdeeeee"
    s1 = "onetwothreefourcowcowcowcowcow"
    # should return true
    
    pat1 = "abcdeeeee"
    s1 = "onetwothreefourcowcowcowcow"
    # should return false
    
    pat1 = "abcd"
    s1 = "thequickbrownfox"
    # should return true

    pat1 = "abba"
    s1 = "redredredred"
    # should return false
    
    pat1 = "aab"
    s1 = "111111"
    # should return true

    pat1 = "abb"
    s1 = "111111"
    # should return true

    pat1 = "abab"
    s1 = "111111"
    # should return true



# Given a board with train tracks (they can overlap)
# find number of squares that don't contain train tracks

### Merge Overlapping Intervals
#http://www.geeksforgeeks.org/merging-intervals/
def overlapping_intervals():
    """
    sample input:
    4 4 3 << n, m, k (row, col, # of tracks)
    2 2 3 << r, c1, c2 (row, start col, end col)
    3 1 4
    4 4 4

    output = 9


    sample input:
    4 5 7
    1 1 2
    1 4 4
    2 1 2
    2 2 3
    2 4 5
    4 1 2
    4 4 5

    output = 8
    """
    n, m, k = map(int, input().split())

    total = n*m
    d = {}

    for i in range(k):
        r, c1, c2 = map(int, input().split())

        if r not in d:
            d[r] = [(c1, c2)]
        else:
            d[r].append((c1, c2))

    for i in d.keys():
        lst = sorted(d[i])
        output = []
        left, right = lst[0]
        for j in lst[1:]:
            c1, c2 = j
            if c1 <= right:
                if c2 > right:
                    right = c2
            else:
                output.append((left, right))
                left, right = c1, c2
        output.append((left, right))

        for k in output:
            total -= k[1]-k[0]+1

    return total


# Given radio transmitters, houses and the range of the transmitters, 
# find minimum number of radio transmitters to install so all houses can have signal
def find_centers():
    """
    sample input:
    8 2 << n, k (num of elements, range)
    7 2 4 6 5 9 12 11 

    output:
    3

    sample input:
    9 2
    9 5 4 2 6 15 11 12 18

    output:
    4
    """
    n, k = map(int, input().split())
    x = sorted(list(map(int, input().split())))

    count = 1

    start = x[0]
    center = start
    for i in range(1, n):
        if x[i] - start <= k and x[i] - center <= k:
            center = x[i]
        if x[i] - start > 2*k or x[i] - center > k:
            count += 1
            start = x[i]
            center = x[i]

    return count

# Given an array of numbers choose a number. choose another number to the right of the first number
# such that the difference between the two is minimum. the first number must be greater than the second number.
def minloss():
    n = int(input())
    lst = list(map(int, input().split()))

    prefix = [(i, j) for i, j in enumerate(lst)]
    prefix.sort(key=lambda x: x[1])

    # make sure this number is big enough
    minloss = 10000000000 

    start = prefix[0]
    for i in prefix[1:]:
        if start[0] > i[0]:
            loss = i[1] - start[1]
            if loss < minloss:
                minloss = loss
        start = i


    return minloss

# HARD on Hackerrank
# given a list of numbers find the biggest xor value between two numbers
# 3, 6, 9, 5, 7
# 6 ^ 9 = 15.
# O(N) time and space
def xor(lst):
    s = lst[0] ^ lst[1] # ((a & b) ^ (a | b)) & (a ^ b) = a ^ b
    stack = [lst[0], lst[1]]
    for i in range(2, len(lst)):
        while(len(stack) != 0):
            s = max(s, stack[-1] ^ lst[i])

            if stack[-1] > lst[i]:
                stack.pop()
            else:
                break
        stack.append(lst[i])
    return s


def nextGreaterElement():
    a = [4, 5, 2, 25]
    b = [13, 7, 6, 12]

    s = []
    s.append(a[0])

    element =0
    next = 0

    for i in range(1, len(a)):
        next = a[i]

        if len(s) != 0:
            element = s.pop()

            while element < next:
                print(str(element) + " -- " + str(next))
                if len(s) == 0:
                    break
                element = s.pop()

            if element > next:
                s.append(element)

        s.append(next)

    print(s)

    while(len(s) != 0):
        element = s.pop()
        next = -1
        print(str(element) + " -- " + str(next))



if __name__=="__main__":
    mystr = 'redblueredblue'
    pattern = 'abab'
    print("%s - %s - %s"%(mystr, pattern, isPattern(mystr, pattern, {})))


    s1 = 'redbluebluered'
    p1 = 'abba'
    print("%s - %s - %s"%(s1, p1, isPattern(s1, p1, {})))

    # #overlapping_intervals()
    # print(xor([3, 6, 9, 5, 7]))


    # nextGreaterElement()










