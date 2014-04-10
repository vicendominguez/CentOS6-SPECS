Name:           perl-autobox
Version:        2.82
Release:        8%{?dist}
Summary:        Grammar-based, user-friendly config parser
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/~chocolate/autobox-2.82/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CH/CHOCOLATE/autobox-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      x86_64
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Test::Simple) perl(Scope::Guard)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	perl(Scope::Guard)
Provides:	perl(autobox::universal)

%description
This module provides a convenient way to perform cleanup or other forms of resource management at the end of a scope. It is particularly useful when dealing with exceptions: the Scope::Guard constructor takes a reference to a subroutine that is guaranteed to be called even if the thread of execution is aborted prematurely. This effectively allows lexically-scoped "promises" to be made that are automatically honoured by perl's garbage collector.

For more information, see: http://www.drdobbs.com/cpp/184403758

%prep
%setup -q -n autobox-%{version}

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
%{_mandir}/man3/auto*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/autobox*
%changelog
* Fri Mar 21 2014 Vicente Dominguez <twitter:@vicendominguez> - 2.82-1
- initial build based on cpanspec
