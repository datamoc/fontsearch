# FontSearch - Complete PyPI Publishing Guide

This guide provides step-by-step instructions for publishing the FontSearch package to PyPI.

## 📋 Prerequisites

### 1. Python Environment

#### Windows (PowerShell)
```powershell
# Ensure Python 3.8+ is installed
python --version

# Create virtual environment (recommended)
python -m venv fontsearch-env
fontsearch-env\Scripts\activate
```

#### Linux/macOS (Bash)
```bash
# Ensure Python 3.8+ is installed
python --version

# Create virtual environment (recommended)
python -m venv fontsearch-env
source fontsearch-env/bin/activate
```

### 2. Install Build Tools

#### All Platforms
```bash
# Install required build tools
pip install --upgrade pip
pip install build twine wheel setuptools
```

### 3. PyPI Account Setup
1. **Create PyPI Account**: Go to https://pypi.org/account/register/
2. **Create Test PyPI Account**: Go to https://test.pypi.org/account/register/
3. **Generate API Tokens**:
   - PyPI: https://pypi.org/manage/account/token/
   - Test PyPI: https://test.pypi.org/manage/account/token/
4. **Save tokens securely** (you'll need them for uploading)

## 🔧 Pre-Publishing Steps

### 1. Verify Package Structure

#### Windows (PowerShell)
```powershell
# Navigate to the release directory
cd fontsearch-release

# Verify structure
tree /F
# Or use: Get-ChildItem -Recurse
```

#### Linux/macOS (Bash)
```bash
# Navigate to the release directory
cd fontsearch-release

# Verify structure
tree .
```

**Expected structure:**
```
fontsearch-release/
├── fontsearch/
│   ├── __init__.py
│   ├── core.py
│   └── cli.py
├── tests/
├── examples/
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
└── MANIFEST.in
```

### 2. Run Tests
```bash
# Run the test suite
python tests/test_fontsearch.py

# Expected output:
# 🚀 FontSearch Module Tests
# ==================================================
# 🧪 Testing basic functionality...
# ✅ get_fonts: Found XXX fonts
# ...
# 📊 Test Results: 6 passed, 0 failed
# 🎉 All tests passed!
```

### 3. Test Local Installation
```bash
# Install locally in development mode
pip install -e .

# Test CLI
fontsearch --help
fontsearch --max 5

# Test Python API
python -c "import fontsearch; print(f'Found {len(fontsearch.get_fonts())} fonts')"

# Uninstall after testing
pip uninstall fontsearch
```

## 📦 Building the Package

### 1. Clean Previous Builds

#### Windows (PowerShell)
```powershell
# Remove any existing build artifacts
if (Test-Path build) { Remove-Item -Recurse -Force build }
if (Test-Path dist) { Remove-Item -Recurse -Force dist }
Get-ChildItem -Filter "*.egg-info" -Recurse | Remove-Item -Recurse -Force
```

#### Linux/macOS (Bash)
```bash
# Remove any existing build artifacts
rm -rf build/ dist/ *.egg-info/
```

### 2. Build Source and Wheel Distributions
```bash
# Build the package
python -m build

# This creates:
# dist/fontsearch-1.0.0.tar.gz      (source distribution)
# dist/fontsearch-1.0.0-py3-none-any.whl  (wheel distribution)
```

### 3. Verify Build

#### Windows (PowerShell)
```powershell
# Check the built packages
Get-ChildItem dist\

# Verify package contents
python -m twine check dist\*
```

#### Linux/macOS (Bash)
```bash
# Check the built packages
ls -la dist/

# Verify package contents
python -m twine check dist/*
```

**Expected result**: "PASSED" for all checks

## 🧪 Test Publishing (Recommended)

### 1. Upload to Test PyPI First
```bash
# Upload to Test PyPI (use your Test PyPI API token)
python -m twine upload --repository testpypi dist/*

# When prompted:
# Username: __token__
# Password: [your-test-pypi-api-token]
```

### 2. Test Installation from Test PyPI

#### Windows (PowerShell)
```powershell
# Create fresh environment
python -m venv test-env
test-env\Scripts\activate

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ fontsearch

# Test the installation
fontsearch --help
python -c "import fontsearch; print('FontSearch works!')"

# Clean up
deactivate
Remove-Item -Recurse -Force test-env
```

#### Linux/macOS (Bash)
```bash
# Create fresh environment
python -m venv test-env
source test-env/bin/activate

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ fontsearch

# Test the installation
fontsearch --help
python -c "import fontsearch; print('FontSearch works!')"

# Clean up
deactivate
rm -rf test-env
```

## 🚀 Publishing to PyPI

### 1. Upload to Production PyPI
```bash
# Upload to production PyPI (use your PyPI API token)
python -m twine upload dist/*

# When prompted:
# Username: __token__
# Password: [your-pypi-api-token]
```

### 2. Verify Publication
```bash
# Check the package page
# Visit: https://pypi.org/project/fontsearch/

# Test installation from PyPI
pip install fontsearch
fontsearch --version
```

## 🔐 Security Best Practices

### 1. API Token Management

#### Windows (PowerShell)
```powershell
# Create .pypirc in user home directory
$pypircContent = @"
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = [your-pypi-api-token]

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = [your-test-pypi-api-token]
"@

$pypircContent | Out-File -FilePath "$env:USERPROFILE\.pypirc" -Encoding UTF8
```

#### Linux/macOS (Bash)
```bash
# Store tokens in ~/.pypirc (more secure)
cat > ~/.pypirc << EOF
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = [your-pypi-api-token]

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = [your-test-pypi-api-token]
EOF

# Set secure permissions
chmod 600 ~/.pypirc
```

### 2. Using Configuration File
```bash
# Upload using stored credentials
python -m twine upload --repository testpypi dist/*  # Test PyPI
python -m twine upload dist/*                        # Production PyPI
```

## 📋 Complete Publishing Checklist

### Pre-Publishing
- [ ] All tests pass (`python tests/test_fontsearch.py`)
- [ ] Version number updated in `setup.py`, `pyproject.toml`, and `__init__.py`
- [ ] README.md is complete and accurate
- [ ] LICENSE file is present
- [ ] CHANGELOG updated (if applicable)

### Building
- [ ] Clean build environment
- [ ] Build package (`python -m build`)
- [ ] Verify package (`python -m twine check dist/*`)

### Testing
- [ ] Upload to Test PyPI
- [ ] Install from Test PyPI and test functionality
- [ ] Verify package metadata on Test PyPI

### Production
- [ ] Upload to production PyPI
- [ ] Verify package page on PyPI
- [ ] Test installation from PyPI
- [ ] Update documentation with installation instructions

## 🔄 Updating the Package

### For Future Releases
1. **Update version numbers** in:
   - `setup.py`
   - `pyproject.toml`
   - `fontsearch/__init__.py`

2. **Update CHANGELOG.md** with new features/fixes

3. **Follow the same build and upload process**

### Version Numbering
Follow semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

Examples:
- `1.0.0` → `1.0.1` (bug fix)
- `1.0.1` → `1.1.0` (new feature)
- `1.1.0` → `2.0.0` (breaking change)

## 🛠 Troubleshooting

### Common Issues

#### "Package already exists"
```bash
# If you need to re-upload the same version (not recommended)
# Increment the version number instead
```

#### "Invalid credentials"
```bash
# Verify your API token
# Ensure you're using __token__ as username
# Check token permissions on PyPI
```

#### "Package validation failed"
```bash
# Run twine check first
python -m twine check dist/*

# Fix any issues reported
# Common issues: missing README, invalid metadata
```

#### "Import errors after installation"
```bash
# Check package structure
# Ensure __init__.py files are present
# Verify MANIFEST.in includes all necessary files
```

## 📞 Support

### Resources
- **PyPI Help**: https://pypi.org/help/
- **Packaging Guide**: https://packaging.python.org/
- **Twine Documentation**: https://twine.readthedocs.io/

### FontSearch Specific
- **Repository**: https://github.com/fontsearch/fontsearch
- **Issues**: https://github.com/fontsearch/fontsearch/issues
- **Documentation**: https://fontsearch.readthedocs.io/

## 🎉 Success!

Once published, users can install FontSearch with:

```bash
# Basic installation
pip install fontsearch

# Full installation with fonttools
pip install fontsearch[full]

# Use the CLI
fontsearch --help

# Use in Python
import fontsearch
fonts = fontsearch.get_fonts()
```

Your package is now available to the Python community! 🚀

---

**Note**: This guide assumes you have the necessary permissions to publish under the `fontsearch` name on PyPI. If the name is taken, you may need to choose a different package name.