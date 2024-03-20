## RESTAPI
### API Definition
an API is a mechanism that enables an application or service(client) to access a resource within another application or service(server). 

### RESTAPI Definition
an application programming interface (API) that conforms to the design principles of the representational state transfer (REST) architectural style; provide a flexible, lightweight way to integrate applications and to connect components in microservices architectures.

### 6 REST design principles(aka architectural constraints)
1. Uniform interface
    - All API requests for the same resource should look the same, no matter where the request comes from
    - For example, each request should contain authentication information instead of relying on the server to maintain a user's logged-in state
2. Client-server decoupling
    - In REST API design, client and server applications must be completely independent of each other
    - The only information that the client application should know is the URI of the requested resource
    - Similarly, a server application shouldn't modify the client application other than passing it to the requested data via HTTP
3. Statelessness
    - REST APIs are stateless, meaning that each request needs to include all the information necessary for processing it. In other words, REST APIs do not require any server-side sessions
    - For example, each request should contain authentication information instead of relying on the server to maintain a user's logged-in state
4. Cacheability
    - When possible, resources should be cacheable on the client or server side. Server responses also need to contain information about whether caching is allowed for the delivered resource
    - This reduces the need to make redundant requests for the same resource, improving application efficiency
5. Layered system architecture
    - In REST APIs, the calls and responses go through different layers. There may be a number of different intermediaries in the communication loop between server and client
    - REST APIs need to be designed so that neither the client nor the server can tell whether it communicates with the end application or an intermediary
    - This enhances the security and scalability of the API
6. Code on demand (optional)
    - REST APIs usually send static resources, but in certain cases, responses can also contain executable code (such as Java applets)
    - For instance, an API might return specific scripts or plugins in response to a client's request to perform particular operations or enhance functionality on the client side

### How REST APIs work
- REST APIs communicate through HTTP requests to perform standard database functions like creating(`POST`), reading(`GET`), updating(`PUT`) and deleting(`DELETE`) records (also known as CRUD) within a resource

- The state of a resource at any particular instant, or timestamp, is known as the **resource representation**. This information can be delivered to a client in virtually any format including JavaScript Object Notation (JSON), HTML, XLT, Python, PHP or plain text. JSON is popular because it’s readable by both humans and machines—and it is programming language-agnostic

- Request headers and parameters are also important in REST API calls because they include important identifier information such as metadata, authorizations, uniform resource identifiers (URIs), caching, cookies and more