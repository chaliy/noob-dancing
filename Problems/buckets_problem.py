# Three Jug Problem - http://mathworld.wolfram.com/ThreeJugProblem.html
# decanting problems

solve = 4
bucket1 = 3
bucket2 = 5

#
# Lake -> bucket1
# bucket1 -> bucket2
# Lake -> bucket1
# bucket1 -> bucket2 # bucket1 with 1 galone
# bucket2 -> Lake
# bucket1 -> bucket2 # bucket2 with 1 galone 
# Lake -> bucket1
# bucket1 -> bucket2 # bucket2 with 4 galone
# solved

min_bucket = min(bucket1, bucket2)
max_bucket = max(bucket1, bucket2)        

# [min_bucket, max_bucket]

# the idea is to go though all possible variants
# - fill first bucket from lake
# - fill second bucket from lake
# - fill both buckets from lake
# - fill first bucket from second
# - fill second bucket from first

visited = {}

def go(cur, d, op):
    # check if already seen this combination
    # no need to go futher
    key = str(cur[0]) + "," + str(cur[1])
    if (visited.has_key(key)):
        return
    visited[key] = key
    print (">" * d) + "[" + key + "]: " + op

    # just in case :)
    if d > 15:
        raise Exception("Cannot solve")

    # check if we already there
    if (cur[0] == solve):
        print "First bucket have what you need"
        return
    if (cur[1] == solve):
        print "Second bucket have what you need"
        return

    if (cur[0] + cur[1] == solve):
        print "Sum of both buckets have what you need"
        return    

    # Go to next level
    if (cur[0] == 0): # first bucket is empty
        go([min_bucket, cur[1]], d+1, "fill first bucket from lake")

    if (cur[1] == 0): # second bucket is empty
        go([cur[0], max_bucket], d+1, "fill second bucket from lake")        

    if (cur[1] != 0):
        go([cur[0], 0], d+1, "empty second bucket")

    if (cur[0] != 0):
        go([0, cur[1]], d+1, "empty first bucket")

    # fill second from first
    d = min(cur[0], max_bucket - cur[1])
    go([cur[0] - d, cur[1] + d], d+1, "fill second bucket from first")
    
    # fill first from second
    d = min(cur[1], min_bucket - cur[0])
    go([cur[0] + d, cur[1] - d], d+1, "fill first bucket from second")
    
go([0,0], 0, "start")