#!/usr/bin/sh
git clone https://github.com/vikdevelop/gitcloner-gui /tmp/gitcloner-gui > /dev/null 2>&1
cd /tmp/gitcloner-gui
cp main.py ~/.local/bin/gitcloner-gui
cp com.github.vikdevelop.gitcloner-gui.desktop ~/.local/share/applications
mkdir -p ~/.local/share/gitcloner
cp -R translations ~/.local/share/gitcloner/
cp -R icon ~/.local/share/gitcloner/
cd
rm -rf /tmp/gitcloner-gui
