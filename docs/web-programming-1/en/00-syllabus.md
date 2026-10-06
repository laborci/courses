# Web Programming I – Web Operations, Standards, and Quality

The subject introduces the web as an open, distributed information system. By the end of the course, students will overview how networks, browsers, servers, web data, and standards connect, and based on this knowledge, will be able to interpret the security, accessibility, and performance decisions of web systems. The emphasis is on enduring concepts and relationships.

## Purpose and benefits of the course

Using and creating web services affects many IT fields. The subject helps students not just to see an interface, but to understand the underlying communication, the tasks of the participants, and the compromises that determine the quality of the service. The perspective acquired here can be used in development, operations, security analysis, and evaluation of digital services.

## Expected learning outcomes

By the end of the course, the student will:

- be able to distinguish between the internet and the World Wide Web, and explain the relationship between the main actors of the web;
- be able to trace the path of a web request and conceptually interpret the role of HTTP, HTTPS, DNS, and TLS;
- recognize the fundamental tasks of web documents, browsers, APIs, and application models;
- be able to interpret the basic concepts of identification, authorization, and web security;
- be able to name accessibility, privacy, performance, and reliability aspects when evaluating a web service.

## Weeks and chapters

### Week 01 – What is the web?

The first week starts from the significance of the web, then discusses its historical evolution, main actors, client-server model, and open standards as parts of a common system. The difference between the internet and the web is presented in the weekly introduction.


- [01.01. The web as a general platform](01-01-web-as-a-platform.md) — the role of the web among IT fields.
- [01.02. The evolution of the web](01-02-web-evolution.md) — the relationship between the document-centric and application-like web.
- [01.03. Main actors of the web](01-03-web-actors.md) — the tasks of the browser, server, content provider, and intermediaries.
- [01.04. Client-server model and tiers](01-04-client-server-and-multitier.md) — the request-response operation and logical tiers.
- [01.05. Web standards and interoperability](01-05-web-standards-and-interoperability.md) — the role of open rules in system cooperation.

### Week 02 – Web addresses and HTTP basics

The second week shows how we name a web resource, how we request it, and how we read the response. It also connects methods, status codes, and headers in the browser's Network panel.


- [02.01. Web addresses and resources](02-01-web-addresses-and-resources.md) — the parts of the URL and the concept of a resource.
- [02.02. The HTTP request and response](02-02-http-request-and-response.md) — the message exchange between the client and the server.
- [02.03. HTTP methods](02-03-http-methods.md) — the intent of the request and the fundamental difference between GET and POST.
- [02.04. HTTP status codes](02-04-http-status-codes.md) — interpreting the result of the response.
- [02.05. Headers, body, and content types](02-05-headers-body-and-content-types.md) — further parts of the message and the difference between HTML/JSON.
- [02.06. Observing a request](02-06-reading-network-panel.md) — basic reading of the Network panel.

### Week 03 – Browser and web document

Examines the role of HTML, CSS, and JavaScript, the DOM, rendering, and loading resources. Covers semantic documents, using Can I use?, as well as the browser role of local files, IndexedDB, and WebGL.


- [03.01. HTML, CSS, and JavaScript](03-01-html-css-and-javascript.md) — the structure, appearance, and behavior of the web interface.
- [03.02. Document structure, DOM, and semantics](03-02-document-structure-and-dom.md) — the difference between the HTML source and the current document tree.
- [03.03. Browser rendering](03-03-browser-rendering.md) — the steps from the document to the visible interface.
- [03.04. Loading web resources](03-04-loading-web-resources.md) — requests for images, stylesheets, scripts, and other files.
- [03.05. Browser compatibility](03-05-browser-compatibility.md) — usability in different environments and Can I use? support tables.
- [03.06. Browser capabilities](03-06-browser-capabilities.md) — local files, IndexedDB, Canvas/WebGL, and other browser APIs.

### Week 04 – The complete path of a web request

Connecting the already known URLs, HTTP messages, and browser resources, it traces through name resolution, connection, and intermediary systems. Discusses the role of DNS, TCP, TLS, proxies, and CDNs at a conceptual level.


- [04.01. Domain name, IP address, and DNS](04-01-dns-and-ip-addresses.md) — the steps from the hostname to the network address.
- [04.02. Connection establishment, TCP, and TLS](04-02-connection-tcp-and-tls.md) — the role of transport and protected communication.
- [04.03. Protection and limits of HTTPS](04-03-https-protection-and-limits.md) — confidentiality, integrity, server authentication, and the limits of protection.
- [04.04. Proxies, reverse proxies, and CDNs](04-04-proxies-and-cdns.md) — intermediaries and content delivery.
- [04.05. The complete path of a web request](04-05-complete-web-request.md) — from the web address to the usable interface.
- [04.06. Latency and failures](04-06-latency-and-failures.md) — interpreting the symptoms of different stages.

### Week 05 – Web data and APIs

Arranges the basic concepts of APIs, JSON and XML data exchange, REST, GraphQL, and RPC. Also presents the role of real-time communication and versioning.


- [05.01. What is a web API?](05-01-what-is-a-web-api.md) — the contract between programs and its parts.
- [05.02. JSON, XML, and structured data](05-02-json-xml-and-data.md) — the format, meaning, and missing values of data.
- [05.03. REST and HTTP resources](05-03-rest-and-http-resources.md) — resources, methods, and responses.
- [05.04. GraphQL and RPC](05-04-graphql-and-rpc.md) — field selection and operation-centric APIs.
- [05.05. Changing data and events](05-05-changing-data-and-events.md) — polling, SSE, WebSocket, and webhook.
- [05.06. Versioning and documentation](05-06-api-evolution-and-documentation.md) — compatibility, changes, and API description.

