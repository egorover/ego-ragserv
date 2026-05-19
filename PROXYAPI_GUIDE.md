# ProxyAPI Integration Guide

## рџ“– РћРїРёСЃР°РЅРёРµ

ProxyAPI РїРѕР·РІРѕР»СЏРµС‚ РјР°СЂС€СЂСѓС‚РёР·РёСЂРѕРІР°С‚СЊ Р·Р°РїСЂРѕСЃС‹ Рє OpenAI С‡РµСЂРµР· РїСЂРѕРєСЃРё-СЃРµСЂРІРёСЃ. Р­С‚Рѕ РїРѕР»РµР·РЅРѕ РґР»СЏ:

- РћР±С…РѕРґР° РѕРіСЂР°РЅРёС‡РµРЅРёР№ РґРѕСЃС‚СѓРїР° Рє OpenAI
- Р¦РµРЅС‚СЂР°Р»РёР·РѕРІР°РЅРЅРѕРіРѕ СѓРїСЂР°РІР»РµРЅРёСЏ API РєР»СЋС‡Р°РјРё
- РњРѕРЅРёС‚РѕСЂРёРЅРіР° Рё Р°РЅР°Р»РёС‚РёРєРё Р·Р°РїСЂРѕСЃРѕРІ
- РљСЌС€РёСЂРѕРІР°РЅРёСЏ СЌРјР±РµРґРґРёРЅРіРѕРІ

## вљ™пёЏ РќР°СЃС‚СЂРѕР№РєР°

### 1. Р”РѕР±Р°РІСЊС‚Рµ РїРµСЂРµРјРµРЅРЅС‹Рµ РІ `.env`:

```env
# ProxyAPI Configuration
PROXYAPI_API_KEY=your_proxyapi_api_key_here
PROXYAPI_BASE_URL=https://api.proxyapi.example.com/v1
PROXYAPI_ENABLED=true
```

### 2. РџР°СЂР°РјРµС‚СЂС‹:

| РџР°СЂР°РјРµС‚СЂ | РћРїРёСЃР°РЅРёРµ | РћР±СЏР·Р°С‚РµР»СЊРЅС‹Р№ |
|----------|----------|--------------|
| `PROXYAPI_API_KEY` | API РєР»СЋС‡ ProxyAPI | Р”Р° (РµСЃР»Рё РІРєР»СЋС‡С‘РЅ) |
| `PROXYAPI_BASE_URL` | Р‘Р°Р·РѕРІС‹Р№ URL РїСЂРѕРєСЃРё-СЃРµСЂРІРёСЃР° | РќРµС‚ (РёСЃРїРѕР»СЊР·СѓРµС‚СЃСЏ РїРѕ СѓРјРѕР»С‡Р°РЅРёСЋ) |
| `PROXYAPI_ENABLED` | Р’РєР»СЋС‡РёС‚СЊ ProxyAPI (true/false) | РќРµС‚ (РїРѕ СѓРјРѕР»С‡Р°РЅРёСЋ: false) |

## рџљЂ РСЃРїРѕР»СЊР·РѕРІР°РЅРёРµ

### РђРІС‚РѕРјР°С‚РёС‡РµСЃРєРѕРµ РІРєР»СЋС‡РµРЅРёРµ (С‡РµСЂРµР· .env)

Р•СЃР»Рё `PROXYAPI_ENABLED=true` РІ `.env`, Embedder Р°РІС‚РѕРјР°С‚РёС‡РµСЃРєРё РёСЃРїРѕР»СЊР·СѓРµС‚ ProxyAPI:

```python
from embeddings.embedder import Embedder

embedder = Embedder()  # РђРІС‚РѕРјР°С‚РёС‡РµСЃРєРё РёСЃРїРѕР»СЊР·СѓРµС‚ ProxyAPI
```

### Р СѓС‡РЅРѕРµ РІРєР»СЋС‡РµРЅРёРµ

```python
from embeddings.embedder import Embedder

embedder = Embedder(use_proxyapi=True)
```

### РЇРІРЅР°СЏ РїРµСЂРµРґР°С‡Р° РїР°СЂР°РјРµС‚СЂРѕРІ

```python
from embeddings.embedder import Embedder

embedder = Embedder(
    api_key="your_proxyapi_key",
    base_url="https://api.proxyapi.example.com/v1"
)
```

## рџ”„ РџРµСЂРµРєР»СЋС‡РµРЅРёРµ РјРµР¶РґСѓ СЂРµР¶РёРјР°РјРё

