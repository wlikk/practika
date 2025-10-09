@echo off
echo === Test 1: Basic commands ===
python vfs_emulator2.py ./vfs1 test_script1.bat

echo.
echo === Test 2: Error handling ===  
python vfs_emulator.py ./vfs2 test_script2.txt

echo.
echo === Test 3: Complex test ===
python vfs_emulator.py ./vfs3 test_script3.txt

echo.
echo === Test 4: Interactive mode (no script) ===
python vfs_emulator.py ./vfs4

pause