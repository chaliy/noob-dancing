# coding=utf8
from copy import copy

def _trace(msg, trace):
    if trace:
        print(msg)


def _exh(data,a,b, trace=False):
    data[a], data[b] = data[b], data[a]
    _trace(str(data), trace)

def _less(a,b):        
    return a < b

def _last(iter):
    result = None
    for i in iter:
        result = i
    return result;

def insertion_sort_steps(data, trace=False):
    data = copy(data)
    
    for i in range(1,len(data)):        
        j = i
        while j > 0 and data[j] < data[j - 1]:
            data[j],data[j - 1] = data[j - 1], data[j]
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

    def exh(a,b):        
        data[a], data[b] = data[b], data[a]

    n = len(data)
    h = 1
    while h < n/3: h = (h * 3) + 1

    while h >= 1:
        for i in range(h, n):
            for j in range(i, h-1, -h):
                if data[j] < data[j-h]:
                    exh(j, j-h)
                    yield data
        h = int(h/3)

def shell_sort(data):
    return _last(shell_sort_steps(data))

def recursive_merge_sort(data, trace=False):
    _trace("Input: " + str(data), trace)

    def merge(data1, data2):
        sorted_data = [0 for x in range(len(data1) + len(data2))]

        data1_index = 0
        data2_index = 0

        _trace("Merge: " + str(data1) + " and " + str(data2), trace)

        # Merge

        for k in range(0, len(sorted_data)):
            if data1_index >= len(data1):
                sorted_data[k] = data2[data2_index]
                data2_index += 1
            elif data2_index >= len(data2):
                sorted_data[k] = data1[data1_index]
                data1_index += 1
            elif _less(data2[data2_index], data1[data1_index]):
                sorted_data[k] = data2[data2_index]
                data2_index += 1
            else:
                sorted_data[k] = data1[data1_index]
                data1_index += 1

        return sorted_data


    def rec_merge_sort(data):
        _trace("Split " +str(data), trace)

        l = len(data)

        if l == 1:
        	return data

        data1 = rec_merge_sort(data[:l//2])
        data2 = rec_merge_sort(data[l//2:])

        return merge(data1, data2)

    sorted_data = rec_merge_sort(data)
    _trace("Result: " + str(sorted_data), trace)
    return sorted_data




def shell_sort(data, trace=False):
    _trace("Input: " + str(data), trace)

    def exh(a,b):        
        data[a], data[b] = data[b], data[a]

    n = len(data)
    h = 1
    while h < n/3: h = (h * 3) + 1

    while h >= 1:
        for i in range(h, n):
            for j in range(i, h-1, -h):
                if data[j] < data[j-h]:
                    exh(j, j-h)
        h = h/3

    _trace("Result: " + str(data), trace)
    return data


def knuth_shuffle(data, trace=False):
    import random

    _trace("Input: " + str(data), trace)

    def exh(a,b):        
        data[a],data[b] = data[b], data[a]

    n = len(data)
    
    for i in range(1, n):
        new_i = random.randint(0, i)
        exh(new_i, i)

    _trace("Result: " + str(data), trace)
    return data


def quick_sort(data, trace=False):
    def partition(a, lo, hi):
        i = lo - 1
        j = hi
        while True:
            # Left
            while (_less(a[i], a[lo])):
                i += 1
                if i > hi: break
            # Right
            while (_less(a[lo], a[j])):
                j -= 1
                if (j < lo): break

            if (i >= j): break

            _exh(a, i, j)
        _exh(a, lo, j)
        return j

    def sort(a, lo, hi):
        if (hi <= lo):
            return
        j = partition(a, lo, hi)
        sort(a, lo, j-1)
        sort(a, j+1, hi)

    knuth_shuffle(data)
    sort(data, 0, len(data) - 1)

    return data

def dijkstra_quick_sort(data, trace=False):

    def compare(x,y):
        if x == y:
            return 0;
        elif x > y:
            return +1;
        else:
            return -1;

    def sort(a, lo, hi):
        if (hi <= lo): return
        lt = lo
        gt = hi
        v = a[lo]
        i = lo;
        while (i <= gt):
            c = compare(a[i], v)
            if (c < 0):
                lt += 1
                i += 1 
                _exh(a, lt, i, _trace)
            elif (c > 0): 
                gt -= 1
                _exh(a, i, gt, _trace)
            else: i += 1
        
        sort(a, lo, lt - 1)
        sort(a, gt + 1, hi)

    sort(data, 0, len(data) - 1)

    return data