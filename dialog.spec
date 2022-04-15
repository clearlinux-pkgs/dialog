#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dialog
Version  : 1.3.20220414
Release  : 32
URL      : https://invisible-mirror.net/archives/dialog/dialog-1.3-20220414.tgz
Source0  : https://invisible-mirror.net/archives/dialog/dialog-1.3-20220414.tgz
Summary  : dialog - display dialog boxes from shell scripts
Group    : Development/Tools
License  : LGPL-2.1 MIT
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
%setup -q -n dialog-1.3-20220414
cd %{_builddir}/dialog-1.3-20220414

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650033530
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
export SOURCE_DATE_EPOCH=1650033530
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dialog
cp %{_builddir}/dialog-1.3-20220414/COPYING %{buildroot}/usr/share/package-licenses/dialog/545f380fb332eb41236596500913ff8d582e3ead
cp %{_builddir}/dialog-1.3-20220414/package/debian/copyright %{buildroot}/usr/share/package-licenses/dialog/d4dae61ed985437566aece1432d58dfa171cd201
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
/usr/share/package-licenses/dialog/545f380fb332eb41236596500913ff8d582e3ead
/usr/share/package-licenses/dialog/d4dae61ed985437566aece1432d58dfa171cd201

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dialog.1

%files locales -f dialog.lang
%defattr(-,root,root,-)

