#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x702353E0F7E48EDB (dickey@invisible-island.net)
#
Name     : dialog
Version  : 1.3.20210117
Release  : 22
URL      : http://invisible-mirror.net/archives/dialog/dialog-1.3-20210117.tgz
Source0  : http://invisible-mirror.net/archives/dialog/dialog-1.3-20210117.tgz
Source1  : http://invisible-mirror.net/archives/dialog/dialog-1.3-20210117.tgz.asc
Summary  : dialog - display dialog boxes from shell scripts
Group    : Development/Tools
License  : HPND LGPL-2.1 MIT X11
Requires: dialog-bin = %{version}-%{release}
Requires: dialog-lib = %{version}-%{release}
Requires: dialog-license = %{version}-%{release}
Requires: dialog-locales = %{version}-%{release}
Requires: dialog-man = %{version}-%{release}
BuildRequires : cppcheck
BuildRequires : ctags
BuildRequires : groff
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(x11)

%description
Dialog is a program that will let you present a variety of questions or
display messages using dialog boxes from a shell script.  These types
of dialog boxes are implemented (though not all are necessarily compiled
into dialog):

     buildlist, calendar, checklist, dselect, editbox, form, fselect,
     gauge, infobox, inputbox, inputmenu, menu, mixedform,
     mixedgauge, msgbox (message), passwordbox, passwordform, pause,
     prgbox, programbox, progressbox, radiolist, rangebox, tailbox,
     tailboxbg, textbox, timebox, treeview, and yesno (yes/no).

This package installs as "cdialog" to avoid conflict with other packages.

%package bin
Summary: bin components for the dialog package.
Group: Binaries
Requires: dialog-license = %{version}-%{release}

%description bin
bin components for the dialog package.


%package dev
Summary: dev components for the dialog package.
Group: Development
Requires: dialog-lib = %{version}-%{release}
Requires: dialog-bin = %{version}-%{release}
Provides: dialog-devel = %{version}-%{release}
Requires: dialog = %{version}-%{release}

%description dev
dev components for the dialog package.


%package lib
Summary: lib components for the dialog package.
Group: Libraries
Requires: dialog-license = %{version}-%{release}

%description lib
lib components for the dialog package.


%package license
Summary: license components for the dialog package.
Group: Default

%description license
license components for the dialog package.


%package locales
Summary: locales components for the dialog package.
Group: Default

%description locales
locales components for the dialog package.


%package man
Summary: man components for the dialog package.
Group: Default

%description man
man components for the dialog package.


%prep
%setup -q -n dialog-1.3-20210117
cd %{_builddir}/dialog-1.3-20210117

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611074727
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --enable-nls \
--with-libtool \
--with-ncursesw \
--includedir=%{_includedir}/dialog
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1611074727
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dialog
cp %{_builddir}/dialog-1.3-20210117/COPYING %{buildroot}/usr/share/package-licenses/dialog/545f380fb332eb41236596500913ff8d582e3ead
cp %{_builddir}/dialog-1.3-20210117/package/debian/copyright %{buildroot}/usr/share/package-licenses/dialog/1daa1585f2992b7a88e55ffb45992ec06bed0875
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
/usr/lib64/libdialog.so
/usr/share/man/man3/dialog.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdialog.so.15
/usr/lib64/libdialog.so.15.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dialog/1daa1585f2992b7a88e55ffb45992ec06bed0875
/usr/share/package-licenses/dialog/545f380fb332eb41236596500913ff8d582e3ead

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dialog.1

%files locales -f dialog.lang
%defattr(-,root,root,-)

