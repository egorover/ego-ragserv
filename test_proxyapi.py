"""
Test script for ProxyAPI integration.
Tests configuration loading and Embedder initialization with ProxyAPI.
"""

import os
import sys
import subprocess


def run_test_in_process(test_code):
    """Run test code in a separate Python process to avoid caching issues."""
    result = subprocess.run(
        [sys.executable, "-c", test_code],
        capture_output=True,
        text=True
    )
    return result.returncode == 0, result.stdout, result.stderr


def test_settings_proxyapi():
    """Test that ProxyAPI settings are correctly loaded."""
    print("=" * 60)
    print("Test 1: ProxyAPI Settings Loading")
    print("=" * 60)
    
    test_code = '''
from config.settings import Settings

# Test default values
assert Settings.PROXYAPI_ENABLED == False, "PROXYAPI_ENABLED should be False by default"
assert Settings.PROXYAPI_API_KEY == "", "PROXYAPI_API_KEY should be empty by default"
assert Settings.PROXYAPI_BASE_URL == "", "PROXYAPI_BASE_URL should be empty by default"

print("All ProxyAPI settings are correct!")
'''
    
    success, stdout, stderr = run_test_in_process(test_code)
    
    if success:
        print("[PASS] Default ProxyAPI settings are correct")
        print()
        return True
    else:
        print(f"[FAIL] {stderr}")
        return False
    

def test_settings_proxyapi_enabled():
    """Test ProxyAPI settings when enabled."""
    print("=" * 60)
    print("Test 2: ProxyAPI Settings with Environment Variables")
    print("=" * 60)
    
    test_code = '''
import os
os.environ["PROXYAPI_ENABLED"] = "true"
os.environ["PROXYAPI_API_KEY"] = "test_api_key_12345"
os.environ["PROXYAPI_BASE_URL"] = "https://api.test-proxy.com/v1"

from config.settings import Settings

assert Settings.PROXYAPI_ENABLED == True, "PROXYAPI_ENABLED should be True"
assert Settings.PROXYAPI_API_KEY == "test_api_key_12345", "PROXYAPI_API_KEY should be set"
assert Settings.PROXYAPI_BASE_URL == "https://api.test-proxy.com/v1", "PROXYAPI_BASE_URL should be set"

print("ProxyAPI settings loaded correctly!")
'''
    
    success, stdout, stderr = run_test_in_process(test_code)
    
    if success:
        print("[PASS] ProxyAPI settings loaded correctly from environment")
        print()
        return True
    else:
        print(f"[FAIL] {stderr}")
        return False
    

def test_embedder_initialization():
    """Test Embedder initialization without API (syntax check only)."""
    print("=" * 60)
    print("Test 3: Embedder Initialization (Syntax Check)")
    print("=" * 60)
    
    import ast
    
    with open('embeddings/embedder.py', 'r', encoding='utf-8') as f:
        source = f.read()
    
    tree = ast.parse(source)
    
    # Find the Embedder class and __init__ method
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == 'Embedder':
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == '__init__':
                    params = [arg.arg for arg in item.args.args]
                    
                    expected_params = ['self', 'model', 'api_key', 'base_url', 'use_proxyapi']
                    for param in expected_params:
                        assert param in params, f"Parameter '{param}' should be in Embedder.__init__"
                    
                    print("[PASS] Embedder has correct parameters:")
                    for param in expected_params:
                        print(f"  - {param}")
                    print()
                    return True
    
    print("[FAIL] Could not find Embedder.__init__ method")
    return False


