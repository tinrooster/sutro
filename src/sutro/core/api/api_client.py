from typing import Dict, Any, Optional, Union, List
from enum import Enum
import aiohttp
import asyncio
import json
import logging
from datetime import datetime
from ratelimit import limits, sleep_and_retry
from backoff import on_exception, expo
import jwt

class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

# ... (rest of the API client code we created earlier)
