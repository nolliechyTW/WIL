# CONTENT
1. VARIABLES, \*POINTERS, ARRAYS[0], USER DEFINED TYPES
2. STRINGS[]
3. FILES(I/O)


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
  - void* pointer allows us to write code that can work with data of different data types without having to specify data explicitely 
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
    1) using `const` modifier
    2) using `#define` directive
        ```
            #define RADIUS 15.0 // can change and recompile
            int main(){
                const double pi = 3.14159; // we cannot change this
                double area = pi * RADIUS * RADIUS;
                pi = 3.1415926 // this won't work
            }    
        ```
- 3 interesting combinations of `const` and pointers:
    1) pointer to a constant: can change **address** pointer contains, not the value of what it points to ; can read but can't update
        `const int* my_pointer;`
        `int const *my_pointer;` 
    2) constant pointer to a variable: cannot change address pointer contains, can change the **value** of what it points to
        `int* const my_pointer;`
    3) constant pointer to a constant variable: cannot change anything
        `const int* const my_pointer;`

### Storage Classes for Variables in C
- 2 basic storage classes:
    1) Automatic
        - variables lose their values once their block terminates
            - e.g. arguments, return types, local variables...
    2) Static:
        - variables retain their values between invocation
            - e.g. global variables
        - local variable can be declared as static!
            - `static int my_local_variable`
                - in this case, the scope is still local, but it will retain its value even after function completes
- 2 other storage classes:
    1) extern
    2) register

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
        - a string in double quotes `" "` is called a *string literal*
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
    1) text (aka ASCII) files: plain printable text
        - e.g. .c, .java, .txt, .tex, .sh, .html, .rst, .py
    2) binary files: everthing else; generally not human readable/editable
        - e.g. .o, .exe, .jpg, .mp3, .wmv, .doc, .xls, .ppt
    3) somewhere in between: e.g. ps., .pdf

### PennSim's .obj file format explained:
- 5 sections contains:
    1) CODE section
        - maps to the .CODE directive
        - `xCADE, <address>, <n=#word>` (16 bits each)
    2) DATA section
        - maps to the .DATA directive 
        - `xDADA, <address>, <n=#word>` (16 bits each)
    3) SYMBOL section
        - maps to the LABELS we create in our assembly code
        - `xC3B7, <address>, <n=#bytes>` (16 bits each)
    4) FILENAME section
        - maps to the name of the .C files the assembly came from
        - `xF17E, <n=#bytes>` (16 bits each)
    5) LINE NUMBER ection 
        - tells us which assembly lines came from which .C file
        - `x715E, <address>, <line>, <file-index>` (16 bits each)
- for example
    -  this is `file_format_example.asm`:
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
    1) BIG endian files::
        - Bytes are stored in file from MSB to LSB
        - e.g. `CADE 0000 0002`
    2) LITTLE endian files:
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
    - fwrite()

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

### Example 2
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