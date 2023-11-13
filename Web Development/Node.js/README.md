## What is Node?
- A **runtime environment** for executing JavaScript code
- Often used to build backend services e.g. API
- Great for prototyping and agile development
- Superfast and highly scalable
- 2x request/sec with 35% faster response time

## Node Architecture
- JS code -> JS engine -> Machine
- v8 (JS engine) + C++ => Node

## How Node Work?
- Non-blocking/ **Asyncronous** by default
    - **Single thread** is used to handle multiple requsests
    - When the database prepares the result, it put a message in an **Event Queue**
        - Node is ideal for I/O-intensive apps
        - Don't use Node for CPU-intensive apps

## How to Install Node?
1) open terminal
2) open your cmd/terminal
3) type `node --version` to see whether you already have node on your machine
4) go to https://nodejs.org and make sure you have the latest stable version of node
5) after installation, type `node --version` again to make sure you have successfully downloaded it

## Build a Node Program
1) open your terminal
    - create a folder e.g. `mkdir my-first-node-app`
    - go to the folder e.g. `cd my-first-node-app`
    - open the folder e.g. `code .`
2) use your editor 
    - create a new file called `app.js`
    - write somehing in it e.g.
    ```
        function sayHi(name){
            console.log('Hi ' + name);
        }

        sayHi('Nollie')
   ```
3) go back to your terminal 
    - type node and pass the name of file as an argument e.g. `node app.js`
    - node it's gonna pass it to V8 for execution

## Node Module Systems
### Global Object
- We can access it anywhere in any file
    - e.g. `console.log()`, `setTimeout()`, `clearTimeout()`, `setInterval()`, `clearInterval()`
### Create a Module
- use `module.export` to export functionality as needed for differnet module
### Loading a Module
- use `require('path')` to import functionality as needed e.g. 
    ```
        var greet = require('./greeting')
        greet.sayHi('Nollie');
    ```
### Modular Wrapper Function
- A Modular Wrapper Function is a concept often used in JavaScript modules to encapsulate code and create a modular structure. 
- It involves using a function as a wrapper around the module's code to create a private scope for the variables and functions within the module. 
- This helps prevent naming conflicts and provides a clean separation of concerns.
e.g. 

```
        // Modular Wrapper Function
        const myModule = (function() {
        // Private variables or functions
        let privateVariable = 'I am private';

        // Public interface (exposed to the outside)
        return {
            publicFunction: function() {
            console.log('Public function is called.');
            },
            getPrivateVariable: function() {
            return privateVariable;
            }
        };
        })();

        // Using the module
        myModule.publicFunction(); // Outputs: Public function is called.
        console.log(myModule.getPrivateVariable()); // Outputs: I am private
```

### Path Module
- https://nodejs.org/api/path.html
- built in module: `const path = require('path');`
```
        var pathObj = path.parse(__filename);
        console.log(pathObj);
```

### OS Module
- https://nodejs.org/api/os.html
- `const os = require('os');`

```
        var totalMemory = os.totalmem();
        var freeMemory = oslfreemem();
        console.log(`Total Memory: ${totalMemory}`);
        console.log(`Free Memory: ${freeMemory}`);
```

### File System Module
- https://nodejs.org/api/fs.html
- `const fs = require('fs');`

``` 
    // const files = fs.readdir('./') // get a string array 
    // console.log(files)

    const filrs = fs.readdir('./', function(err, files)){// async
        if (err) console.log('Error', err);
        else const.log(`Result`, files)
    } 

```

### Events Module
- https://nodejs.org/api/events.html
```
    // in app.js

    const EventEmitter = require('event');  // first char is capital indicting it's a class, a container for a bunch of related methods and properties

    const emitter = new EventEmitter(); // create a instance/object for the class

    // order is important 
    // Register a listener
    emitter.on('messageLogged', function(arg){
        console.log('Listener called', arg);
    })

    // Raise an event
    // emitter.emit('messageLogged');
    // we can also add argument
    emitter.emit('messageLogged', { id: 1, url: 'https://www.google'});

```

### Extending EventEmitter
- In practice, we usually create a class that has all the capabilities of the event emitter and then we will use that class in our code
- When extending EventEmitter, you typically create a custom class that inherits from it, providing your class with event handling capabilities. 
    - Let's say I want an additional class `logger` that has an additional method `log`
```
    // in logger.js

    const EventEmitter = require('event'); 

    var url = "https://mylogger.io/log"

    class Logger extends EventEmitter{
        log(message){       // don't need to add function key word in a class
            console.log(message);
            this.emit('messageLogged', { id: 1, url: 'https://google.com'})
        } // this is a method
    }

    module.exports = Logger

    // in app.js

    const EventEmitter = require('event'); 

    const Logger = require('./logger'); // class
    const logger = new Logger(); // instance of the custom class that we have defined

    // Resiger a listener
    logger.on('messageLogged', function(arg){
        console.log('Listener called', arg);
    })

    logger.log('message');
```

### HTTP Module
- https://nodejs.org/api/async_context.html
```
    // in app.js
    const http = require('http');

    const server = http.createServer((req, res) => { // this is an event emitter
        if (req.url === '/'){ // root route
            res.write('Hello World');
            res.end();
        }

        if (req.url === '/api/courses'){
            res.write(JSON.stringify([1, 2, 3])); // convert data into JSON syntax
            res.end();
        }
    }); 

    server.listen(3000);
    console.log('Listening on port 3000...');
```
- In practice, we use `Express` which gives our application a clean sturcture to handle various routes.









