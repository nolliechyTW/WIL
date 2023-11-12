# Memory and Pointers

## C code includes pointers
- A pointer is just the **address** of a piece of data in memory
- Instead of passing around a whole copy of the data, we can just pass a pointer
- To find out the memory address of the variable, we can use the `&` operator
    ```
        printf("x is stored at %p\n", &x);
    ```
    - `%p` is used to format address 
    - `&x` is the address of x

## Why do we use pointer?
- One of the main reasons for using pointers is to let function share memory.The data created by one function can be modified by another function, so long as it knows where to find it in memory.


## Three things to keep in mind
1) Get the address of a variable
    - find where a variable is stored in the memory using `&`
    - to store the value of the address, we use **pointer variable**
    ```
        int *address_of_x = &x;
    ```
2) Read the contents of an address
    - we do that using `*` to derefernce a pointer 
    ```
        int value_stored = *address_of_x;
    ```

3) Change the contents of an address
    ```
        *address_of_x = 99;
    ``` 

## sizeof
C has an **operator** called sizeof that can tell us how many *bytes* of space something takes in memory. We can either call it with a data type or with a piece of data:
```
    sizeof(int) // return 4 on most machines
    sizeof("turtle!") // return 8, which is 7 charaters + \o end character
``` 
- `sizeof` is an operator, not a function
    - cmp: An operator is compiled to a sequence of instructions by the compiler. But if the code calls a function, it has to jump to a separate piece of code
    - Therefore, sizeof is calculated when the program is compiled

- Take a look at the following code:
    - the code will returns 4 or 8 bytes depends on different machines instead of the length of the msg because **msg is a pointer variable** aka an address
    - so sizeof(msg) is just the size of a pointer
    
```
        void cookies(char msg[]){
            printf("Message reads: %s\n", msg);
            printf("msg occupies %i bytes\n", sizeof(msg));

        }
```
- On 32-bit operating systems, a pointer takes 4 bytes of memory and on 64-bit operating systems, a pointer takes 8 bytes


## Difference betwwen array variable and pointer
```
    char s[] = "how are you";
    char *t = s;
```
1) size of an array it's just the size of an array!
    - sizeof(s) :
    size of an array; it's 12
    - sizeof(t):
    size of an pointer; could be 4 or 8
2) the address of the array is the address of the array!
    - &s == s
    - &t != t
3) An array variable can't point anywhere else!
    - When we create a pointer variable, the machine will allocate 4 or 8 bytes of space to store it. But what if we create an array? The computer will allocate space to store the array, but it won’t allocate any memory to store the array variable. The compiler simply plugs in the address of the start of the array

## Pointer Decay
- Every time we pass an array to a function, we'll decay to a pointer, since the pointer variable will only contain the address of the array and the pointer doesn’t know anything about the size of the array
- It’s unavoidable. But we need to keep track of where arrays decay in our code because it can cause very subtle bugs
- That loss of **information** is called decay

## Pointer Arithmetic
- Because an address is just a number, we can do pointer arithmetic and actually add values to a pointer value and find the next address. 
    - E.g. The following codes are equivalent:
```
        drinks[i],
        *(drinks + i)
```
- a good demonstration:
```
        void skip(char *msg){
            put(msg + 6); // print from character 7 
        }

        char *msg_from_nollie = "Don't look at me!";
        skip(msg_from_nollie); 
        // will get "look at me!";
```


## Pointer Type
-  Pointer types exist so that the compiler knows how much to adjust the pointer arithmetic; since different data types have different size
    - char: 1 byte
    - int: 4 bytes

- e.g. if we run this, (nums+1) will be 4 bytes away from nums
```
        int nums[] = {1, 2, 3}
        printf("nums is at %p/n", nums);
        printf("nums + 1 is at %p/n", nums + 1)';
        // nums is at 0x7fff66ccedac
        // nums + 1 is at 0x7fff66ccedb0
```
- C adjust the pointer arithmetic calculations when the compiler is generating the executable. It looks at the type of the variable and then multiplies the pluses and minuses by the size of the underlying variable.

## Use pointers for data entry
### Entering numbers with scanf()
- The following program will crash if the user writes data way beyond the end of the space allocated to the food arry:
    - scanf() can cause buffer overflows when we  forget to limit the length of the string that we read with scanf()
    - It might be called a *segmentation fault* or an *abort trap*
```
        char food[5];
        printf("Enter any food: ");
        scanf("s%", food);
        printf("Food is: %s\n", food)
```
- Alternatively, we can use **fgets()** instead
    - The code below sets the maximum length using the sizeof operator
```
        char food[5];
        printf("Enter any food: ");
        fgets(food, sizeof(food), stdin)
        printf("Food is: %s\n", food)
```

## String literals can never be updated
- A variable that points to a string literal can’t be used to change the contents of the string since string literal is stored in read-only memory:
```
        char *cards = "JQK"
```
- but if we create an array from a string literal, we can modify it!
```
        char cards[] = "JQK"
```
- TLDR: In the first code, cards was just a pointer. In the second code, cards it's an array. If we declare an array called cards and then set it to a string literal, the cards array will be a completely new copy. 
- One way to aviod this problem is to **never write code that sets a simple char pointer to a string literal value** like:
```
        char *s = "some random string";
```
- Instead, if we want to set a pointer to a literal, always use the **const** keyword:
```
        const char *s = "some random string";
``` 


## Memory Memorizer
### STACK
This is the section of memory used for local variable storage. Every time we call a function, all of the function’s local variables get created on the stack. 

### HEAP
The heap is for dynamic memory: pieces of data that get created when the program is running and then hang around a long time. 

### GLOBALS
A global variable is a variable that lives outside all of the functions and is visible to all of them. Globals get created when the program first runs, and we can update them freely.

### CONSTANT
Constants are also created when the program first runs, but they are stored in read-only memory. E.g. string literals 