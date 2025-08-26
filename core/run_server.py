#!/usr/bin/env python3
import asyncio
import logging
from mcp.server.stdio import stdio_server
from zep_cloud_server import ZepCloudMCPServer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Starting Zep Cloud MCP Server...")
    
    # Create the server instance
    server = ZepCloudMCPServer()
    
    # Run with stdio transport
    async with stdio_server(server.app) as (read_stream, write_stream):
        logger.info("Zep Cloud MCP Server running on stdio")
        await server.app.run(
            read_stream, 
            write_stream, 
            server.app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())