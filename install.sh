#!/usr/bin/sh
git clone https://github.com/vikdevelop/gitcloner-gui /tmp/gitcloner-gui > /dev/null 2>&1
cd /tmp/gitcloner-gui
install -D main.py ~/.local/bin/gitcloner-gui
chmod +x ~/.local/bin/gitcloner-gui
python3 create-desktop-file.py
mkdir -p ~/.local/share/gitcloner
cp -R translations ~/.local/share/gitcloner/
cp -R icon ~/.local/share/gitcloner/
install -D icon/git.png ~/.local/share/icons/hicolor/256x256/apps/gitcloner.png
cd
rm -rf /tmp/gitcloner-gui
