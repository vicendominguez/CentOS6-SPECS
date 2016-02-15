%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
Name:           python-pyV8
Version:        1.0
Release:        preview_r586svn%{?dist}
Summary:        Python Wrapper for Google V8 Javascript Engine

Group:          Development/Languages
License:        Apache License 2.0
URL:            https://code.google.com/p/pyv8/
Source0:        %{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python-devel, boost-devel

%description
PyV8 is a python wrapper for Google V8 engine. 
it acts as a bridge between the Python and JavaScript objects, 
and support to hosting Google's v8 engine in a python script.

%prep
%setup -q 

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitearch}/_PyV8.so
%{python_sitearch}/PyV8*

%changelog
* Tue Jan 17 2015 Vicen Dominguez <twitter:@vicendomiguez> - 1.0r586svn
- first dirty package
