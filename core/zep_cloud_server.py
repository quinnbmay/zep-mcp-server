#!/usr/bin/env python3
"""
MCP Server for Zep Cloud
This server provides tools for Claude Desktop to interact with Zep Cloud API.
"""

import os
import json
import sys
import logging
from dotenv import load_dotenv
from fastmcp import FastMCP
from zep_cloud_client import ZepCloudClient
from typing import Optional, Dict, Any, Union

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("ZepCloudServer")

# Load environment variables
load_dotenv()

# Initialize FastMCP
mcp = FastMCP("Zep Cloud MCP Server")

# Create client
client = ZepCloudClient()

@mcp.tool()
def search_memory(user_id: str, query: str, limit: int = 10) -> str:
    """Search user's memory graph in Zep Cloud"""
    try:
        result = client.search_graph(user_id, query, limit)
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error searching memory: {e}")
        return json.dumps({"error": str(e)})

@mcp.tool()
def add_memory(user_id: str, data: str, data_type: str = "text") -> str:
    """Add data to user's memory graph"""
    try:
        result = client.add_graph_data(user_id, data, data_type)
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error adding memory: {e}")
        return json.dumps({"error": str(e)})

@mcp.tool()
def check_connection() -> str:
    """Test Zep Cloud API connection"""
    try:
        test = client.search_graph("quinn_may", "test", 1)
        return json.dumps({"status": "connected", "working": True})
    except Exception as e:
        return json.dumps({"status": "failed", "error": str(e)})

if __name__ == "__main__":
    logger.info("🧠✨ Starting Zep Memory MCP Server")
    port = int(os.getenv("PORT", 8080))
    mcp.run("http", port=port, host="0.0.0.0")