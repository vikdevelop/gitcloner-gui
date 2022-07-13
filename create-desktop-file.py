import os
HOME = os.path.expanduser('~')
if not os.path.exists('%s/.local/share/applications' % HOME):
  os.makedirs('%s/.local/share/applications' % HOME)
with open('%s/.local/share/applications/com.github.vikdevelop.gitcloner-gui.desktop' % HOME, 'w') as d:
  d.write("[Desktop Entry]\nName=Git cloner\nComment=Simple GUI for download Git repository\nType=Application\nExec=%s/.local/bin/gitcloner-gui\nIcon=gitcloner\nTerminal=false\nCategories=System;System-Tools" % HOME)
