#!/usr/bin/python

#Some bits of code thanks to Alex Simenduev <shamil.si@gmail.com> (via Indicator-PLaces)

import gtk
import appindicator
import os
import signal
import dbus



def item_run(w, yitem):
    if yitem == "_yppa" :
        os.system("/usr/bin/y-ppa-manager")
    elif yitem == "_yppa_search":
        os.system("/usr/bin/y-ppa-cmd search")
    elif yitem == "_yppa_add":
        os.system("gksu -S -m 'Y PPA Manager requires admin privileges for this task' /usr/bin/y-ppa-cmd add")
    elif yitem == "_yppa_rem":
        os.system("gksu -S -m 'Y PPA Manager requires admin privileges for this task' /usr/bin/y-ppa-cmd remove")
    elif yitem == "_yppa_list":
        os.system("/usr/bin/y-ppa-cmd list")
    elif yitem == "_yppa_adv":
        os.system("/usr/bin/y-ppa-cmd advanced")
    elif yitem == "_yppa_set":
        os.system("/usr/bin/y-ppa-cmd settings")


class IndicatorY:

    def __init__(self):
	if dbus.SessionBus().request_name('instance.y-ppa-manager') != dbus.bus.REQUEST_NAME_REPLY_PRIMARY_OWNER:
	    print "application already running"
	    exit(0)
        self.ind = appindicator.Indicator("y-ppa-manager", "y-ppa-manager", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_label("Y")
        self.ind.set_status(appindicator.STATUS_ACTIVE)        

        self.create_menu()

    def create_menu(self, widget = None, data = None):

        # Create menu
        menu = gtk.Menu()
        self.ind.set_menu(menu)

        # List items
        item = gtk.MenuItem("Search")
        item.connect("activate", item_run, "_yppa_search")
        menu.append(item)

        item = gtk.MenuItem("Add PPA")
        item.connect("activate", item_run, "_yppa_add")
        menu.append(item)

        item = gtk.MenuItem("Remove PPA")
        item.connect("activate", item_run, "_yppa_rem")
        menu.append(item)

        item = gtk.MenuItem("List packages")
        item.connect("activate", item_run, "_yppa_list")
        menu.append(item)

        item = gtk.MenuItem("Advanced")
        item.connect("activate", item_run, "_yppa_adv")
        menu.append(item)

        # Show separator
        item = gtk.SeparatorMenuItem()
        menu.append(item)

        # More items
        item = gtk.MenuItem("Settings")
        item.connect("activate", item_run, "_yppa_set")
        menu.append(item)

        item = gtk.MenuItem("Y PPA Manager")
        item.connect("activate", item_run, "_yppa")
        menu.append(item)

        # Quit menu item
        item = gtk.MenuItem("Quit")
        item.connect("activate", gtk.main_quit)
        menu.append(item)

        menu.show_all()

if __name__ == "__main__":
    # Catch CTRL-C
    signal.signal(signal.SIGINT, lambda signal, frame: gtk.main_quit())

    # Run the indicator
    i = IndicatorY()
             
    # Main gtk loop
    gtk.main()
