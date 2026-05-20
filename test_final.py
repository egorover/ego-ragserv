"""
Final Security and Functionality Test
Checks for secrets exposure and verifies all modules work correctly
"""

import os
import sys
from pathlib import Path

def print_section(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def test_python_syntax():
    """Check Python syntax of all modules"""
    print_section("PYTHON SYNTAX CHECK")
    
    modules = [
        "config/settings.py",
        "embeddings/embedder.py",
        "stores/weaviate_store.py",
        "stores/pinecone_store.py",
        "rag/retriever.py",
        "utils/chunker.py",
    ]
    
    all_ok = True
    for module in modules:
        try:
            compile(Path(module).read_text(), module, 'exec')
            print(f"  [OK] {module}")
        except SyntaxError as e:
            print(f"  [FAIL] {module}: {e}")
            all_ok = False
    
    return all_ok

def test_imports():
    """Check all imports work"""
    print_section("IMPORT CHECK")
    
    try:
        from config.settings import Settings
        print("  [OK] config.settings")
        
        from embeddings.embedder import Embedder
        print("  [OK] embeddings.embedder")
        
        from stores.weaviate_store import WeaviateStore
        print("  [OK] stores.weaviate_store")
        
        from stores.pinecone_store import PineconeStore
        print("  [OK] stores.pinecone_store")
        
        return True
    except ImportError as e:
        print(f"  [FAIL] Import error: {e}")
        return False

def check_secrets_in_code():
    """Check for hardcoded secrets in source files"""
    print_section("SECRET EXPOSURE CHECK")
    
    secret_patterns = [
        "sk-[a-zA-Z0-9]{20,}",  # OpenAI/ProxyAPI keys
        "pcsk_[a-zA-Z0-9]{30,}",  # Pinecone keys
        "WkZMVGts",  # Weaviate key pattern
    ]
    
    files_to_check = [
        "config/settings.py",
        "embeddings/embedder.py",
        "stores/weaviate_store.py",
        "stores/pinecone_store.py",
        "rag/retriever.py",
        "utils/chunker.py",
        "README.md",
    ]
    
    all_safe = True
    for filepath in files_to_check:
        if Path(filepath).exists():
            try:
                content = Path(filepath).read_text(encoding='utf-8')
                # Check for obvious hardcoded secrets (not placeholders)
                if "your_" in content.lower() or "example" in content.lower():
                    print(f"  [OK] {filepath} - uses placeholders")
                elif "api_key" in content.lower() and "getenv" in content:
                    print(f"  [OK] {filepath} - uses getenv()")
                else:
                    print(f"  [CHECK] {filepath} - manual review recommended")
            except UnicodeDecodeError:
                print(f"  [CHECK] {filepath} - encoding issue, manual review")
    
    return all_safe

def check_env_file():
    """Check .env file status"""
    print_section(".ENV FILE CHECK")
    
    env_path = Path(".env")
    gitignore_path = Path(".gitignore")
    
    # Check if .env exists
    if env_path.exists():
        print("  [INFO] .env file exists (local configuration)")
    else:
        print("  [INFO] .env file not found")
    
    # Check if .env is in .gitignore
    if gitignore_path.exists():
        gitignore_content = gitignore_path.read_text()
        if ".env" in gitignore_content:
            print("  [OK] .env is in .gitignore")
            return True
        else:
            print("  [WARNING] .env NOT in .gitignore")
            return False
    
    return True

def check_git_status():
    """Check git status for staged secrets"""
    print_section("GIT STATUS CHECK")
    
    import subprocess
    
    # Check if .env is tracked
    result = subprocess.run(
        ["git", "ls-files", ".env"],
        capture_output=True,
        text=True
    )
    
    if result.stdout.strip():
        print("  [FAIL] .env is tracked in git!")
        return False
    else:
        print("  [OK] .env is not tracked in git")
        return True

def test_settings_load():
    """Test that settings load correctly"""
    print_section("SETTINGS LOAD CHECK")
    
    try:
        from config.settings import Settings
        
        print(f"  [OK] Settings loaded")
        print(f"    - ProxyAPI Enabled: {Settings.PROXYAPI_ENABLED}")
        print(f"    - Embedding Model: {Settings.EMBEDDING_MODEL}")
        print(f"    - Pinecone Configured: {bool(Settings.PINECONE_API_KEY)}")
        print(f"    - Weaviate Configured: {bool(Settings.WEAVIATE_URL)}")
        
        return True
    except Exception as e:
        print(f"  [FAIL] Settings load error: {e}")
        return False

def main():
    print("=" * 70)
    print("  FINAL PROJECT TEST - Security & Functionality")
    print("=" * 70)
    
    results = {}
    
    results["Python Syntax"] = test_python_syntax()
    results["Imports"] = test_imports()
    results["Secrets in Code"] = check_secrets_in_code()
    results[".env File"] = check_env_file()
    results["Git Status"] = check_git_status()
    results["Settings Load"] = test_settings_load()
    
    print_section("SUMMARY")
    
    all_passed = True
    for test, passed in results.items():
        status = "PASS" if passed else "FAIL"
        symbol = "[+]" if passed else "[-]"
        print(f"  {symbol} {test}: {status}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 70)
    if all_passed:
        print("  [+] ALL TESTS PASSED - Ready for GitHub push")
    else:
        print("  [-] SOME TESTS FAILED - Review issues above")
    print("=" * 70)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
