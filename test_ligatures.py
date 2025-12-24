#!/usr/bin/env python3
"""
Test script to verify ligature functionality in FontSearch GUI.
"""

import sys
from pathlib import Path

# Test PIL availability
try:
    from PIL import Image, ImageDraw, ImageFont, ImageTk
    print("✅ PIL (Pillow) is available")
    PIL_AVAILABLE = True
except ImportError as e:
    print(f"❌ PIL (Pillow) not available: {e}")
    PIL_AVAILABLE = False

# Test FontSearch import
try:
    import fontsearch
    from fontsearch.gui import PIL_AVAILABLE as GUI_PIL_AVAILABLE
    print(f"✅ FontSearch imported successfully")
    print(f"✅ GUI PIL availability: {GUI_PIL_AVAILABLE}")
except ImportError as e:
    print(f"❌ FontSearch import failed: {e}")
    sys.exit(1)

# Test font discovery
fonts = fontsearch.get_fonts()
print(f"✅ Found {len(fonts)} fonts")

# Test ligature-capable fonts
if PIL_AVAILABLE:
    print("\n🔤 Testing ligature support...")
    
    # Look for common fonts that support ligatures
    ligature_test_fonts = [
        "Calibri", "Georgia", "Times New Roman", "Arial", 
        "Libertinus Serif", "Source Code Pro", "Fira Code"
    ]
    
    found_ligature_fonts = []
    for font_name in ligature_test_fonts:
        if font_name in fonts:
            found_ligature_fonts.append(font_name)
    
    if found_ligature_fonts:
        print(f"✅ Found {len(found_ligature_fonts)} potential ligature fonts:")
        for font in found_ligature_fonts[:3]:  # Show first 3
            print(f"   - {font}")
    else:
        print("⚠️  No common ligature fonts found, but ligatures may still work")

    # Test ligature text
    ligature_text = "fi fl ff ffi ffl"
    print(f"\n📝 Ligature test text: '{ligature_text}'")
    print("   This text should show ligatures when rendered with supporting fonts")

else:
    print("\n❌ Ligatures require PIL (Pillow) to be installed")
    print("   Install with: pip install pillow")

print("\n🎯 To test ligatures in GUI:")
print("   1. Run: fontsearch --gui")
print("   2. Enter ligature text: 'fi fl ff ffi ffl'")
print("   3. Check 'Ligatures contextuelles' checkbox")
print("   4. Look for connected characters in supporting fonts")

print("\n📋 Ligature Requirements:")
print("   ✅ FontSearch installed" if 'fontsearch' in sys.modules else "   ❌ FontSearch not installed")
print("   ✅ PIL (Pillow) installed" if PIL_AVAILABLE else "   ❌ PIL (Pillow) not installed")
print("   ✅ GUI PIL detection working" if GUI_PIL_AVAILABLE else "   ❌ GUI PIL detection failed")

if PIL_AVAILABLE and GUI_PIL_AVAILABLE:
    print("\n🎉 Ligatures should work in FontSearch GUI!")
else:
    print("\n⚠️  Ligatures may not work properly. Install missing dependencies.")