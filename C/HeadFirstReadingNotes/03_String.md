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
            // If it finds the string, it will return the address of the located string in the memory. Else return value 0.
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
- there is no actaul string type in standard C
    - A string is defined as an array of characters terminated by a NULL; aka "NULL terminated string"
        - e.g. `char my_string[4] = {'T', 'O', 'M', '\o'};`
            - without the NULL `\o`, it is just an array of characters
    - We can also wrap a string in quotes; this will automatically be NULL terminated by the compiler 
        - a string in double quotes `" "` is called a *string literal*
        - e.g. `char my_string = "TOM";`
## Pointer to a string
- This is a pointer to a string in C:
    - e.g. `char* my_string_ptr = "TOM";`
    - !notice! string literal will live in a region of memory that is read only
     
