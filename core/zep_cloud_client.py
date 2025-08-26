#!/usr/bin/env python3
import os
import requests
import logging
from typing import Any, Dict, List, Optional
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class ZepCloudClient:
    def __init__(self):
        self.api_key = os.getenv('ZEP_API_KEY')
        self.base_url = os.getenv('ZEP_CLOUD_API_URL', 'https://api.getzep.com/api/v2')
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def create_user(self, user_id: str, email: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create a new user"""
        data = {'user_id': user_id}
        if email:
            data['email'] = email
        if metadata:
            data['metadata'] = metadata
        
        response = requests.post(f'{self.base_url}/users', json=data, headers=self.headers)
        return response.json()
    
    def get_user(self, user_id: str) -> Dict[str, Any]:
        """Get user details"""
        response = requests.get(f'{self.base_url}/users/{user_id}', headers=self.headers)
        return response.json()
    
    def search_graph(self, user_id: str, query: str, limit: int = 10) -> Dict[str, Any]:
        """Search user's memory graph"""
        data = {
            'user_id': user_id,
            'query': query,
            'limit': limit
        }
        response = requests.post(f'{self.base_url}/graph/search', json=data, headers=self.headers)
        return response.json()
    
    def add_graph_data(self, user_id: str, data: str, data_type: str = 'text') -> Dict[str, Any]:
        """Add data to user's memory graph"""
        payload = {
            'user_id': user_id,
            'data': data,
            'data_type': data_type
        }
        response = requests.post(f'{self.base_url}/graph/add', json=payload, headers=self.headers)
        return response.json()
    
    def check_connection(self) -> Dict[str, Any]:
        """Check API connection"""
        try:
            response = requests.get(f'{self.base_url}/health', headers=self.headers, timeout=5)
            return {'status': 'connected', 'code': response.status_code}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}