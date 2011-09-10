#!/usr/bin/env python
import pygtk
pygtk.require('2.0')

import gtk
import gnomeapplet
import gobject

import sys
import codecs
import random

# http://www.znasibov.info/blog/post/gnome-applet-with-python-part-2.html

class PR2Dashboard(gnomeapplet.Applet):
	def __init__(self,applet,iid):
		self.timeout_interval = 1000 * 10 #Timeout set to 10secs
		self.applet = applet

		self.label = gtk.Label("l")
		self.label.set_markup('fooo')
		self.applet.add(self.label)

		self.applet.show_all()
		gobject.timeout_add(self.timeout_interval, self.update)
	def update(self):
		pass

#Register the applet datatype
gobject.type_register(PR2Dashboard)

def pr2_db_factory(applet,iid):
	PR2Dashboard(applet,iid)
	return gtk.TRUE

#Very useful if I want to debug. To run in debug mode python applet.py -d
if len(sys.argv) == 2:
	if sys.argv[1] == "-d": #Debug mode
		main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		main_window.set_title("Python Applet")
		main_window.connect("destroy", gtk.main_quit)
		app = gnomeapplet.Applet()
		pr2_db_factory(app,None)
		app.reparent(main_window)
		main_window.show_all()
		gtk.main()
		sys.exit()

#If called via gnome panel, run it in the proper way
if __name__ == '__main__':
	gnomeapplet.bonobo_factory("OAFIID:PR2Dashboard_Factory", PR2Dashboard.__gtype__, "hello", "0", pr2_db_factory)

