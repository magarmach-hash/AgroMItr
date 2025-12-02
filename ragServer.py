from mcp.server.fastmcp import FastMCP
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings

PDF_PATHS = ["document1.pdf", "insect.pdf", "fertmanual.pdf","fertmanual2.pdf","schemes.pdf","subsi.pdf"]  # List of PDFs
EMBEDDING_MODEL = "nomic-embed-text"

mcp = FastMCP("rag-server")

all_docs = []
for pdf_path in PDF_PATHS:
    print(f"Loading {pdf_path}...")
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    print(f"Loaded {len(docs)} pages from {pdf_path}")
    all_docs.extend(docs)

# print(f"Total pages loaded from all PDFs: {len(all_docs)}")
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
splits = splitter.split_documents(all_docs)
print(f"Created {len(splits)} chunks from all PDFs")


print("Generating embeddings...")
embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
vectorstore = FAISS.from_documents(splits, embeddings)
retriever = vectorstore.as_retriever()
print("Vector DB Ready")

@mcp.tool()
def rag_query(query: str) -> str:
    docs = retriever.get_relevant_documents(query)
    context = "\n".join([d.page_content for d in docs])
    prompt = f"Answer the question using the context below:\n\n{context}\n\nQuestion: {query}"
    return prompt

if __name__ == "__main__":
    print("Starting MCP RAG server...")
    mcp.run(transport="stdio")
