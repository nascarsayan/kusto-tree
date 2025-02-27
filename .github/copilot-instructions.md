- Always read files in relative path from the current script file's location. The user can invoke the script from any location, but still the path references should work if those refs are relative to the script file.
- A script or code can get interrupted at any point of time. So, ensure the following:
  + It is idempotent.
  + It can be resumed from the point of interruption.
- Use poetry for managing dependencies. For poetry use local folder `.venv`. If not present, creaate it using `python3 -m venv .venv`.
- Use `black` for code formatting.
- Use python version 3.13 or above. Import `annotations` from `__future__` for type hints in older versions. Use built-in generic types instead of `typing.List`, `typing.Tuple`, `typing.Optional`, etc.
- Use `pytest` for testing.
