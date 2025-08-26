#!/usr/bin/env python3

import os
import json
import logging
from fastmcp import FastMCP
from zep_cloud import Zep

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Your actual Zep setup
client = Zep(
    api_key="z_1dWlkIjoiZWYxMTAyZjAtZDljNi00YmY2LWE5MTItNDVjNDk2YzM5YjQ3In0.XBbxvysrlbFDjLhZzWQSt0xZyKkfTXvRNUNEVJ4ywcle8WaK2ckpNOzaSoks-hWk55TGTScmk3286-O7JR3PbQ",
)

mcp = FastMCP("Zep Memory Server")

@mcp.tool()
def search_memory(query: str) -> str:
    """Search Quinn's memory graph for relevant information"""
    try:
        results = client.graph.search(user_id="quinn_may", query=query)
        return json.dumps(results, indent=2)
    except Exception as e:
        logger.error(f"Memory search failed: {e}")
        return json.dumps({"error": str(e)})

@mcp.tool() 
def check_zep_connection() -> str:
    """Test connection to Zep Cloud API"""
    try:
        # Try to search for anything to test connection
        test = client.graph.search(user_id="quinn_may", query="test", limit=1)
        return json.dumps({"status": "connected", "test_results": len(test.get("edges", []))})
    except Exception as e:
        return json.dumps({"status": "failed", "error": str(e)})

if __name__ == "__main__":
    logger.info("🧠✨ Starting Quinn's Zep Memory MCP Server")
    port = int(os.getenv("PORT", 8080))
    mcp.run("http", port=port, host="0.0.0.0")