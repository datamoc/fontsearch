# FontSearch Internationalization (i18n) Guide

## 🌍 Supported Languages

FontSearch now supports **10 major world languages** with automatic locale detection:

| Language | Code | Native Name | Speakers |
|----------|------|-------------|----------|
| **English** | `en` | English | 1.5B+ |
| **Mandarin Chinese** | `zh` | 中文 | 1.1B+ |
| **Hindi** | `hi` | हिन्दी | 600M+ |
| **Spanish** | `es` | Español | 500M+ |
| **Arabic** | `ar` | العربية | 400M+ |
| **French** | `fr` | Français | 280M+ |
| **Bengali** | `bn` | বাংলা | 270M+ |
| **Portuguese** | `pt` | Português | 260M+ |
| **Russian** | `ru` | Русский | 250M+ |
| **Japanese** | `ja` | 日本語 | 125M+ |

**Total Coverage**: Over **5.2 billion** native speakers worldwide! 🌎

## 🚀 How to Use

### **Launch Internationalized GUI**
```bash
# Launch i18n GUI with automatic language detection
fontsearch --gui-i18n
```

### **Language Selection**
1. **Automatic Detection**: FontSearch automatically detects your system language
2. **Manual Selection**: Use the language dropdown in the top-right corner
3. **Real-time Switching**: Change languages without restarting the application

### **Available GUI Options**
```bash
fontsearch --gui          # Basic GUI (English/French)
fontsearch --gui-advanced # Advanced GUI with SVG (English/French)  
fontsearch --gui-i18n     # Internationalized GUI (10 languages)
```

## 🎯 Features Translated

### **Complete Interface Translation**
- ✅ **Window titles** and **menu items**
- ✅ **Button labels** and **navigation controls**
- ✅ **Tooltips** and **help text**
- ✅ **Status messages** and **error messages**
- ✅ **Font type descriptions**
- ✅ **Pagination** and **search placeholders**

### **Localized Content**
- ✅ **Sample text** adapted for each language
- ✅ **Ligature test strings** with appropriate characters
- ✅ **Demo text** using language-specific examples
- ✅ **Font counts** and **status information**

### **Cultural Adaptations**
- ✅ **Text direction** support (RTL for Arabic)
- ✅ **Character sets** appropriate for each language
- ✅ **Typography conventions** respected
- ✅ **Number formatting** localized

## 📝 Sample Text Examples

Each language includes culturally appropriate sample text:

### **English**
```
AaBbCc 0123 àéïöü ÆŒß
```

### **Chinese (中文)**
```
AaBbCc 0123 你好世界 字体测试
```

### **Arabic (العربية)**
```
AaBbCc 0123 مرحبا بالعالم àéïöü ÆŒß
```

### **Hindi (हिन्दी)**
```
AaBbCc 0123 नमस्ते दुनिया àéïöü ÆŒß
```

### **Spanish (Español)**
```
AaBbCc 0123 àéïöü ÆŒß ñáéíóú
```

### **French (Français)**
```
AaBbCc 0123 àéïöü ÆŒß çñ
```

### **Japanese (日本語)**
```
AaBbCc 0123 こんにちは世界 フォントテスト
```

### **Russian (Русский)**
```
AaBbCc 0123 Привет мир àéïöü ÆŒß
```

### **Portuguese (Português)**
```
AaBbCc 0123 àéïöü ÆŒß ção
```

### **Bengali (বাংলা)**
```
AaBbCc 0123 হ্যালো বিশ্ব àéïöü ÆŒß
```

## 🔧 Technical Implementation

### **Automatic Language Detection**
1. **Environment Variables**: Checks `LANG` environment variable
2. **System Locale**: Uses `locale.getdefaultlocale()`
3. **Fallback**: Defaults to English if detection fails

### **Translation System**
- **JSON-based**: Each language has a dedicated JSON file
- **Key-value pairs**: Consistent translation keys across languages
- **Variable substitution**: Dynamic content with `{variable}` placeholders
- **Fallback mechanism**: Falls back to English if translation missing

### **File Structure**
```
fontsearch/i18n/
├── __init__.py                    # i18n system core
└── translations/
    ├── en.json                    # English (base)
    ├── zh.json                    # Chinese
    ├── hi.json                    # Hindi
    ├── es.json                    # Spanish
    ├── ar.json                    # Arabic
    ├── fr.json                    # French
    ├── bn.json                    # Bengali
    ├── pt.json                    # Portuguese
    ├── ru.json                    # Russian
    └── ja.json                    # Japanese
```

