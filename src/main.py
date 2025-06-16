from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from routers import agent
from container import MCPContainer
from fastapi_mcp import FastApiMCP

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting")
    container = MCPContainer()
    app.container = container

    # Router'ı bağla
    app.include_router(agent.router, tags=["MCP Tools"])

    yield
    print("End")

# Ana uygulama
main_app = FastAPI(
    title="MCP Agent API",
    description="Modular Tool Agent Server using FastMCP",
    version="1.0.0",
    lifespan=lifespan,
)

# MCP için ayrı bir FastAPI uygulaması oluştur
mcp_sub_app = FastAPI()

# MCP'yi bu alt uygulama üzerine kur
mcp_app = FastApiMCP(
    app=mcp_sub_app,
    name="API MCP",
    description="MCP server for the Item API",
    describe_full_response_schema=True,
    describe_all_responses=True,
)

# MCP'yi ana uygulamanın altına mount et
main_app.mount("/mcp", mcp_sub_app)

if __name__ == "__main__":
    uvicorn.run("main:main_app", host="127.0.0.1", port=9000, reload=False)
