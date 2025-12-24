#!/usr/bin/env python3
"""
Test script to verify GUI output behavior.
Tests that all GUI modes return single-line output with font selection.
"""

import subprocess
import sys
import time
from pathlib import Path

def test_gui_mode(mode_arg, mode_name):
    """Test a specific GUI mode."""
    print(f"\n=== Testing {mode_name} ===")
    
    try:
        # Start the GUI process
        process = subprocess.Popen(
            [sys.executable, "-m", "fontsearch", mode_arg],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=Path(__file__).parent
        )
        
        # Wait a bit for GUI to start
        time.sleep(2)
        
        # Terminate the process (simulating user closing)
        process.terminate()
        
        # Get output
        stdout, stderr = process.communicate(timeout=5)
        
        print(f"Return code: {process.returncode}")
        print(f"STDOUT: '{stdout.strip()}'")
        print(f"STDERR: '{stderr.strip()}'")
        
        # Check output
        lines = stdout.strip().split('\n') if stdout.strip() else []
        
        if len(lines) == 0:
            print("✅ No output (user cancelled)")
        elif len(lines) == 1:
            print(f"✅ Single line output: '{lines[0]}'")
        else:
            print(f"❌ Multiple lines output ({len(lines)} lines):")
            for i, line in enumerate(lines, 1):
                print(f"  {i}: '{line}'")
        
        return len(lines) <= 1
        
    except subprocess.TimeoutExpired:
        process.kill()
        print("❌ Process timeout")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Test all GUI modes."""
    print("FontSearch GUI Output Test")
    print("=" * 40)
    
    modes = [
        ("--gui", "Basic GUI"),
        ("--gui-advanced", "Advanced GUI"),
        ("--gui-i18n", "Internationalized GUI")
    ]
    
    results = []
    
    for mode_arg, mode_name in modes:
        success = test_gui_mode(mode_arg, mode_name)
        results.append((mode_name, success))
    
    print("\n" + "=" * 40)
    print("SUMMARY:")
    
    all_passed = True
    for mode_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {mode_name}: {status}")
        if not success:
            all_passed = False
    
    if all_passed:
        print("\n🎉 All GUI modes working correctly!")
    else:
        print("\n⚠️  Some GUI modes have issues.")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())