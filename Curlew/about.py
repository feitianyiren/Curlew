#-*- coding:utf-8 -*-

from gi.repository import Gtk
import i18n

APP_VERSION = '0.1.14.1'
APP_NAME = _('Curlew')

class About(Gtk.AboutDialog):
    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self, parent=parent, wrap_license=True)
        self.set_program_name(APP_NAME)
        self.set_authors(['Fayssal Chamekh <chamfay@gmail.com>'])
        self.set_copyright("Copyright © 2012, 2013 Fayssal Chamekh <chamfay@gmail.com>")
        self.set_version(APP_VERSION)
        self.set_title(_('About ') + APP_NAME)
        self.set_logo_icon_name('curlew')
        self.set_comments(_('Easy to use Multimedia Converter for Linux'))
        self.set_license("""
Released under terms on waqf public license.

This program is free software; you can redistribute it and/or modify it under the terms of the latest version waqf public license as published by ojuba.org.

This program is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose.
        
The latest version of the license can be found on:
http://www.ojuba.org/wiki/doku.php/waqf/license
""")
        self.set_website('https://github.com/chamfay/Curlew')
        self.set_website_label('https://github.com/chamfay/Curlew')
        self.set_translator_credits(_('Fayssal Chamekh <chamfay@gmail.com>'))
    
    def show(self):
        self.run()
        self.destroy()
