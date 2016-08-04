# Using `vegeta`

## Target Files
A target file contains, more or less, one or more raw HTTP requests. An example:
```
GET http://google.com
Content-type: application/json
Extra-Header: stuff_and_things
@/path/to/body_contents
```

`body_contents` is sent verbatim, meaning that if the endpoint these reuqests are being sent to requires a form-encoded payload, body_contents must literally be a form-encoded string. You can include JSON or raw binary data. It's important to note that you must handle your own Content-type header if the endpoint requires it.

## Invoking vgtron
For help using vgtron, please see the help output: `vgtron --help`.

# Testing Methodology
The example tests cover the most common types of page access, enumerated below. This should offer coverage for a reasonable majority of use cases.

1. GET, statically cachable page.
2. GET with query parameters, no database interaction.
3. POST that triggers database writes.
4. POST that triggers database read.

# Caveats
Vegeta is capable of generating an effectively arbitrary number of requests per second for equally arbitrary durations. Pass large parameters at your own risk; your OS is likely to interfere with the tests at large values but there is still the risk of generating enough load to bring Apache down entirely.
