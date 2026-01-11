"""
Test script to verify the Excel Data Chatbot setup
Run this before starting the main app to ensure everything is configured correctly
"""

import sys

def test_imports():
    """Test if all required libraries can be imported"""
    print("Testing imports...")
    try:
        import streamlit as st
        print("✓ Streamlit")
    except ImportError as e:
        print(f"✗ Streamlit: {e}")
        return False
    
    try:
        import pandas as pd
        print("✓ Pandas")
    except ImportError as e:
        print(f"✗ Pandas: {e}")
        return False
    
    try:
        import plotly
        print("✓ Plotly")
    except ImportError as e:
        print(f"✗ Plotly: {e}")
        return False
    
    try:
        import langchain
        print("✓ LangChain")
    except ImportError as e:
        print(f"✗ LangChain: {e}")
        return False
    
    try:
        import openai
        print("✓ OpenAI")
    except ImportError as e:
        print(f"✗ OpenAI: {e}")
        return False
    
    return True


def test_data_loading():
    """Test if the Excel file can be loaded"""
    print("\nTesting data loading...")
    try:
        import pandas as pd
        import os
        
        # Check for default data file
        default_path = '/mnt/user-data/uploads/بيانات.xlsx'
        if os.path.exists(default_path):
            df = pd.read_excel(default_path)
            print(f"✓ Successfully loaded data: {len(df)} rows, {len(df.columns)} columns")
            print(f"  Columns: {', '.join(df.columns.tolist()[:5])}...")
            return True
        else:
            print("⚠ Default data file not found. You'll need to upload an Excel file in the app.")
            return True  # Not a critical error
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return False


def test_api_key():
    """Test if OpenAI API key is configured"""
    print("\nTesting API key configuration...")
    import os
    
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print(f"✓ API key found (length: {len(api_key)})")
        if api_key.startswith("sk-"):
            print("✓ API key format looks correct")
        else:
            print("⚠ API key doesn't start with 'sk-' - please verify it's correct")
        return True
    else:
        print("⚠ No API key found in environment variables")
        print("  You can either:")
        print("  1. Set OPENAI_API_KEY environment variable")
        print("  2. Enter it in the app sidebar when you run it")
        return True  # Not a critical error for this test


def test_arabic_support():
    """Test if Arabic text can be displayed"""
    print("\nTesting Arabic support...")
    try:
        arabic_text = "مرحبا بك في تطبيق تحليل البيانات"
        print(f"  Arabic test: {arabic_text}")
        print("✓ Arabic text can be displayed")
        return True
    except Exception as e:
        print(f"✗ Error with Arabic text: {e}")
        print("  Your terminal may not support Arabic, but the web app should work fine")
        return True  # Not critical


def main():
    print("=" * 60)
    print("Excel Data Chatbot - Setup Verification")
    print("=" * 60)
    print()
    
    tests = [
        ("Imports", test_imports),
        ("Data Loading", test_data_loading),
        ("API Key", test_api_key),
        ("Arabic Support", test_arabic_support)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"✗ {test_name} failed with exception: {e}")
            results.append((test_name, False))
        print()
    
    print("=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    all_passed = True
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    print()
    if all_passed:
        print("🎉 All tests passed! You're ready to run the app.")
        print("\nTo start the application, run:")
        print("  streamlit run app.py")
    else:
        print("⚠️  Some tests failed. Please fix the issues above before running the app.")
        print("\nTo install missing dependencies, run:")
        print("  pip install -r requirements.txt")
    
    print()
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
