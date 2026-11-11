import os
from fastmcp import FastMCP

mcp = FastMCP("Ferramentas Compartilhadas")

@mcp.tool()
def consultar_status(servico: str) -> str:
    """Consulta o status atual de um sistema ou servico interno."""
    return f"O servico {servico} esta ativo e sincronizado."

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 8000))
    mcp.run(transport="http", host="0.0.0.0", port=porta)
  