```python
# РџСЂСЏРјРѕР№ РґРѕСЃС‚СѓРї Рє OpenAI
from embeddings.embedder import Embedder

# Р РµР¶РёРј 1: РџСЂСЏРјРѕР№ OpenAI
embedder_direct = Embedder(use_proxyapi=False)

# Р РµР¶РёРј 2: Р§РµСЂРµР· ProxyAPI
embedder_proxy = Embedder(use_proxyapi=True)

# Р РµР¶РёРј 3: РђРІС‚РѕРѕРїСЂРµРґРµР»РµРЅРёРµ РїРѕ .env
embedder_auto = Embedder()  # РСЃРїРѕР»СЊР·СѓРµС‚ PROXYAPI_ENABLED
```

## рџ“‹ РџСЂРѕРІРµСЂРєР° РєРѕРЅС„РёРіСѓСЂР°С†РёРё

```python
from config.settings import settings

print(f"ProxyAPI Enabled: {settings.PROXYAPI_ENABLED}")
print(f"ProxyAPI Base URL: {settings.PROXYAPI_BASE_URL}")
print(f"ProxyAPI API Key set: {bool(settings.PROXYAPI_API_KEY)}")
```

## вљ пёЏ Р’Р°Р¶РЅС‹Рµ Р·Р°РјРµС‡Р°РЅРёСЏ

1. **РџСЂРёРѕСЂРёС‚РµС‚ РЅР°СЃС‚СЂРѕРµРє**: Р•СЃР»Рё `PROXYAPI_ENABLED=true`, СЃРёСЃС‚РµРјР° РёРіРЅРѕСЂРёСЂСѓРµС‚ `OPENAI_API_KEY`
2. **Р‘РµР·РѕРїР°СЃРЅРѕСЃС‚СЊ**: РќРёРєРѕРіРґР° РЅРµ РєРѕРјРјРёС‚СЊС‚Рµ `.env` С„Р°Р№Р» СЃ СЂРµР°Р»СЊРЅС‹РјРё РєР»СЋС‡Р°РјРё
3. **РЎРѕРІРјРµСЃС‚РёРјРѕСЃС‚СЊ**: ProxyAPI РґРѕР»Р¶РµРЅ РїРѕРґРґРµСЂР¶РёРІР°С‚СЊ OpenAI API С„РѕСЂРјР°С‚

## рџ”§ РџСЂРёРјРµСЂС‹ РїСЂРѕРєСЃРё-СЃРµСЂРІРёСЃРѕРІ

- **Lmarena API**: `https://api.lmarena.io/v1`
- **Local OpenAI Proxy**: Р—Р°РїСѓСЃС‚РёС‚Рµ СЃРІРѕР№ РїСЂРѕРєСЃРё-СЃРµСЂРІРµСЂ
- **РљРѕСЂРїРѕСЂР°С‚РёРІРЅС‹Рµ РїСЂРѕРєСЃРё**: РЈС‚РѕС‡РЅРёС‚Рµ Сѓ РІР°С€РµРіРѕ IT-РѕС‚РґРµР»Р°

## рџђ› Troubleshooting

### РћС€РёР±РєР°: "ProxyAPI is enabled but PROXYAPI_API_KEY is not set"
**Р РµС€РµРЅРёРµ**: Р”РѕР±Р°РІСЊС‚Рµ `PROXYAPI_API_KEY` РІ `.env` РёР»Рё РѕС‚РєР»СЋС‡РёС‚Рµ ProxyAPI:
```env
PROXYAPI_ENABLED=false
```

### РћС€РёР±РєР° РїРѕРґРєР»СЋС‡РµРЅРёСЏ Рє ProxyAPI
**Р РµС€РµРЅРёРµ**: РџСЂРѕРІРµСЂСЊС‚Рµ:
1. РљРѕСЂСЂРµРєС‚РЅРѕСЃС‚СЊ `PROXYAPI_BASE_URL`
2. Р”РѕСЃС‚СѓРїРЅРѕСЃС‚СЊ СЌРЅРґРїРѕРёРЅС‚Р°
3. Р’Р°Р»РёРґРЅРѕСЃС‚СЊ API РєР»СЋС‡Р°

### Р­РјР±РµРґРґРёРЅРіРё РЅРµ РіРµРЅРµСЂРёСЂСѓСЋС‚СЃСЏ
**Р РµС€РµРЅРёРµ**: РџРѕРїСЂРѕР±СѓР№С‚Рµ РѕС‚РєР»СЋС‡РёС‚СЊ ProxyAPI:
```python
embedder = Embedder(use_proxyapi=False)
```

## рџ“љ Р”РѕРїРѕР»РЅРёС‚РµР»СЊРЅС‹Рµ СЂРµСЃСѓСЂСЃС‹

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [ProxyAPI Best Practices](https://example.com/proxy-best-practices)
