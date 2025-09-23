# main.py
from server import mcp

import tools.project
import tools.devices
import tools.software

# Entry point to run the server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")