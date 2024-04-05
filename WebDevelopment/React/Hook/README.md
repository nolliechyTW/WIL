## What's React Hook?
A hook is a special function that lets you "hook into" various React features. Imagine a function that returns an array with two values:
- The first value: a variable with the *state*.
    - In truth, state is kept inside the hook, but is accessible from the component where you "call" the hook.
- The second value: a variable with an handler (a function to change the current state).

## The Rules of React Hooks
1. Only call Hooks at the top level
2. Only call Hooks from React functions (not from regular JavaScript functions)

## Side effects 
Side effects are not predictable because they are actions which are performed with the "outside world."

Common side effects include:
1. Making a request to an API for data from a backend server
2. To interact with browser APIs (that is, to use document or window directly)
3. Using unpredictable timing functions like setTimeout or setInterval

Side effects should be separated from the rendering process. If we need to perform a side effect, it should strictly be done after our component renders.

```
    function User({ name }) {
    document.title = name; 
    // This is a side effect. Don't do this in the component body!
        
    return <h1>{name}</h1>;   
    }
```
->> **useEffect** is a tool that lets us interact with the outside world but not affect the rendering or performance of the component that it's in.

## Hook1 - useEffect
The basic syntax of useEffect:
```
    // 1. import useEffect
    import { useEffect } from 'react';

    function MyComponent() {
        // 2. call it above the returned JSX  
        // 3. pass two arguments to it: a function and an array
        useEffect(() => {}, []);
    
    // return ...
    }
```

The correct way to perform the side effect in our User component is as follows:
```
    import { useEffect } from 'react';

    function User({ name }) {
        useEffect(() => {
            document.title = name;
        }, [name]);
            
        return <h1>{name}</h1>;   
    }
```

- The function passed to useEffect is a callback function. This will be called after the component renders.

- The second argument is an array, called the dependencies array. This array should include all of the values that our side effect relies upon.
    - If you do not provide the dependencies array at all and only provide a function to useEffect, it will run after every render.
    - If you are updating state within your useEffect, make sure to provide an empty dependencies array. This will cause the effect function to only run once after the component has rendered the first time.
    ```
    function MyComponent() {
        const [data, setData] = useState([])  
            
        useEffect(() => {
            fetchData().then(myData => setData(myData))
            // Correct! Runs once after render with empty array
        }, []); 
        
        return <ul>{data.map(item => <li key={item}>{item}</li>)}</ul>
    }
    ```
Sometimes our side effects need to be shut off -> **effect cleanup function**

To use the cleanup function, we need to return a function from within the useEffect function.

The cleanup function will be called when the component is unmounted. When a component is unmounted, our cleanup function runs, our interval is cleared, and we no longer get an error of attempting to update a state variable that doesn't exist.

```
    function Timer() {
        const [time, setTime] = useState(0);
            
        useEffect(() => {
            let interval = setInterval(() => setTime(1), 1000); 

            return () => {
            // setInterval cleared when component unmounts
            clearInterval(interval);
            }
        }, []);
    }
```



## Hook2 - useState
As a rule of thumb, ｗe should only use state to keep the information that requires the user to input data, or trigger events.

Unlike class components that have a single this.state object, useState allows you to declare *multiple* state variables in the same component.


The basic syntax of useState:
```
    import { useState } from 'react';

    function MyComponent() {
    const [state, setState] = useState(initialValue)
    const [counter, setCounter] = useState(initialCount)
    const [something, setSomething] = useState(initialSomething)
    
    return (
        <section>
            <div>{state}</div>
            <button onClink={() => setCounter(counter + 1)}>More</button>
        </section>
    )
    }
```