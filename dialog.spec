#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dialog
Version  : 1.3
Release  : 3
URL      : ftp://invisible-island.net/dialog/dialog-1.3-20160209.tgz
Source0  : ftp://invisible-island.net/dialog/dialog-1.3-20160209.tgz
Summary  : dialog - display dialog boxes from shell scripts
Group    : Development/Tools
License  : LGPL-2.1
Requires: dialog-bin
Requires: dialog-lib
Requires: dialog-locales
Requires: dialog-doc
BuildRequires : groff
BuildRequires : ncurses-dev
Patch1: 0001-change-include-dir-path.patch
Patch2: 0002-change-link-path-by-shared-library.patch
Patch3: dialog-libs.patch

%description
Dialog is a program that will let you present a variety of questions or
display messages using dialog boxes from a shell script.   These  types
of  dialog  boxes  are  implemented  (though  not  all  are necessarily
compiled into dialog):

     buildlist, calendar, checklist, dselect, editbox, form, fselect,
     gauge, infobox, inputbox, inputmenu, menu, mixedform,
     mixedgauge, msgbox (message), passwordbox, passwordform, pause,
     prgbox, programbox, progressbox, radiolist, rangebox, tailbox,
     tailboxbg, textbox, timebox, treeview, and yesno (yes/no).

This package installs as "cdialog" to avoid conflict with other packages.

%package bin
Summary: bin components for the dialog package.
Group: Binaries

%description bin
bin components for the dialog package.


%package dev
Summary: dev components for the dialog package.
Group: Development
Requires: dialog-lib
Requires: dialog-bin
Provides: dialog-devel

%description dev
dev components for the dialog package.


%package doc
Summary: doc components for the dialog package.
Group: Documentation

%description doc
doc components for the dialog package.


%package lib
Summary: lib components for the dialog package.
Group: Libraries

%description lib
lib components for the dialog package.


%package locales
Summary: locales components for the dialog package.
Group: Default

%description locales
locales components for the dialog package.


%prep
%setup -q -n dialog-1.3-20160209
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure --disable-static --enable-nls --with-libtool --with-ncursesw --includedir=%{_includedir}/dialog
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
%find_lang dialog

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dialog
/usr/bin/dialog-config

%files dev
%defattr(-,root,root,-)
/usr/include/dialog/dialog.h
/usr/include/dialog/dlg_colors.h
/usr/include/dialog/dlg_config.h
/usr/include/dialog/dlg_keys.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files locales -f dialog.lang 
%defattr(-,root,root,-)

