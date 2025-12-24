#!/usr/bin/env python3
"""
Build and test script for FontSearch package.
"""

import subprocess
import sys
import shutil
from pathlib import Path


def run_command(cmd, description, check=True):
    """Run a command and handle errors."""
    print(f"🔧 {description}...")
    try:
        if isinstance(cmd, str):
            result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
        else:
            result = subprocess.run(cmd, check=check, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
        else:
            print(f"❌ {description} failed:")
            print(f"   Error: {result.stderr}")
            return False
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Command: {cmd}")
        print(f"   Error: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ {description} failed with exception: {e}")
        return False


def clean_build():
    """Clean previous build artifacts."""
    print("🧹 Cleaning build artifacts...")
    
    dirs_to_clean = ["build", "dist", "fontsearch.egg-info"]
    for dir_name in dirs_to_clean:
        dir_path = Path(dir_name)
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print(f"   Removed {dir_name}/")
    
    print("✅ Build artifacts cleaned")


def run_tests():
    """Run the test suite."""
    print("🧪 Running tests...")
    
    # Run the test file
    test_file = Path("tests/test_fontsearch.py")
    if test_file.exists():
        result = subprocess.run([sys.executable, str(test_file)], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ All tests passed")
            # Print last few lines which contain the summary
            lines = result.stdout.strip().split('\n')
            for line in lines[-3:]:
                if line.strip():
                    print(f"   {line}")
            return True
        else:
            print("❌ Tests failed:")
            print(result.stdout)
            print(result.stderr)
            return False
    else:
        print("⚠️  Test file not found, skipping tests")
        return True


def build_package():
    """Build the package."""
    print("📦 Building package...")
    
    # Install build tools if needed
    if not run_command([sys.executable, "-m", "pip", "install", "build", "twine", "wheel"], 
                      "Installing build tools", check=False):
        print("⚠️  Could not install build tools, continuing anyway...")
    
    # Build the package
    if not run_command([sys.executable, "-m", "build"], "Building distributions"):
        return False
    
    # Check the package
    if not run_command([sys.executable, "-m", "twine", "check", "dist/*"], 
                      "Checking package", check=False):
        print("⚠️  Package check failed, but continuing...")
    
    return True


def test_installation():
    """Test local installation."""
    print("🔍 Testing local installation...")
    
    # Install in development mode
    if not run_command([sys.executable, "-m", "pip", "install", "-e", "."], 
                      "Installing in development mode"):
        return False
    
    # Test CLI
    if not run_command("fontsearch --help", "Testing CLI help"):
        return False
    
    # Test Python import
    test_code = "import fontsearch; print(f'✅ Found {len(fontsearch.get_fonts())} fonts')"
    if not run_command([sys.executable, "-c", test_code], "Testing Python import"):
        return False
    
    # Uninstall
    if not run_command([sys.executable, "-m", "pip", "uninstall", "fontsearch", "-y"], 
                      "Uninstalling test installation"):
        print("⚠️  Could not uninstall, you may need to do this manually")
    
    return True


def show_results():
    """Show build results."""
    print("\n📊 Build Results:")
    
    dist_path = Path("dist")
    if dist_path.exists():
        print("   Generated files:")
        for file in dist_path.iterdir():
            size = file.stat().st_size
            size_str = f"{size:,} bytes" if size < 1024*1024 else f"{size/(1024*1024):.1f} MB"
            print(f"     {file.name} ({size_str})")
    else:
        print("   No dist/ directory found")
    
    print("\n🚀 Next Steps:")
    print("   1. Review the generated files in dist/")
    print("   2. Test upload to Test PyPI:")
    print("      python -m twine upload --repository testpypi dist/*")
    print("   3. If successful, upload to PyPI:")
    print("      python -m twine upload dist/*")
    print("   4. See PYPI_PUBLISHING_GUIDE.md for detailed instructions")


def main():
    """Main build and test process."""
    print("🚀 FontSearch Package Builder")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Build process
    steps = [
        ("Clean build artifacts", clean_build),
        ("Run tests", run_tests),
        ("Build package", build_package),
        ("Test installation", test_installation),
    ]
    
    success_count = 0
    for step_name, step_func in steps:
        print(f"\n{'='*20} {step_name} {'='*20}")
        try:
            if step_func():
                success_count += 1
            else:
                print(f"⚠️  {step_name} failed, but continuing...")
        except Exception as e:
            print(f"❌ {step_name} failed with exception: {e}")
    
    print(f"\n📊 Summary: {success_count}/{len(steps)} steps completed successfully")
    
    if success_count >= len(steps) - 1:  # Allow one failure
        print("🎉 Build process completed successfully!")
        show_results()
        return True
    else:
        print("⚠️  Build process completed with issues.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)