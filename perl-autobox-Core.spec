Name:           perl-autobox-Core
Version:        1.27
Release:        8%{?dist}
Summary:        Provide core functions to autoboxed scalars, arrays and hashes.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/~swalters/autobox-Core-1.27/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SW/SWALTERS/autobox-Core-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      x86_64
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Test::Simple) perl(autobox)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	perl(autobox)


%description
The autobox module promotes Perl's primitive types (literals (strings and numbers), scalars, arrays and hashes) into first-class objects. However, autobox does not provide any methods for these new classes.
autobox::CORE provides a set of methods for these new classes. It includes almost everything in perlfunc, some things from Scalar::Util and List::Util, and some Perl 5 versions of methods taken from Perl 6.

%prep
%setup -q -n autobox-Core-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
%{__make} test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc Changes README
%{perl_vendorarch}/auto/autobox/Core*
%{perl_vendorlib}/autobox*
%{_mandir}/man3//autobox::Core*

%changelog
* Fri Mar 21 2014 Vicente Dominguez <twitter:@vicendominguez> - 1.27-1
- initial build based on cpanspec
