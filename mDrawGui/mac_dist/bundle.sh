#!/bin/sh
python3 setup.py py2app
echo ========== cp qt plugins ==========
cp -r ~/Qt5.3.2/5.3/clang_64/plugins dist/mDraw.app//Contents/PlugIns
echo ========== macdeployqt ==========
~/Qt5.3.2/5.3/clang_64/bin/macdeployqt dist/mDraw.app
