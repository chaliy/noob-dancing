# coding=utf8
from copy import copy

def _exh(data,a,b):
    data[a], data[b] = data[b], data[a]

def _less(a,b):        
    return a < b

def _last(iter):
    result = None
    for i in iter:
        result = i
    return result;

def insertion_sort_steps(data):
    data = copy(data)
    
    for i in range(1,len(data)):        
        j = i
        while j > 0 and data[j] < data[j - 1]:
            _exh(data, j, j - 1)
            yield data
            j -= 1

def insertion_sort(data):
    return _last(insertion_sort_steps(data))

def selection_sort_steps(data):
    data = copy(data)

    for i in range(len(data)):
        m = i
        for j in range(i, len(data)):
            if _less(data[j], data[m]):
                m = j
        _exh(data, i,m)
        yield data

def selection_sort(data):
    return _last(selection_sort_steps(data))

def shell_sort_steps(data):
    data = copy(data)

    n = len(data)
    h = 1
    while h < n/3: 
        h = (h * 3) + 1

    while h >= 1:
        for i in range(h, n):
            for j in range(i, h-1, -h):
                if data[j] < data[j-h]:
                    _exh(data, j, j-h)
                    yield data
        h = int(h/3)

def shell_sort(data):
    return _last(shell_sort_steps(data))

def merge(data1, data2):
    s = data1 + data2
    i1 = 0
    i2 = 0

    # Merge
    for k in range(len(s)):
        if i1 >= len(data1):
            s[k] = data2[i2]
            i2 += 1
        elif i2 >= len(data2):
            s[k] = data1[i1]
            i1 += 1
        elif _less(data2[i2], data1[i1]):
            s[k] = data2[i2]
            i2 += 1
        else:
            s[k] = data1[i1]
            i1 += 1

    return s


def recursive_merge_sort(data):


    def sort(data):

        l = len(data)

        if l == 1:
        	return data

        data1 = sort(data[:l//2])
        data2 = sort(data[l//2:])

        if _less(data2[0], data1[-1]) == False:
            return data1 + data2

        return merge(data1, data2)

    return sort(data)

def merge_sort(data):

    N = len(data)
    s = copy(data)

    sz = 1
    while sz < N:

        lo = 0
        while lo < N-sz:
            mid = lo+sz
            hi = min(lo+sz+sz, N)

            s[lo:hi] = merge(s[lo:mid], s[mid:hi])
            lo += sz+sz

        sz = sz+sz


    return s



def knuth_shuffle(data):
    import random    

    def exh(a,b):        
        data[a],data[b] = data[b], data[a]

    n = len(data)
    
    for i in range(1, n):
        new_i = random.randint(0, i)
        exh(new_i, i)
    
    return data


# def quick_sort(data):
#     def partition(a, lo, hi):
#         i = lo - 1
#         j = hi
#         while True:
#             # Left
#             while (_less(a[i], a[lo])):
#                 i += 1
#                 if i > hi: break
#             # Right
#             while (_less(a[lo], a[j])):
#                 j -= 1
#                 if (j < lo): break

#             if (i >= j): break

#             _exh(a, i, j)
#         _exh(a, lo, j)
#         return j

#     def sort(a, lo, hi):
#         if (hi <= lo):
#             return
#         j = partition(a, lo, hi)
#         sort(a, lo, j-1)
#         sort(a, j+1, hi)

#     knuth_shuffle(data)
#     sort(data, 0, len(data) - 1)

#     return data

# def dijkstra_quick_sort(data):

#     def compare(x,y):
#         if x == y:
#             return 0;
#         elif x > y:
#             return +1;
#         else:
#             return -1;

#     def sort(a, lo, hi):
#         if (hi <= lo): return
#         lt = lo
#         gt = hi
#         v = a[lo]
#         i = lo;
#         while (i <= gt):
#             c = compare(a[i], v)
#             if (c < 0):
#                 lt += 1
#                 i += 1 
#                 _exh(a, lt, i)
#             elif (c > 0): 
#                 gt -= 1
#                 _exh(a, i, gt)
#             else: i += 1
        
#         sort(a, lo, lt - 1)
#         sort(a, gt + 1, hi)

#     sort(data, 0, len(data) - 1)

#     return data


if __name__ == '__main__':
    data = [29,100,130,4,6,13,19,20]

    # for step in shell_sort_steps(data):    
    #     print("#", step)

    #print(merge_sort(data))