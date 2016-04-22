# Original from https://github.com/remicollet/remirepo/blob/master/mydumper/mydumper.spec

Name:           mydumper
Version:        0.9.1
Release:        1%{?dist}
Summary:        A high-performance MySQL backup tool

Group:          Applications/Databases
License:        GPLv3+
URL:            http://www.mydumper.org/
Source0:        http://launchpad.net/mydumper/0.9/%{version}/+download/%{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  glib2-devel mysql-devel zlib-devel pcre-devel
BuildRequires:  cmake 

%description
Mydumper (aka. MySQL Data Dumper) is a high-performance multi-threaded backup
(and restore) toolset for MySQL and Drizzle.

The main developers originally worked as Support Engineers at MySQL
(one has moved to Facebook and another to SkySQL) and this is how they would
envisage mysqldump based on years of user feedback.

%prep
%setup -q

sed -e 's/-Werror//' -i CMakeLists.txt


%build
cmake -DCMAKE_INSTALL_PREFIX="%{_prefix}" .
make %{?_smp_mflags} VERBOSE=1


%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_datadir}/doc/%{name}/html/.buildinfo


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/mydumper
%{_bindir}/myloader


%changelog
* Mon Nov 16 2015 Vicente Dominguez <twitter:@vicendominguez> - 0.9.1
- Ugly and fast rpm for CentOS 6.5

* Mon Sep 29 2014 Vicente Dominguez <twitter:@vicendominguez> - 0.6.2
- Ugly fast rpm for CentOS 6.5 

* Mon Feb 28 2014 Vicente Dominguez <twitter:@vicendominguez> - 0.6.1
- Ugly fast rpm for CentOS 6 

* Mon Feb 28 2014 Vicente Dominguez <twitter:@vicendominguez> - 0.6.0
- Ugly fast rpm for CentOS 6 but it works 

* Thu Jan  3 2013 Remi Collet <remi@fedoraproject.org> - 0.2.3-2
- don't break build because of warnings
  (lot of deprecated glib calls on fedora 18)

* Sun Apr 15 2012 Remi Collet <remi@fedoraproject.org> - 0.2.3-1
- initial package
