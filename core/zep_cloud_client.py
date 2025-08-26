#!/usr/bin/env python3
import os
import json
import logging
from typing import Any, Dict, List, Optional
from dotenv import load_dotenv
from zep_cloud import Zep

load_dotenv()
logger = logging.getLogger(__name__)

class ZepCloudClient:
    def __init__(self):
        api_key = os.getenv('ZEP_API_KEY')
        self.client = Zep(api_key=api_key)
        logger.info("Zep Cloud client initialized successfully")
    
    def search_graph(self, user_id: str, query: str, limit: int = 10) -> Dict[str, Any]:
        """Search user's memory graph"""
        try:
            results = self.client.graph.search(user_id=user_id, query=query, limit=limit)
            
            # Format results for JSON serialization
            formatted = {
                "query": query,
                "user_id": user_id, 
                "limit": limit,
                "success": True,
                "edges": [],
                "nodes": []
            }
            
            # Process edges (facts)
            if hasattr(results, 'edges') and results.edges:
                for edge in results.edges:
                    formatted["edges"].append({
                        "fact": edge.fact,
                        "score": edge.score,
                        "created_at": str(edge.created_at)
                    })
            
            # Process nodes 
            if hasattr(results, 'nodes') and results.nodes:
                for node in results.nodes:
                    formatted["nodes"].append({
                        "label": node.label,
                        "score": node.score,
                        "attributes": node.attributes
                    })
            
            return formatted
            
        except Exception as e:
            logger.error(f"Graph search failed: {e}")
            return {"error": str(e), "success": False}
    
    def add_graph_data(self, user_id: str, data: str, data_type: str = "text") -> Dict[str, Any]:
        """Add data to user's memory graph"""
        try:
            response = self.client.graph.add(
                user_id=user_id,
                type=data_type, 
                data=data
            )
            
            return {
                "success": True,
                "user_id": user_id,
                "data_type": data_type,
                "uuid": response.uuid,
                "processed": response.processed
            }
            
        except Exception as e:
            logger.error(f"Adding graph data failed: {e}")
            return {"error": str(e), "success": False}