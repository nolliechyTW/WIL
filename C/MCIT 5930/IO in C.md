## The C standard library
- To use a function defined within the C standard library, we must include the appropriate header file (`.h` file). The functions within the standard library are grouped based on their funtionality
    - e.g., `math.h` has `sin` and `tan`
- A library header file does not contain the source code for libraray functions
- The standard I/O functions use the header file `stdio.h`

## I/O one charater at a time
- The function `getchar` and `putchar` perform input and output on a single character at a time. Input is read in as ASCII and output is written out as ASCII, in a manner similar to the PUTC and GETC TRAP routines of the LC-4

### I/O Streams
- Conceptually, all character-based input and output is performed on *streams*
- Stream abstration allows us to further decouple the producer from the consumer, which is helpful because the two are usually operating at different rates 
    - e.g. if a program wants to perform some output, it adds characters to the end of the output stream without being required to wait for the output device to finish displaying the previous character
    - C++ also provide a similar stream-based abstraction for I/O
- In C, the standard input stream is `stdin` and is mapped to the keyboard by default; the standard output stream is referred as `stdout` and is mapped to the display by default
    - The function `getchar` and `putchar` operate on these two streams


### putchar
- The function `putchar` is the high-level language equivalent of the LC4 TRAP_PUTC 
- The value passed to it is assumed to be ASCII and is added directly to the output stream

```
        // C program to demonstrate putchar() method

        #include <stdio.h>;

        int main()
        {

            // Get the character to be written
            char ch = 'G';

            // Write the Character to stdout
            putchar(ch);

            return (0);
        }

        // OUTPUT: G
```

### getchar
- The function `getchar` is the high-level language equivalent of the LC4 TRAP_GETC
- It returns the ASCII value of the next input character appearing in the `stdin` input stream

```
        int main()
        {
            // getchar returns the ASCII value of the next character typed at the keyboard
            char c;
            c = getchar();

            return (0);
        }

```

### Buddered I/O
- On most computer systems, I/O streams are buffered.
    - Every key typed on the keyboard is captured by the low-level operating system software and kept in a buffer until it is realsed into the input stream
    - In the case of the input stream, the buffer is realsed when the user presses Enter; the enter key itself appears as a newline character in the input stream


## Formatted I/O
- The functions `putchar` and `getchar` suffice for simple I/O tasks but are cumbersome for performing non-ASCII I/O.

### printf
- `printf` writes formatted text to the output stream
- `printf` takes care of all the type conversions
    - Conversion specifications all begin with a `&` character
        - %d: interger
        - %x: interger as hexadecimal numbers
        - %b: binary numbers
        - %s: strings(be of type char*)
        - %f: floating point number
        - %%: print out % itself
    
```
        int a = 110;
        int b = 40;
        printf("The value in decimal is %d\n", a);
        printf("'a' plus 'b' as character: %c\n", a + b)

```
### scanf
- `scanf` reads formatted text to the input stream
- `scanf` ignores white space for formatted string
- `scanf` differs in that all arguments following the format string must be pointers!
    - Since `scanf` modifies the values of the variables passed to it, arguments are passed by reference using the `&` operator
    - In the following code, we do not need to use the `&` operator in front of the `name` variable because the name array is already a pointer to the beginning of the character array. When you use `name` as an argument to scanf, it refers to the memory location where the character array starts

```
        #include <stdio.h>

        int main() {
            char name[100];
            int month, day, year;
            double gpa;

            printf("Enter: lastname birthdate grade_point_average\n");
            scanf("%s %d/%d/%d %lf", name, &month, &day, &year, &gpa);

            printf("\n");
            printf("Name: %s\n", name);
            printf("Birthday: %d/%d/%d\n", month, day, year);
            printf("GPA: %f\n", gpa);

            return 0;
        }

        <!-- 
        INPUT:
        Enter: lastname birthdate grade_point_average
        Smith 5/12/1990 3.75

        OUTPUT:
        Name: Smith
        Birthday: 5/12/1990
        GPA: 3.750000 
        -->

```