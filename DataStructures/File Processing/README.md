## Primary versus Secondary Storage
- Computer storage devices are typically classified into *primary storage* or *main memory*, and *secondary storage *or* peripheral storage*. 
    - Primary memory usually refers to Random Access Memory (RAM), and it also includes registers, cache, and video memories.
    - Secondary storage refers to devices such as hard disk drives, solid state drives, removable “USB” drives, CDs, and DVDs.

- Two main strategies exist for minimizing disk accesses:
    - Organizing information to reduce the number of accesses needed, ideally retrieving the required data on the first try.
        - The organization of data in secondary memory is termed *file structure*.
        - File structures aim to minimize disk access by efficient organization.
    - Saving information that has already been retrieved, or preemptively fetching extra data, to lessen the need for future disk accesses.
        - This strategy relies on accurately predicting future data needs and storing this data in primary memory, a process known as *caching*.

## Disk Drives
- A programmer perceives a random access file as a logically contiguous series of bytes, potentially forming data records, known as the *logical file*.
- The *physical file* on disk is not necessarily contiguous; it can be scattered across the disk.
- The *file manager*, part of the operating system, maps requests for data from the logical file to their physical disk locations.
- When writing to a logical file, the file manager converts logical byte positions to corresponding physical locations on the disk.

## Buffer Pools
- Once a sector is read, its information is stored in main memory. This is known as *buffering* or *caching* the information. If the next disk request is to that same sector, then it is not necessary to read from disk again because the information is already stored in main memory.
- In practice most disk requests are close to the location (in the logical file at least) of the previous request, a concept referred to as locality of reference. This means that the probability of the next request “hitting the cache” is much higher than chance would indicate.
- What is Sector-level Buffering?
    - Sector-level buffering refers to the temporary storage (buffers) used to hold data being read from or written to disk sectors. A *sector* is a specific segment of a disk drive, and it's the smallest unit that can be handled in a single read or write operation.
    - Most operating systems maintain separate buffers for input (reading from disk) and output (writing to disk). The necessity for distinct input and output buffers becomes evident when considering operations that require both reading from and writing to disk, such as copying data from one location to another.
    - By segregating the read and write operations into different buffers, the OS avoids the constant destruction and refilling of buffer contents that would occur with a single buffer system. This significantly speeds up I/O operations, particularly those involving large amounts of data transfer, such as file copying.
