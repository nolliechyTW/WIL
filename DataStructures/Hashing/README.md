# Hashing
Hashing is a storage and retrival technique.
- Why do we need Hashing?
    - **Efficient Data Retrieval**: Enables fast data lookup, especially in hash tables, leading to efficient data storage and retrieval.
    - **Security**: Ensures data integrity and security, making it vital for verifying data integrity, securely storing passwords, and other cryptographic applications.
    - **Cryptography**: Fundamental for creating digital signatures and secure transactions, especially in blockchain and cryptocurrencies.
    - **Data Deduplication**: Helps in identifying and storing only unique data instances, saving storage space.
    - **Load Balancing and Caching**: Useful in distributing data evenly across servers in distributed systems and implementing efficient caching mechanisms.
    - **Unique Identifiers**: Generates unique identifiers for items within large datasets, aiding in tracking and management.

- Hash Systems?
    - Hash function: `%`
        - follow SUHA: Simple uniform hashing assumption
    - Hash table: `array`

- Two Types of Hashing
    - Open hashing and closed hashing

- Hashing with Collision Resolution Techniques
    - When implementing a hash table, *collisions* occur when *two keys hash to the same index or "home slot"*. Efficiently resolving these collisions is crucial to maintaining the performance of the hash table. Here’s a streamlined approach:
        1. Compute the Home Slot:
            The home slot for a key `i` is determined using a hash function `h`, defined as `h(i) = i % m`, where `m` is the size of the hash table. This function maps each key to a specific index in the table.
        2. Probe Sequence for Collision Resolution:
            If the calculated home slot is already occupied, indicating a collision, a probe sequence is initiated to find an alternate slot. The position for the next probe, `pos`, is calculated as `pos = (h(k) + P(k, i)) % m`, where:
                - `h(k)` is the original hash value of the key k.
                - `P(k, i)` is the probe function that provides the offset from the home slot, dependent on the probing iteration `i` and possibly the key `k`.
                - `% m` ensures that the probing wraps around the hash table if it exceeds the table size.


## Open Hashing
- The slot in the HT contains reference to a Linked List
Open hashing, also known as *separate chaining*, is a strategy used in hash tables to handle collisions by allowing multiple elements to be stored at the same index in the table. Unlike closed hashing, where collisions are resolved within the hash table itself through probing, open hashing stores colliding elements outside the main table structure, typically using linked lists or other data structures. 

Here are the key concepts involved in open hashing:

1. Chaining: When a collision occurs (i.e., when two or more keys hash to the same index), the new key is added to a chain (for example, a linked list or a binary search tree) at that index. This allows multiple keys to be stored at the same location without requiring any special probing sequence.

2. Linked Lists: The most common way to implement chaining is through linked lists. Each index in the hash table points to the head of a linked list, and all keys that hash to that index are stored in the list.

3. Binary Search Trees: For tables with a high load factor or where the distribution of keys might lead to long chains, binary search trees (BSTs) can be used instead of linked lists. This can help keep the worst-case search time logarithmic in the size of the chain, compared to linear time with linked lists.

Best Practices for Using Open Hashing:

1. Choosing the Right Data Structure for Chains: While linked lists are simple and effective for short chains, consider using more sophisticated structures like BSTs or even self-balancing trees (like AVL or Red-Black trees) for the chains if you anticipate long chains, as they can significantly improve search times within a chain.

2. Maintain Low Load Factors: Although open hashing can handle high load factors better than closed hashing by avoiding clustering, keeping the load factor relatively low is still beneficial for performance. A lower load factor means shorter chains on average, leading to faster searches. A common practice is to resize the hash table and rehash the elements when the load factor exceeds a certain threshold.

3. Use a Good Hash Function: The choice of hash function is crucial in open hashing, just as it is in closed hashing. A good hash function should distribute keys uniformly across the hash table to minimize the length of the chains, improving the average search time.

4. Handling Deletions: Deletions are more straightforward with open hashing than with closed hashing. To remove an element, you can simply find it within its chain and remove it from the data structure (linked list, BST, etc.) without affecting other elements.

5. Memory Considerations: While open hashing can handle collisions gracefully, it may require more memory overhead than closed hashing, especially if you're using pointers (as in linked lists or trees). This should be considered when designing systems where memory usage is a critical factor.


## Closed Hashing
Closed hashing, also known as open addressing, is a method used in hash tables to resolve collisions. A collision occurs when two or more keys are hashed to the same index in the hash table. Closed hashing addresses this issue by finding another spot within the table for the colliding element, instead of using external data structures like linked lists (which is done in open hashing).

