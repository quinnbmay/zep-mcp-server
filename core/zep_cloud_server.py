#!/usr/bin/env python3
import json
import logging
import os
from typing import Any, Dict, List, Optional
from dotenv import load_dotenv
from fastmcp import FastMCP
from zep_cloud_client import ZepCloudClient

# Load environment variables
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the FastMCP app
app = FastMCP("Zep Cloud MCP Server")
client = ZepCloudClient()

@app.tool()
def create_user(user_id: str, email: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> str:
    """Create a new user in Zep Cloud"""
    try:
        result = client.create_user(user_id, email, metadata)
        return json.dumps(result)
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return json.dumps({"error": str(e)})

@app.tool()
def get_user(user_id: str) -> str:
    """Get user details from Zep Cloud"""
    try:
        result = client.get_user(user_id)
        return json.dumps(result)
    except Exception as e:
        logger.error(f"Error getting user: {e}")
        return json.dumps({"error": str(e)})

@app.tool()
def search_graph(user_id: str, query: str, limit: int = 10) -> str:
    """Search user's memory graph in Zep Cloud"""
    try:
        result = client.search_graph(user_id, query, limit)
        return json.dumps(result)
    except Exception as e:
        logger.error(f"Error searching graph: {e}")
        return json.dumps({"error": str(e)})

@app.tool()
def add_graph_data(user_id: str, data: str, data_type: str = "text") -> str:
    """Add data to user's memory graph in Zep Cloud"""
    try:
        result = client.add_graph_data(user_id, data, data_type)
        return json.dumps(result)
    except Exception as e:
        logger.error(f"Error adding graph data: {e}")
        return json.dumps({"error": str(e)})

@app.tool()
def check_connection() -> str:
    """Check connection to Zep Cloud API"""
    try:
        result = client.check_connection()
        return json.dumps(result)
    except Exception as e:
        logger.error(f"Error checking connection: {e}")
        return json.dumps({"error": str(e)})