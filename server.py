# server.py
import atexit
import utils.tia_functions as tf
from mcp.server.fastmcp import FastMCP

atexit.register(tf.close_project)

# This is the shared MCP server instance
mcp = FastMCP(name="tia_mcp_server", port=8000, log_level="DEBUG")