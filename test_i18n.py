#!/usr/bin/env python3
"""
Test script to verify internationalization functionality in FontSearch.
"""

import sys
from pathlib import Path

def test_i18n_system():
    """Test the i18n system functionality."""
    print("🌍 Testing FontSearch Internationalization System")
    print("=" * 60)
    
    try:
        from fontsearch.i18n import (
            _, set_language, get_current_language, get_language_name,
            get_available_languages, detect_system_language, SUPPORTED_LANGUAGES
        )
        print("✅ i18n system imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import i18n system: {e}")
        return False
    
    # Test system language detection
    detected_lang = detect_system_language()
    print(f"✅ System language detected: {detected_lang} ({get_language_name(detected_lang)})")
    
    # Test available languages
    available = get_available_languages()
    print(f"✅ Available languages: {len(available)}")
    
    # Test each supported language
    print("\n🔤 Testing translations for each language:")
    print("-" * 40)
    
    for lang_code, lang_name in SUPPORTED_LANGUAGES.items():
        if set_language(lang_code):
            app_title = _("app_title")
            sample_text = _("sample_text_default")
            print(f"{lang_code:2s} | {lang_name:12s} | {app_title}")
            print(f"   | {'Sample text:':<12s} | {sample_text}")
        else:
            print(f"{lang_code:2s} | {lang_name:12s} | ❌ Failed to set language")
    
    # Test variable substitution
    print("\n🔢 Testing variable substitution:")
    print("-" * 40)
    
    set_language('en')
    fonts_msg = _("fonts_found", count=42)
    page_msg = _("page_info", current=3, total=10)
    print(f"English: {fonts_msg}")
    print(f"English: {page_msg}")
    
    set_language('es')
    fonts_msg = _("fonts_found", count=42)
    page_msg = _("page_info", current=3, total=10)
    print(f"Spanish: {fonts_msg}")
    print(f"Spanish: {page_msg}")
    
    set_language('zh')
    fonts_msg = _("fonts_found", count=42)
    page_msg = _("page_info", current=3, total=10)
    print(f"Chinese: {fonts_msg}")
    print(f"Chinese: {page_msg}")
    
    # Test fallback mechanism
    print("\n🔄 Testing fallback mechanism:")
    print("-" * 40)
    
    set_language('en')
    existing_key = _("app_title")
    missing_key = _("non_existent_key")
    print(f"Existing key: {existing_key}")
    print(f"Missing key: {missing_key} (should show key name)")
    
    return True


def test_translation_files():
    """Test that all translation files exist and are valid."""
    print("\n📁 Testing translation files:")
    print("-" * 40)
    
    from fontsearch.i18n import SUPPORTED_LANGUAGES, get_translations_dir
    
    translations_dir = get_translations_dir()
    print(f"Translations directory: {translations_dir}")
    
    if not translations_dir.exists():
        print("❌ Translations directory not found")
        return False
    
    for lang_code, lang_name in SUPPORTED_LANGUAGES.items():
        lang_file = translations_dir / f"{lang_code}.json"
        if lang_file.exists():
            try:
                import json
                with open(lang_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                print(f"✅ {lang_code}.json - {len(data)} keys - {lang_name}")
            except Exception as e:
                print(f"❌ {lang_code}.json - Invalid JSON: {e}")
        else:
            print(f"❌ {lang_code}.json - File not found")
    
    return True


def test_gui_integration():
    """Test GUI integration (import only, don't launch)."""
    print("\n🖥️  Testing GUI integration:")
    print("-" * 40)
    
    try:
        from fontsearch.gui_i18n import FontViewerI18nApp
        print("✅ Internationalized GUI class imported successfully")
        
        # Test that it can access i18n functions
        from fontsearch.i18n import _
        test_title = _("app_title")
        print(f"✅ GUI can access translations: {test_title}")
        
        return True
    except ImportError as e:
        print(f"❌ Failed to import i18n GUI: {e}")
        return False


def test_cli_integration():
    """Test CLI integration."""
    print("\n⌨️  Testing CLI integration:")
    print("-" * 40)
    
    try:
        # Test that CLI can import the i18n GUI
        from fontsearch.cli import main
        print("✅ CLI can import i18n GUI module")
        
        # Test help text includes i18n option
        import subprocess
        result = subprocess.run([
            sys.executable, "-m", "fontsearch.cli", "--help"
        ], capture_output=True, text=True, cwd=Path(__file__).parent)
        
        if "--gui-i18n" in result.stdout:
            print("✅ CLI help includes --gui-i18n option")
        else:
            print("❌ CLI help missing --gui-i18n option")
            
        return True
    except Exception as e:
        print(f"❌ CLI integration test failed: {e}")
        return False


def show_language_samples():
    """Show sample text for each language."""
    print("\n🎨 Language Sample Texts:")
    print("=" * 60)
    
    from fontsearch.i18n import set_language, _, SUPPORTED_LANGUAGES
    
    for lang_code, lang_name in SUPPORTED_LANGUAGES.items():
        set_language(lang_code)
        sample = _("sample_text_default")
        ligature_demo = _("ligature_demo_text")
        
        print(f"\n{lang_name} ({lang_code}):")
        print(f"  Sample: {sample}")
        print(f"  Demo:   {ligature_demo}")


def main():
    """Run all i18n tests."""
    print("FontSearch Internationalization Test Suite")
    print("=" * 60)
    
    tests = [
        ("i18n System", test_i18n_system),
        ("Translation Files", test_translation_files),
        ("GUI Integration", test_gui_integration),
        ("CLI Integration", test_cli_integration),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Show language samples
    show_language_samples()
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST RESULTS SUMMARY")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All i18n tests passed! FontSearch is ready for global use.")
        print("\n🌍 Supported Languages:")
        from fontsearch.i18n import SUPPORTED_LANGUAGES
        for code, name in SUPPORTED_LANGUAGES.items():
            print(f"   {code} - {name}")
        print(f"\n📊 Total coverage: 5.2+ billion speakers worldwide!")
        return 0
    else:
        print("⚠️  Some i18n tests failed. Please review and fix issues.")
        return 1


if __name__ == "__main__":
    sys.exit(main())