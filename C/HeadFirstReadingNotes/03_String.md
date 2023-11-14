# Strings

## string.h 
```
    #include <string.h>
```
- for string manipulation
    - strchr() : find the location of a character inside a string
    - strcmp() : compare two strings
    - strstr() : find the location of a astring inside another string
    - strcpy() : copy one string to another
    - strlen() : find the length of a string
    - strcat() : concatenate two strings
        - for example:
        ```
            // to look for a string "fun" inside a larger string
            // If it finds the string, it will return the address of the located string in the memory. 
            // Else return value 0.
            strstr("dysfunctional", "fun)
        ```
## Create an array of arrays
- We can create an array of arrays with char strings[ooo][xxx]
    - The first set of brackets is used to access the outer array
    - The second set of brackets is used to access the details of each of the inner arrays
    ```
        char songs[][80] ={
            "Love Story",
            "Back to December",
            "Dancing with your ghost"
        }
        // the compiler can tell there are 4 items in the list, so we can skip the [4] and just put []
    ```

## Array of arrays vs. array of pointers
- array of pointers: a list of memory addresses stored in an array

<br>
================ 5930 Strings in C ================ 
<br>

## Character array vs String
- There is no actaul string type in standard C
    - A string is defined as an array of characters terminated by a NULL; aka "NULL terminated string"
        - e.g. `char my_string[4] = {'T', 'o', 'm', '\0'};`
            - without the NULL `\0`, it is just an array of characters
    - We can also wrap a string in quotes; this will automatically be NULL terminated by the compiler 
        - a string in double quotes `" "` is called a *string literal*
        - e.g. `char my_string = "Tom";`
## Pointer to a String
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
            - e.g. my_string_ptr[0] = "M" -> THIS IS NOT ALLOWED
            -      my_string[0] "M" -> THIS IS ALLOWED

## STRLEN() Implementation
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

## Arrays of Strings
- This is an array of strings in C:
```
    char my_2D_array[3][4] = {  {'I', '\0'},
                                {'a', 'm', '\0'}, 
                                {'T', 'o', 'm', '\0'} };
```

## Passing a 2D Array in C
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

## Arrays of Pointers to Strings
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

## Pointers to Arrays of Pointers to Strings
- We can create antoehr pointer to the array of pointers:
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
        