## 🎨 Usage Examples

### **Basic Usage**
```python
from fontsearch.i18n import _, set_language

# Use current language
print(_("app_title"))  # "FontSearch - Font Viewer"

# Change language
set_language('es')
print(_("app_title"))  # "FontSearch - Visor de Fuentes"

# With variables
print(_("fonts_found", count=42))  # "42 fuentes encontradas"
```

### **Language Detection**
```python
from fontsearch.i18n import detect_system_language, get_available_languages

# Detect system language
lang = detect_system_language()
print(f"Detected language: {lang}")

# Get available languages
langs = get_available_languages()
for code, name in langs.items():
    print(f"{code}: {name}")
```

### **GUI Integration**
```python
from fontsearch.i18n import _, set_language, get_available_languages

# Create language selector
languages = get_available_languages()
language_combo['values'] = [f"{code} - {name}" for code, name in languages.items()]

# Handle language change
def on_language_change():
    selection = language_var.get()
    lang_code = selection.split(" - ")[0]
    set_language(lang_code)
    update_ui_text()
```

## 🌐 Adding New Languages

### **1. Create Translation File**
```bash
# Create new translation file
cp fontsearch/i18n/translations/en.json fontsearch/i18n/translations/de.json
```

### **2. Update Language List**
```python
# In fontsearch/i18n/__init__.py
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'de': 'Deutsch',  # Add new language
    # ... other languages
}
```

### **3. Translate Content**
```json
{
  "app_title": "FontSearch - Schriftarten-Viewer",
  "sample_text_default": "AaBbCc 0123 äöü ß",
  "filter_compatible": "Kompatible Schriftarten filtern",
  // ... translate all keys
}
```

### **4. Test Translation**
```bash
# Test new language
LANG=de fontsearch --gui-i18n
```

## 🔍 Translation Keys Reference

### **Core Interface**
- `app_title` - Main window title
- `sample_text_label` - Preview text label
- `sample_text_default` - Default preview text
- `language_label` - Language selector label

### **Controls**
- `filter_compatible` - Filter checkbox text
- `contextual_ligatures` - Contextual ligatures checkbox
- `historical_ligatures` - Historical ligatures checkbox
- `enable_svg_rendering` - SVG rendering checkbox

### **Navigation**
- `navigation_first` - First page button
- `navigation_previous` - Previous page button
- `navigation_next` - Next page button
- `navigation_last` - Last page button

### **Status Messages**
- `fonts_found` - Font count message (with {count} variable)
- `page_info` - Page information (with {current} and {total} variables)
- `no_fonts_message` - No fonts found message
- `loading_fonts` - Loading message

### **Tooltips**
- `tooltip_sample_text` - Sample text input tooltip
- `tooltip_filter` - Filter checkbox tooltip
- `tooltip_contextual` - Contextual ligatures tooltip
- `tooltip_historical` - Historical ligatures tooltip
- `tooltip_language` - Language selector tooltip

## 🎯 Best Practices

### **For Users**
1. **System Language**: FontSearch automatically detects your system language
2. **Manual Override**: Use the language dropdown to switch languages
3. **Font Testing**: Each language includes appropriate test characters
4. **Cultural Context**: Sample text is culturally relevant for each language

### **For Developers**
1. **Consistent Keys**: Use the same translation keys across all languages
2. **Variable Substitution**: Use `{variable}` for dynamic content
3. **Fallback**: Always provide English fallback for missing translations
4. **Testing**: Test with different languages and character sets

### **For Translators**
1. **Context**: Understand the UI context for each translation key
2. **Length**: Keep translations reasonably similar in length to English
3. **Cultural Adaptation**: Adapt content for local culture and conventions
4. **Technical Terms**: Maintain consistency for technical terms

## 🏆 Benefits

### **Global Accessibility**
- **5.2B+ speakers** can use FontSearch in their native language
- **Cultural relevance** with appropriate sample text and examples
- **Professional quality** translations for all supported languages

### **Technical Excellence**
- **Automatic detection** of system language
- **Real-time switching** without application restart
- **Fallback mechanism** ensures stability
- **Extensible design** for easy addition of new languages

### **User Experience**
- **Familiar interface** in user's native language
- **Appropriate typography** samples for each language
- **Cultural context** in demo text and examples
- **Professional presentation** for global users

FontSearch's internationalization makes it truly accessible to users worldwide! 🌍✨