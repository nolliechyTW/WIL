# Content
- Understand the Relationship Between TypeScript and JavaScript
- Know Which TypeScript Options You're Using
- Understand That Code Generation Is Independent of Types
- Get Comfortable with Structural Typing
- Limit Use of the `any` Type

## Understand the Relationship Between TypeScript and JavaScript
- TypeScript compiles to the high-level language, JavaScript. It is this JavaScript that runs, not your TypeScript.
- TypeScript is a superset of JavaScript in a syntactic sense: so long as your JavaScript program doesn’t have any syntax errors then it is also a TypeScript program.
- There are TypeScript programs that are not JavaScript programs. This is because TypeScript adds additional syntax for specifying types. e.g.
```
    function greet(who: string) {
    console.log('Hello', who);
    }
```
- You didn’t have to tell TypeScript that the type of variable: it inferred it from the initial value. e.g.
```
let city = 'new york city';
console.log(city.toUppercase());
//               ~~~~~~~~~~~ Property 'toUppercase' does not exist on type
//                           'string'. Did you mean 'toUpperCase'?
```
- The guiding principle of TypeScript’s type system is that it should model JavaScript’s runtime behavior. But in all of these cases, TypeScript considers it more likely that the odd usage is the result of an error than the developer’s intent, so it goes beyond simply modeling the runtime behavior.  e.g. both expressions below result in the string "23"
```
const x = 2 + '3';  // OK
//    ^? const x: string
const y = '2' + 3;  // OK
//    ^? const y: string
```
- TypeScript adds a static type system that models JavaScript’s runtime behavior and tries to spot code that will throw exceptions at runtime.

## Know Which TypeScript Options You're Using
- Create the configuration file for TypeSciprt to indicate your high-level design choices. You can create one by running `tsc --init`.
- a configuration file, tsconfig.json, can look like this:
```
{
  "compilerOptions": {
    "noImplicitAny": true
  }
}
```
- `noImplicitAny`: controls what TypeScript does when it can’t determine the type of a variable.
    - This becomes an error if you set the `noImplicitAny` option:
        ```
        function add(a, b) {
        //         ~    Parameter 'a' implicitly has an 'any' type
        //            ~ Parameter 'b' implicitly has an 'any' type
        return a + b;
        }
        ```
    - These errors can be fixed by explicitly writing type declarations, either : any or a more specific type:
        ```
        function add(a: number, b: number) {
        return a + b;
        }
        ```
    - Leaving `noImplicitAny` off is only appropriate if you’re transitioning a project from JavaScript to TypeScript. Even then, this should only be a temporary state and you should turn it on as soon as possible.

-  `strictNullChecks`: controls whether `null` and `undefined` are permissible values in every type.
    - This becomes an error if you set the `strictNullChecks` option:
        ```
        const x: number = null;
        //    ~ Type 'null' is not assignable to type 'number'
        ```
    - If you mean to allow `null`, you can fix the error by making your intent explicit:
        ```
        const x: number | null = null;
        ```
    - If you do not wish to permit `null`, you’ll need to track down where it came from and add either a check or an assertion:
        ```
        const statusEl = document.getElementById('status');
        statusEl.textContent = 'Ready';
        // ~~~~~ 'statusEl' is possibly 'null'.

        if (statusEl) {
        statusEl.textContent = 'Ready';  // OK, null has been excluded
        }
        statusEl!.textContent = 'Ready';  // OK, we've asserted that el is non-null
        ```
        - Using an `if` statement in this way is known as “narrowing” or “refining” a type.
        - The “!” on the last line is called a “non-null assertion.” Type assertions have their place in TypeScript.
- There are many other settings that affect language semantics (e.g., `noImplicitThis` and `strictFunctionTypes`); turn on the strict setting. TypeScript is able to catch the most errors with strict. (If you create a project using `tsc --init`, you’ll be in strict mode by default.)
    - There are also a few “stricter than strict” options available. e.g.
        - `noUncheckedIndexedAccess`

## Understand That Code Generation Is Independent of Types
## Get Comfortable with Structural Typing
## Limit Use of the `any` Type