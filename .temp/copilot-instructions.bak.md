# Common Instructions

- Always use consistent naming conventions for variables, functions, and classes.
- Ensure that the code is well-documented and easy to understand.
- Always read files in relative path from the current script file's location. The user can invoke the script from any location, but still the path references should work if those refs are relative to the script file.
- In Windows, ensure TLS values are set to 1.3, and if 1.3 is not supported, then use 1.2.
- A script or code can get interrupted at any point of time. So, ensure the following:
  + It is idempotent.
  + It can be resumed from the point of interruption.
- The user facing API needs to be simple, don't expose too many options, as user might get confused. Keep calues for the options as constants in the script itself.
- Don't assume the versions of any external dependency while adding it to the source code. Using agent mode, you can ask to install the packages, but don't edit the configuration file to add the package.

# Custom Instructions

## SQL

When writing SQL queries, always use lower case for keywords, functions, and identifiers. This helps maintain consistency and readability across the codebase.

Example:
```sql
select first_name, last_name
from users
where user_id = 1;
```

## Python

When writing Python code, always use type hints and ensure compatibility with Python 3.13 and above. Use built-in generic types instead of `typing.List`, `typing.Tuple`, `typing.Optional`, etc., for better readability and simplicity.

Example:
```python
def greet(name: str) -> str:
  return f"Hello, {name}"

def process_data(data: list[int]) -> dict[str, int]:
  return {str(i): i for i in data}
```

## PowerShell

When writing PowerShell scripts, always ensure the code works both in PowerShell 5.1 and PowerShell 7. This helps maintain correctness and consistency across different environments.

Example:
```powershell
# Get the current date and time
$currentDateTime = Get-Date

# Output the current date and time
Write-Output "Current Date and Time: $currentDateTime"
```

# What Not to Do Examples

## SQL

Avoid using uppercase for keywords and functions:
```sql
SELECT First_Name, Last_Name
FROM Users
WHERE User_ID = 1;
```

## Python

Avoid using old-style type hints and ensure compatibility with Python 3.13 and above:
```python
from typing import List, Dict

def greet(name: str) -> str:
  return "Hello, " + name

def process_data(data: List[int]) -> Dict[str, int]:
  return {str(i): i for i in data}
```

## PowerShell

Avoid using code that only works in a specific version of PowerShell:
```powershell
# This might not work in PowerShell 5.1
$currentDateTime = [datetime]::Now

# Output the current date and time
Write-Output "Current Date and Time: $currentDateTime"
```
