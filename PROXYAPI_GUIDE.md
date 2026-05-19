# ProxyAPI Integration Guide

## 📖 Описание

ProxyAPI позволяет маршрутизировать запросы к OpenAI через прокси-сервис. Это полезно для:

- Обхода ограничений доступа к OpenAI
- Централизованного управления API ключами
- Мониторинга и аналитики запросов
- Кэширования эмбеддингов

## ⚙️ Настройка

### 1. Добавьте переменные в `.env`:

```env
# ProxyAPI Configuration
PROXYAPI_API_KEY=your_proxyapi_api_key_here
PROXYAPI_BASE_URL=https://api.proxyapi.example.com/v1
PROXYAPI_ENABLED=true
```

### 2. Параметры:

| Параметр | Описание | Обязательный |
|----------|----------|--------------|
| `PROXYAPI_API_KEY` | API ключ ProxyAPI | Да (если включён) |
| `PROXYAPI_BASE_URL` | Базовый URL прокси-сервиса | Нет (используется по умолчанию) |
| `PROXYAPI_ENABLED` | Включить ProxyAPI (true/false) | Нет (по умолчанию: false) |

## 🚀 Использование

### Автоматическое включение (через .env)

Если `PROXYAPI_ENABLED=true` в `.env`, Embedder автоматически использует ProxyAPI:

```python
from embeddings.embedder import Embedder

embedder = Embedder()  # Автоматически использует ProxyAPI
```

### Ручное включение

```python
from embeddings.embedder import Embedder

embedder = Embedder(use_proxyapi=True)
```

### Явная передача параметров

```python
from embeddings.embedder import Embedder

embedder = Embedder(
    api_key="your_proxyapi_key",
    base_url="https://api.proxyapi.example.com/v1"
)
```

## 🔌 Переключение между режимами

```python
# Прямой доступ к OpenAI
from embeddings.embedder import Embedder

# Режим 1: Прямой OpenAI
embedder_direct = Embedder(use_proxyapi=False)

# Режим 2: Через ProxyAPI
embedder_proxy = Embedder(use_proxyapi=True)

# Режим 3: Автоопределение по .env
embedder_auto = Embedder()  # Использует PROXYAPI_ENABLED
```

## 📋 Проверка конфигурации

```python
from config.settings import settings

print(f"ProxyAPI Enabled: {settings.PROXYAPI_ENABLED}")
print(f"ProxyAPI Base URL: {settings.PROXYAPI_BASE_URL}")
print(f"ProxyAPI API Key set: {bool(settings.PROXYAPI_API_KEY)}")
```

## ⚠️ Важные замечания

1. **Приоритет настроек**: Если `PROXYAPI_ENABLED=true`, система игнорирует `OPENAI_API_KEY`
2. **Безопасность**: Никогда не коммитьте `.env` файл с реальными ключами
3. **Совместимость**: ProxyAPI должен поддерживать OpenAI API формат

## 🔧 Примеры прокси-сервисов

- **Lmarena API**: `https://api.lmarena.io/v1`
- **Local OpenAI Proxy**: Запустите свой прокси-сервер
- **Корпоративные прокси**: Уточните у вашего IT-отдела

## 🐛 Troubleshooting

### Ошибка: "ProxyAPI is enabled but PROXYAPI_API_KEY is not set"
**Решение**: Добавьте `PROXYAPI_API_KEY` в `.env` или отключите ProxyAPI:
```env
PROXYAPI_ENABLED=false
```

### Ошибка подключения к ProxyAPI
**Решение**: Проверьте:
1. Корректность `PROXYAPI_BASE_URL`
2. Доступность эндпоинта
3. Валидность API ключа

### Эмбеддинги не генерируются
**Решение**: Попробуйте отключить ProxyAPI:
```python
embedder = Embedder(use_proxyapi=False)
```

## 📚 Дополнительные ресурсы

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [ProxyAPI Best Practices](https://example.com/proxy-best-practices)