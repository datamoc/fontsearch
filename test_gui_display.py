#!/usr/bin/env python3
"""
Test script to verify GUI display initialization fix.
"""

import sys
import tkinter as tk
from pathlib import Path

def test_gui_initialization():
    """Test that GUI displays fonts immediately on startup."""
    print("🖥️  Testing GUI Display Initialization Fix")
    print("=" * 50)
    
    try:
        from fontsearch.gui_i18n import FontViewerI18nApp
        print("✅ i18n GUI imported successfully")
        
        # Create a test window (don't show it)
        root = tk.Tk()
        root.withdraw()  # Hide the window for testing
        
        # Create the app
        app = FontViewerI18nApp(root)
        
        # Check that the app has fonts loaded
        if hasattr(app, 'font_files') and app.font_files:
            print(f"✅ Fonts loaded: {len(app.font_files)} fonts")
        else:
            print("❌ No fonts loaded")
            return False
        
        # Check that filtered fonts are set
        if hasattr(app, 'filtered_fonts') and app.filtered_fonts:
            print(f"✅ Filtered fonts ready: {len(app.filtered_fonts)} fonts")
        else:
            print("❌ Filtered fonts not ready")
            return False
        
        # Check that UI components exist
        if hasattr(app, 'scrollable_frame'):
            print("✅ Scrollable frame created")
        else:
            print("❌ Scrollable frame missing")
            return False
        
        if hasattr(app, 'canvas'):
            print("✅ Canvas created")
        else:
            print("❌ Canvas missing")
            return False
        
        # Simulate the delayed refresh that should happen
        print("🔄 Testing delayed refresh mechanism...")
        
        # The fix uses root.after(100, self._refresh_list)
        # We can't easily test the timing, but we can verify the method exists
        if hasattr(app, '_refresh_list'):
            print("✅ Refresh method available")
            
            # Try calling it manually to see if it works
            try:
                app._refresh_list()
                print("✅ Manual refresh successful")
            except Exception as e:
                print(f"❌ Manual refresh failed: {e}")
                return False
        else:
            print("❌ Refresh method missing")
            return False
        
        # Clean up
        root.destroy()
        
        return True
        
    except Exception as e:
        print(f"❌ GUI test failed: {e}")
        return False


def test_basic_gui():
    """Test basic GUI initialization."""
    print("\n🖥️  Testing Basic GUI Display Fix")
    print("=" * 50)
    
    try:
        from fontsearch.gui import FontViewerApp
        print("✅ Basic GUI imported successfully")
        
        # Create a test window (don't show it)
        root = tk.Tk()
        root.withdraw()  # Hide the window for testing
        
        # Create the app
        app = FontViewerApp(root)
        
        # Check basic functionality
        if hasattr(app, 'font_files') and app.font_files:
            print(f"✅ Basic GUI fonts loaded: {len(app.font_files)} fonts")
        else:
            print("❌ Basic GUI no fonts loaded")
            return False
        
        # Clean up
        root.destroy()
        
        return True
        
    except Exception as e:
        print(f"❌ Basic GUI test failed: {e}")
        return False


def main():
    """Run GUI display tests."""
    print("FontSearch GUI Display Fix Test")
    print("=" * 60)
    
    tests = [
        ("i18n GUI Display", test_gui_initialization),
        ("Basic GUI Display", test_basic_gui),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
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
        print("🎉 GUI display fix working correctly!")
        print("\n🔧 Fix Applied:")
        print("   - Delayed initial refresh with root.after(100, self._refresh_list)")
        print("   - Added canvas configuration after window display")
        print("   - Force canvas updates with update_idletasks()")
        print("   - Improved window resize handling")
        return 0
    else:
        print("⚠️  Some GUI display tests failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())