### Week 06 – Web applications and rendering strategies

Compares multi-page and single-page applications, client-side, server-side, and static rendering. Connects the aspects of architecture selection to the user goal and the data exchange learned in the previous week.


- [06.01. Multi-page and single-page applications](06-01-multi-page-and-single-page-apps.md) — MPA, SPA, and navigation.
- [06.02. Client-side rendering](06-02-client-side-rendering.md) — JavaScript, API data, and the view built in the browser.
- [06.03. Server-side rendering](06-03-server-side-rendering.md) — HTML generated on request and hydration.
- [06.04. Static and hybrid rendering](06-04-static-rendering-and-hybrids.md) — pre-built HTML and mixed strategies.
- [06.05. Navigation and client-side state](06-05-navigation-and-client-state.md) — URL, history, and local state.
- [06.06. Service worker and offline operation](06-06-service-workers-and-offline.md) — resource caching and the limits of offline use.
- [06.07. Choosing an application architecture](06-07-choosing-an-application-architecture.md) — model and rendering adapted to the user task.

### Week 07 – State, identity, and access

Alongside stateless HTTP, it discusses necessary state management, cookies, sessions, and tokens. Separates authentication from authorization, then introduces the basic idea of external login and single sign-on.


- [07.01. Stateless HTTP and application state](07-01-stateless-http-and-application-state.md) — separate requests and user continuity.
- [07.02. Cookies and sessions](07-02-cookies-and-sessions.md) — session identifier and server-side state.
- [07.03. Browser storage and tokens](07-03-browser-storage-and-tokens.md) — localStorage, sessionStorage, IndexedDB, and access values.
- [07.04. Authentication and authorization](07-04-authentication-and-authorization.md) — the difference between identity and operation permission.
- [07.05. OAuth 2.0 and OpenID Connect](07-05-oauth-and-openid-connect.md) — delegated access and external identity.
- [07.06. Single and external login](07-06-sso-and-external-login.md) — shared identity provider and local sessions.

### Week 08 – Web security basics

Starting from a threat model, it examines the role of the same-origin policy, CORS, XSS, CSRF, and injection attacks. Covers defense aspects of passwords, multi-factor authentication, and HTTPS.


- [08.01. Threat models and trust boundaries](08-01-threat-models-and-trust-boundaries.md) — assets to protect, actors, and the boundaries of the request.
- [08.02. Same-origin policy and CORS](08-02-same-origin-policy-and-cors.md) — the origin, browser reading, and preflight.
- [08.03. XSS, CSRF, and injection](08-03-xss-csrf-and-injection.md) — three different attack paths and defense principles.
- [08.04. Passwords, MFA, and sessions](08-04-passwords-mfa-and-sessions.md) — password storage, second factor, and access values.
- [08.05. The role and limits of HTTPS](08-05-https-and-its-limits.md) — the difference between the protected network segment and application errors.
- [08.06. OWASP and security review](08-06-owasp-and-security-review.md) — risk framework and analysis of a login process.

### Week 09 – The quality web

Discusses accessibility, semantics, responsiveness, performance, and searchability as parts of the user experience. Also connects privacy and digital ethics issues here.


- [09.01. Accessibility and inclusive design](09-01-accessibility-and-inclusive-design.md) — different use situations and the WCAG approach.
- [09.02. Semantics, keyboard, and screen reader](09-02-semantics-keyboard-and-screen-readers.md) — the meaning and operability of the document.
- [09.03. Responsive and device-independent design](09-03-responsive-and-device-independent-design.md) — flexible layout and different input methods.
- [09.04. User-perceived performance](09-04-user-perceived-performance.md) — visible content, interaction, and stability.
- [09.05. Searchability and content quality](09-05-searchability-and-content-quality.md) — crawling, indexing, and useful content.
- [09.06. Privacy, tracking, and digital ethics](09-06-privacy-tracking-and-digital-ethics.md) — data collection, consent, and genuine choice.

### Week 10 – Reliable and high-performance web

Gathers the concepts of availability, error handling, load time, caching, and load peaks. Shows how performance, security, and costs interact.


- [10.01. Quality of service and availability](10-01-service-quality-and-availability.md) — user goals, recovery, SLI, SLO, and SLA.
- [10.02. Error handling and user communication](10-02-errors-and-user-communication.md) — status codes, clear feedback, and retry.
- [10.03. Response time, loading, and resource needs](10-03-response-time-load-and-resources.md) — the complete request path and measuring slow cases.
- [10.04. HTTP cache and CDN](10-04-http-cache-and-cdn.md) — cache layers, freshness, and geographical distance.
- [10.05. Load peaks and observability](10-05-load-peaks-and-observability.md) — queue, graceful degradation, and diagnosis.
- [10.06. Performance, security, and cost](10-06-performance-security-and-cost.md) — conscious compromises measured against application goals.

## Course information

The final rules for completion, evaluation, and submission are recorded in the course's separate documents issued to students. This overview does not establish independent deadlines or scoring.

Disclaimer: This document was translated from the Hungarian version using AI (Gemini).
