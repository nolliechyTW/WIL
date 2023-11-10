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

## Three things to keep in mind
1) Get the addres of a variable
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
C has an **operator** called sizeof that can tell you how many *bytes* of space something takes in memory. You can either call it with a data type or with a piece of data:
```
    sizeof(int) // return 4 on most machines
    sizeof("turtle!") // return 8, which is 7 charaters + \o end character
``` 
- `sizeof` is an operator, not a function
    - cmp: An operator is compiled to a sequence of instructions by the compiler. But if the code calls a function, it has to jump to a separate piece of code
    - Therefore, sizeof is calculated when the program is compiled

## Pointer Decay
- Every time you pass an array to a function, you’ll decay to a pointer, since the pointer variable will only contain the address of the array and the pointer doesn’t know anything about the size of the array
- It’s unavoidable. But you need to keep track of where arrays decay in your code because it can cause very subtle bugs
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
