# coding=utf8
from copy import copy


def _exch(data,a,b):
    data[a], data[b] = data[b], data[a]


def _less(a,b):        
    return a < b


def _last(iter):
    result = None
    for i in iter:
        result = i
    return result


def insertion_sort_steps(data):
    data = copy(data)
    
    for i in range(1,len(data)):        
        j = i
        while j > 0 and data[j] < data[j - 1]:
            _exch(data, j, j - 1)
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
        _exch(data, i,m)
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
                    _exch(data, j, j-h)
                    yield data
        h = int(h/3)


def shell_sort(data):
    return _last(shell_sort_steps(data))


def merge(data1, data2):
    # NOTE does not uses inplace changes

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


def inplace_merge_top_down_sort_steps(a):

    # Port of Sedgewick impl

    steps = []

    def inplace_merge(a, aux, lo, mid, hi):
    
        for k in range(lo, hi+1):
            aux[k] = a[k]

        i = lo
        j = mid+1
        for k in range(lo, hi+1):        
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif _less(aux[j], aux[i]):
                a[k] = aux[j]
                j +=1
            else:
                a[k] = aux[i]
                i += 1    

    def sort(a, aux, lo, hi):
        if hi <= lo: 
            return
        mid = int(lo + (hi - lo) / 2)
        sort(a, aux, lo, mid)
        sort(a, aux, mid+1, hi)
        inplace_merge(a, aux, lo, mid, hi)
        steps.append(copy(a))
        
    aux = copy(a)
    sort(copy(a), aux, 0, len(a) - 1)

    return steps


def inplace_merge_top_down_sort(data):
    return _last(inplace_merge_top_down_sort_steps(data))


def recursive_merge_sort(data):
    # NOTE does not uses inplace changes

    def sort(data):

        l = len(data)

        if l == 1:
            return data

        data1 = sort(data[:l//2])
        data2 = sort(data[l//2:])

        if not _less(data2[0], data1[-1]):
            return data1 + data2

        return merge(data1, data2)

    return sort(data)


def merge_sort(data):
    # NOTE does not uses inplace changes

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

    n = len(data)
    
    for i in range(1, n):
        new_i = random.randint(0, i)
        _exch(data, new_i, i)
    
    return data


def quick_sort_steps(data):
    steps = []
    def partition(a, lo, hi):
        # TODO Fails on list("BBBBBAAABBBA")
        i = lo
        j = hi + 1
        v = a[lo]
        while True:
            # Left
            while i < hi:
                i += 1
                if not _less(a[i], v):
                    break
            # Right
            while j > lo:
                j -= 1
                if not _less(v, a[j]):
                    break

            if i >= j: break

            _exch(a, i, j)
        _exch(a, lo, j)
        return j

    def sort(a, lo, hi):
        if (hi <= lo):
            return

        j = partition(a, lo, hi)
        sort(a, lo, j-1)
        sort(a, j+1, hi)
        steps.append(copy(a))

    data = copy(data)
    sort(data, 0, len(data) - 1)

    return steps


def quick_sort(data):
    data = copy(data)
    knuth_shuffle(data)
    return _last(quick_sort_steps(data))


def dijkstra_quick_sort(data):

    def compare(x, y):
        if x == y:
            return 0
        elif x > y:
            return +1
        else:
            return -1

    def sort(a, lo, hi):
        if hi <= lo:
            return
        lt = lo
        gt = hi  
        i = lo
        v = a[lo]
        while i <= gt:
            c = compare(a[i], v)            
            if c < 0:
                _exch(a, lt, i)
                lt += 1
                i += 1 
            elif c > 0:
                _exch(a, i, gt)
                gt -= 1
            else:
                i += 1
        
        sort(a, lo, lt-1)
        sort(a, gt+1, hi)

    sort(data, 0, len(data) - 1)

    return data


def heap_sort_steps(data):

    steps = []

    def sink(data, k, N):
        while 2*k <= N:
            j = 2*k
            if j < N and _less(data[j-1], data[j]):
                j += 1
            if not _less(data[k-1], data[j-1]):
                break
            _exch(data, k-1, j-1)
            k = j
    
    data = copy(data)
    N = len(data)
    for k in range(int(N/2), 0, -1):        
        sink(data, k, N)

    while N > 1:
        _exch(data, 0, N-1)
        N -= 1
        sink(data, 1, N)

        steps.append(copy(data))

    return steps


def heap_sort(data):
    return _last(heap_sort_steps(data))



if __name__ == '__main__':
    data = ['frog', 'crab', 'seal', 'goat', 'wasp', 'mink', 'kiwi', 'moth', 'pony', 'bear', 'worm', 'slug', 'deer', 'carp', 'tuna', 'hoki', 'dove', 'hare', 'lion', 'duck', 'mule', 'swan', 'ibex', 'bass']

    # print(inplace_merge_top_down_sort_steps(data))