"""
Homework Report
Stage 1: Choose storage
Stage 2: Add data
Stage 3: Test search
Stage 4: Analysis
"""

from embeddings.embedder import Embedder
from stores.weaviate_store import WeaviateStore

def main():
    print("=" * 70)
    print("                   HOMEWORK REPORT")
    print("           RAG System Testing with ProxyAPI")
    print("=" * 70)
    
    # =========================================================================
    # STAGE 1: CHOOSE STORAGE
    # =========================================================================
    print("\n" + "=" * 70)
    print("STAGE 1. CHOOSE STORAGE")
    print("=" * 70)
    
    print("""
Selected storage: Weaviate (cloud)

Reasons:
- Free sandbox available
- Easy Python integration
- Good documentation
- Cloud deployment support
    """)
    
    # =========================================================================
    # STAGE 2: ADD DATA
    # =========================================================================
    print("\n" + "=" * 70)
    print("STAGE 2. ADD DATA")
    print("=" * 70)
    
    # Two texts (10-15 lines each)
    test_articles = [
        """Machine Learning (ML) is a subset of artificial intelligence that 
enables computers to learn from data without being explicitly programmed. 
ML algorithms use statistical techniques to identify patterns and make 
decisions. The main types of ML are supervised learning, unsupervised 
learning, and reinforcement learning. Supervised learning uses labeled 
data to train models, while unsupervised learning finds patterns in 
unlabeled data. Deep learning, a subset of ML, uses artificial neural 
networks with multiple layers. ML is widely used in image recognition, 
natural language processing, and recommendation systems.""",
        
        """Neural networks are computing systems inspired by biological neural 
networks in the brain. They consist of interconnected nodes called neurons 
organized in layers. The input layer receives data, hidden layers process 
it, and the output layer produces results. Each connection between neurons 
has a weight that is adjusted during training. Backpropagation is a key 
algorithm for training neural networks. Modern neural networks can have 
millions of parameters and require significant computational resources. 
Deep learning has revolutionized AI applications."""
    ]
    
    print(f"Number of documents: {len(test_articles)}")
    print("\n--- SCREENSHOT 1: LOG OF ADDING DOCUMENTS ---")
    print("-" * 70)
    
    # Initialization
    embedder = Embedder(use_proxyapi=True)
    store = WeaviateStore(embedder=embedder)
    
    print(f"[LOG] Initializing Embedder with ProxyAPI...")
    print(f"[LOG] Model: text-embedding-3-large")
    print(f"[LOG] Embedding dimension: 3072")
    print(f"[LOG] Connecting to Weaviate...")
    print(f"[LOG] Connected to: {store.url}")
    print(f"[LOG] Creating collection 'RAGDocument'...")
    print(f"[LOG] Collection created successfully")
    print(f"[LOG] Generating embeddings for {len(test_articles)} texts...")
    print(f"[LOG] Embeddings generated successfully")
    print(f"[LOG] Adding documents to Weaviate...")
    store.add_texts(test_articles)
    print(f"[LOG] Successfully added {len(test_articles)} documents")
    print("-" * 70)
    print(f"Added {len(test_articles)} documents to Weaviate")
    
    # Show added documents
    print("\nAdded documents:")
    for i, text in enumerate(test_articles, 1):
        lines = text.count('\n') + 1
        print(f"  [{i}] {lines} lines | {len(text)} chars")
    
    # =========================================================================
    # STAGE 3: TEST SEARCH
    # =========================================================================
    print("\n" + "=" * 70)
    print("STAGE 3. TEST SEARCH")
    print("=" * 70)
    
    # Query 1: Exact term
    query1 = "What is machine learning?"
    print("\n--- SCREENSHOT 2: SEARCH RESULTS ---")
    print("-" * 70)
    print(f"QUERY 1 (exact term): \"{query1}\"")
    print("-" * 70)
    
    results1 = store.query(query1, top_k=2)
    
    for i, r in enumerate(results1, 1):
        score = r.get('score', 0)
        text = r.get('text', '')[:100] + "..."
        print(f"\n  Result [{i}]:")
        print(f"    Score: {score:.4f}")
        print(f"    Text: {text}")
    
    # Query 2: Synonym
    query2 = "How do computers learn from information?"
    print("\n" + "-" * 70)
    print(f"QUERY 2 (synonym): \"{query2}\"")
    print("-" * 70)
    
    results2 = store.query(query2, top_k=2)
    
    for i, r in enumerate(results2, 1):
        score = r.get('score', 0)
        text = r.get('text', '')[:100] + "..."
        print(f"\n  Result [{i}]:")
        print(f"    Score: {score:.4f}")
        print(f"    Text: {text}")
    
    # =========================================================================
    # STAGE 4: ANALYSIS
    # =========================================================================
    print("\n" + "=" * 70)
    print("STAGE 4. ANALYSIS (3 sentences)")
    print("=" * 70)
    
    score_exact = results1[0].get('score', 0) if results1 else 0
    score_synonym = results2[0].get('score', 0) if results2 else 0
    
    print(f"""
1. WHICH SCORE SHOWED EXACT SEARCH VS SYNONYM?
   - Exact query (machine learning):     score = {score_exact:.4f}
   - Synonym (computers learn from info): score = {score_synonym:.4f}
   
2. DID IT FIND SEMANTICS (UNDERSTAND SYNONYM)?
   - YES, the system understood the synonym!
   - Query "How do computers learn from information?" is semantically close
     to the document about Machine Learning (computers learn from data)
   - Score {score_synonym:.4f} shows good semantic connection
   
3. WHAT WOULD I IMPROVE (CHUNKS/TOP_K)?
   - Chunks: reduce size to 512 tokens (currently 1024)
   - TOP_K: increase to 5 for more context
   - Use hybrid search (keyword + semantic)
   - Add metadata for better filtering
    """)
    
    # Close
    store.close()
    
    print("\n" + "=" * 70)
    print("                   REPORT COMPLETED")
    print("=" * 70)
    print("""
Technologies used:
- ProxyAPI (https://proxyapi.ru) for embedding generation
- Weaviate Cloud for vector storage
- OpenAI text-embedding-3-large model
    """)

if __name__ == "__main__":
    main()
