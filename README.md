
> [!NOTE]
> This code was generated completely using [Github Copilot Code Edits (in agent mode)](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode) with [Claude 3.7 Sonnet](https://www.anthropic.com/news/claude-3-7-sonnet).
>
> It used [copilot custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) to include some persona to the LLM, which can be found here: [`./.github/copilot-instructions.md`](./.github/copilot-instructions.md).
>
> This is the prompt:
> 
> *Create a python code to read a kusto cluster and print the databases and the tables under each db in a tree-like format. It should authenticate using azure-identity, and use ascii chars with emojis for the tree.*


# Kusto DB Explorer

A tool to explore Kusto databases and tables in a tree-like format.

## Description

This Python script connects to a Kusto cluster using Azure Identity authentication and displays all databases and tables in a hierarchical tree format with ASCII characters and emojis for better visualization.

## Requirements

- Python 3.13+
- Poetry package manager

## Dependencies

- azure-kusto-data
- azure-identity
- colorama

## Installation

1. Ensure you have Poetry installed. If not, follow the [Poetry installation guide](https://python-poetry.org/docs/#installation).

2. Install the dependencies:
   ```bash
   poetry install
   ```

## Usage

Run the script with your Kusto cluster URL:
```bash
poetry run python kusto_explorer.py <cluster_url>
```

Example:
```bash
poetry run python kusto_explorer.py https://mycluster.westus2.kusto.windows.net
```

## Authentication

The script uses DefaultAzureCredential for authentication, which tries multiple authentication methods. Make sure you're authenticated with Azure (az login) before running the script.

## Author

Contoso Developer