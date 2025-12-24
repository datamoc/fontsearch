# FontSearch Ligature Support Guide

## 🔤 What are Ligatures?

Ligatures are special characters where two or more letters are joined together as a single glyph. They improve readability and aesthetics in typography.

### **Common Ligatures**
- **fi** → **fi** (f and i connected)
- **fl** → **fl** (f and l connected)  
- **ff** → **ff** (double f connected)
- **ffi** → **ffi** (f, f, and i connected)
- **ffl** → **ffl** (f, f, and l connected)

### **Historical Ligatures**
- **st** → **st** (s and t connected)
- **ct** → **ct** (c and t connected)
- **sp** → **sp** (s and p connected)

## ✅ Ligature Support in FontSearch

FontSearch includes comprehensive ligature support in both GUI interfaces:

### **Features Available**
- ✅ **Contextual Ligatures**: Standard ligatures (fi, fl, ff, etc.)
- ✅ **Historical Ligatures**: Classical ligatures (st, ct, sp, etc.)
- ✅ **Real-time Toggle**: Enable/disable ligatures with checkboxes
- ✅ **OpenType Features**: Full OpenType feature support
- ✅ **Font Detection**: Automatic detection of ligature-capable fonts

### **GUI Controls**
- **☑ Ligatures contextuelles**: Enables standard ligatures (liga, clig, calt)
- **☐ Ligatures historiques**: Enables historical ligatures (hlig, dlig)

## 🔧 Requirements

### **Essential**
- **Pillow (PIL)**: Required for ligature rendering
  ```bash
  pip install pillow
  ```

### **Installation Options**
```bash
# Basic FontSearch (no ligatures)
pip install fontsearch

# FontSearch with GUI and ligatures
pip install fontsearch[gui]

# FontSearch with all features
pip install fontsearch[all]
```

## 🎯 How to Use Ligatures

### **1. Launch FontSearch GUI**
```bash
# Basic GUI
fontsearch --gui

# Advanced GUI (with SVG support)
fontsearch --gui-advanced
```

### **2. Test Ligature Text**
Enter this text in the preview field:
```
fi fl ff ffi ffl office staff
```

### **3. Enable Ligature Controls**
- ☑ **Check "Ligatures contextuelles"** for standard ligatures
- ☑ **Check "Ligatures historiques"** for historical ligatures

### **4. Browse Fonts**
Look for fonts that support ligatures:
- **Calibri** - Excellent contextual ligatures
- **Georgia** - Good standard and historical ligatures  
- **Times New Roman** - Classic ligatures
- **Libertinus Serif** - Comprehensive ligature support
- **Source Code Pro** - Programming ligatures
- **Fira Code** - Advanced programming ligatures

## 🔍 Testing Ligatures

### **Quick Test Script**
```bash
# Run the ligature test
python test_ligatures.py
```

### **Visual Test**
1. Open FontSearch GUI
2. Enter: `fi fl ff ffi ffl`
3. Enable contextual ligatures
4. Browse through fonts like Calibri, Georgia
5. Look for connected characters

### **Expected Results**
- **Without ligatures**: `f i  f l  f f  f f i  f f l`
- **With ligatures**: `fi fl ff ffi ffl` (connected)

## 🎨 Supported OpenType Features

### **Contextual Ligatures** (when enabled)
- `liga` - Standard Ligatures
- `clig` - Contextual Ligatures  
- `calt` - Contextual Alternates

### **Historical Ligatures** (when enabled)
- `hlig` - Historical Ligatures
- `dlig` - Discretionary Ligatures

### **Disabled Features** (when unchecked)
- `-liga` - Disable standard ligatures
- `-clig` - Disable contextual ligatures
- `-calt` - Disable contextual alternates

## 🐛 Troubleshooting

### **Ligatures Not Showing**

#### **Check PIL Installation**
```bash
python -c "from PIL import Image; print('PIL OK')"
```

#### **Check FontSearch PIL Detection**
```bash
python -c "from fontsearch.gui import PIL_AVAILABLE; print(f'PIL: {PIL_AVAILABLE}')"
```

#### **Install Missing Dependencies**
```bash
pip install pillow
```

### **Font Doesn't Support Ligatures**
- Not all fonts have ligatures
- Try fonts like Calibri, Georgia, Times New Roman
- Look for "ligature" in font descriptions

### **Ligatures Appear Broken**
- Ensure Pillow version is 8.0.0 or higher
- Some fonts have limited ligature support
- Try different fonts to compare

## 📊 Font Recommendations

### **Excellent Ligature Support**
- **Libertinus Serif** - Comprehensive classical ligatures
- **EB Garamond** - Beautiful historical ligatures
- **Minion Pro** - Professional ligature set

### **Good Standard Support**
- **Calibri** - Clean contextual ligatures
- **Georgia** - Readable ligatures for screen
- **Times New Roman** - Classic print ligatures

### **Programming Fonts**
- **Fira Code** - Advanced programming ligatures (==, ->, etc.)
- **Source Code Pro** - Clean code ligatures
- **JetBrains Mono** - Modern programming ligatures

## 🎉 Advanced Usage

### **Custom Ligature Text**
Try these test strings:
```
# Standard ligatures
fi fl ff ffi ffl office staff affirm

# Historical ligatures  
start stop cast best quest

# Mixed content
The office staff affirmed the final offer
```

### **Programming Ligatures** (with Fira Code)
```
== != <= >= -> => && || ++ --
```

### **Language-Specific Ligatures**
```
# German
ß ä ö ü

# French  
œ æ ç

# Nordic
å ø æ
```

## 📚 Technical Details

### **Implementation**
- Uses PIL's `font.getmask()` with OpenType features
- Supports both positive (`liga`) and negative (`-liga`) features
- Real-time feature toggling without font reload
- Automatic fallback for non-supporting fonts

### **Performance**
- Ligature rendering adds minimal overhead
- Features are cached per font
- Efficient OpenType feature detection

### **Compatibility**
- Works with all OpenType and TrueType fonts
- Graceful degradation for non-supporting fonts
- Cross-platform ligature support

FontSearch provides professional-grade ligature support for typography enthusiasts and developers! 🚀