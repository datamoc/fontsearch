# FontSearch Widget Integration Guide

## 🎯 Overview

The FontSearch widget (`FontPickerWidget`) is a reusable tkinter component that can be embedded into any Python application. It provides a complete font selection interface with advanced features like internationalization, ligature controls, and font filtering.

## 🚀 Quick Start

### Basic Integration

```python
import tkinter as tk
from tkinter import ttk
from fontsearch.widget import FontPickerWidget

def on_font_selected(font_name):
    print(f"Selected font: {font_name}")

root = tk.Tk()
root.title("My App with FontSearch")

# Create the FontPicker widget
font_picker = FontPickerWidget(
    root,
    width=600,
    height=400,
    on_font_selected=on_font_selected
)
font_picker.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
```

## 📋 Widget Parameters

### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `parent` | Widget | Required | Parent tkinter widget |
| `width` | int | 800 | Widget width in pixels |
| `height` | int | 500 | Widget height in pixels |
| `show_language_selector` | bool | True | Show language dropdown |
| `show_ligature_controls` | bool | True | Show ligature checkboxes |
| `show_filter_controls` | bool | True | Show font filtering controls |
| `show_navigation` | bool | True | Show pagination navigation |
| `on_font_selected` | Callable | None | Callback for font selection (single-click) |
| `on_font_double_click` | Callable | None | Callback for font double-click |

### Example with All Options

```python
font_picker = FontPickerWidget(
    parent_frame,
    width=800,
    height=600,
    show_language_selector=True,
    show_ligature_controls=True,
    show_filter_controls=True,
    show_navigation=True,
    on_font_selected=lambda font: print(f"Selected: {font}"),
    on_font_double_click=lambda font: apply_font(font)
)
```

## 🎨 Customization Options

### Minimal Widget (Simple Font List)

```python
# Simplified widget with minimal UI
simple_picker = FontPickerWidget(
    parent,
    width=400,
    height=300,
    show_language_selector=False,
    show_ligature_controls=False,
    show_filter_controls=False,
    show_navigation=True,
    on_font_selected=on_font_selected
)
```

### Full-Featured Widget

```python
# Complete widget with all features
full_picker = FontPickerWidget(
    parent,
    width=800,
    height=600,
    show_language_selector=True,
    show_ligature_controls=True,
    show_filter_controls=True,
    show_navigation=True,
    on_font_selected=on_font_selected,
    on_font_double_click=on_font_double_clicked
)
```

## 🔧 Public API Methods

### Font Selection

```python
# Get currently selected font
selected_font = font_picker.get_selected_font()

# Check if a font is selected
if selected_font:
    print(f"Current selection: {selected_font}")
```

### Sample Text Control

```python
# Set custom sample text
font_picker.set_sample_text("Your custom preview text here")

# Get current sample text
current_text = font_picker.get_sample_text()
```

### Language Control

```python
# Set interface language
font_picker.set_language('fr')  # French
font_picker.set_language('es')  # Spanish
font_picker.set_language('zh')  # Chinese
```

### Font Information

```python
# Get total font count
total_fonts = font_picker.get_font_count()

# Get filtered font count
filtered_count = font_picker.get_filtered_font_count()

# Refresh font list
font_picker.refresh()
```

## 📱 Integration Examples

### 1. Text Editor Integration

```python
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.current_font = "Arial"
        
        # Main layout
        paned = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)
        
        # Text area
        self.text_area = tk.Text(paned)
        paned.add(self.text_area, weight=2)
        
        # Font picker
        self.font_picker = FontPickerWidget(
            paned,
            width=400,
            on_font_selected=self.on_font_selected,
            on_font_double_click=self.apply_font
        )
        paned.add(self.font_picker, weight=1)
    
    def on_font_selected(self, font_name):
        self.current_font = font_name
        # Update UI to show selected font
    
    def apply_font(self, font_name):
        self.current_font = font_name
        self.text_area.configure(font=(font_name, 12))
```

### 2. Font Picker Dialog

```python
class FontPickerDialog:
    def __init__(self, parent=None):
        self.result = None
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Select Font")
        self.dialog.geometry("600x500")
        self.dialog.grab_set()  # Modal
        
        # Font picker
        self.font_picker = FontPickerWidget(
            self.dialog,
            on_font_double_click=self.accept_font
        )
        self.font_picker.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Buttons
        button_frame = ttk.Frame(self.dialog)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(button_frame, text="OK", command=self.ok).pack(side=tk.RIGHT, padx=(5, 0))
        ttk.Button(button_frame, text="Cancel", command=self.cancel).pack(side=tk.RIGHT)
    
    def accept_font(self, font_name):
        self.result = font_name
        self.dialog.destroy()
    
    def ok(self):
        self.result = self.font_picker.get_selected_font()
        self.dialog.destroy()
    
    def cancel(self):
        self.result = None
        self.dialog.destroy()
    
    def show(self):
        self.dialog.wait_window()
        return self.result

# Usage
def choose_font():
    dialog = FontPickerDialog(root)
    selected_font = dialog.show()
    if selected_font:
        print(f"User selected: {selected_font}")
```