Two types of closed hashing:
1. Bucket Hashing:
- In bucket hashing, the hash table (HT) is divided into `b` buckets, with each bucket containing multiple slots. For a HT of capacity `m`, each bucket will contain `m/b` slots. This approach allows for a more organized handling of collisions, as all entries hashed to the same bucket can be searched sequentially or through another layer of hashing.
- Bucket Hashing Pseudocode
```
    class BucketHashing:
        def initialize(m, b):
            self.tableSize = m
            self.bucketCount = b
            self.buckets = [list() for _ in range(b)]  # Create b empty lists (buckets)

        def hashFunction(key):
            return key % self.bucketCount

        def insert(key, value):
            bucketIndex = self.hashFunction(key)
            self.buckets[bucketIndex].append((key, value))  # Append the (key, value) pair to the appropriate bucket

        def search(key):
            bucketIndex = self.hashFunction(key)
            for (k, v) in self.buckets[bucketIndex]:  # Search for the key in the appropriate bucket
                if k == key:
                    return v
            return None  # Key not found

        def delete(key):
            bucketIndex = self.hashFunction(key)
            for i, (k, _) in enumerate(self.buckets[bucketIndex]):
                if k == key:
                    del self.buckets[bucketIndex][i]  # Delete the (key, value) pair if found
                    return True
            return False  # Key not found
```

2. Linear Probing:
- Instead of the "Hash function" as a type, the second common type of closed hashing is better exemplified by a specific collision resolution technique like linear probing. In linear probing, when a collision occurs (two keys hash to the same slot), the algorithm searches for the next available slot in the HT by moving sequentially through the slots. If it reaches the end of the table, it wraps around to the beginning and continues the search until an empty slot is found.
- Linear Probing Pseudocode
```
    class LinearProbing:
        def initialize(m):
            self.tableSize = m
            self.table = [None] * m  # Initialize a table of size m with all slots as None

        def hashFunction(key):
            return key % self.tableSize

        def insert(key, value):
            startIndex = index = self.hashFunction(key)
            while self.table[index] is not None:
                if self.table[index][0] == key:  # Key already exists, update value
                    self.table[index] = (key, value)
                    return
                index = (index + 1) % self.tableSize
                if index == startIndex:  # Table is full
                    return  # Table overflow or resizing needed
            self.table[index] = (key, value)  # Insert new (key, value) pair

        def search(key):
            startIndex = index = self.hashFunction(key)
            while self.table[index] is not None:
                if self.table[index][0] == key:
                    return self.table[index][1]  # Return value if key is found
                index = (index + 1) % self.tableSize
                if index == startIndex:  # Went through the entire table
                    break
            return None  # Key not found

        def delete(key):
            startIndex = index = self.hashFunction(key)
            while self.table[index] is not None:
                if self.table[index][0] == key:
                    self.table[index] = None  # Delete the (key, value) pair
                    return True  # Key deleted successfully
                index = (index + 1) % self.tableSize
                if index == startIndex:  # Went through the entire table
                    break
            return False  # Key not found
```

Here are the key concepts involved in closed hashing:

1. Linear Probing: When a collision occurs, linear probing looks for the next available slot in the hash table by incrementally checking subsequent positions (i.e., index + 1, index + 2, ...) until an empty slot is found. This method is simple but can lead to "clustering," where a group of occupied slots gets clustered together, which can adversely affect performance.

2. Quadratic Probing: This is a variant that reduces clustering by using a quadratic function to calculate the interval between probes, rather than incrementing by one each time. For example, if the first hash index is i, subsequent indices might be i+1², i+2², i+3², and so on, until an empty slot is found.

3. Double Hashing: This involves using a second hash function when a collision occurs. The interval between probes is calculated based on the result of this second hash function. This method is more effective at reducing clustering compared to linear and quadratic probing.

Best Practices for Using Closed Hashing:
1. Choose an Appropriate Hash Function: The hash function should distribute keys uniformly across the hash table to minimize collisions. A poor choice of hash function can lead to clustering and poor performance.

2. Load Factor Management: The load factor (the number of entries divided by the number of slots in the hash table) is crucial for maintaining the efficiency of a hash table. Keeping the load factor under a certain threshold (commonly 0.7 or 0.75) is advisable to avoid excessive collisions. When the load factor exceeds this threshold, resizing the hash table and rehashing all entries can help maintain performance.

3. Use a Good Probing Sequence: The choice between linear probing, quadratic probing, and double hashing depends on the specific use case and the expected distribution of hash keys. However, quadratic probing and double hashing generally provide better performance than linear probing by reducing clustering.

4. Consider Using Universal Hashing: Universal hashing involves selecting a hash function at random from a family of functions at the time of hash table creation. This approach can further minimize the chances of collisions and clustering, improving the performance of the hash table.

5. Handle Deletions Carefully: Deletions in a closed hashing scheme can be tricky because simply emptying a slot might break the probe sequence for keys that were inserted after a collision. One common solution is to mark deleted slots in a special way (e.g., with a "deleted" flag) rather than leaving them empty.

## Rehashing
- Usually people try not to rehash
Rehashing is the process of resizing the hash table and re-distributing the existing elements into the new, larger set of slots. This involves:

1. Creating a New Hash Table: Typically, the size of the new hash table is chosen to be a prime number or a power of two that is larger than the original size, to reduce the likelihood of collisions and evenly distribute the data.

2. Applying a New Hash Function: A new hash function may be applied, especially if the new table size requires it. This function must re-map the existing keys to the new set of slots in the expanded table.

3. Re-inserting Existing Elements: Each element from the original hash table is removed and inserted into the new hash table using the new hash function. This step ensures that the elements are evenly distributed according to the new size and hash function, optimizing the performance of hash table operations.