#!/usr/bin/env python3
import asyncio
import logging
from zep_cloud_server import app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Starting Zep Cloud MCP Server...")
    await app.run()

if __name__ == "__main__":
    asyncio.run(main())