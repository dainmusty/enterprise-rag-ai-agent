import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("company_docs")

results = collection.query(
    query_texts=["What is the leave policy?"],
    n_results=2
)

print(results["documents"])