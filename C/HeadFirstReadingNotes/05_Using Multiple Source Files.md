## Goal
- Learn how C allows us to break our source code into small, manageable chunks and then rebuild them into one huge program.
- get to meet your new best friend: `make`

## Casting
```
    int x = 7;
    int y = 2;
    float z = x / y;
    printf("z = %f\n", z);
    // this will print 3.0000
    // because if we divide integers we always get a rounded-off whole number, in this case 3
```
What if we want to get floating-point results?
```
    int x = 7;
    int y = 2
    float z = (float)x / (float)y;
    printf("z = %f\n", z);
    // this will print 3.5000
```

## Data Types Different on Different Operating Systems
- C uses different data types on different operating systems and processors because that allows it to make the most out of the hardware
- When C was first created, most machines were 8-bit. Now, most machines are 32- or 64-bit. Because C doesn’t specify the exact size of its data types, it’s been able to adapt over time

## Function Declaration
- If the compiler finds a call to a function it hasn’t heard of, it will assume the function returns an `int`
- To avoid the compiler making assumptions by explicitly telling it what functions it should expect, that is **function declaration**
- The declaration is just a function *signature*: a record of what the function will be called, what kind of parameters it will accept, and *what type of data it will return*
- If we have a whole bunch of functions in our code and we don’t want to worry about their order in the file, we can put a list of function declarations at the start of your C program code:
    ```
        float do_something_fantastic();
        double awesomeness_2_dot_0();
        int stinky_pete();
        char make_maguerita(int count);
    ```
- **Even better than that**, we can take the whole set of declarations out of our code and put them in a **header file**
    - common header file we've already used: `#include <stdio.h>`

## Create a Header File
1. Create a new file with a `.h` extension
    - For example, create a header file called `totaller.h`, and write declarations inside it: `float add_with_tax(float f)`
2. Include header file in main program
    - At the top of the program, add: `#include "totaller.h"`
        - double quotes tell the complier to look for a local file

## Reserved Words in C
If you use these for names, the compiler will be very, very upset:
- auto
- if
- break
- int
- case
- long
- char
- register
- continue
- return
- default
- short
- do
- sizeof
- double
- static
- else
- struct
- entry
- switch
- extern
- typedef
- float
- union
- for
- unsigned
- goto
- while
- enum
- void
- const
- signed
- volatile

## Create a Single Executable Program from Several Files
- Once you have all of the separate pieces of object code, you need to **link** them together
- For example, if we want to share the `encrypt.c` code between programs, we do that with a header file:
    - in `encrypt.h`:
        ```
            void encrypt(char *message)
        ```
    - in `encrypt.c`:
        ```
        #include "encrypt.h"

        void encrypt(char *message){
            while (*message){
                *message = *message ^ 31;
                message ++;
            }
        }
        ```
    - in my program `message_hider.c`:
        ```
        #include <stdio.h>
        #include "encrypt.h"

        int main(){
            char msg[80];
            while (fgets(msg, 80, stdin)){
                encrypt(msg);
                printf("%s", msg);
            }
        }
        ```
    - At the linking stage, the compiler will be able to connect the call to encrypt(msg) in message_hider.c to the actual encrypt() function in encrypt.c
    - to complie everything in `gcc`: `gcc message_hider.c encrypt.c -o message_hider`
- What if I want to share variables instead?
    - use `extern`. e.g. `extern int passcode;`

## Don't Recomplile Every File
- Only recompile the source code that has changed to improve efficiency; the compiler will update the object code that's stored in a file
- If you change a single file, you will have to recreate the object code file from it, but you won’t need to create the object code for any other file
- Then you can pass all the object code files to the linker and create a new version of the program

