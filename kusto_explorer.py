#!/usr/bin/env python3
"""
Kusto DB Explorer - Displays Kusto databases and tables in a tree format
"""
from __future__ import annotations

import argparse
import logging
import sys
import traceback
from datetime import datetime
from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from colorama import Fore, Style, init as colorama_init

# Initialize colorama for cross-platform colored terminal output
colorama_init(autoreset=True)

# Configure logging
def setup_logging() -> logging.Logger:
    """Set up logging to file"""
    script_dir = Path(__file__).parent.resolve()
    log_dir = script_dir / "logs"
    log_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"kusto_explorer_{timestamp}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

# Emojis and styles for the tree structure
class TreeStyle:
    """Styles for the tree display"""
    CLUSTER = f"{Fore.CYAN}🌐 {Style.BRIGHT}"
    DATABASE = f"{Fore.GREEN}📁 {Style.BRIGHT}"
    TABLE = f"{Fore.YELLOW}📋 "
    PIPE = f"{Fore.WHITE}│ "
    TEE = f"{Fore.WHITE}├─"
    ELBOW = f"{Fore.WHITE}└─"
    SPACE = "  "

def parse_args() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Display Kusto databases and tables in a tree format"
    )
    parser.add_argument(
        "cluster_url", 
        help="Kusto cluster URL (e.g., https://mycluster.westus2.kusto.windows.net)"
    )
    return parser.parse_args()

def connect_to_kusto(cluster_url: str) -> KustoClient:
    """
    Connect to Kusto cluster using Azure Identity
    
    Args:
        cluster_url: The URL of the Kusto cluster
        
    Returns:
        KustoClient: A client connected to the Kusto cluster
    """
    try:
        logger.info(f"Connecting to Kusto cluster: {cluster_url}")
        credential = DefaultAzureCredential()
        connection_string = KustoConnectionStringBuilder.with_azure_token_credential(
            cluster_url,
            credential
        )
        client = KustoClient(connection_string)
        logger.info("Successfully connected to Kusto cluster")
        return client
    except Exception as e:
        logger.exception(f"Error connecting to Kusto cluster: {e}")
        print(f"Error connecting to Kusto cluster: {e}")
        traceback.print_exc()
        sys.exit(1)

def get_databases(client: KustoClient) -> list[str]:
    """
    Get all databases from the Kusto cluster
    
    Args:
        client: KustoClient instance
        
    Returns:
        list[str]: List of database names
    """
    try:
        logger.info("Fetching databases")
        result = client.execute_mgmt("", ".show databases")
        databases = [row["DatabaseName"] for row in result.primary_results[0]]
        logger.info(f"Found {len(databases)} databases")
        return databases
    except Exception as e:
        logger.exception(f"Error fetching databases: {e}")
        print(f"Error fetching databases: {e}")
        traceback.print_exc()
        return []

def get_tables(client: KustoClient, database: str) -> list[str]:
    """
    Get all tables from a specific database
    
    Args:
        client: KustoClient instance
        database: Database name
        
    Returns:
        list[str]: List of table names
    """
    try:
        logger.info(f"Fetching tables for database: {database}")
        result = client.execute_mgmt(database, ".show tables")
        tables = [row["TableName"] for row in result.primary_results[0]]
        logger.info(f"Found {len(tables)} tables in database {database}")
        return tables
    except Exception as e:
        logger.exception(f"Error fetching tables for database {database}: {e}")
        print(f"Error fetching tables for database {database}: {e}")
        traceback.print_exc()
        return []

def print_tree(cluster_url: str, databases_tables: dict[str, list[str]]) -> None:
    """
    Print the cluster, databases, and tables in a tree-like format
    
    Args:
        cluster_url: The URL of the Kusto cluster
        databases_tables: Dictionary with database names as keys and lists of tables as values
    """
    # Print cluster
    print(f"{TreeStyle.CLUSTER}{cluster_url}")
    
    # Print databases and tables
    db_count = len(databases_tables)
    for i, (db, tables) in enumerate(databases_tables.items()):
        is_last_db = i == db_count - 1
        
        # Print database
        if is_last_db:
            print(f"{TreeStyle.ELBOW}{TreeStyle.DATABASE}{db}")
            db_prefix = f"{TreeStyle.SPACE}"
        else:
            print(f"{TreeStyle.TEE}{TreeStyle.DATABASE}{db}")
            db_prefix = f"{TreeStyle.PIPE}"
        
        # Print tables
        table_count = len(tables)
        for j, table in enumerate(tables):
            is_last_table = j == table_count - 1
            if is_last_table:
                print(f"{db_prefix}{TreeStyle.ELBOW}{TreeStyle.TABLE}{table}")
            else:
                print(f"{db_prefix}{TreeStyle.TEE}{TreeStyle.TABLE}{table}")

def main() -> None:
    """Main function"""
    try:
        args = parse_args()
        
        # Connect to Kusto
        client = connect_to_kusto(args.cluster_url)
        
        # Get databases
        databases = get_databases(client)
        
        if not databases:
            print("No databases found or unable to fetch databases.")
            return
        
        # Get tables for each database
        databases_tables: dict[str, list[str]] = {}
        for db in databases:
            tables = get_tables(client, db)
            databases_tables[db] = tables
        
        # Print the tree
        print_tree(args.cluster_url, databases_tables)
        
        logger.info("Tree display completed successfully")
    
    except KeyboardInterrupt:
        logger.info("Execution interrupted by user")
        print("\nExecution interrupted by user")
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()