### 3. Design Application Integration

```python
class DesignApp:
    def __init__(self, root):
        self.font_collection = []
        
        # Main layout
        main_paned = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        main_paned.pack(fill=tk.BOTH, expand=True)
        
        # Font browser
        browser_frame = ttk.LabelFrame(main_paned, text="Font Browser")
        self.font_picker = FontPickerWidget(
            browser_frame,
            on_font_selected=self.preview_font,
            on_font_double_click=self.add_to_collection
        )
        self.font_picker.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        main_paned.add(browser_frame, weight=2)
        
        # Font collection
        collection_frame = ttk.LabelFrame(main_paned, text="My Fonts")
        self.collection_listbox = tk.Listbox(collection_frame)
        self.collection_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        main_paned.add(collection_frame, weight=1)
    
    def preview_font(self, font_name):
        # Update preview area
        pass
    
    def add_to_collection(self, font_name):
        if font_name not in self.font_collection:
            self.font_collection.append(font_name)
            self.collection_listbox.insert(tk.END, font_name)
```

## 🌍 Internationalization

The widget supports 10 languages automatically:

```python
# Supported languages
languages = {
    'en': 'English',
    'zh': '中文',           # Chinese
    'hi': 'हिन्दी',         # Hindi  
    'es': 'Español',        # Spanish
    'ar': 'العربية',        # Arabic
    'fr': 'Français',       # French
    'bn': 'বাংলা',          # Bengali
    'pt': 'Português',      # Portuguese
    'ru': 'Русский',        # Russian
    'ja': '日本語',         # Japanese
}

# Set language programmatically
font_picker.set_language('fr')  # Switch to French
```

## 🎛️ Advanced Features

### Ligature Controls

The widget includes controls for typography ligatures:

```python
# Access ligature settings
contextual_enabled = font_picker.contextual_ligatures.get()
historical_enabled = font_picker.historical_ligatures.get()

# Set ligature options programmatically
font_picker.contextual_ligatures.set(True)
font_picker.historical_ligatures.set(False)
```

### Font Filtering

```python
# Enable text-based filtering
font_picker.filter_glyphs.set(True)
font_picker.set_sample_text("🌷😀")  # Filter for emoji support

# Refresh to apply filters
font_picker.refresh()
```

### Custom Styling

```python
# Configure widget appearance
font_picker.configure(
    relief="sunken",
    borderwidth=2,
    background="#f0f0f0"
)

# Access internal components for advanced styling
font_picker.canvas.configure(bg="#ffffff")
```

## 📦 Dependencies

### Required
- Python 3.8+
- tkinter (usually included with Python)

### Optional (for enhanced features)
- **Pillow**: Better font rendering and ligature support
- **fonttools**: Advanced font analysis and text filtering

```bash
# Install optional dependencies
pip install pillow fonttools
```

## 🔍 Troubleshooting

### Common Issues

**Widget not displaying fonts:**
```python
# Force refresh after creation
font_picker.after(100, font_picker.refresh)
```

**Font selection not working:**
```python
# Check if callbacks are properly set
def debug_callback(font_name):
    print(f"DEBUG: Font selected: {font_name}")

font_picker = FontPickerWidget(
    parent,
    on_font_selected=debug_callback
)
```

**Language switching not working:**
```python
# Ensure language selector is enabled
font_picker = FontPickerWidget(
    parent,
    show_language_selector=True  # Must be True
)
```

## 🎯 Best Practices

### 1. Responsive Design
```python
# Use proper packing for responsive layout
font_picker.pack(fill=tk.BOTH, expand=True)

# Or use grid with sticky
font_picker.grid(row=0, column=0, sticky="nsew")
parent.grid_rowconfigure(0, weight=1)
parent.grid_columnconfigure(0, weight=1)
```

### 2. Callback Handling
```python
def safe_font_callback(font_name):
    try:
        # Your font handling code
        apply_font(font_name)
    except Exception as e:
        print(f"Error applying font {font_name}: {e}")

font_picker = FontPickerWidget(
    parent,
    on_font_selected=safe_font_callback
)
```

### 3. Memory Management
```python
# Clear widget when done
def cleanup():
    font_picker.destroy()
    
# Bind to window close
root.protocol("WM_DELETE_WINDOW", cleanup)
```

## 📚 Complete Examples

See the `examples/` directory for complete working examples:

- `widget_integration.py` - Text editor with font picker
- `simple_font_picker.py` - Font picker dialog
- `custom_font_widget.py` - Advanced design application

## 🤝 Contributing

The FontSearch widget is designed to be extensible. You can:

1. **Subclass** `FontPickerWidget` for custom behavior
2. **Override** methods for custom rendering
3. **Extend** with additional features
4. **Contribute** improvements back to the project

## 📄 License

FontSearch Widget is licensed under LGPL-3.0, making it suitable for use in both open source and proprietary applications.

---

The FontSearch widget makes it easy to add professional font selection capabilities to any tkinter application! 🎨✨