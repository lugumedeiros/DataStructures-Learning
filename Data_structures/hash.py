# A basic hash table using lists and a naive hash function, with support for insert, delete, and duplicate detection.
# Uses chaining (lists) to handle collisions and a Count-Min Sketch (with 3 simple hash functions) to approximate counts.
# Designed for learning purposes with intentionally poor hash functions to explore behavior and limitations.

class Hash:
    class CountMinSketch():
        # Count Min with 3 terrible hash funtions...
        def __init__(self, size_hash):
            self.counters = [[0]*size_hash for _ in range(3)]
            self.size_hash = size_hash

        def insert(self, number):
            key_1, key_2, key_3 = self._get_keys(number)
            self.counters[0][key_1] += 1
            self.counters[1][key_2] += 1
            self.counters[2][key_3] += 1

        def check(self, number):
            key_1, key_2, key_3 = self._get_keys(number)
            arr_1 = self.counters[0][key_1]
            arr_2 = self.counters[1][key_2]
            arr_3 = self.counters[2][key_3]
            return min(arr_1, arr_2, arr_3)
            
        def _get_keys(self, number):
            key_1 = (number * number * 9) % self.size_hash
            key_2 = ((number * number) + (number * 3)) % self.size_hash
            key_3 = (number * 13) % self.size_hash
            return (key_1, key_2, key_3)
    
    # Simple int hash just to test what I learned, with terrible hashFunctions
    # Didn't want to use sets, just normal arrays
    def __init__(self, hash_size, hashf_lst=None):
        if hashf_lst is None:
            self.hash_function = self.bad_hash_func

        self.hash = [None]*hash_size
        self.hash_size = hash_size

        self.count_min_sketch = self.CountMinSketch(hash_size)

    def insert(self, number):
        self.count_min_sketch.insert(number)
        
        key = self.hash_function(number) % self.hash_size
        
        # Test if key is empty
        if self.hash[key] is None:
            self.hash[key] = [number]
            return
        # test if number in key
        for value in self.hash[key]:
            if value == number:
                return
        # Add number to end of list
        self.hash[key].append(number)

    def delete(self, number):
        key = self.hash_function(number) % self.hash_size

        # Doesn't exist
        if self.hash[key] is None:
            return
        
        for idx, value in enumerate(self.hash[key]):
            # Try to find in array
            if value == number:
                self.hash[key].pop(idx)
                # Make it None if empty
                if len(self.hash[key]) == 0:
                    self.hash[key] = None

    def check_count(self, number):
        return self.count_min_sketch.check(number)

    # Terrible :D
    def bad_hash_func(self, number):
        return (3 * number * number) + (number * 9)
    
if __name__ == "__main__":

    # Create hash table with 10 slots
    h = Hash(10)

    # Insert values
    h.insert(5)
    h.insert(14)
    h.insert(5)  # Duplicate, will be ignored in hash table but counted again in Count-Min Sketch
    h.insert(15)
    print(h.hash)

    # Delete value
    h.delete(14)

    # Check estimated count (frequency) of a number
    print("Estimated count of 5:", h.check_count(5))
    print("Estimated count of 14:", h.check_count(14)) 

    # Directly inspect the hash table
    print(h.hash)  # May show 5 stored, but not 14 anymore