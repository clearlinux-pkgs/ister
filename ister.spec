#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ister
Version  : 61
Release  : 95
URL      : https://github.com/bryteise/ister/releases/download/v61/ister-61.tar.xz
Source0  : https://github.com/bryteise/ister/releases/download/v61/ister-61.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: ister-bin
Requires: ister-config
Requires: ister-data
BuildRequires : pkgconfig(systemd)
BuildRequires : pycurl
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : systemd-dev
Patch1: 0001-Disable-swap-devices-enabled-by-ister.patch

%description
ister is a template based installer for linux
Ister aims to be pylint and pep8 clean. New code should verify both pass without
exception before being submitted. If a new exception makes sense it can be added
on a case by case basis.

%package bin
Summary: bin components for the ister package.
Group: Binaries
Requires: ister-data
Requires: ister-config

%description bin
bin components for the ister package.


%package config
Summary: config components for the ister package.
Group: Default

%description config
config components for the ister package.


%package data
Summary: data components for the ister package.
Group: Data

%description data
data components for the ister package.


%package extras
Summary: extras components for the ister package.
Group: Default

%description extras
extras components for the ister package.


%prep
%setup -q -n ister-61
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1516911502
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1516911502
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ister.py
/usr/bin/ister_gui.py

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/ister-provision.service
%exclude /usr/lib/systemd/system/ister.service

%files data
%defattr(-,root,root,-)
/usr/share/defaults/ister/ister.conf
/usr/share/defaults/ister/ister.json

%files extras
%defattr(-,root,root,-)
/usr/lib/systemd/system/ister-provision.service
/usr/lib/systemd/system/ister.service
