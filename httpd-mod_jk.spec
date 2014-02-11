%define _httpd_apxs /usr/sbin/apxs
%define httpd httpd
 
Name:           httpd-mod_jk
Version:        1.2.37
Release:        1%{?org_tag}%{?dist}
Epoch:          0
Summary:        Tomcat mod_jk connector for Apache
License:        Apache License
Group:          Development/Java
URL:            http://tomcat.apache.org/
Source0:        http://www.apache.org/dist/tomcat/tomcat-connectors/jk/tomcat-connectors-%{version}-src.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       %{httpd}
BuildRequires:  %{httpd}-devel
BuildRequires:  libtool
Obsoletes:      mod_jk < %{epoch}:%{version}-%{release}
Provides:       mod_jk = %{epoch}:%{version}-%{release}
Obsoletes:      tomcat-mod < %{epoch}:%{version}-%{release}
 
%description
mod_jk allows Apache to serve as a front-end for Tomcat, GlassFish or any other
AJP1.3-enabled application server, with optional load-balancing.
 
%prep
%setup -q -n tomcat-connectors-%{version}-src
 
(cd native && %{__libtoolize} --copy --force)
 
%build
cd native
 
%configure \
  --with-apxs=%{_httpd_apxs} \
 
make
cd ..
 
%install
rm -rf %{buildroot}
 
mkdir -p %{buildroot}/%{httpd}/modules
mkdir -p %{buildroot}/%{httpd}/conf/
mkdir -p %{buildroot}/%{httpd}/conf.d/
 
%{__install} -D -m 755 native/apache-2.0/mod_jk.so %{buildroot}/%{_sysconfdir}/%{httpd}/modules/mod_jk.so
%{__install} -D -m 644 conf/workers.properties -D %{buildroot}/%{_sysconfdir}/%{httpd}/conf/workers.properties
%{__install} -D -m 644 conf/httpd-jk.conf -D %{buildroot}/%{_sysconfdir}/%{httpd}/conf.d/10_mod_jk.conf
 
%files
%doc LICENSE NOTICE conf/workers.properties.minimal
%doc native/BUILDING.txt native/README.txt native/STATUS.txt native/TODO.txt
%config(noreplace) /%{_sysconfdir}/%{httpd}/conf.d/10_mod_jk.conf
%config(noreplace) /%{_sysconfdir}/%{httpd}/conf/workers.properties
/%{_sysconfdir}/%{httpd}/modules/mod_jk.so
 
%changelog
* Tue Jun 18 2013 Vicente Dominguez <twitter:@vicendominguez> 1.2.37
- Initial release
