# ego-ragserv

A production-ready, modular RAG (Retrieval-Augmented Generation) service featuring multi-provider vector database orchestration.
---
## 📌 О проекте (About)
**ego-ragserv** — это гибкий бэкенд-сервис для реализации архитектуры RAG. Главная особенность проекта — полная независимость от конкретного хранилища векторов. Благодаря абстракции уровня данных (Data Access Layer), сервис позволяет бесшовно переключаться между локальными, облачными и enterprise-платформами для работы с эмбеддингами.

> 🛠 **Credits**: Данный проект основан на базе репозитория/шаблона преподавателя `[Имя или Ник преподавателя]` — [ссылка на оригинальный репозиторий]. 
> Проект был структурно переработан, расширен поддержкой новых провайдеров и адаптирован для личного портфолио.

## 🚀 Ключевые возможности (Features)
* **Multi-Provider Vector Support**: Интеграция с тремя ведущими решениями на рынке:
  * **Weaviate** — для быстрых локальных (Docker) или облачных векторных вычислений.
  * **Pinecone** — для полностью управляемого облачного production-scale поиска.
  * **Relevance AI** — для интеграции с Low-Code/No-Code AI-платформами и агентными воркфлоу.
* **Pluggable Architecture**: Переключение между базами данных происходит «на лету» изменением одной переменной в конфигурации, без изменения бизнес-логики приложения.
* **REST API**: Эндпоинты для загрузки/индексации документов, генерации эмбеддингов и выполнения семантического поиска.

## 🛠 Стек технологий (Tech Stack)
* **Язык**: Python / TypeScript `[оставьте нужное]`
* **Инфраструктура**: FastAPI / Express `[оставьте нужное]`
* **Векторные клиенты**: `weaviate-client`, `pinecone-client`, `relevanceai` SDK
* =================================================================
* =================================================================

# RAG Vector Store Demo 🚀

Полноценный Python-проект, демонстрирующий работу RAG (Retrieval-Augmented Generation) стека с тремя векторными хранилищами: **Relevance AI**, **Weaviate**, и **Pinecone**.

## 📋 Описание проекта

Этот проект предоставляет унифицированный интерфейс для работы с различными векторными базами данных в контексте RAG-системы. Вы можете:

- Генерировать эмбеддинги с помощью OpenAI's `text-embedding-3-large`
- Хранить и индексировать документы в трёх разных векторных хранилищах
- Выполнять семантический поиск по документам
- Сравнивать результаты поиска между разными хранилищами
- Легко переключаться между векторными базами данных

## 🏗️ Структура проекта

```
rag-vector-demo/
├── README.md                    # Документация проекта
├── requirements.txt             # Зависимости Python
├── config/
│   └── settings.py              # Конфигурация и переменные окружения
├── embeddings/
│   └── embedder.py              # Генерация эмбеддингов через OpenAI
├── stores/
│   ├── relevance_store.py       # Интеграция с Relevance AI
│   ├── weaviate_store.py        # Интеграция с Weaviate
│   └── pinecone_store.py        # Интеграция с Pinecone
├── rag/
│   └── retriever.py             # Унифицированный RAG retriever
├── examples/
│   └── demo_usage.py            # Демонстрация использования
└── utils/
    ├── logger.py                # Настройка логирования (loguru)
    └── chunker.py               # Разбиение текста на чанки
```

## 🔧 Установка

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd rag-vector-demo
```

### 2. Создание виртуального окружения

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

## ⚙️ Конфигурация

> **📖 Подробные инструкции**: 
> - **[SETUP_GUIDE_RU.md](SETUP_GUIDE_RU.md)** - Полная пошаговая инструкция по настройке всех сервисов
> - **[QUICK_SETUP_CHEATSHEET.md](QUICK_SETUP_CHEATSHEET.md)** - Быстрая шпаргалка со всеми ссылками

### Создание файла .env

Создайте файл `.env` в корневой директории проекта со следующими переменными:

```env
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Pinecone Configuration
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=your_pinecone_environment_here
PINECONE_INDEX_NAME=rag-demo-index

