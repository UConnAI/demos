# House Control MCP Server

An instructional MCP server that demonstrates all components of the Model Context Protocol (MCP): Tools, Resources, Prompts, and Sampling. This server simulates control and monitoring of a smart house.

## Features

### Tools (Executable Actions)
- **Garage Door Control**: `open_garage_door`, `close_garage_door`
- **Door Locks**: `unlock_front_door`, `lock_front_door`, `unlock_back_door`, `lock_back_door`
- **Lighting**: `turn_on_lights`, `turn_off_lights` (by room)
- **Security**: `arm_security_system`, `disarm_security_system`
- **Sampling**: `sample_temperature`, `sample_motion` (simulated sensor data)

### Resources (Data Access)
- **Static Resources**:
  - `house://status/garage_door` - Garage door status
  - `house://status/security_system` - Security system status
- **Dynamic Resource Templates**:
  - `house://status/{room}/lights` - Light status for any room
  - `house://status/{door}/lock` - Lock status for any door

### Prompts (Predefined Scenarios)
- **secure_house**: Instructions to secure the house
- **welcome_home**: Instructions to prepare for arrival
- **check_house_status**: Complete house status report

### Sampling (Sensor Data)
- Temperature sampling with time-series data
- Motion detection events with timestamps

## Installation

1. Install dependencies:
```bash
pip install -e .
```

2. Add to MCP settings (typically `~/.cline/data/settings/cline_mcp_settings.json`):
```json
{
  "mcpServers": {
    "house-control": {
      "command": "python",
      "args": ["/path/to/house-control-server/src/house_control_server/server.py"]
    }
  }
}
```

## Demo Scenarios

### Example Tool Usage
**Open Garage Door:**
```json
{
  "method": "tools/call",
  "params": {
    "name": "open_garage_door",
    "arguments": {}
  }
}
```

**Response:**
```json
{
  "content": [
    {
      "type": "text",
      "text": "Garage door opened successfully"
    }
  ]
}
```

### Example Resource Access
**Read Garage Door Status:**
```json
{
  "method": "resources/read",
  "params": {
    "uri": "house://status/garage_door"
  }
}
```

**Response:**
```json
{
  "contents": [
    {
      "uri": "house://status/garage_door",
      "mimeType": "application/json",
      "text": "{\"status\": \"open\", \"timestamp\": \"2025-09-23T22:19:52\"}"
    }
  ]
}
```

### Example Prompt Usage
**Get Secure House Prompt:**
```json
{
  "method": "prompts/get",
  "params": {
    "name": "secure_house"
  }
}
```

**Response:**
```json
{
  "description": "Secure the house by closing doors, locking them, and turning off lights",
  "messages": [
    {
      "content": {
        "type": "text",
        "text": "Please secure the house by performing these actions:\n1. Close the garage door\n2. Lock both front and back doors\n3. Turn off all lights in all rooms\n4. Arm the security system\n\nUse the available tools to execute these actions."
      }
    }
  ]
}
```

### Example Sampling
**Sample Temperature:**
```json
{
  "method": "tools/call",
  "params": {
    "name": "sample_temperature",
    "arguments": {
      "duration_minutes": 3
    }
  }
}
```

**Response:**
```json
{
  "content": [
    {
      "type": "text",
      "text": "[\n  {\n    \"timestamp\": \"2025-09-23T22:19:52\",\n    \"temperature_celsius\": 20,\n    \"room\": \"living_room\"\n  },\n  {\n    \"timestamp\": \"2025-09-23T22:20:52\",\n    \"temperature_celsius\": 21,\n    \"room\": \"living_room\"\n  },\n  {\n    \"timestamp\": \"2025-09-23T22:21:52\",\n    \"temperature_celsius\": 22,\n    \"room\": \"living_room\"\n  }\n]"
    }
  ]
}
```

## Architecture

The server maintains simulated state for all house components and provides realistic responses for demonstration purposes. All operations are synchronous for simplicity, though real implementations would interface with actual smart home systems.

## Educational Purpose

This server serves as a comprehensive example of MCP implementation, showcasing:
- Tool definition and execution
- Resource and resource template management
- Prompt creation and retrieval
- Data sampling patterns
- State management in MCP servers
- JSON Schema for tool parameters
