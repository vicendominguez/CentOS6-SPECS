Summary: geoip VMOD for Varnish
Name: varnish-vmod-geoip
Version: 0.1
Release: 1%{?dist}
License: MIT
Group: System Environment/Daemons
Source0: libvmod-geoip.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish >= 4.0.2
Requires: GeoIP
BuildRequires: make
BuildRequires: python-docutils
BuildRequires: varnish >= 4.0.2
BuildRequires: varnish-libs-devel >= 4.0.2
BuildRequires: GeoIP-devel

%description
geoip VMOD

%prep
%setup -n libvmod-geoip-master

%build
./autogen.sh
%configure --prefix=/usr/
make
make check

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/doc/%{name}/
cp README.rst %{buildroot}/usr/share/doc/%{name}/
cp LICENSE %{buildroot}/usr/share/doc/%{name}/
rm %{buildroot}/usr/share/doc/libvmod-geoip/README.rst

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnis*/vmods/
%doc /usr/share/doc/%{name}/*
%{_mandir}/man?/*

%changelog
* Tue Nov 14 2012 Lasse Karstensen <lasse@varnish-software.com> - 0.1-0.20121114
- Initial version.
