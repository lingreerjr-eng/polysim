import os
from dotenv import load_dotenv

load_dotenv()

# API Endpoints
GAMMA_API_URL = "https://gamma-api.polymarket.com"
CLOB_API_URL = "https://clob.polymarket.com"

# Strategy Parameters
ARB_THRESHOLD = 0.99  # Combined price check
MIN_LIQUIDITY = 1000  # Minimum liquidity to consider a market
POLL_INTERVAL = 1.0   # Seconds between polls

# Credentials (load from env)
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
API_KEY = os.getenv("CLOB_API_KEY")
API_SECRET = os.getenv("CLOB_API_SECRET")
API_PASSPHRASE = os.getenv("CLOB_API_PASSPHRASE")

# Market Filtering
TARGET_TAGS = ["Crypto", "Politics"]
