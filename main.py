#!/usr/bin/python3
import gi
import os
import sys
import subprocess
gi.require_version("Gtk", "4.0")
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
HOME = os.path.expanduser('~')
cs = 'LANG=cs_CZ.UTF-8\nLC_CTYPE="cs_CZ.UTF-8"\nLC_NUMERIC="cs_CZ.UTF-8"\nLC_TIME="cs_CZ.UTF-8"\nLC_COLLATE="cs_CZ.UTF-8"\nLC_MONETARY="cs_CZ.UTF-8"\nLC_MESSAGES="cs_CZ.UTF-8"\nLC_PAPER="cs_CZ.UTF-8"\nLC_NAME="cs_CZ.UTF-8"\nLC_ADDRESS="cs_CZ.UTF-8"\nLC_TELEPHONE="cs_CZ.UTF-8"\nLC_MEASUREMENT="cs_CZ.UTF-8"\nLC_IDENTIFICATION="cs_CZ.UTF-8"\nLC_ALL='
if subprocess.getoutput("locale") == cs:
    sys.path.append('%s/.local/share/gitcloner' % HOME)
    from translations.cs import *
else:
    sys.path.append('%s/.local/share/gitcloner' % HOME)
    from translations.en import *
class Dialog_successfully(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(transient_for=parent, use_header_bar=True)
        self.parent = parent

        self.set_title(title=repository_is_cloned)
        self.use_header_bar = True
        self.set_modal(modal=True)
        self.connect('response', self.dialog_response)

        self.add_buttons(
            close, Gtk.ResponseType.CANCEL,
            open_folder, Gtk.ResponseType.OK,
        )

        btn_ok = self.get_widget_for_response(
            response_id=Gtk.ResponseType.OK,
        )
        btn_ok.get_style_context().add_class(class_name='suggested-action')
        btn_cancel = self.get_widget_for_response(
            response_id=Gtk.ResponseType.CANCEL,
        )
        btn_cancel.get_style_context().add_class(class_name='destructive-action')

        content_area = self.get_content_area()
        content_area.set_orientation(orientation=Gtk.Orientation.VERTICAL)
        content_area.set_spacing(spacing=12)
        content_area.set_margin_top(margin=12)
        content_area.set_margin_end(margin=12)
        content_area.set_margin_bottom(margin=12)
        content_area.set_margin_start(margin=12)

        label = Gtk.Label()
        label.set_markup(repository_was_cloned_successfully_message)
        content_area.append(child=label)

        self.show()

    def dialog_response(self, dialog, response):
        if response == Gtk.ResponseType.OK:
            os.system("xdg-open %s/Gits" % HOME)
            dialog.close()

        elif response == Gtk.ResponseType.CANCEL:
            dialog.close()

    def get_entry_text(self):
        return self.entry.get_text()

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(650, 350)
        self.set_title(git_cloner_title)
        headerbar = Gtk.HeaderBar.new()
        
        self.set_titlebar(titlebar=headerbar)
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.set_child(self.box1)
        
        self.img = Gtk.Image()
        self.img.set_from_file("%s/.local/share/gitcloner/icon/git.png" % HOME)
        self.img.set_pixel_size(100)
        self.box1.append(self.img)
        
        self.label = Gtk.Label()
        self.label.set_markup(git_cloner_description)
        self.box1.append(self.label)
        
        self.entry_clone = Gtk.Entry()
        self.entry_clone.set_placeholder_text(enter_url)
        self.box1.append(self.entry_clone)
        
        self.buttonC = Gtk.Button(label=clone)
        self.buttonC.connect("clicked", self.on_buttonC_clicked)
        self.box1.append(self.buttonC)
        
    def on_buttonC_clicked(self, widget, *args):
        self.clone()
    def clone(self):
        entryc = self.entry_clone.get_text()
        if not os.path.exists("%s/Gits" % HOME):
            os.mkdir("%s/Gits" % HOME)
        os.chdir("%s/Gits" % HOME)
        os.popen("git clone %s > /dev/null 2>&1" % entryc)
        dialog_s = Dialog_successfully(self)
        
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
    
    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()
app = MyApp(application_id="com.github.vikdevelop.gitcloner-gui")
app.run(sys.argv)
