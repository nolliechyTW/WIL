# Strings

## string.h 
```
    #include <string.h>
```
- for string manipulation
    - strchr() : find the location of a character inside a string
    - strcmp() : compare two strings
    - strstr() : find the location of a string inside another string
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
        // the compiler can tell there are 3 items in the list, so we can skip the [3] and just put []
    ```

## Array of arrays vs. array of pointers
- array of pointers: a list of memory addresses stored in an array