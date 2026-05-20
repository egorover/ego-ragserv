"""
Домашнее задание - Тестирование RAG системы
Этап 1: Выбрано хранилище - Weaviate
Этап 2: Добавление данных
Этап 3: Тестирование поиска
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from embeddings.embedder import Embedder
from stores.weaviate_store import WeaviateStore


def main():
    print("=" * 60)
    print("HOMEWORK - RAG SYSTEM TEST")
    print("=" * 60)
    
    # Test data - 2 articles (10-15 lines each)
    test_articles = [
        """
Machine Learning (ML) is a subset of artificial intelligence that enables 
computers to learn from data without being explicitly programmed. ML algorithms 
use statistical techniques to identify patterns and make decisions. The main 
types of ML are supervised learning, unsupervised learning, and reinforcement 
learning. Supervised learning uses labeled data to train models, while 
unsupervised learning finds patterns in unlabeled data. Deep learning, a subset 
of ML, uses artificial neural networks with multiple layers.
        """.strip(),
        
        """
Neural networks are computing systems inspired by biological neural networks 
in the brain. They consist of interconnected nodes (neurons) organized in layers. 
The input layer receives data, hidden layers process it, and the output layer 
produces results. Each connection between neurons has a weight that is adjusted 
during training. Backpropagation is a key algorithm for training neural networks. 
Modern neural networks can have millions of parameters and require significant 
computational resources for training.
        """.strip()
    ]
    
    print("\n[STEP 1] Chosen store: Weaviate")
    print("-" * 40)
    
    # Initialize embedder and store
    print("\n[STEP 2] Adding data to Weaviate...")
    print("-" * 40)
    
    try:
        embedder = Embedder()
        store = WeaviateStore(embedder=embedder)
        
        # Add documents
        print(f"Adding {len(test_articles)} articles...")
        store.add_texts(test_articles)
        print(f"Successfully added {len(test_articles)} documents to Weaviate")
        
        # Show added documents
        print("\nAdded documents:")
        for i, text in enumerate(test_articles, 1):
            preview = text[:80] + "..." if len(text) > 80 else text
            print(f"  [{i}] {preview}")
        
        print("\n[STEP 3] Testing search...")
        print("-" * 40)
        
        # Query 1: Exact term
        query1 = "What is machine learning?"
        print(f"\nQuery 1 (exact term): {query1}")
        results1 = store.query(query1, top_k=2)
        
        print("\nResults:")
        for i, r in enumerate(results1, 1):
            score = r.get('score', 0)
            text = r.get('text', '')[:150]
            print(f"  [{i}] Score: {score:.4f}")
            print(f"      Text: {text}...")
        
        # Query 2: Synonym
        query2 = "How do computers learn from information?"
        print(f"\n\nQuery 2 (synonym): {query2}")
        results2 = store.query(query2, top_k=2)
        
        print("\nResults:")
        for i, r in enumerate(results2, 1):
            score = r.get('score', 0)
            text = r.get('text', '')[:150]
            print(f"  [{i}] Score: {score:.4f}")
            print(f"      Text: {text}...")
        
        # Analysis
        print("\n" + "=" * 60)
        print("ANALYSIS")
        print("=" * 60)
        
        score1 = results1[0].get('score', 0) if results1 else 0
        score2 = results2[0].get('score', 0) if results2 else 0
        
        print(f"\n1. Score comparison:")
        print(f"   - Exact term query: {score1:.4f}")
        print(f"   - Synonym query:    {score2:.4f}")
        
        print(f"\n2. Semantic understanding:")
        if score2 > 0.5:
            print("   YES - The system found semantic similarity")
            print(f"   (score {score2:.4f} indicates the synonym was recognized)")
        else:
            print("   PARTIALLY - The system found some similarity")
        
        print(f"\n3. Potential improvements:")
        print("   - Use smaller chunks (512 tokens instead of 1024)")
        print("   - Increase TOP_K to 5 for more context")
        print("   - Use hybrid search (keyword + semantic)")
        
        store.close()
        print("\n" + "=" * 60)
        print("TEST COMPLETED SUCCESSFULLY")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
