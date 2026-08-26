# mcp
## MCP standardizes how AI models interact with tools and data

🧱 High-Level MCP Architecture Overview

MCP follows a client-server model, where:
- MCP Hosts run the AI models
- MCP Clients initiate requests
- MCP Servers serve context, tools, and capabilities

Key Components:
- Resources – Static or dynamic data for models
- Prompts – Predefined workflows for guided generation
- Tools – Executable functions like search, calculations
- Sampling – Agentic behavior via recursive interactions

## Quickstart:
+ uv init mcp-server-demo
+ cd mcp-server-demo
+ uv add "mcp[cli]"
+ uv run mcp
+ uv run mcp install server.py # install this server in Claude Desktop, https://claude.ai/download
+ uv run mcp dev server.py # test it with the MCP Inspector

### Server.py
- uv run mcp run server.py
- uv run mcp dev server.py # need to install MCP Inspector, copy token to "Proxy Session Token"
