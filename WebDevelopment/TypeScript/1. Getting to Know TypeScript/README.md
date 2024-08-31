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
At a high level, tsc (the TypeScript compiler) does two things:
- It converts next-generation TypeScript/JavaScript to an older version of JavaScript that works in browsers or other runtimes (“transpiling”).
- It checks your code for type errors.<br>

You Cannot Check TypeScript Types at Runtime
- You may be tempted to write code like this:
    ```
        interface Square {
        width: number;
        }
        interface Rectangle extends Square {
        height: number;
        }
        type Shape = Square | Rectangle;

        function calculateArea(shape: Shape) {
        if (shape instanceof Rectangle) {
            //                 ~~~~~~~~~ 'Rectangle' only refers to a type,
            //                           but is being used as a value here
            return shape.height * shape.width;
            //           ~~~~~~ Property 'height' does not exist on type 'Shape'
        } else {
            return shape.width * shape.width;
          }
        }
    ```
- However, the `instanceof` check happens at runtime, but Rectangle is a type and so it cannot affect the runtime behavior of the code.
    - `instanceof` is an operator in JavaScript used to check whether an object is an instance of a particular class or function. However, Rectangle is a TypeScript type, not a JavaScript class or function.
    - Therefore, when you try to use instanceof Rectangle for the check, TypeScript will throw an error: Rectangle only refers to a type and cannot be used as a value.
    - Additionally, since TypeScript types do not appear in the compiled JavaScript code, this check will also be ineffective at runtime because JavaScript has no knowledge of what Rectangle is.
- There are several ways to do this. One is to introduce a “tag” to explicitly store the type in a way that’s available at runtime:
    ```
    interface Square {
    kind: 'square';
    width: number;
    }
    interface Rectangle {
    kind: 'rectangle';
    height: number;
    width: number;
    }
    type Shape = Square | Rectangle;

    function calculateArea(shape: Shape) {
    if (shape.kind === 'rectangle') {
        return shape.width * shape.height;
        //     ^? (parameter) shape: Rectangle
    } else {
        return shape.width * shape.width;
        //     ^? (parameter) shape: Square
        }
    }
    ```
- Another is to use `class`, as this construct introduces both a type and a corresponding value.
    ```
    class Square {
    width: number;
    constructor(width: number) {
        this.width = width;
        }
    }
    class Rectangle extends Square {
    height: number;
    constructor(width: number, height: number) {
        super(width);
        this.height = height;
        }
    }
    type Shape = Square | Rectangle;

    function calculateArea(shape: Shape) {
    if (shape instanceof Rectangle) {
        return shape.width * shape.height;
        //     ^? (parameter) shape: Rectangle
    } else {
        return shape.width * shape.width;
        //     ^? (parameter) shape: Square
        }
    }
    ```
- You Cannot Overload a Function Based on TypeScript Types
    - Languages like C++ allow you to define multiple versions of a function that differ only in the types of their parameters. This is called “function overloading.” Because the runtime behavior of your code is independent of its TypeScript types, this construct isn’t possible in TypeScript:
        ```
        function add(a: number, b: number) { return a + b; }
        //       ~~~ Duplicate function implementation
        function add(a: string, b: string) { return a + b; }
        //       ~~~ Duplicate function implementation
        ```
    - TypeScript does provide a facility for overloading functions, but it operates entirely at the type level. **You can provide multiple type signatures for a function, but only a single implementation**:
        ```
        function add(a: number, b: number): number;
        function add(a: string, b: string): string;

        function add(a: any, b: any) {
        return a + b;
        }

        const three = add(1, 2);
        //    ^? const three: number
        const twelve = add('1', '2');
        //    ^? const twelve: string
        ```
- TypeScript Types Have No Effect on Runtime Performance
    - Because types and type operations are erased when you generate JavaScript, they cannot have an effect on runtime performance.
    - While there is no runtime overhead, the TypeScript compiler will introduce build time overhead. The TypeScript team takes compiler performance seriously and compilation is usually quite fast, especially for incremental builds.
    - The code that TypeScript emits to support older runtimes may incur a performance overhead versus native implementations.
        - When you use JavaScript features beyond the target version’s support, the TypeScript compiler automatically generates helper code to ensure these features work in older JavaScript versions.
## Get Comfortable with Structural Typing
- Structural typing is a system TypeScript uses that focuses on the shape of objects rather than their specific types or classes. If an object has all the right properties, it fits the type, regardless of how it was created.
    - For example, you define a 2D vector type (Vector2D) with x and y properties.
    - You then create a NamedVector type that adds a name property but still has x and y.
    -  TypeScript allows you to use NamedVector with a function expecting Vector2D because it has the right properties (x and y).
    - This is structural typing in action: TypeScript checks if the object fits the expected structure rather than its declared type.
- Potential Pitfalls: Structural typing can cause unexpected behavior, such as:
    - Adding a 3D vector (Vector3D with x, y, and z) and using it in a function designed for 2D vectors (calculateLength). TypeScript allows this since the structure matches partially, but it leads to logical errors because the z component is ignored.
    - TypeScript doesn’t catch this error because it checks compatibility by structure, not the exact intended type.
- Open Types vs. Sealed Types
    - TypeScript types are "open," meaning they can have more properties than explicitly declared.
    - This openness can cause unexpected behavior when iterating over object properties, as TypeScript can't guarantee all properties match the expected type.
- Classes and Structural Typing
    - Classes in TypeScript are also structurally typed. An object with matching properties can be considered an instance of a class, even if it didn’t go through the class’s constructor, which can bypass validation logic.
- Structural typing is advantageous in testing because it allows you to use simpler objects that conform to a function’s expected interface without needing complex mocking libraries.
    - For example, say you have a function that runs a query on a database and processes the results:
        ```
        interface Author {
            first: string;
            last: string;
        }
        function getAuthors(database: PostgresDB): Author[] {
            const authorRows = database.runQuery(`SELECT first, last FROM authors`);
            return authorRows.map(row => ({first: row[0], last: row[1]}));
        }
        ```
    - Instead of using a full PostgresDB, you can define a narrower interface (DB) and pass a mock object that meets the structural requirements:
        ```
        interface DB {
            runQuery: (sql: string) => any[];
        }
        function getAuthors(database: DB): Author[] {
            const authorRows = database.runQuery(`SELECT first, last FROM authors`);
            return authorRows.map(row => ({first: row[0], last: row[1]}));
        }

        test('getAuthors', () => {
            const authors = getAuthors({
                runQuery(sql: string) {
                return [['Toni', 'Morrison'], ['Maya', 'Angelou']];
                }
            });
            expect(authors).toEqual([
                {first: 'Toni', last: 'Morrison'},
                {first: 'Maya', last: 'Angelou'}
            ]);
        });
        ```

## Limit Use of the `any` Type
- TypeScript’s `any` type allows you to disable most forms of type checking for a symbol.
- The `any` type eliminates type safety, lets you break contracts, harms developer experience, makes refactoring error prone, hides your type design, and undermines confidence in the type system.
- Avoid using `any` when you can!