from fastapi import FastAPI
from fastapi.routing import APIRouter

class FastApiMCP:
    def __init__(self, app: FastAPI, name: str = "MCP Server", description: str = "", describe_full_response_schema: bool = False, describe_all_responses: bool = False):
        self.app = app
        self.name = name
        self.description = description
        self.describe_full_response_schema = describe_full_response_schema
        self.describe_all_responses = describe_all_responses

    def mount(self):
        router = APIRouter()

        @router.get("/")
        async def root_info():
            return {
                "name": self.name,
                "description": self.description,
                "status": "MCP server is running!"
            }

        self.app.include_router(router, prefix="/mcp")
