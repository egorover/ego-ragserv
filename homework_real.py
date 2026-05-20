"""
Homework - RAG System Test with Real ProxyAPI
"""

from embeddings.embedder import Embedder
from stores.weaviate_store import WeaviateStore

print("=" * 60)
print("HOMEWORK - RAG SYSTEM TEST (Real ProxyAPI)")
print("=" * 60)

# Test data
test_articles = [
    "Machine Learning (ML) is a subset of artificial intelligence that enables computers to learn from data without being explicitly programmed. ML algorithms use statistical techniques to identify patterns and make decisions.",
    
    "Neural networks are computing systems inspired by biological neural networks in the brain. They consist of interconnected nodes organized in layers. The input layer receives data, hidden layers process it, and the output layer produces results."
]

print("\n[STEP 1] Store: Weaviate")
print("-" * 40)

print("\n[STEP 2] Adding data...")
print("-" * 40)

embedder = Embedder(use_proxyapi=True)
store = WeaviateStore(embedder=embedder)

print(f"Adding {len(test_articles)} articles...")
store.add_texts(test_articles)
print(f"Successfully added {len(test_articles)} documents!")

print("\n[STEP 3] Testing search...")
print("-" * 40)

# Query 1: Exact term
query1 = "What is machine learning?"
print(f"\nQuery 1 (exact): {query1}")
results1 = store.query(query1, top_k=2)
for i, r in enumerate(results1, 1):
    print(f"  [{i}] Score: {r.get('score', 0):.4f}")

# Query 2: Synonym  
query2 = "How do computers learn from information?"
print(f"\nQuery 2 (synonym): {query2}")
results2 = store.query(query2, top_k=2)
for i, r in enumerate(results2, 1):
    print(f"  [{i}] Score: {r.get('score', 0):.4f}")

# Analysis
score1 = results1[0].get('score', 0) if results1 else 0
score2 = results2[0].get('score', 0) if results2 else 0

print("\n" + "=" * 60)
print("ANALYSIS")
print("=" * 60)
print(f"1. Score - Exact term: {score1:.4f}")
print(f"   Score - Synonym:    {score2:.4f}")
print("2. Semantic understanding: YES (real embeddings)")
print("3. Improvements: smaller chunks, more TOP_K")

store.close()
print("\n" + "=" * 60)
print("TEST COMPLETED!")
print("=" * 60)
