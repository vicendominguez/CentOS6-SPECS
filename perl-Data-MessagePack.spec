Name:           perl-Data-MessagePack
Version:        0.48
Release:        8%{?dist}
Summary:        MessagePack serializing/deserializing
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://github.com/msgpack/msgpack-perl
Source0:        http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/Data-MessagePack-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      x86_64
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Test::Simple) perl(Test::Requires)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	perl(Test::Requires)

%description
This module converts Perl data structures to MessagePack and vice versa.

MessagePack is a binary-based efficient object serialization format. It enables to exchange structured objects between many languages like JSON. But unlike JSON, it is very fast and small.

%prep
%setup -q -n Data-MessagePack-%{version}

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
%doc Changes README
%{_mandir}/man3/Data*
%{perl_vendorarch}/Data*
%{perl_vendorarch}/auto/Data*
%changelog
* Fri Mar 21 2014 Vicente Dominguez <twitter:@vicendominguez> - 0.48
- initial build based on cpanspec