def test_embedder_proxyapi_mode():
    """Test Embedder with ProxyAPI mode (mock test)."""
    print("=" * 60)
    print("Test 4: Embedder ProxyAPI Mode Configuration")
    print("=" * 60)
    
    test_code = '''
import os
os.environ["PROXYAPI_ENABLED"] = "true"
os.environ["PROXYAPI_API_KEY"] = "proxy_test_key"
os.environ["PROXYAPI_BASE_URL"] = "https://proxy.example.com/v1"

from unittest.mock import MagicMock, patch

with patch.dict("sys.modules", {
    "loguru": MagicMock(),
    "openai": MagicMock(),
}):
    from embeddings.embedder import Embedder
    
    embedder = Embedder(use_proxyapi=True)
    
    assert embedder.api_key == "proxy_test_key", f"Expected proxy_test_key, got {embedder.api_key}"
    assert embedder.base_url == "https://proxy.example.com/v1", f"Expected proxy URL, got {embedder.base_url}"
    
    print(f"API Key: {embedder.api_key}")
    print(f"Base URL: {embedder.base_url}")
    print("ProxyAPI mode configured correctly!")
'''
    
    success, stdout, stderr = run_test_in_process(test_code)
    
    if success:
        print("[PASS] Embedder correctly configured for ProxyAPI mode")
        print(stdout.strip())
        print()
        return True
    else:
        print(f"[FAIL] {stderr}")
        return False
    

def test_embedder_direct_mode():
    """Test Embedder with direct OpenAI mode."""
    print("=" * 60)
    print("Test 5: Embedder Direct OpenAI Mode")
    print("=" * 60)
    
    test_code = '''
import os
os.environ["PROXYAPI_ENABLED"] = "false"
os.environ["OPENAI_API_KEY"] = "openai_test_key"

from unittest.mock import MagicMock, patch

with patch.dict("sys.modules", {
    "loguru": MagicMock(),
    "openai": MagicMock(),
}):
    from embeddings.embedder import Embedder
    
    embedder = Embedder(use_proxyapi=False)
    
    assert embedder.api_key == "openai_test_key", f"Expected openai_test_key, got {embedder.api_key}"
    assert embedder.base_url is None, f"Expected None base_url, got {embedder.base_url}"
    
    print(f"API Key: {embedder.api_key}")
    print("Direct OpenAI mode configured correctly!")
'''
    
    success, stdout, stderr = run_test_in_process(test_code)
    
    if success:
        print("[PASS] Embedder correctly configured for direct OpenAI mode")
        print(stdout.strip())
        print()
        return True
    else:
        print(f"[FAIL] {stderr}")
        return False
    

def test_embedder_auto_mode():
    """Test Embedder auto-detection based on settings."""
    print("=" * 60)
    print("Test 6: Embedder Auto-Mode (Based on Settings)")
    print("=" * 60)
    
    test_code = '''
import os
os.environ["PROXYAPI_ENABLED"] = "true"
os.environ["PROXYAPI_API_KEY"] = "auto_proxy_key"
os.environ["PROXYAPI_BASE_URL"] = "https://auto.proxy.com/v1"

from unittest.mock import MagicMock, patch

with patch.dict("sys.modules", {
    "loguru": MagicMock(),
    "openai": MagicMock(),
}):
    from embeddings.embedder import Embedder
    
    # use_proxyapi=None should auto-detect from settings
    embedder = Embedder(use_proxyapi=None)
    
    assert embedder.api_key == "auto_proxy_key", f"Expected auto_proxy_key, got {embedder.api_key}"
    assert embedder.base_url == "https://auto.proxy.com/v1", f"Expected auto proxy URL, got {embedder.base_url}"
    
    print("Auto-detection works correctly!")
'''
    
    success, stdout, stderr = run_test_in_process(test_code)
    
    if success:
        print("[PASS] Embedder auto-detects ProxyAPI when enabled in settings")
        print(stdout.strip())
        print()
        return True
    else:
        print(f"[FAIL] {stderr}")
        return False
    

def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print(" ProxyAPI Integration Tests")
    print("=" * 60 + "\n")
    
    tests = [
        test_settings_proxyapi,
        test_settings_proxyapi_enabled,
        test_embedder_initialization,
        test_embedder_proxyapi_mode,
        test_embedder_direct_mode,
        test_embedder_auto_mode,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            failed += 1
            print(f"[FAIL] {test.__name__}: {e}")
            print()
    
    print("=" * 60)
    print(f" Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
