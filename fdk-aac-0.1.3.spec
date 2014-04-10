Name: fdk-aac
License: GPL-2.0
Group: Development/Libraries/C and C++ 
Version: 0.1.3
Release: 1
BuildRequires: pkgconfig libtool automake
BuildRequires: gcc-c++
Summary: Free AAC codec library
Source: %{name}-%{version}.tar.gz
URL: http://sourceforge.net/projects/opencore-amr/

%description
fdk-aac is a free software library and application for encoding video
streams into the H.264/MPEG-4 AVC format, and is released under the
terms of the GNU GPL.


%prep
%setup


%build
libtoolize
aclocal
automake --add-missing
autoreconf
%configure --enable-shared --disable-static
make %{?_smp_mflags}


%install
make DESTDIR=${RPM_BUILD_ROOT} install


%files
%defattr(-,root,root)
%{_libdir}/libfdk-aac.so.*


%post
/sbin/ldconfig


%postun
/sbin/ldconfig


# ----------------------------------------------------------------------------

%package devel
Group: Development/Libraries/C and C++ 
Requires: %{name} = %{version}
Summary: Development files for libfdk-aac

%description devel
Development files for libfdk-aac.

fdk-aac is a free software library and application for encoding video
streams into the H.264/MPEG-4 AVC format, and is released under the
terms of the GNU GPL.

%files devel
%defattr(-,root,root)
%{_libdir}/libfdk-aac.so
%{_libdir}/libfdk-aac.la
%{_libdir}/pkgconfig/fdk-aac.pc
%{_includedir}/%{name}

%changelog
* Mon Apr 07 2014 Vicente Dominguez <twitter:@vicendominguez> 0.1.3-1
- Initial build for CentOS 6.5
