# CONTENT

1. VARIABLES, \*POINTERS, ARRAYS[0], USER DEFINED TYPES
2. STRINGS[]
3. FILES(I/O)
4. Dynamic Memory Allocation


## VARIABLES, \*POINTERS, ARRAYS[0], USER DEFINED TYPES

### Variables in C

- 4 built-in data types:
  - char
  - int
  - float (doesn't exist on LC4)
  - double (doesn't exist on LC4)
- the width of each data type is machine dependent:
  - char 8 bits
  - int 16/32/64 bits (16 bits on LC4)
  - float 32 bits
  - double 64 bits
    - bigger to smaller conversions need to cast explicitly!
      - for example:
        ```
        int a ;
        float b = 5.6;
        a = (int) b;
        ```
- 3 modifiers to change width of data types:
  - long (double width)
  - short (halves width)
  - unsigned (binary is unsigned)

### Arrays in C

- the name of an array in C is essentially just a `label`
  declaration/ initialization of an array: `int my_int[4] = {1, 2, 3, 4}; `
  or `int_my_int[] = {1, 2, 3, 4}`

### User Defined Types in C

1. using `struct`
   for example,

   ```
       // define
       struct fraction {
           int numerator;
           int denominator;
       };

       // use
       struct fraction my_frac;
       my_frac.numberator = 3;
       my_frac.denominator = 5;
   ```

2. using `typedef`
   for example,

   ```
       // define
       typedef struct {
           int numerator;
           int denominator;
       } fraction;

       // use
       fraction my_fracl // allow us to drop "struct" keyword
   ```

### Determine the Address of a Variable: &

- Address operator: `&`

  ```
      int main(){
          int my_int = 32767;
          int* my_pointer = &my_int; // compiler will figure out the address and assign it to the pointer
      }
  ```

- Have pointers to any data type in C:

  ```
      typedef struct {
          int numerator;
          int denominator;
      } fraction;

      fraction my_frac;
      fraction* my_frac_ptr = &my_frac;
      (*my_frac_ptr).numerator = 3; // way1 to dereference ptr to struct
      my_frac_ptr -> denominator = 5; // way2 to dereference ptr to struct
  ```

### Why We Need Pointers in C?

- One particular purpose is to help us pass address to functions instead of data

  ```
      void square(int* var){
          *var = (*var) * (*var);
      }

      int main(){
          int a = 10;
          square(&a);
      }

  ```

### Pointers to Arrays in C

- We can have a pointer to an array

  ```
      int main(){
          int a[3] = {1, 2, 3};
          int* var = &a[0];
          // or
          int* var2 = a;
      }
  ```

- Example of passing an array to a function in C

  ```
      void square(int var[], int length){
          for(int i = 0; i < length; i++){
              var[i] = var[i] * var[i];
          }
      }

      int main(){
          int a[3] = {1, 2, 3};
          square( &a[0], 3);
          // or square( a, 3);
      }
  ```

### Pointers to Pointers (\*\*)

- For example,

  ```
      int main(){
          int a = 5;
          int* b_ptr = &a;
          int** c_ptr = &b_ptr;
      }
  ```

### Always initialize a pointer to avoid unexpected behavior

```
    int main(){
        int a = 5;
        int* b_ptr = 0;
        // or
        int* b_ptr = NULL; // better

        print(a);
        print(b_ptr);
        print(*b_ptr); // this will cause a "segmentation fault"
        // becuase our program is trying to access a memory location that is not allowed to access
    }

```

### void and void\*

- `void` is a basic data type in C indicating the `absence of data`
- `void*` pointer is a typeless pointer, so it can point to any type of data

  - void\* pointer allows us to write code that can work with data of different data types without having to specify data explicitely
  - however, we cannot dereference `void*` pointer since we don't know the type/ how much space to access in memory
  - this is how we work around:

        ```
            void square(void* var){
                int* my_cast = (int*) var;
                *my_cast = (*my_cast) * (*my_cast);
                // nothing to return
            }

            int main(){
                int a = 10;
                square(&a);
            }
        ```

### Constants in C

- 2 ways to make a constant in C:
  1. using `const` modifier
  2. using `#define` directive
     ```
         #define RADIUS 15.0 // can change and recompile
         int main(){
             const double pi = 3.14159; // we cannot change this
             double area = pi * RADIUS * RADIUS;
             pi = 3.1415926 // this won't work
         }
     ```
- 3 interesting combinations of `const` and pointers:
  1. pointer to a constant: can change **address** pointer contains, not the value of what it points to ; can read but can't update
     `const int* my_pointer;`
     `int const *my_pointer;`
  2. constant pointer to a variable: cannot change address pointer contains, can change the **value** of what it points to
     `int* const my_pointer;`
  3. constant pointer to a constant variable: cannot change anything
     `const int* const my_pointer;`

### Storage Classes for Variables in C

- 2 basic storage classes:
  1. Automatic
     - variables lose their values once their block terminates
       - e.g. arguments, return types, local variables...
  2. Static:
     - variables retain their values between invocation
       - e.g. global variables
     - local variable can be declared as static!
       - `static int my_local_variable`
         - in this case, the scope is still local, but it will retain its value even after function completes
- 2 other storage classes:
  1. extern
  2. register

## STRINGS[]

### Character Array versus String

- A string is defined as **an array of characters terminated by a NULL**
  - e.g. `char my_string[4] = {'T', 'o', 'm', '\0'};`
    - without the NULL `'\0'`, it is just an array of characters
  - if we wrap a string in quotes `" "`, it is automatically NULL terminated
    - a string in double quotes is called a **string literal**
      - these two are the same:
        - `char my_string[] = {'T', 'o', 'm', '\0'};`
        - `char my_string[] = "Tom";`
      - this is a pointer to a string instead:
        - `char* my_string_ptr = "Tom";`
          - string literal will live in a region of memory that is read only(in global/static region/ object file)
  - You cannot edit a pointer to a string literal
    ```
        char* my_string_ptr = "Tom";
        my_string_ptr[0] = "M" // not allowed!
    ```
  - You can edit a character array
    ```
        char my_string[] = "Tom";
        my_string[0] = "M"; // perfectly legal
    ```

### Standard C Library

e.g. #include <string.h> [link](https://www.tutorialspoint.com/c_standard_library/string_h.htm)

### Character array vs String

- There is no actaul string type in standard C
  - A string is defined as an array of characters terminated by a NULL; aka "NULL terminated string"
    - e.g. `char my_string[4] = {'T', 'o', 'm', '\0'};`
      - without the NULL `\0`, it is just an array of characters
  - We can also wrap a string in quotes; this will automatically be NULL terminated by the compiler
    - a string in double quotes `" "` is called a _string literal_
    - e.g. `char my_string = "Tom";`

### Pointer to a String

- This is a pointer to a string in C:
  - e.g. `char* my_string_ptr = "Tom";`
  - !notice! string literal will live in a region of memory that is read only
  - cmp:
    ```
    int main(){
        char my_string [] = "Tom";
        char* my_string_ptr = "Tom";
    }

    ```
  - We cannot edit a pointer to a string literal
    - but we can edit a character array
      - `my_string_ptr[0] = "M" -> THIS IS NOT ALLOWED`
      - `my_string[0] "M" -> THIS IS ALLOWED`

### STRLEN() Implementation

- Array Style

```
    int strlen(char* string){
        int length = 0
        while (string[length] != '\0'){
            length ++;
        }
        return length;
    }

    int main(){
        int len = 0;
        char my_string[] = "Tom";
        len = strlen(my_string);
    }
```

- Pointer Style

```
    int strlen(char* string){
        char* s;
        for (s = string; *s; s++)
        return (s - string);
    }

    int main(){
        int len = 0;
        char my_string[] = "Tom";
        len = strlen(my_string);
    }
```

### Arrays of Strings

- This is an array of strings in C:

```
    char my_2D_array[3][4] = {  {'I', '\0'},
                                {'a', 'm', '\0'},
                                {'T', 'o', 'm', '\0'} };
```

### Passing a 2D Array in C

- Let's say we want to pass the 2D to a function

```
        int strlen_2D(char my_2D_pointer [3][4]) {
            int i = 0;
            int length = 0;
            for (i = 0; i < 3; i++){
                length += strlen(my_2D_pointer[i]);
            }
            return (length);
        }

        int main() {
            int len = 0;
            char my_2D_array[3][4] = {
                {'I', '\0'},
                {'a', 'm', '\0'},
                {'T', 'o', 'm', '\0'}
            };
            len = strlen_2D(my_2D_array);
        }
```

- In reality, our function is receiving a memory address:

```
        int strlen_2D(char (*my_2D_pointer)[4]) { // this line
            int i = 0;
            int length = 0;
            for (i = 0; i < 3; i++){
                length += strlen(my_2D_pointer[i]);
            }
            return (length);
        }

        int main() {
            int len = 0;
            char my_2D_array[3][4] = {
                {'I', '\0'},
                {'a', 'm', '\0'},
                {'T', 'o', 'm', '\0'}
            };
            len = strlen_2D(my_2D_array);
        }
```

- Dereferencing with `[]` is automated pointer arithmetic
  - By providing the # of coloumns in the 2d array, we are telling the compiler how many rows in memory to advance each time the pointer is dereferenced using the first [] operator

### Arrays of Pointers to Strings

- We can achieve something similiar using an array of pointers

```
    char I_array [] = {'I', '\0'};
    char Am_array [] = {'a', 'm', '\0'};
    char Tom_array [] = {'T', 'o', 'm', '\0'};
    char * array_of_ptrs [3] = { I_array, Am_array, Tom_array};
```

- And dereference as follows:

```
    print(array_of_ptrs[0][0]);     // print out 'I'
    print(array_of_ptrs[2][1]);     // print out 'o'
    array_of_ptrs[2][0] = 'M';      // update 'T' to 'M'
```

### Pointers to Arrays of Pointers to Strings

- We can create another pointer to the array of pointers:
  `char** ptr_to_ptr = array_of_ptrs`;
- And dereference as follows:

```
    print(ptr_to_ptr);               // prints out x7ff0
    print(ptr_to_ptr[0]);            // prints out x7ffa
    print(ptr_to_ptr[0][0]);         // print out 'I'
    ptr_to_ptr[2][0] = 'M';          // update 'T' to 'M'
```

### Pointers to Pointers in main()

- The function `main()`can actaully be set up to take arguments
  - we can declared it as follows
    - `int main(int argc, char** argv)` or
    - `int main(int argc, char* argb[])`
  - OS would pass main() arguments. In command line we can pass it as:
    - `./myprogram argument1 argument2`

## FILES(I/O)

### What is file?

- File is a logical collection of 1s and 0s
- 2 basic types:
  1. text (aka ASCII) files: plain printable text
     - e.g. .c, .java, .txt, .tex, .sh, .html, .rst, .py
  2. binary files: everthing else; generally not human readable/editable
     - e.g. .o, .exe, .jpg, .mp3, .wmv, .doc, .xls, .ppt
  3. somewhere in between: e.g. ps., .pdf

### PennSim's .obj file format explained:

- 5 sections contains:
  1. CODE section
     - maps to the .CODE directive
     - `xCADE, <address>, <n=#word>` (16 bits each)
  2. DATA section
     - maps to the .DATA directive
     - `xDADA, <address>, <n=#word>` (16 bits each)
  3. SYMBOL section
     - maps to the LABELS we create in our assembly code
     - `xC3B7, <address>, <n=#bytes>` (16 bits each)
  4. FILENAME section
     - maps to the name of the .C files the assembly came from
     - `xF17E, <n=#bytes>` (16 bits each)
  5. LINE NUMBER ection
     - tells us which assembly lines came from which .C file
     - `x715E, <address>, <line>, <file-index>` (16 bits each)
- for example

  - this is `file_format_example.asm`:

    ```
        .CODE
        .ADDR x0000

        LABEL1
            CONST R0, #2
            ADD R0, R0, R0

        .DATA
        .ADDR x4000
            MYVAR .BLKW x1
    ```

  - this is how it looks like in `file_format_example.obj`:
    ```
        CA DE 00 00 00 02 90 02
        10 00 DA DA 40 00 00 01
        00 00 C3 B7 40 00 00 05
        4D 59 56 41 52 C3 B7 00
        00 00 06 4C 41 42 45 4C
        31
    ```

### Order of Bytes in a File

- `Endianness`: how the binary data in a file is ordered
  1. BIG endian files::
     - Bytes are stored in file from MSB to LSB
     - e.g. `CADE 0000 0002`
  2. LITTLE endian files:
     - Bytes are stored in file from LSB to MSB
     - e.g. `DECA 0000  0200`

### Type: FILE

- `FILE` is a data type that holds information about an open file
- It's operating system dependent; we use helper function to interact with it
- Example structure declaration:
  ```
      typedef struct{
          short int level;
          short int token;
          short int bsize;
          char fd;
          unsigned int flags;
          unsigned char hold;
          unsigned char *buffer;
          unsigned char *curp;
          unsigned int istemp;
      } FILE
  ```

### Basic operations on files

- open

  - fopen()
    - `FILE* fopen(const char *filename, const char *mode)`
      - mode:
        - `"r"` - open file for reading
        - `"w"` - open file for writing
        - `"a"` - append to file; if file exist, add stuff at the end
        - `"rb"` - open binary file for reading
        - `"wb"` - open file for binary output
      - if file doesn't exist or cannot be created, NULL is returned
      - otherwise, a pointer to the open FILE is returned

- close
  - fclose()
- read
  - fgetc() // 1 character
    - `int fgetc(FILE *stream)`
      - stream: the pointer to an open file one wishes to read a char from
      - if the file is at its end, returns EOF (typically -1)
      - otherwise, return a byte(1 character) read from the file as an integer
  - fgets() // 1 line
    - `char* fgets(char* str, int n, FILE *stream)`
      - str: pointer to an array of chars to read string into
      - n: maximum number of characters to be read from file(including NULL)
      - stream: pointer to an open file to read from
      - return pointer to str if succeed
      - return NULL pointer if fail
  - fread() // multiple bytes
    - `size_t fread(void* ptr, size_t size, size_t nmemb, FILE *stream)`
      - `size_t` is typically an "unsigned int"
        - ptr: to an array you want to read data into
        - size: of a single element of your array
        - nmemb: total number of elements in your array
      - return the total number of elements successfully read
      - if the number is different from nmemb, either we've hit EOF or an error occurred
- write

  - fputc()
    - `int fputc(int character, FILE* stream)`
      - if an error occurs, return EOF
      - if no error occurs, return the same character that has been written
  - fputs()
    - `char* fputs(const char* str, FILE* stream)`
      - return non-negative value if succeed
      - return EOF if fail
  - fwrite()
    - `size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream)`
      -

- formatted string
  - fprintf()
    - `int fprintf(FILE *stream, const char* format)`
      - return total number of characters written if succeed
      - return a negative number if fail
  - fscanf()
    - `int fscanf(FILE *stream, const char* format, ...)`
      - return number of items matched and assigned if succeed
      - return less number that we expected if fail

  - sscanf()
    - `int sscanf(const char* str, const char* format, ...)`
        - str: a string sscanf() will parse; the input to the function
        - return number of items matched and assigned if succeed
        - return EOF is less number is return

- position
    - `EOF`
        - At the end of the file -> return 1 
    - `int feof(FILE *f);`
        - At the end of the file -> return 1
    - `long int ftell(FILE *f);`
        - Return current position in file and -1 if an error occurs
    - `void fseek(FILE *f, long int offset, int origin);`
        - Advances position in file: offset + origin 

### Example 1

```
    #include <stdio.h>

    int main(){
        FILE *my_file;
        my_file = fopen("tom.txt", "w");
        if (my_file == NULL) {return 1;}

        fputc('T', my_file);
        fputc('o', my_file);
        fputc('m', my_file);

        fclose(my_file);
    }
```

#### Example 2

```
    #include <stdio.h>

    /* this code will copy a file byte by byte */

    int main(){
        FILE *src_file, *des_file;
        int byte_read;

        src_file = fopen("file_format_ex.obj", "rb");
        if(src_file == NULL) {return 1;}  // error code

        des_file = fopen("file_format_ex_cp.obj", "wb");
        if (des_file == NULL) {
            fclose(src_file);
            return 2; // different error code
        }

        do {
            byte_read = fgetc(src_file);
            if (byte_read == EOF) break;

            fputc(byte_read, des_file);
        } while (1);

        fclose(src_file); // fclose() return 0 if file closes
        fclose(des_file); // otherwise return EOF on failure

        return 0;
    }
```

#### Example 3

```
    #include <stdio.h>
    #define ARRAY_SIZE 4

    /* this code will write data from a string */

    int main(){
        char array[ARRAY_SIZE] = {'T', 'o', 'm', '\0'};
        char* array2 = "Tom";

        FILE *theFile = fopen("outputfile.txt", "w");
        if (theFile == NULL) {return 1;}

        fputs(array, theFile);
        fputs(array2, theFile);
        fputs("Tom", theFile);

        fclose(theFile);
        return 0;
    }
```

#### Example 4

```
    #include <stdio.h>
    int main(){
        int a = 5;
        char* string = "World";
        FILE *theFile = fopen("output_file.txt", "w");
        if (theFile == NULL) {return 1;}

        fprintf(theFile, "Hello World\n");
        fprintf(theFile, "Hello %s\n", string); // string concatenation
        fprintf(theFile, "a = %d\n", a); // print in decimal
        fprintf(theFile, "a = %x\n", a); // print in hex
        fprintf(theFile, "a's address = %p\n", &a);

        fclose(theFile);
        return 0;
    }
```

### File Handles in the C Library

- constant; always open; cannot close
  - stdin: pointer to the keyboard
  - stdout: pointer to the ASCII output console
  - stderr: pointer to an error ASCII console
  - `printf("hi\n")` equals to `fprintf(stdout, "hi\n")`;

#### Example 5

```
    #include <stdio.h>
    int main(){
        int a = 5;
        char* string = "World";

        fprintf(stdout, "Hello World\n"); // print to screen
        fprintf(stderr, "Error has occurred!\n"); // print to admin's console

        return 1;
    }
```

#### Example 6
```
    #include <stdio.h>
    int main(){
        char str1[10], str2[10];
        int year, match;
        FILE *theFile = fopen("input_file.txt", "r");
        if (theFile == NULL) {return 1;}

        match = fscanf(theFile, "%s %s %d", str1, str2, &year);
        printf("READ in %d items from file", match); // prints 3

        fclose(theFile);
    } // if text file contained: "I love 1990"
    // str1 = "I", str2 = "love", year = 1980
```

#### Example 7
```
    #include <stdio.h>
    #include <string.h>
    #define MAX_LINE_LENGTH 80

    int main(){
        int i, num1, num2;
        char input[MAX_LINE_LENGTH];
        char fname[MAX_LINE_LENGTH];

        printf("Enter command: SCRIPT <filename>, SET R<number> <value>, EXIT\n");

        /* drop into a loop and read string from keyboard*/
        while (fgets(input, MAX_LINE_LENGTH, stdin)){
            printf("\nString Read In: %s\n", input);

            if (sscanf(input, "SCRIPT %s", fname) == 1) //success
                printf("It's a SCRIPT command - fname = %s\n", fname)
            
            if (sscanf(intput, "SET R% %", &num1, &num2) == 2)
                printf("It's a SET command: Set register %d to 0x%x\n", num1, num2);

            if (strcmp(input, "EIXT\n") == 0){
                printf("Existing loop");
                break;
            }
            printf("########################################")
        }
    }
```

### argc; argv
- two default arguments to main recall C's roots in Unix.
    - `int main(int argc, char **argv)`
        - argc: number of words on the command line (argc >= 1)
        - argv: list of strings containing all of these words
            - declaration of argv as a pointer to an array of pointers

#### Example 8
```
    int main(int argc, char** argv){
        int i;
        for (i = 0; i < argc; ++i){
            printf("argument %d = %s \n", i, argv[i]);
        }
    }


```

### comparison 
- `fputs` vs `fprintf`
    - `fputs` is specifically designed for writing strings to a file
        - `int fputs(const char *str, FILE *stream);`
    - `fprintf` is a versatile function for writing various types of data to a file
        - `int fprintf(FILE *stream, const char *format, ...);`

    - Example Usage:
        - fputs:
            ```
            FILE *file = fopen("example.txt", "w");
            if (file != NULL) {
                const char *text = "Hello, world!";
                fputs(text, file);
                fclose(file);
            }
            ```
        - fprintf:
            ```
            FILE *file = fopen("example.txt", "w");
            if (file != NULL) {
                int num = 42;
                fprintf(file, "The answer is %d\n", num);
                fclose(file);
            }
            ```
## Dynamic Memory Allocation

### What's the Heap?
- Dynamic means at run time! 
- Heap is accessible at run time, x4000 - x6FFF

### Heap API
  - `malloc()` and `free()` in `stdlib.h`
    - `*void malloc(size_t size)`
      - return a pointer to a region on the heap of size bytes
      - return `NULL` if heap can't fulfill request
    - `void free(*void ptr)`
      - clear reservation for address pointed to be `ptr`
      - the memory region pointed to by ptr, was previously given to you by malloc()

#### Example 9
```
  #include <stdlib.h>
  int main(){
    int* int_array;
    /* request memory allocation from heap; 2 rows * 4  bytes(int size) */
    // int_array = malloc(2 * 4);
    int_array = malloc( 2 * sizeof(int));

    /* make certain malloc succeeded */
    if (int_array == NULL) return 1;

    /* populate array */
    int_array[0] = 0;
    int_array[1] = 1;

    /* return allocated memory back to heap */
    free(int_array);

    return 0;
  }
```
#### Example 10
```
  #include <stdlib.h>
  int* create_array(int length){
    int* array = NULL;
    array = malloc(length * sizeof(int));
    return array;
  }

  int main(){
    int len = 2;
    int* int_array = NULL;

    int_array = create_array(len);
    if (int_array == NULL) return 1;

    int_array[0] = 0; // data is in heap
    int_arrayp[1] = 1;

    free(int_array);
    return 0;
  }
```

#### Example 11
```
  #include <stdlib.h>
  
  char str_global[3]; // in global/static memory

  int main(){
    char* str_readonly = "Hi"; // global/static memory
    char str_stack[3]; // in stack memory
    char* str_heap; // in heap memory

    str_heap = malloc(strlen(str_readonly) + 1);

    strcpy(str_global, str_readonly);
    strcpy(str_stack, str_readonly);
    strcpy(str_heap, str_readonly);

    free(str_heap);

  }
```

#### Example 12 - structure on the stack/heap
```
  #include <stdlib.h>
  typedef struct cust_struct{
    int id;
    char* name;
  } customer

  int main(){
    customer my_cust; // allocate my_cust on stack
    my_cust.id = 1234;
    
    // allocate memory for "name" on the heap
    my_cust.name = malloc(strlen("Tom")+1);
    strcpy(my_cust.name, "Tom");

    free(my_cust.name); // done the reservation
    return 0;
  }
```

#### Example 13 - structure on the stack/heap 2
```
  #include <stdlib.h>
  typedef struct cust_struct{
    int id;
    char* name;
  } customer

  int main(){
    customer* my_cust;
    my_cust = malloc(size(customer));
    
    my_cust->id = 1234;
    
    // allocate memory for "name" on the heap
    my_cust->name = malloc(strlen("Tom")+1);
    strcpy(my_cust->name, "Tom");

    free(my_cust.name); // done the reservation
    free(my_cust);
    return 0;
  }

```

### Linked Lists
#### Linking Structure on the Heap
```
  #include <stdlib.h>
  typedef struct cust_struct{
    int id;
    char* name;
    struct cust_struct *next;
  } customer;

  int main(){
    customer* my_cust = malloc(sizeof(customer));
      my_cust -> id = 1;
      my_cust -> name = malloc(strlen("Tom") + 1);
      strcpy(my_cust -> name, "Tom");

    // allocate memory for 2nd customer
    my_cust -> next = malloc(sizeof(customer));
      my_cust -> next -> id = 2;
      my_cust -> next -> name = malloc(strlen("Bob") + 1);
      strcpy(my_cust -> next -> name, "Bob");
      my_cust -> next -> next = NULL;
  }
```
### Linked List Management 
- A common technique to manage a linked list is to create functions to accomplish common tasks:
  - add nodes to a linked list
  - delete nodes
  - find nodes
  - rearrange nodes
  - print the list
    - We can use C's **multifile** development capability to create a library that contains helper function
- In practice, we create a **header file** and put structure and function declarations in it, e.g. in `customer.h`:
  ```
    typedef struct cust_struct {
      int id;
      char* name;
      struct cust_struct *next;
    } customer
  
  ```

#### Example 14 - working with header file
```
  /* customer.h */
  typedef struct cust_struct {
    int id;
    char* name;
    struct cust_struct *next;
  } customer;
  
  customer* add_customer(customer* list, int id, char* name);


```

```
  /* my_database.c - main file */
  #include "customer.h"
  #include <stdlib.h>

  // definition of customer structure is in customer.h
  int main(){
    <!-- customer* my_list = malloc(sizeof(customer));
      my_list -> id = 1;
      my_list -> name = malloc(strlen("Tom")+1);
      strcpy(my_list -> name, "Tom");
      my_list -> next = NULL;

      // add second customer using helper function
      add_customer(my_list, 2, "Bob"); -->

      // refactor - to add node
      customer* my_list = NULL;
      my_list = add_customer(my_list, 1, "Tom");

      add_customer(my_list, 2, "Bob");
      
      // search for customer2
      customer* a_customer = NUL;
      a_customer = find_customer_by_ID(my_list, 2);

      if (a_customer != NULL)
        printf("Customer ID=%d, Name = %s\n", a_customer->id, a_customer->name);
        

  }

```

```
  /*  customer.c */
  #include "customer.h" // include customer structure declaration
  #include <stdlib.h>

  // args: pointer to head of linked list + new customer info
  // returns: pointer to head of linked list
  customer* add_customer(customer* list, int id, char* name){
    // ALLOCATE MEMORY FOR A CUSTOMER
    customer* new_cust = malloc(sizeof(customer));
    if (new_cust == NULL) return 1;
      new_cust -> id = id;
      new_cust -> name = malloc(strlen(name)+ 1);
      strcpy(new_cust -> name, name);
      new_cust -> next  = NULL;

    // if list was empty, return new customer as the head
    if (list == NULL) {return (new_cust);} 

    // otherwise, traverse list to the end, glue on new cust
    customer* head = list;
    // traverse to the end
    while (last -> next != NULL){
      list = list -> next;
    }

    // glue new customer to the end of the list
    list-> next = new_cust;

    // return head of the list
    return head;
  }

  // args: pointer to head of linked list + customer id to find
  // returns: pointer to matching customer on heap if found (else NULL)
  customer* find_customer_by_ID (customer* list, int id){
    // traverse the list until we find first node with matchin id
    while ((list != NULL) && (list -> id != id))
      list = list->next;
    // return either the found customer, or NULL
    return list
  }
```