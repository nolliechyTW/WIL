### The general form of the switch statement
```
    switch (variable) {
        case value1:
            // do something here
            break; // If a case does not have the break keyword, the following case will be executed as well, including the default case
        case value2:
            // do something here
            break;
        
        //... other cases
        
        case valueN:
            // do something here
            break;
        default:
            // do something by default
            break; // it can be omitted
    }
```