# Weaviate Configuration
WEAVIATE_URL=http://localhost:8080
WEAVIATE_API_KEY=your_weaviate_api_key_here

# Relevance AI Configuration
RELEVANCE_PROJECT=your_relevance_project_id_here
RELEVANCE_API_KEY=your_relevance_api_key_here
RELEVANCE_DATASET_ID=rag-demo-dataset

# ProxyAPI Configuration (Optional)
# Enable to route OpenAI requests through ProxyAPI
PROXYAPI_API_KEY=your_proxyapi_api_key_here
PROXYAPI_BASE_URL=https://api.proxyapi.example.com/v1
PROXYAPI_ENABLED=false

# Embedding Configuration
EMBEDDING_MODEL=text-embedding-3-large
EMBEDDING_DIMENSION=3072
```

### Получение API ключей

> **⚡ Быстрая настройка**: См. [QUICK_SETUP_CHEATSHEET.md](QUICK_SETUP_CHEATSHEET.md) для всех ссылок

#### OpenAI
1. Зарегистрируйтесь на [platform.openai.com](https://platform.openai.com)
2. Перейдите в раздел API Keys
3. Создайте новый API ключ

#### Pinecone
1. Зарегистрируйтесь на [pinecone.io](https://app.pinecone.io/)
2. Создайте проект
3. Скопируйте API ключ и environment из дашборда

#### Weaviate (бесплатно через облако)
**Вариант 1: Weaviate Cloud (Рекомендуется)**
1. Зарегистрируйтесь на [console.weaviate.cloud](https://console.weaviate.cloud)
2. Создайте кластер (выберите "Free Sandbox")
3. Скопируйте Cluster URL (https://your-cluster.weaviate.network)
4. Создайте API Key во вкладке "API Keys"

**Вариант 2: Локальный Weaviate**
```bash
docker run -d -p 8080:8080 semitechnologies/weaviate:latest
```
URL: `http://localhost:8080`, API key оставить пустым

