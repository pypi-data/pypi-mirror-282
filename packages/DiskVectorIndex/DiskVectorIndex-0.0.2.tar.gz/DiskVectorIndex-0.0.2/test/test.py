from DiskVectorIndex import DiskVectorIndex

index = DiskVectorIndex("Cohere/trec-rag-2024-index")

while True:
    query = input("\n\nEnter a question: ")
    docs = index.search(query, top_k=3)
    for doc in docs:
        print(doc)
        print("=========")
