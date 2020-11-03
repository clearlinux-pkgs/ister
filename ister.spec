#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ister
Version  : 69
Release  : 116
URL      : https://github.com/bryteise/ister/releases/download/v69/ister-69.tar.xz
Source0  : https://github.com/bryteise/ister/releases/download/v69/ister-69.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: ister-bin = %{version}-%{release}
Requires: ister-data = %{version}-%{release}
Requires: ister-license = %{version}-%{release}
Requires: cryptsetup
Requires: pycurl
BuildRequires : cryptsetup
BuildRequires : pkgconfig(systemd)
BuildRequires : pycurl

%description
ister is a template based installer for linux
Ister aims to be pylint and pep8 clean. New code should verify both pass without
exception before being submitted. If a new exception makes sense it can be added
on a case by case basis.

%package bin
Summary: bin components for the ister package.
Group: Binaries
Requires: ister-data = %{version}-%{release}
Requires: ister-license = %{version}-%{release}

%description bin
bin components for the ister package.


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


%package license
Summary: license components for the ister package.
Group: Default

%description license
license components for the ister package.


%prep
%setup -q -n ister-69
cd %{_builddir}/ister-69

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604365424
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604365424
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ister
cp %{_builddir}/ister-69/COPYING %{buildroot}/usr/share/package-licenses/ister/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ister.py
/usr/bin/ister_gui.py

%files data
%defattr(-,root,root,-)
/usr/share/defaults/ister/ister.conf
/usr/share/defaults/ister/ister.json
/usr/share/defaults/ister/release-image-config.json

%files extras
%defattr(-,root,root,-)
/usr/lib/systemd/system/ister-provision.service
/usr/lib/systemd/system/ister.service

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ister/8624bcdae55baeef00cd11d5dfcfa60f68710a02
