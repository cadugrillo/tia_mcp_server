# server.py
import atexit
import utils.tia_functions as tf
from mcp.server.fastmcp import FastMCP

atexit.register(tf.close_project)

# This is the shared MCP server instance
mcp = FastMCP("tia_mcp_server")