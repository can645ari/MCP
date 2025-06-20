
Sample MCP API
===============

📌 Project Overview

Sample MCP API is a scalable, extendable, and maintainable API solution designed for Modular Code Processing (MCP) systems. Built on top of FastAPI, it provides a solid foundation for developing microservice architectures with modular design patterns.

The project is enhanced with dependency injection, code analysis tools, and customizable modules to support enterprise-grade applications.

---

🚀 Technologies

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- Dependency Injection (Custom Container Design)

## 📂 Project Structure

```bash
Sample_MCP_API/
│
├── src/
│   ├── business/core/            # Core dependency injection container
│   ├── mcp_client/               # MCP client module
│   ├── mcp_server_fastmcp/       # MCP server module
│   ├── models/                   # Data models (Pydantic)
│   ├── routers/                  # API route definitions
│   ├── tools/                    # Code analysis & utility tools
│   └── main.py                   # Application entry point
│
├── tests/                        # Unit tests (expandable)
├── requirements.txt              # Project dependencies
└── README.txt                    # Documentation file

```

⚙️ Installation Guide

1️⃣ Clone the Repository

```bash
git clone https://github.com/fatihdagdeviren/Sample_MCP_API.git
cd Sample_MCP_API


2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

🖥️ Running the Application

To start the server in development mode:

```bash
uvicorn src.main:app --reload
```

---

📊 API Documentation

Automatically generated by FastAPI:

- Swagger UI: http://localhost:9000/docs

---

🧩 Key Components

🔧 Dependency Injection

Custom DI container defined in `business/core/container.py`.

🧮 Data Models

Defined with Pydantic in the `models/` directory.

🌐 Routers

API endpoints are defined under `routers/agent.py`. Routes are registered as:

```python
app.include_router(agent.router, tags=["MCP Tools"])
```

🛠 Code Analysis Tools

- code_analysis_tool.py
- code_docstring_tool.py
- base_tool.py

---

🎯 Target Use Cases

- Enterprise microservice-based systems
- Code quality evaluation and analysis
- Modular and scalable API architectures
- Automation and tooling systems

---

🔒 License

This project is licensed under the MIT License.

---

✉️ Contact

Developer: Fatih Dağdeviren  
GitHub: https://github.com/fatihdagdeviren

---

Note:
This project serves both as a learning platform and a reference architecture for enterprise API development.
