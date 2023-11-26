# Small Tools can Solve Big Problems

## Goal
- learn how to control command-line options, how to manage streams of information, and redirection, getting tooled up in no time

## Make Program Work With Files 
- Tools that read data line by line, process it, and write it out again are called **filters**
    - `head`: This tool displays the first few lines of a file
    - `tail`: This filter displays the lines at the end of a file
    - `sed`: The stream editor lets you do things like search and replace text
- The operating system controls how data gets into and out of the **Standard Input** and **Standard Output**. 
    - If you run a program from the command prompt or terminal, the operating system will send all of the keystrokes from the keyboard into the Standard Input
    - If the operating system reads any data from the Standard Output, by default it will send that data to the display
    - `scanf(format_specifier, &variable);`
    - `printf(format_string, value1, value2, ...);`
        - Using the Standard Input and the Standard Output, we can redirect the Standard Input and Standard Output so that they read and write data somewhere else, such as to and from files

## Redirect the Standard Input with `<`
- Instead of entering data at the keyboard, we can use the `<` operator to read the data from a file
    - `./geo2json < gps.data.cvs`: This is telling the operating systems to send the data from the file into the Standard Input of the program instead of the keyboard

## Redirect the Standard Output with `>`
- Becuase we redirect the Standard Output, we won't see any data appearing on the screen. Instead, the program has now created a file called *output.json*
    - `./geo2json < gps.data.cvs > output.json`
    - how can we still display error messages if we are redirecting the output?
        - `echo $?` will  display the number returned by the program when it finished
    
## Standard Error
- The *Standard Error* is a second output that was created for sending error messages
- By default, the Standard Error is sent to the display

## fprintf() prints to a data stream
- The `fprintf()` function allows you to choose where you want to send text to.
    - You can tell fprintf() to send text to `stdout` (the Standard Output) or `stderr` (the Standard Error)
    - cmp: The `printf() `function sends data to the `Standard Output`
    - we can redirect the Standard Error using `2>`, for example: `./your_program 2> error.log`


## fscanf() scans to a data stream
- The `fscanf()` function, on the other hand, is used for scanning and parsing data from a specified data stream
- It is particularly useful when you need to read formatted input from a file or another source
- The basic syntax of fscanf() is similar to scanf(), but instead of reading from the standard input (keyboard), it reads from a specified file stream
    - cmp:The Standard Input reads data from the keyboard by default

## Sample code for fprintf() and fscanf()
```
#include <stdio.h>

int main() {
    FILE *inputFile = fopen("input.txt", "r");
    if (inputFile == NULL) {
        fprintf(stderr, "Error opening input file\n");
        return 1;
    }

    FILE *outputFile = fopen("output.txt", "w");
    if (outputFile == NULL) {
        fprintf(stderr, "Error opening output file\n");
        fclose(inputFile);
        return 1;
    }

    int num1, num2, result;

    // Reading two integers from the input file
    int readCount = fscanf(inputFile, "%d %d", &num1, &num2);

    if (readCount == 2) {
        // Performing a simple operation (addition)
        result = num1 + num2;

        // Writing the result to both stdout and the output file
        fprintf(stdout, "Sum: %d\n", result);
        fprintf(outputFile, "Sum: %d\n", result);

    } else {
        fprintf(stderr, "Error reading from input file\n");
    }

    fclose(inputFile);
    fclose(outputFile);

    return 0;
}
```

## Connect Input and Output with a Pipe
- The `|` symbol is a pipe that connects the Standard Output of one process to the Standard Input of another process
- `Pipe` accepts data in one end, and send the data out of the other in sequence
- The operating system will handle the details of exactly how the pipe will do this. All we have to do to get things running is issue a command like this:
`./program1 | ./program2`
- The output of program1 will become the input of program2
    - combine everything together: `(./program1 | ./program2) < spooky.csv > output.json`
    - A series of connected processes is called a pipeline

## What If We Want to Output to More Than One File?
- we can create a new data stream using the `fopen()` function:
    - `FILE *in_file = fopen("input.txt", "r");`
    - `FILE *out_file = fopen("output.txt", "w"); `
        - mode `w`: write to a file
        - mode `r`: read from a file
        - mode `a`: append data to the end of a file
-  When we finish with a data stream, we need to close it
    - `fclose(in_file)`
    - `fclose(out_file)`

## Pass command-line arguments
```
// The main() function can read the command-line arguments as an array of strings. 

int main(int argc, char*argv[]){
    .... do stuff here ....
}

```
- for example, this is the *categorize* program that can read the keywords to search for and the files to use from the command line
    - the program runs using `./categorize mermaid mermaid.csv Elvis elvises.csv the rest.csv`
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char * argv[]){
    char line[80];
    if (argc != 6){
        fprintf(stderr, "you need to give 5 arguments");
        return 1;
    }
    FILE *in = fopen("spooky.csv", "r");
    FILE *file1 = fopen(argv[2], "w");
    FILE *file2 = fopen(argv[4], "w"); 
    FILE *file3 = fopen(argv[5], "w"); 

    while (fscanf(in "%79[^\n]\n", line) == 1){
        if (strstr(line, argv[1]))
        fprintf(file1, "%s\n", line);
        else if (strstr(lins, argv[3]))
        fprint(file2, "%s\n", line)
        else
        fprintf(file3, "%s\n", line);
    }
    fclose(file1);
    fclose(file2);
    fclose(file3);
    fclose(in);
    return 0;
}
```

