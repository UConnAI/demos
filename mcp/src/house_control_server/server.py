#!/usr/bin/env python3
"""
House Control MCP Server - Demonstrates all MCP components
"""
import asyncio
import json
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource,
    ResourceTemplate,
    Tool,
    Prompt,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel
)

# Simulated house state
class HouseState:
    def __init__(self):
        self.garage_door_open = False
        self.front_door_locked = True
        self.back_door_locked = True
        self.security_armed = False
        self.lights = {
            "living_room": False,
            "kitchen": False,
            "bedroom": False,
            "bathroom": False
        }
        self.temperature_readings = []
        self.motion_events = []

    def get_status(self) -> Dict[str, Any]:
        return {
            "garage_door": "open" if self.garage_door_open else "closed",
            "front_door": "locked" if self.front_door_locked else "unlocked",
            "back_door": "locked" if self.back_door_locked else "unlocked",
            "security_system": "armed" if self.security_armed else "disarmed",
            "lights": self.lights.copy()
        }

# Global house state
house_state = HouseState()

# Server setup
server = Server("house-control-server")

@server.list_tools()
async def list_tools() -> List[Tool]:
    """List available tools for house control."""
    return [
        Tool(
            name="open_garage_door",
            description="Open the garage door",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="close_garage_door",
            description="Close the garage door",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="unlock_front_door",
            description="Unlock the front door",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="lock_front_door",
            description="Lock the front door",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="unlock_back_door",
            description="Unlock the back door",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="lock_back_door",
            description="Lock the back door",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="turn_on_lights",
            description="Turn on lights in a specific room",
            inputSchema={
                "type": "object",
                "properties": {
                    "room": {
                        "type": "string",
                        "description": "Room name (living_room, kitchen, bedroom, bathroom)"
                    }
                },
                "required": ["room"]
            }
        ),
        Tool(
            name="turn_off_lights",
            description="Turn off lights in a specific room",
            inputSchema={
                "type": "object",
                "properties": {
                    "room": {
                        "type": "string",
                        "description": "Room name (living_room, kitchen, bedroom, bathroom)"
                    }
                },
                "required": ["room"]
            }
        ),
        Tool(
            name="arm_security_system",
            description="Arm the security system",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="disarm_security_system",
            description="Disarm the security system",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="sample_temperature",
            description="Sample temperature readings from rooms",
            inputSchema={
                "type": "object",
                "properties": {
                    "duration_minutes": {
                        "type": "integer",
                        "description": "Duration to sample in minutes",
                        "default": 5
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="sample_motion",
            description="Sample motion detection events",
            inputSchema={
                "type": "object",
                "properties": {
                    "duration_minutes": {
                        "type": "integer",
                        "description": "Duration to sample in minutes",
                        "default": 5
                    }
                },
                "required": []
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent | ImageContent | EmbeddedResource]:
    """Handle tool calls for house control actions."""
    if name == "open_garage_door":
        house_state.garage_door_open = True
        return [TextContent(type="text", text="Garage door opened successfully")]

    elif name == "close_garage_door":
        house_state.garage_door_open = False
        return [TextContent(type="text", text="Garage door closed successfully")]

    elif name == "unlock_front_door":
        house_state.front_door_locked = False
        return [TextContent(type="text", text="Front door unlocked successfully")]

    elif name == "lock_front_door":
        house_state.front_door_locked = True
        return [TextContent(type="text", text="Front door locked successfully")]

    elif name == "unlock_back_door":
        house_state.back_door_locked = False
        return [TextContent(type="text", text="Back door unlocked successfully")]

    elif name == "lock_back_door":
        house_state.back_door_locked = True
        return [TextContent(type="text", text="Back door locked successfully")]

    elif name == "turn_on_lights":
        room = arguments.get("room")
        if room in house_state.lights:
            house_state.lights[room] = True
            return [TextContent(type="text", text=f"Lights turned on in {room}")]
        else:
            return [TextContent(type="text", text=f"Unknown room: {room}")]

    elif name == "turn_off_lights":
        room = arguments.get("room")
        if room in house_state.lights:
            house_state.lights[room] = False
            return [TextContent(type="text", text=f"Lights turned off in {room}")]
        else:
            return [TextContent(type="text", text=f"Unknown room: {room}")]

    elif name == "arm_security_system":
        house_state.security_armed = True
        return [TextContent(type="text", text="Security system armed")]

    elif name == "disarm_security_system":
        house_state.security_armed = False
        return [TextContent(type="text", text="Security system disarmed")]

    elif name == "sample_temperature":
        duration = arguments.get("duration_minutes", 5)
        # Simulate temperature sampling
        readings = []
        for i in range(duration):
            temp = 20 + (i % 5)  # Simulate varying temperature
            timestamp = datetime.now() + timedelta(minutes=i)
            readings.append({
                "timestamp": timestamp.isoformat(),
                "temperature_celsius": temp,
                "room": "living_room"
            })
        house_state.temperature_readings = readings
        return [TextContent(type="text", text=json.dumps(readings, indent=2))]

    elif name == "sample_motion":
        duration = arguments.get("duration_minutes", 5)
        # Simulate motion detection
        events = []
        for i in range(duration):
            if i % 2 == 0:  # Motion every other minute
                timestamp = datetime.now() + timedelta(minutes=i)
                events.append({
                    "timestamp": timestamp.isoformat(),
                    "motion_detected": True,
                    "location": "living_room"
                })
        house_state.motion_events = events
        return [TextContent(type="text", text=json.dumps(events, indent=2))]

    else:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]

@server.list_resources()
async def list_resources() -> List[Resource]:
    """List static resources."""
    return [
        Resource(
            uri="house://status/garage_door",
            name="Garage Door Status",
            description="Current status of the garage door",
            mimeType="application/json"
        ),
        Resource(
            uri="house://status/security_system",
            name="Security System Status",
            description="Current status of the security system",
            mimeType="application/json"
        )
    ]

@server.list_resource_templates()
async def list_resource_templates() -> List[ResourceTemplate]:
    """List dynamic resource templates."""
    return [
        ResourceTemplate(
            uriTemplate="house://status/{room}/lights",
            name="Room Lights Status",
            description="Current status of lights in a specific room",
            mimeType="application/json"
        ),
        ResourceTemplate(
            uriTemplate="house://status/{door}/lock",
            name="Door Lock Status",
            description="Current status of a door lock",
            mimeType="application/json"
        )
    ]

@server.read_resource()
async def read_resource(uri: str) -> str:
    """Read resource content."""
    if uri == "house://status/garage_door":
        return json.dumps({
            "status": "open" if house_state.garage_door_open else "closed",
            "timestamp": datetime.now().isoformat()
        })

    elif uri == "house://status/security_system":
        return json.dumps({
            "status": "armed" if house_state.security_armed else "disarmed",
            "timestamp": datetime.now().isoformat()
        })

    elif uri.startswith("house://status/") and uri.endswith("/lights"):
        room = uri.split("/")[-2]
        if room in house_state.lights:
            return json.dumps({
                "room": room,
                "lights_on": house_state.lights[room],
                "timestamp": datetime.now().isoformat()
            })
        else:
            raise ValueError(f"Unknown room: {room}")

    elif uri.startswith("house://status/") and uri.endswith("/lock"):
        door = uri.split("/")[-2]
        if door == "front_door":
            locked = house_state.front_door_locked
        elif door == "back_door":
            locked = house_state.back_door_locked
        else:
            raise ValueError(f"Unknown door: {door}")

        return json.dumps({
            "door": door,
            "locked": locked,
            "timestamp": datetime.now().isoformat()
        })

    else:
        raise ValueError(f"Unknown resource: {uri}")

@server.list_prompts()
async def list_prompts() -> List[Prompt]:
    """List available prompts."""
    return [
        Prompt(
            name="secure_house",
            description="Secure the house by closing doors, locking them, and turning off lights",
            arguments=[]
        ),
        Prompt(
            name="welcome_home",
            description="Prepare house for arrival by unlocking front door, turning on lights, and disarming security",
            arguments=[]
        ),
        Prompt(
            name="check_house_status",
            description="Provide a complete status report of all house components",
            arguments=[]
        )
    ]

@server.get_prompt()
async def get_prompt(name: str, arguments: Dict[str, Any]) -> List[TextContent | ImageContent | EmbeddedResource]:
    """Get prompt content with instructions."""
    if name == "secure_house":
        return [TextContent(
            type="text",
            text="""Please secure the house by performing these actions:
1. Close the garage door
2. Lock both front and back doors
3. Turn off all lights in all rooms
4. Arm the security system

Use the available tools to execute these actions."""
        )]

    elif name == "welcome_home":
        return [TextContent(
            type="text",
            text="""Please prepare the house for arrival by performing these actions:
1. Unlock the front door
2. Turn on lights in the living room and kitchen
3. Disarm the security system

Use the available tools to execute these actions."""
        )]

    elif name == "check_house_status":
        status = house_state.get_status()
        return [TextContent(
            type="text",
            text=f"""Current house status:

Garage Door: {status['garage_door']}
Front Door: {status['front_door']}
Back Door: {status['back_door']}
Security System: {status['security_system']}

Lights:
{json.dumps(status['lights'], indent=2)}

Use the available resources to get more detailed information if needed."""
        )]

    else:
        return [TextContent(type="text", text=f"Unknown prompt: {name}")]

async def main():
    """Main server entry point."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
