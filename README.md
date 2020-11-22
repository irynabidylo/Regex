Function "isValidBCLicensePlate" returns True if the parameter matches this pattern:
Six characters total:
- three letters then three digits, or
- three digits then three letters, or
- two letters, digit, space or hyphen, two digits, letter
- all letters are UPPERCASE

Function "isValidPythonVariableName" returns True if the parameter matches this pattern:
- Between one and 32 characters total,
- all characters must be lowercase letters or underscores, but not more than one underscore in a row.

Function "isValidEmailAddress" returns True if the parameter matches this pattern:
- Username followed by @ followed by domain name followed by period followed by top-level-domain.
- Username rules: letters (upper or lower case) and underscores (as long as _ is neither the first nor last character): between 1 and 256 characters total,
- Domain name rules: letters (upper or lower case) between 1 and 32 characters total,
- Top-level-domain rules: letters (upper or lower case) between 2 and 5 characters total.

Function "isValidHumanHeight" returns True if the parameter matches this pattern:
- Number of feet, apostrophe, number of inches, double quotation mark.
- The number of feet must be 2-8 inclusive,
- The number of inches must be 0-11 inclusive,
- The number of inches between 0 and 9 may have an optional leading zero (e.g. 5’08” or 5’8”),
- The shortest height is 2’1” (not 2’0”) and the tallest height is 8’11”
- Instead of double quotation marks for inches, the word “in” can be accepted instead.