**Подробная инструкция**: См. [SETUP_GUIDE_RU.md](SETUP_GUIDE_RU.md#2-weaviate-бесплатно-через-облако)

#### Relevance AI
1. Зарегистрируйтесь на [relevance.ai](https://relevance.ai) → "Get Started Free"
2. Войдите в [cloud.relevance.ai](https://cloud.relevance.ai/)
3. Скопируйте Project ID из URL браузера или Settings
4. Создайте API Key: Settings → API Keys → Create New

**Подробная инструкция**: См. [SETUP_GUIDE_RU.md](SETUP_GUIDE_RU.md#3-relevance-ai)

#### ProxyAPI (Опционально)
ProxyAPI позволяет маршрутизировать запросы к OpenAI через прокси-сервис.

1. Получите API ключ у вашего провайдера ProxyAPI
2. Укажите `PROXYAPI_BASE_URL` (эндпоинт прокси-сервиса)
3. Установите `PROXYAPI_ENABLED=true`

**Применение**: Полезна для:
- Обхода ограничений доступа к OpenAI
- Централизованного управления API ключами
- Мониторинга и аналитики запросов
- Кэширования эмбеддингов

## 🚀 Запуск

### Запуск демонстрации

```bash
python examples/demo_usage.py
```

Этот скрипт выполнит:
1. Инициализацию всех трёх векторных хранилищ
2. Добавление тестовых документов в каждое хранилище
3. Выполнение тестовых запросов
4. Сравнение результатов между хранилищами
5. Демонстрацию чанкинга текста

### Пример использования в коде

```python
from embeddings.embedder import Embedder
from rag.retriever import Retriever

# Инициализация
embedder = Embedder()
retriever = Retriever(embedder)

# Добавление документов
documents = [
    "Machine learning is a subset of AI...",
    "Deep learning uses neural networks..."
]

retriever.add_documents(
    texts=documents,
    store_type="pinecone"  # или "weaviate", "relevance"
)

# Поиск
results = retriever.retrieve(
    query="What is machine learning?",
    store_type="pinecone",
    top_k=5
)

# Сравнение всех хранилищ
retriever.compare_stores(
    query="What is machine learning?",
    top_k=3
)
```

## 📚 Использование отдельных компонентов

### Embedder

```python
from embeddings.embedder import Embedder

# Стандартное использование (прямой доступ к OpenAI)
embedder = Embedder()

# Использование с ProxyAPI
embedder = Embedder(use_proxyapi=True)

# Или с явными параметрами
embedder = Embedder(
    api_key="your_api_key",
    base_url="https://api.proxyapi.example.com/v1"
)

# Одиночный текст
embedding = embedder.embed_text("Hello world")
```

### Text Chunker

```python
from utils.chunker import TextChunker

chunker = TextChunker(chunk_size=512, chunk_overlap=50)

# Разбиение текста
chunks = chunker.chunk_text(long_text)

# Разбиение с метаданными
chunked_docs = chunker.chunk_documents([doc1, doc2, doc3])
```

### Отдельные векторные хранилища

#### Pinecone

```python
from stores.pinecone_store import PineconeStore

store = PineconeStore()
store.create_index()
store.add_texts(["text1", "text2"])
results = store.query("query text", top_k=5)
```

#### Weaviate

```python
from stores.weaviate_store import WeaviateStore

store = WeaviateStore()
store.create_schema()
store.add_texts(["text1", "text2"])
results = store.query("query text", top_k=5)
store.close()  # Важно закрыть соединение
```

#### Relevance AI

```python
from stores.relevance_store import RelevanceStore

store = RelevanceStore()
store.create_collection()
store.add_texts(["text1", "text2"])
results = store.query("query text", top_k=5)
```

## 🔍 Особенности реализации

### Качество кода
- ✅ PEP8 совместимость
- ✅ Полная типизация (Python 3.10+)
- ✅ Подробные docstrings
- ✅ Обработка ошибок
- ✅ Логирование с помощью loguru

### Архитектура
- 🏗️ Модульная структура
- 🔄 Единый интерфейс для всех хранилищ
- 🎯 Легкое переключение между хранилищами
- 📦 Переиспользуемые компоненты

### Функциональность
- 🧮 Генерация эмбеддингов через OpenAI
- 💾 Поддержка трёх векторных БД
- 🔎 Семантический поиск
- 📊 Сравнение результатов
- ✂️ Чанкинг текста с учётом токенов

## 📝 Логирование

Проект использует `loguru` для логирования:
- Логи выводятся в консоль с цветовым форматированием
- Ошибки записываются в файлы `logs/rag_demo_YYYY-MM-DD.log`
- Автоматическая ротация и сжатие логов

## 🐛 Troubleshooting

### Ошибка: "OpenAI API key is required"
Убедитесь, что в `.env` файле указан валидный `OPENAI_API_KEY`.

### Ошибка подключения к Weaviate
Если используете локальный Weaviate, убедитесь что Docker контейнер запущен:
```bash
docker ps | grep weaviate
```

### Ошибка при создании Pinecone индекса
Проверьте правильность `PINECONE_ENVIRONMENT` и наличие квоты в вашем аккаунте.

### Import ошибки
Убедитесь, что все зависимости установлены:
```bash
pip install -r requirements.txt --upgrade
```

## 🔄 Обновление зависимостей

```bash
pip install --upgrade openai pinecone-client weaviate-client relevanceai
```

## 📄 Лицензия

MIT License - используйте свободно в своих проектах.

## 🤝 Вклад

Contributions приветствуются! Пожалуйста:
1. Форкните репозиторий
2. Создайте feature branch
3. Сделайте коммит изменений
4. Отправьте pull request

## 📧 Контакты

Если у вас есть вопросы или предложения, создайте issue в репозитории.

---

**Создано с ❤️ для демонстрации RAG систем с векторными базами данных**

