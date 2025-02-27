- Always read files in relative path from the current script file's location. The user can invoke the script from any location, but still the path references should work if those refs are relative to the script file.
- A script or code can get interrupted at any point of time. So, ensure the following:
  + It is idempotent.
  + It can be resumed from the point of interruption.
- Use poetry for managing dependencies. For poetry use local folder `.venv`.
- Use python version 3.13 or above. Import `annotations` from `__future__` for type hints in older versions. Use built-in generic types instead of `typing.List`, `typing.Tuple`, `typing.Optional`, etc.
- Use `logging`, and log to a file, but don't log to stdout.
- Generate relevant `.gitignore` to ignore log files, and other temporary files.
- Run `poetry init` at the root folder specifying the dependencies, and then run `poetry install` to install the dependencies. **DO NOT CREATE THE `pyproject.toml` MANUALLY, AS YOU DON'T KNOW THE VERSIONS OF THE DEPENDENCIES**.
- No need to create extra directories, keep the project structure flat.
- Author name is Contoso Developer.
- While printing an exception always print the full stack trace in the logs and show a user-friendly message to the user.
- Generate a proper `README.md` file with the project name, description, and instructions to run the script.
