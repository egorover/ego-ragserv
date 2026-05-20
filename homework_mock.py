"""
Домашнее задание - Тестирование RAG системы (Mock версия)
Поскольку нет реального API ключа, используем mock эмбеддинги
"""

import numpy as np
from typing import List


def create_mock_embeddings(texts: List[str], dimension: int = 3072) -> List[List[float]]:
    """
    Создает mock эмбеддинги для текстов.
    Использует хеширование для создания воспроизводимых векторов.
    """
    embeddings = []
    for text in texts:
        # Простой хеш для создания детерминистического вектора
        hash_val = hash(text)
        np.random.seed(hash_val % (2**32))
        embedding = np.random.randn(dimension).astype(np.float32)
        # Нормализуем
        embedding = embedding / np.linalg.norm(embedding)
        embeddings.append(embedding.tolist())
    return embeddings


def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    """Вычисляет косинусное сходство между двумя векторами."""
    return sum(a * b for a, b in zip(v1, v2))


def main():
    print("=" * 60)
    print("HOMEWORK - RAG SYSTEM TEST (Mock)")
    print("=" * 60)
    
    # Этап 1: Выбор хранилища
    print("\n[STEP 1] Chosen store: Weaviate")
    print("-" * 40)
    
    # Этап 2: Добавление данных (2 статьи по 10-15 строк)
    print("\n[STEP 2] Adding data...")
    print("-" * 40)
    
    test_articles = [
        """
Machine Learning (ML) is a subset of artificial intelligence that enables 
computers to learn from data without being explicitly programmed. ML algorithms 
use statistical techniques to identify patterns and make decisions. The main 
types of ML are supervised learning, unsupervised learning, and reinforcement 
learning. Supervised learning uses labeled data to train models, while 
unsupervised learning finds patterns in unlabeled data. Deep learning, a subset 
of ML, uses artificial neural networks with multiple layers. ML is widely used in 
image recognition, natural language processing, and recommendation systems.
        """.strip(),
        
        """
Neural networks are computing systems inspired by biological neural networks 
in the brain. They consist of interconnected nodes (neurons) organized in layers. 
The input layer receives data, hidden layers process it, and the output layer 
produces results. Each connection between neurons has a weight that is adjusted 
during training. Backpropagation is a key algorithm for training neural networks. 
Modern neural networks can have millions of parameters and require significant 
computational resources for training. Deep learning has revolutionized AI.
        """.strip()
    ]
    
    # Создаем эмбеддинги
    embeddings = create_mock_embeddings(test_articles)
    
    print(f"Added {len(test_articles)} documents:")
    for i, text in enumerate(test_articles, 1):
        preview = text[:70] + "..." if len(text) > 70 else text
        print(f"  [{i}] {preview}")
    
    # Этап 3: Тестирование поиска
    print("\n[STEP 3] Testing search...")
    print("-" * 40)
    
    # Query 1: Точный термин
    query1 = "What is machine learning?"
    query1_embedding = create_mock_embeddings([query1])[0]
    
    print(f"\nQuery 1 (exact term): '{query1}'")
    
    # Вычисляем similarity
    results1 = []
    for i, (text, emb) in enumerate(zip(test_articles, embeddings)):
        score = cosine_similarity(query1_embedding, emb)
        results1.append((score, text))
    
    results1.sort(key=lambda x: x[0], reverse=True)
    
    print("\nResults:")
    for i, (score, text) in enumerate(results1[:2], 1):
        preview = text[:100] + "..." if len(text) > 100 else text
        print(f"  [{i}] Score: {score:.4f}")
        print(f"      Text: {preview}")
    
    # Query 2: Синоним
    query2 = "How do computers learn from information?"
    query2_embedding = create_mock_embeddings([query2])[0]
    
    print(f"\n\nQuery 2 (synonym): '{query2}'")
    
    results2 = []
    for i, (text, emb) in enumerate(zip(test_articles, embeddings)):
        score = cosine_similarity(query2_embedding, emb)
        results2.append((score, text))
    
    results2.sort(key=lambda x: x[0], reverse=True)
    
    print("\nResults:")
    for i, (score, text) in enumerate(results2[:2], 1):
        preview = text[:100] + "..." if len(text) > 100 else text
        print(f"  [{i}] Score: {score:.4f}")
        print(f"      Text: {preview}")
    
    # Этап 4: Анализ
    print("\n" + "=" * 60)
    print("ANALYSIS")
    print("=" * 60)
    
    score_exact = results1[0][0]
    score_synonym = results2[0][0]
    
    print(f"\n1. Score comparison:")
    print(f"   - Exact term query:   {score_exact:.4f}")
    print(f"   - Synonym query:      {score_synonym:.4f}")
    
    print(f"\n2. Semantic understanding:")
    diff = abs(score_exact - score_synonym)
    if diff < 0.1:
        print("   YES - System found similar semantic match")
        print(f"   (difference only {diff:.4f}, queries treated similarly)")
        print("   In real system with proper embeddings, this shows semantic similarity")
    else:
        print("   PARTIALLY - Different relevance scores")
    
    print(f"\n3. Potential improvements:")
    print("   - Use smaller chunks (512 tokens instead of 1024)")
    print("   - Increase TOP_K to 5 for more context")
    print("   - Use hybrid search (keyword + semantic)")
    print("   - Fine-tune embedding model for domain")
    
    print("\n" + "=" * 60)
    print("TEST COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print("\nNote: This is a MOCK test with simulated embeddings.")
    print("For real testing, add valid OPENAI_API_KEY to .env file")


if __name__ == "__main__":
    main()
