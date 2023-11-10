# Intro
## How to compile and run the program using gcc (GNU Compiler Collection)
1. Save the code in a file named with the extension .c
2. complie with `gcc filename.c -o filename`
3. run by typing `./filename` on Mac, Linux, and Cygwin

## Strings in C
- Strings in C end in a sentinel character (the null character) because it needs to know when it gets to the end of the character array. We have to allow for an extra character `\0` in the array.
- Single quotes are used for individual characters, but double quotes are always used for strings. (aka string literals; immutable)

## Sample Code - card.c
```
/*
 * Program to evaluate face values.
 * Released under the Vegas Public License.
 * (c)2014 The College Blackjack Team.
 */
#include <stdio.h>
#include <stdlib.h>
int main()
{
    char card_name[3]; // one space for sentinel character
    puts("Enter the card_name: ");
    scanf("%2s", card_name);
    int val = 0;
    if (card_name[0] == 'K') {
        val = 10;
    } else if (card_name[0] == 'Q') {
        val = 10;
    } else if (card_name[0] == 'J') {
        val = 10;
    } else if (card_name[0] == 'A') {
        val = 11;
    } else {
        val = atoi(card_name); // convert the text into a number
    }
    /* Check if the value is 3 to 6 */
    if ((val > 2) && (val < 7))
        puts("Count has gone up");
    /* Otherwise check if the card was 10, J, Q, or K */
    else if (val == 10)
        puts("Count has gone down");
    return 0; // success
}
```

## Boolean Value
- To C, the number `0` is the value for `false`. Anything that is not equal to 0 is treated as `true`. 
- cmp: for `return value`, number `0` means `success`; anything that is not 0 means fail.

## switch
- can test for multiple variables of a single variable.
```
    int val = 0
    switch (card_name[0]){
    case 'K':
    case 'Q':
    case 'J':
        val = 10;
        break;
    case 'A':
        val = 11;
        break;
    default:
        val = atoi(card_name);
    }
```