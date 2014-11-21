# Hashmap.py for Example 39

def new(num_buckets = 256): # initializer, makes a list of num_bucket length
    """Initializes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to an
    index for the aMap's buckets."""
    return hash(key) % len(aMap) # convert string to a number, mod it to get a bucket wher this key can go

def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key) # uses this function to check where the key COULD be
    return aMap[bucket_id]

def get_slot(aMap, key, default = None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set) when not found
    """
    bucket = get_bucket(aMap, key)

    for i, kv in enumerate(bucket):
        k, v, = kv
        if key == k:
            return i, k, v # index key was found, key itself, value at that key
    return -1, key, default

def get(aMap, key, default = None):
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default = default) # gets all the key numbers and the value there
    return v # only returns the value

def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key) # see if key already exists in the bucket
    i, k, v = get_slot(aMap, key) # if i is a positive integer, then it already exists and will be replaced

    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not, append to create it
        bucket.append((key, value)) # add value to the list

def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key) # get the bucket the value is in

    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i] # delete the value
            break

def list(aMap): # prints out what is in the hashmap
    """Prints out what's in the Map."""
    for bucket in aMap: # gets each bucket in the hashmap
        if bucket:
            for k, v in bucket:
                print k, v # prints every slot in the bucket
