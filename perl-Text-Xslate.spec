Name:           perl-Text-Xslate
Version:        3.1.2
Release:        8%{?dist}
Summary:        Scalable template engine for Perl5
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://xslate.org/
Source0:        http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/Text-Xslate-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      x86_64
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Test::Simple) perl(Mouse) perl(Data::MessagePack) perl(parent) perl(File::Copy::Recursive) perl(Time::HiRes)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	perl(Mouse) perl(Data::MessagePack) perl(parent) perl(Time::HiRes)

%description
Xslate is a template engine, tuned for persistent applications, safe as an HTML generator, and with rich features.

There are a lot of template engines in CPAN, for example Template-Toolkit, Text::MicroTemplate, HTML::Template, and so on, but all of them have some weak points: a full-featured template engine may be slow, while a fast template engine may be too simple to use. This is why Xslate is developed, which is the best template engine for web applications.

The concept of Xslate is strongly influenced by Text::MicroTemplate and Template-Toolkit 2, but the central philosophy of Xslate is different from them. That is, the philosophy is sandboxing that the template logic should not have no access outside the template beyond your permission.

%prep
%setup -q -n Text-Xslate-%{version}

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
%doc Changes README.md
%{_mandir}/man3/Text*
%{_mandir}/man1/xslate*
%{perl_vendorarch}/auto/Text*
%{perl_vendorarch}/Text*
/usr/bin/xslate
%changelog
* Fri Mar 21 2014 Vicente Dominguez <twitter:@vicendominguez> - 3.1.2
- initial build based on cpanspec
