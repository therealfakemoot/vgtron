# Usage
1. Clone the repository.
2. In the repository, the tests/ directory contains the Vegeta targets files. 
3. If necessary, modify the URL in the target files to point to the test site. Give the target files descriptive names (example: `static_get.wp_demo_domain`) as these will be used to label the stored report data files (see note below).
4. When the target files are prepared, simply execute `incremental.sh`. All test cases in the tests/ directory will be executed individually with provided rate, duration, and increment parameters applied. Report data will be stored in appropriately named output files.
5. At this point, you may refer to the Vegeta [report documentation](https://github.com/tsenart/vegeta#report) for details on generating report data.

Note: each test case is isolated into its own target file because Vegeta generates report data per target file. If all test cases were consolidated into a single target file, test data would become clouded. Vegeta's reporting facilities allow collation of arbitrary amounts of report data, so running all test cases individually allows for finer grained reporting.

# Testing Methodology
The default tests cover the most common types of page access, enumerated below. This should offer coverage for a reasonable majority of use cases and allow greater insight into what sort of requests are cached by Engintron.

1. GET
2. GET with query parameters
3. POST that triggers database writes.
4. POST that triggers database read.

# Caveats
Vegeta is capable of generating an effectively arbitrary number of requests per second for equally arbitrary durations. Pass large parameters at your own risk; your OS is likely to interfere with the tests at large values but there is still the risk of generating enough load to bring Apache down entirely.
