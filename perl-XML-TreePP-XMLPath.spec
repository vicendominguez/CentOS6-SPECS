Name:           perl-XML-TreePP-XMLPath
Version:        0.72
Release:        8%{?dist}
Summary:        Similar to XPath, defines a path as an accessor to nodes of an XML::TreePP parsed XML Document.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            https://metacpan.org/pod/XML::TreePP::XMLPath
Source0:        http://cpan.metacpan.org/authors/id/R/RG/RGLAUE/XML-TreePP-XMLPath-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      x86_64
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Test::Simple) perl(XML::TreePP)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	perl(XML::TreePP)

%description
Similar to XPath, defines a path as an accessor to nodes of an XML::TreePP parsed XML Document.

%prep
%setup -q -n XML-TreePP-XMLPath-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
%{__make} test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc CHANGES README
%{_mandir}/man3/XML*
%{perl_vendorarch}/auto/XML*
%{perl_vendorlib}/XML*
%changelog
* Fri Mar 21 2014 Vicente Dominguez <twitter:@vicendominguez> - 2.82-1
- initial build based on cpanspec
