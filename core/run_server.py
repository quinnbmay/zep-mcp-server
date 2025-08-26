#!/usr/bin/env python3
import logging
from zep_cloud_server import app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting Zep Cloud MCP Server...")
    app.run()