%define _prefix /usr/ant

Name:		apache-ant
Version:	1.9.2
Release:	2%{?dist}
Summary:	Apache ant
License:	Apache
URL:		http://ant.apache.org
Source: 	http://apache.mogo.be/ant/binaries/apache-ant-%{version}-bin.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

%description
%{summary}
%
%prep
%setup -q -n apache-ant-%{version}


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_prefix}
cp -r bin etc lib %{buildroot}%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}

%changelog
* Thu Mar 1 2012 Jean-Francois Roche <jfroche@affinitic.be>
- Initial implementation
