#
# spec file for package boost
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define ver 1.54.0
%define file_version 1_54_0
%define short_version 1_54
%define lib_appendix 1_54_0

#Only define to 1 to generate the man pages
%define build_docs 0

#Define to 0 to not generate the pdf documentation
%define build_pdf 0

# Just hardcode build_mpi to 1 as soon as openmpi builds on all
# named architectures.

#%ifarch s390 s390x ia64 hppa %arm
#%define build_mpi 0
#%else
#%define build_mpi 1
#%endif
%define build_mpi 0

%ifarch hppa
%define disable_long_double 1
%else
%define disable_long_double 0
%endif

%define boost_libs1 libboost_date_time%{lib_appendix} libboost_filesystem%{lib_appendix} libboost_graph%{lib_appendix}
%define boost_libs2 libboost_iostreams%{lib_appendix} libboost_math%{lib_appendix} libboost_test%{lib_appendix}
%define boost_libs3 libboost_program_options%{lib_appendix} libboost_python%{lib_appendix} libboost_serialization%{lib_appendix}
%define boost_libs4 libboost_signals%{lib_appendix} libboost_system%{lib_appendix} libboost_thread%{lib_appendix}
%define boost_libs5 libboost_wave%{lib_appendix} libboost_regex%{lib_appendix} libboost_regex%{lib_appendix}
%define boost_libs6 libboost_random%{lib_appendix} libboost_chrono%{lib_appendix} libboost_locale%{lib_appendix}
%define boost_libs7 libboost_timer%{lib_appendix} libboost_atomic%{lib_appendix}

%define most_libs %boost_libs1 %boost_libs2 %boost_libs3 %boost_libs4 %boost_libs5 %boost_libs6 %boost_libs7

%if %build_mpi
%define all_libs %{most_libs} libboost_mpi%{lib_appendix}
%else
%define all_libs %{most_libs}
%endif

%define debug_package_requires %{all_libs}

Name:           boost
BuildRequires:  chrpath
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  bzip2-devel
%if 0%{?suse_version}
BuildRequires:  libexpat-devel
%else
BuildRequires:  expat-devel
%endif
BuildRequires:  libicu-devel
BuildRequires:  python-devel
%if %build_mpi
BuildRequires:  openmpi-devel
%endif
%if %build_docs
BuildRequires:  docbook
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libxslt
BuildRequires:  python-devel
BuildRequires:  texlive-latex
%endif
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif
Url:            http://www.boost.org
Summary:        Boost C++ Libraries
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Version:        %{ver}
Release:        8.20.2
Source0:        %{name}_%{file_version}.tar.bz2
Source1:        boost-rpmlintrc
Source4:        existing_extra_docs
Source5:        NEWS
%if %{defined suse_version}
#Recommends:     %{all_libs}
%endif

%define _docdir %{_datadir}/doc/packages/boost-%{version}

%description
Boost provides free peer-reviewed portable C++ source libraries. The
emphasis is on libraries that work well with the C++ Standard Library.
One goal is to establish "existing practice" and provide reference
implementations so that the Boost libraries are suitable for eventual
standardization. Some of the libraries have already been proposed for
inclusion in the C++ Standards Committee's upcoming C++ Standard
Library Technical Report.

Although Boost was begun by members of the C++ Standards Committee
Library Working Group, membership has expanded to include nearly two
thousand members of the C++ community at large.

This package is mainly needed for updating from a prior version, the
dynamic libraries are found in their respective package. For development
using Boost, you also need the boost-devel package. For documentation,
see the boost-doc package.



%package        devel
Summary:        Development package for Boost C++
Group:          Development/Libraries/C and C++
Requires:       %{all_libs}
Requires:       libstdc++-devel

%description    devel
This package contains all that is needed to develop/compile
applications that use the Boost C++ libraries. For documentation see
the documentation packages (html, man or pdf).



%package     -n boost-license%{lib_appendix}

Summary:        Boost License
Group:          Development/Libraries/C and C++
Provides:       boost-license = %{version}-%{release}
Obsoletes:      boost-license < %{version}
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description    -n boost-license%{lib_appendix}
This package contains the license boost is provided under.



%package        doc-html
Summary:        HTML documentation for the Boost C++ Libraries
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description    doc-html
This package contains the documentation of the boost dynamic libraries
in HTML format.



%if %build_pdf

%package        doc-pdf
Summary:        PDF documentation for the Boost C++ Libraries
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description     doc-pdf
This package contains the documentation of the boost dynamic libraries
in PDF format.
%endif

%package        -n libboost_date_time%{lib_appendix}

Summary:        Boost::Date.Time Runtime libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_date_time%{lib_appendix}
This package contains the Boost Date.Time runtime libraries.



%package        -n libboost_filesystem%{lib_appendix}

Summary:        Boost::Filesystem Runtime Libraries
Group:          System/Localization
Requires:       boost-license%{lib_appendix}

%description    -n libboost_filesystem%{lib_appendix}
This package contains the Boost::Filesystem libraries.



%package        -n libboost_graph%{lib_appendix}

Summary:        Boost::Graph Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_graph%{lib_appendix}
This package contains the Boost::Graph Runtime libraries.



%package        -n libboost_iostreams%{lib_appendix}

Summary:        Boost::IOStreams Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_iostreams%{lib_appendix}
This package contains the Boost::IOStreams Runtime libraries.



%package        -n libboost_math%{lib_appendix}

Summary:        Boost::Math Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_math%{lib_appendix}
This package contains the Boost::Math Runtime libraries.


%if %build_mpi

%package        -n libboost_mpi%{lib_appendix}

Summary:        Boost::MPI Runtime libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_mpi%{lib_appendix}
This package contains the Boost::MPI Runtime libraries.

%endif

%package        -n libboost_test%{lib_appendix}

Summary:        Boost::Test Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_test%{lib_appendix}
This package contains the Boost::Test runtime libraries.



%package        -n libboost_program_options%{lib_appendix}

Summary:        Boost::ProgramOptions Runtime libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_program_options%{lib_appendix}
This package contains the Boost::ProgramOptions Runtime libraries.



%package        -n libboost_python%{lib_appendix}

Summary:        Boost::Python Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_python%{lib_appendix}
This package contains the Boost::Python Runtime libraries.



%package        -n libboost_serialization%{lib_appendix}

Summary:        Boost::Serialization Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_serialization%{lib_appendix}
This package contains the Boost::Serialization Runtime libraries.



%package        -n libboost_signals%{lib_appendix}

Summary:        Boost::Signals Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_signals%{lib_appendix}
This package contains the Boost::Signals Runtime libraries.



%package        -n libboost_system%{lib_appendix}

Summary:        Boost::System Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_system%{lib_appendix}
This package contains the Boost::System runtime libraries.



%package        -n libboost_thread%{lib_appendix}

Summary:        Boost::Thread Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_thread%{lib_appendix}
This package contains the Boost::Thread runtime libraries.



%package        -n libboost_wave%{lib_appendix}

Summary:        Boost::Wave Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_wave%{lib_appendix}
This package contains the Boost::Wave runtime libraries.



%package        -n libboost_regex%{lib_appendix}

Summary:        The Boost::Regex runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_regex%{lib_appendix}
This package contains the Boost::Regex runtime library.

%package        -n libboost_random%{lib_appendix}

Summary:        The Boost::Random runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_random%{lib_appendix}
This package contains the Boost:Random runtime library.

%package        -n libboost_chrono%{lib_appendix}

Summary:        The Boost::Chrono runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_chrono%{lib_appendix}
This package contains the Boost:Chrono runtime library.

%package        -n libboost_locale%{lib_appendix}

Summary:        The Boost::Locale runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_locale%{lib_appendix}
This package contains the Boost:Locale runtime library.

%package        -n libboost_timer%{lib_appendix}

Summary:        The Boost::Timer runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_timer%{lib_appendix}
This package contains the Boost:Timer runtime library.

%package        -n libboost_atomic%{lib_appendix}

Summary:        The Boost::Atomic runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_atomic%{lib_appendix}
This package contains the Boost:Atomic runtime library.

%package        -n libboost_context%{lib_appendix}

Summary:        The Boost::Context runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_context%{lib_appendix}
This package contains the Boost:Context runtime library.

%package        -n libboost_log%{lib_appendix}

Summary:        The Boost::Log runtime library
Group:          System/Libraries
Requires:       boost-license%{lib_appendix}

%description    -n libboost_log%{lib_appendix}
This package contains the Boost:Log runtime library.



%prep
%setup -q -n %{name}_%{file_version}
#%patch0 -p1

#everything in the tarball has the executable flag set ...
find -type f ! \( -name \*.sh -o -name \*.py -o -name \*.pl \) -exec chmod -x {} +

#stupid build machinery copies .orig files
find . -name \*.orig -exec rm {} +

%build
find . -type f -exec chmod u+w {} +

./bootstrap.sh --libdir=%{buildroot}%{_libdir} --includedir=%{buildroot}%{_includedir} --without-libraries=mpi
./b2 -j4 -d0

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/boost

./b2 install -j4 

mkdir -p %{buildroot}%{_docdir}

pushd %{buildroot}%{_libdir}
blibs=$(find . -name \*.so.%{version})
echo $blibs | xargs chrpath -d 

for lib in ${blibs}; do
  BASE=$(basename ${lib} .so.%{version})
  SONAME_MT="$BASE-mt.so"
  ln -sf ${lib} $SONAME_MT
done
popd

#install the man pages
rm -rf doc/man/man3/boost::units::operator

for sec in 3 7 9; do
    install -d %buildroot/%{_mandir}/man${sec}
done

#
##install the pdf documentation
#install -d %buildroot/%{_docdir}/pdf
#install -p -m 644 ../%{name}_%{short_version}_pdf/*.pdf %{buildroot}/%{_docdir}/pdf/
#
#install autoconf macros
#install -d %{buildroot}%{_datadir}/aclocal
#install -m 644 m4/*.m4 %{buildroot}%{_datadir}/aclocal

#install doc files
dos2unix libs/ptr_container/doc/tutorial_example.html \
	libs/parameter/doc/html/reference.html \
	libs/parameter/doc/html/index.html \
	libs/iostreams/doc/tree/tree.js \
	libs/graph/doc/lengauer_tarjan_dominator.htm \
	libs/test/test/test_files/errors_handling_test.pattern \
	libs/test/test/test_files/result_report_test.pattern
find . -name \*.htm\* -o -name \*.gif -o -name \*.css -o -name \*.jpg -o -name \*.png -o -name \*.ico | \
	tar --files-from=%{S:4} -cf - --files-from=- | tar -C %{buildroot}%{_docdir} -xf -
rm -rf %{buildroot}%{_docdir}/boost
ln -s /usr/include/boost %{buildroot}%{_docdir}
ln -s ../LICENSE_1_0.txt %{buildroot}%{_docdir}/libs
#Copy the news file.
cp %{S:5} %{buildroot}%{_docdir}
#only for documentation, doesn't need to be executable
find %{buildroot}%{_docdir} -name \*.py -exec chmod -x {} +
#symlink dupes
%if 0%{?suse_version} > 1020
%fdupes %buildroot
%endif

%post -n libboost_date_time%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_filesystem%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_iostreams%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_test%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_program_options%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_python%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_regex%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_serialization%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_signals%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_thread%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_math%{lib_appendix} -p /sbin/ldconfig 
%if %build_mpi

%post -n libboost_mpi%{lib_appendix} -p /sbin/ldconfig       
%endif

%post -n libboost_graph%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_system%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_wave%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_random%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_chrono%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_locale%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_timer%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_atomic%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_context%{lib_appendix} -p /sbin/ldconfig

%post -n libboost_log%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_date_time%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_filesystem%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_iostreams%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_test%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_program_options%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_python%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_regex%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_serialization%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_signals%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_thread%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_math%{lib_appendix} -p /sbin/ldconfig
%if %build_mpi

%postun -n libboost_mpi%{lib_appendix} -p /sbin/ldconfig
%endif

%postun -n libboost_graph%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_system%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_wave%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_random%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_chrono%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_locale%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_timer%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_atomic%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_context%{lib_appendix} -p /sbin/ldconfig

%postun -n libboost_log%{lib_appendix} -p /sbin/ldconfig

%files -n boost-license%{lib_appendix}
%defattr(-, root, root, -)
%dir %{_docdir}
%doc %{_docdir}/NEWS
%doc %{_docdir}/LICENSE_1_0.txt

%files -n libboost_date_time%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_date_time*.so.*

%files -n libboost_filesystem%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_filesystem*.so.*

%files -n libboost_graph%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_graph*.so.*

%files -n libboost_iostreams%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_iostreams*.so.*

%files -n libboost_math%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_math_*.so.*

%if %build_mpi

%files -n libboost_mpi%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_mpi*.so.*
%{_libdir}/mpi.so
%endif

%files -n libboost_test%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_prg_exec_monitor*.so.*
%{_libdir}/libboost_unit_test_framework*.so.*

%files -n libboost_program_options%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_program_options*.so.*

%files -n libboost_python%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_python*.so.*

%files -n libboost_serialization%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_*serialization*.so.*

%files -n libboost_signals%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_signals*.so.*

%files -n libboost_system%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_system*.so.*

%files -n libboost_thread%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_thread*.so.*

%files -n libboost_wave%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_wave*.so.*

%files -n libboost_regex%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_regex*.so.*

%files -n libboost_random%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_random*.so.*

%files -n libboost_chrono%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_chrono*.so.*

%files -n libboost_locale%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_locale*.so.*

%files -n libboost_timer%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_timer*.so.*

%files -n libboost_atomic%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_atomic*.so.*

%files -n libboost_context%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_context*.so.*

%files -n libboost_log%{lib_appendix}
%defattr(-, root, root, -)
%{_libdir}/libboost_log*.so.*

%files devel
%defattr(-, root, root, -)
%{_includedir}/boost
%{_libdir}/*.so
%{_libdir}/*.a
%if %build_mpi
%exclude %{_libdir}/mpi.so
%endif

#%%{_datadir}/aclocal/*.m4

%files doc-html
%defattr(-, root, root, -)
%doc %{_docdir}/*
%exclude %{_docdir}/NEWS
%exclude %{_docdir}/LICENSE_1_0.txt
%if %build_pdf
%exclude %{_docdir}/pdf
%endif

%if %build_pdf

%files doc-pdf
%defattr(-, root, root, -)
%doc %{_docdir}/pdf
%endif

%changelog
* Mon Oct  3 2011 dmueller@suse.de
- disable openmpi on %%%%arm
* Tue Apr 19 2011 ro@suse.de
- update baselibs.conf
* Mon Mar 21 2011 idoenmez@novell.com
- Fix attribute handling problem in spirit library,
  See http://comments.gmane.org/gmane.comp.parsers.spirit.general/22073
* Mon Mar 21 2011 pth@suse.de
- Prefix bug numbers.
* Fri Mar 18 2011 pth@suse.de
- Make packaging of the pdf documentation configurable.
* Fri Mar 18 2011 pth@suse.de
- Update to 1.46.1, a bugfix release:
  • Asio:
  - EV_ONESHOT seems to cause problems on some versions of Mac OS X, with
    the io_service destructor getting stuck inside the close() system call.
    Changed the kqueue backend to use EV_CLEAR instead (boost#5021).
  - Fixed compile failures with some versions of g++ due to the use of
    anonymous enums (boost#4883).
  - Fixed a bug on kqueue-based platforms, where some system calls that
    repeatedly fail with EWOULDBLOCK are not correctly re-registered with
    kqueue.
  - Changed asio::streambuf to ensure that its internal pointers are
    updated correctly after the data has been modified using std::streambuf
    member functions.
  - Fixed a bug that prevented the linger socket option from working on
    platforms other than Windows.
  For the rest see NEWS or the boost web site http://www.boost.org
* Wed Mar 16 2011 pth@suse.de
- Remove comment chars from doc-pdf description.
* Mon Mar 14 2011 pth@suse.de
- Use xz to compress tarballs.
- Generate new man pages tarball.
- Update pdf tarball.
- Update to 1.46:
  New Libraries
    Icl: Interval Container Library, interval sets and maps and
    aggregation of associated values, from Joachim Faulhaber.
  For the rest of the changes see NEWS in the package documentation
  directory or see http://www.boost.org/users/news/version_1_46_0 .
* Thu Nov 25 2010 pth@suse.de
- Remove the boost specific autoconf macros now that we have the
  complete autoconf archive packaged (bnc#655747).
- Move the lib64 patch over to autoconf-archive.
* Mon Oct 25 2010 jslaby@novell.com
- take care of random library (build 32bit on x86_64 and
  require it in boost-devel)
* Wed Sep 29 2010 coolo@novell.com
- fix baselibs.conf
* Fri Sep  3 2010 pth@suse.de
- Shorten the list of update items.
- Fix typo in spec.
* Thu Aug 26 2010 pth@suse.de
- Redo the lib64 patch for the boost autoconf macros so that
  lib64 is used on all archs that need it.
- Remove the ICU patch.
* Thu Aug 26 2010 pth@suse.de
- Update to 1.44.0:
  New Libraries:
  * Meta State Machine: High-performance expressive UML2 finite
    state machines
  * Polygon: Booleans/clipping, resizing/offsetting and more for
    planar polygons with integral coordinates
  Updated Libraries:
  * Accumulators:
  * Asio:
  * Foreach:
  * Fusion:
  * Hash:
  * Math:
  * MPL:
  * Multi-index Containers:
  * Proto:
  * Regex:
  * Thread:
  * Type Traits:
  * uBLAS:
  * Utility:
  * Uuid:
  * Config:
  * Xpressive:
  * Filesystem:
    o This release contains both version 2 and version 3 of the
    library.  Version 3 is a major upgrade that will break some
    existing user code, so version 2 is the default.  Users are
    encouraged to migrate to version 3.  See 'Version 2' and
    'Version 3' for more information.
  * Iostreams:
    o Several fixes for file descriptors class, including a
    breaking change to the constructors and open methods for
    file_descriptor, file_descriptor_source and
    file_descriptor_sink.  See the documentation for details.
    The old methods are still available if you define
    BOOST_IOSTREAMS_USE_DEPRECATED
  * Spirit: Spirit V2.4, see the 'What's New' section for details.
  * System:
    o Change system_category and generic_category to functions, to
    conform to the C++0x FCD.  This change may cause compile
    errors some user code; the fix is add "()" to references to
    system_category and generic_category, so that they become
    function calls.
  * Wave: See the Changelog for details.
  Major Changes in 1.43.0:
  New Libraries
  * Functional/factory: Function objects for dynamic and by-value
    construction
  * Functional/forward: Function object adapters to address the
    forwarding problem
  For a complete list of changes see
  http://www.boost.org/users/news/version_1_43_0 and
  http://www.boost.org/users/news/version_1_44_0.
* Fri Jul  9 2010 pth@suse.de
- Rename patch to be identical to the one checked in for 11.3.
  The patch adds an explicite specialization to the call to prevent
  unwanted temporary instantiations.
* Fri Jul  9 2010 lnussel@suse.de
- fix bug that shows with gcc 4.5 (bnc#621140)
* Wed Jun 16 2010 pth@suse.de
- Noarch sub packages only doable from 11.2 on up.
* Thu Jun 10 2010 wittemar@googlemail.com
- build 32bit-packages
* Mon May 24 2010 bg@novell.com
- disable long double support for hppa
* Thu May 20 2010 bg@novell.com
- openmpi does not build on hppa
* Thu Apr 29 2010 pth@novell.com
- Move provides/obsoletes for boost-license to the right section
  (bnc#544958).
* Mon Apr 26 2010 pth@novell.com
- Delete unneeded patches.
* Wed Apr 14 2010 pth@suse.de
- Readd those patches that are still needed.
- Try to fix an aliasing bug in function_base.hpp
- Build man pages locally and only include them as a tarball.
- Split documentation in in format specific packages.
* Sat Apr  3 2010 freespacer@gmx.de
- update to 1.42.0:
  New Libraries
  * Uuid: A universally unique identifier, from Andy Tompkins.
  Updated Libraries (see README for details)
  * Asio:
  * Circular Buffer:
  * Fusion:
  * Graph:
  * Integer:
  * Iostreams:
  * Program.Options:
  * PropertyMap:
  * Proto:
  * Regex:
  * Spirit:
  * Unordered:
  * Xpressive:
- update to 1.41.0:
  New Libraries
  * Property Tree: A tree data structure especially suited to storing
    configuration data, from Marcin Kalicinski and Sebastian Redl.
  Updated Libraries (see README for details)
  * DateTime:
  * Filesystem:
  * Iostreams:
  * Math:
  * Multi-index Containers:
  * Proto:
  * Regex:
  * Spirit:
  * System:
  * Thread:
  * Unordered:
  * Utility:
  * Wave:
  * Xpressive:
- update to 1.40.0:
  Updated Libraries (see README for details)
  * Accumulators:
  * Asio:
  * Circular Buffer:
  * Foreach:
  * Function:
  * Fusion:
  * Graph:
  * Hash:
  * Interprocess:
  * Intrusive:
  * MPL:
  * Program.Options:
  * Property Map:
  * Proto:
  * Random:
  * Serialization:
  * Unordered:
  * Xpressive:
- removed patches no longer needed
* Wed Jan  6 2010 jengelh@medozas.de
- documentation change needed to be done in boost.spec.in
  (not boost.spec)
- openmpi change was missing too; add it now
* Tue Dec 15 2009 jengelh@medozas.de
- add baselibs for SPARC
- add baselibs.conf as a source
- deactivate use of openmpi on SPARC, as compat-dapl is not
  available
- package documentation as noarch
* Mon Oct 19 2009 pth@suse.de
- Provide/Obsolete boost-license (bnc#544958)
* Thu Aug  6 2009 pth@suse.de
- Add a fix from boost bugtracker that fixes the hash resizing
  (boost#54376)
- Add a test for cancelling deadline timers from the same changeset.
* Tue Aug  4 2009 pth@suse.de
- Readd the patch to fix the misplaced ifdef in
  template_function.hpp:move_assign.
* Tue Jul 28 2009 coolo@novell.com
- update to 1.39.0:
  New Libraries
  * Signals2: Managed signals & slots callback implementation (thread-safe version 2),
    from Frank Mori Hess.
  Updated Libraries (see README for details)
  * Asio:
  * Flyweight:
  * Foreach:
  * Hash:
  * Interprocess:
  * Intrusive:
  * Program.Options:
  * Proto:
  * PtrContainer:
  * Range:
  * Unordered:
  * Xpressive:
- removed patches no longer needed (hoping the best for ppc asm)
* Thu Apr 16 2009 crrodriguez@suse.de
- as agreed with maintainer, get rid of static libraries
* Thu Apr 16 2009 ro@suse.de
- buildfix: fix typo in specfile
* Mon Mar 16 2009 pth@suse.de
- Don't rely on system default mpi implementation being set. This
  fixes building boost on systems before openSUSE 11.0.
* Tue Mar  3 2009 pth@suse.de
- Fix misplaced ifdef in template_function.hpp:move_assign. Fixes
  building software that defines BOOST_NO_EXCEPTION (bnc#479659).
* Wed Feb 25 2009 pth@suse.de
- Fix packaging of the documentation.
* Sun Feb 22 2009 pth@suse.de
- Fix the line in the spec that copies the documentation.
* Fri Feb 20 2009 pth@suse.de
- Put the license in a versioned package. This allows installing
  libraries in parallel (bnc#477603).
* Fri Feb 13 2009 pth@suse.de
- Fix spec file (remove patches).
* Wed Feb 11 2009 pth@suse.de
- Add boost autoconf macros from the autoconf archive to the
  - devel package.
- Update to 1.38.0:
  New Libraries
  * Flyweight:
    o Design pattern to manage large quantities of highly redundant
    objects, from Joaquín M López Muñoz.
  * ScopeExit:
    o Execute arbitrary code at scope exit, from Alexander Nasonov.
  * Swap:
    o Enhanced generic swap function, from Joseph Gauterin.
  Updated Libraries
  * Accumulators:
    o Add rolling_sum, rolling_count and rolling_mean accumulators.
  * Any:
    o Use a by-value argument for operator= (#2311).
  * Asio:
    o Improved compatibility with some Windows firewall software.
    o Ensured arguments to windows::overlapped_ptr::complete() are
    correctly passed to the completion handler (#2614).
    o Drop back to using a pipe for notification if eventfd is not
    available at runtime on Linux (#2683).
    o Various minor bug and documentation fixes (#2534, #2541,
    [#2607], #2617, #2619)
  * Config:
    o Add new macros BOOST_NO_STD_UNORDERED and
    BOOST_NO_INITIALIZER_LISTS.
    o Added Codegear compiler support.
    o Added Dragonfly to the BSD family of configs.
    o Recognise latest compilers from MS and Intel.
  * Date_Time:
    o Added support for formatting and reading time durations longer
    than 24 hours with new formatter: %%0.
    o Removed the testfrmwk.hpp file from the public include directory.
    o Fixed several bugs and compile errors.
    o For full details see the change history
  * Exception:
    o Improved and more customizable diagnostic_information output.
  * Filesystem:
    o Fix native(name) test failures on POSIX-like systems.
    o Several bugfixes (#2543, #2224, #2531, #1840, #2542).
  * Graph:
    o Added a new algorithms for Travelling Salesman Problem
    approximation (metric_tsp_approx) and resource-constrained
    Shortest Paths (r_c_shortest_paths).
    o Support for named vertices in adjacency_list.
    o A number of bugfixes ( #416, #1622, #1700, #2209, #2392,
    [#2460], and #2550)
  * Hash:
    o boost/functional/detail/container_fwd.hpp has been moved to
    boost/detail/container_fwd.hpp.  The current location is
    deprecated.
    o For more detail, see the library changelog.
  * Interprocess:
    o Updated documentation to show rvalue-references functions
    instead of emulation functions.
    o More non-copyable classes are now movable.
    o Move-constructor and assignments now leave moved object in
    default-constructed state instead of just swapping contents.
    o Several bugfixes (#2391, #2431, #1390, #2570, #2528).
  * Intrusive:
    o New treap-based containers: treap, treap_set, treap_multiset.
    o Corrected compilation bug for Windows-based 64 bit compilers.
    o Corrected exception-safety bugs in container constructors.
    o Updated documentation to show rvalue-references functions
    instead of emulation functions.
  * Lexical Cast:
    o Changed to work without RTTI when BOOST_NO_TYPEID is defined
    (#1220).
  * Math:
    o Added Johan Råde's optimised floating point classification routines.
    o Fixed code so that it compiles in GCC's -pedantic mode (bug report #1451).
  * Multi-index Containers:
    o Some redundant type definitions have been deprecated. Consult the
    library release notes for further information.
  * Proto:
    o Fix problem with SFINAE of binary operators (Bug 2407).
    o Fix proto::call transform for callable transforms with >3 arguments.
    o result_of::value changed behavior for array-by-value terminals.
    o unpack_expr requires only Forward Sequences rather than Random Access
    Sequences.
    o Deprecate legacy undocumented BOOST_PROTO_DEFINE_(VARARG_)FUNCTION_TEMPLATE
    macros.
    o Add BOOST_PROTO_REPEAT and BOOST_PROTO_LOCAL_ITERATE macros to help with
    repetitive code generation
    o Support for nullary expressions with tag types other than
    proto::tag::terminal
    o Allow 0- and 1-argument variants of proto::or_ and proto::and_
  * Regex:
    o Breaking change: empty expressions, and empty alternatives are
    now allowed when using the Perl regular expression syntax.
    This change has been added for Perl compatibility, when the
    new syntax_option_type no_empty_expressions is set then the
    old behaviour is preserved and empty expressions are
    prohibited.  This is issue #1081.
    o Added support for Perl style ${n} expressions in format strings
    (issue #2556).
    o Added support for accessing the location of sub-expressions
    within the regular expression string (issue #2269).
    o Fixed compiler compatibility issues #2244, #2514, and #2458.
  * Thread:
    o No longer catches unhandled exceptions in threads as this debuggers
    couldn't identify the cause of unhandled exceptions in threads. An
    unhandled exception will still cause the application to terminate.
  * TR1:
    o Added support for the TR1 math functions and the unordered
    containers.
  * Type Traits:
    o Added support for Codegear intrinsics.
    o Minor tweaks to warning suppression and alignment_of code.
  * Unordered:
    o Use boost::swap.
    o Use a larger prime number list for selecting the number of buckets.
    o Use aligned storage to store the types.
    o Add support for C++0x initializer lists where they're available.
    o For more detail, see the library changelog.
  * Xpressive:
    o basic_regex gets nested syntax_option_flags and value_type typedef,
    for compatibility with std::basic_regex
    o Ported to Proto v4; Proto v2 at boost/xpressive/proto has been
    removed.
    o regex_error inherits from boost::exception
  Other Changes
  * Experimental support for building Boost with CMake has been introduced in
    this version. For more details see the wiki, Discussion is taking place
    on the Boost-cmake mailing list.
  * Fixed subversion properties for several files. Most notably, unix shell
    scripts should always have unix line endings, even in the windows
    packages.
* Fri Jan  9 2009 pth@suse.de
- Apply patch in boost.spec.in
* Thu Jan  8 2009 pth@suse.de
- Actually use the patch.
* Wed Jan  7 2009 pth@suse.de
- Initialize all data passed in the syscall to keep valgrind
  happy (bnc#461372).
* Thu Dec 11 2008 ro@suse.de
- fix baselibs.conf (no requirement for boost-xxbit)
  (bnc#457699)
* Thu Nov 27 2008 ro@suse.de
- update baselibs.conf
- package mpi.so only in mpi package, not in devel
* Wed Nov 19 2008 jjolly@suse.de
- Made the use of the mpi-selector conditional for mpi-enabled
  platforms.
* Tue Nov 11 2008 ro@suse.de
- SLE-11 uses PPC64 instead of PPC, adapt baselibs.conf
* Fri Oct 31 2008 pth@suse.de
- Fix the bug that made boost.monitor mix up uid and pib and
  also make boost.monitor not special-case SIGCLD (bnc#439805)
- Fix generation of default extension in boost.filesystem.
- Make boost recommend library subpackages instead of requiring
  them to allow removal of unwanted libraries after update.
- Run mkspec explicitely in a shell so that mkspec.sh doesn't
  need to be executable.
- Disable deletion of full-name symlinks in boost.spec.in.
- Make boost-devel directly require all library subpackages.
- boost.rpm isn't needed, even for updates, so don't build it and
  remove the README file needeed only for this package.
- Make debug package require all library subpackages.
- Add pre_checkin.sh to ensure that boost.spec is regenerated
  at check-in time.
- Make boost.build use sane library names. Only the multi-threaded
  libraries are built and these have no -mt in their name.
  Symlinks for convenience are spupplied.
- Use -fno-strict-aliasing only for boost.python, where it's needed.
- Don't use configure and make (only convenience wrappers) but
  call bjam directly.
* Mon Oct 27 2008 ro@suse.de
- do not remove full-name symlinks for shared libs
* Thu Oct 23 2008 pth@suse.de
- Use a script and a Makefile to generate boost.spec.
- Pull in all libraries on update.
- Modify README to apply to both openSUSE and SLE.
* Thu Oct 23 2008 ro@suse.de
- fix regexp for short symlinks
- hook all mpi related parts to build_mpi macro
- disable build_mpi on ia64 s390 s390x for the moment
* Fri Oct 17 2008 pth@suse.de
- Using a rpm macros in package name doesn't work with autobuild.
* Wed Oct 15 2008 pth@suse.de
- Fix naming of library packages to match the horribly broken
  sonames of the boost libraries.
- Add post/postun for all library packages.
- Stop rpmlint warning about explicit library dependencies
  needed to pull in all library subpackages during updates.
* Tue Oct 14 2008 pth@suse.de
- Fix build failure (README not in build directory).
* Tue Sep  2 2008 pth@suse.de
- Split off runtime libraries into their own packages.
- Update to 1.36.0:
  New Libraries
  * Accumulators: Framework for incremental calculation, and
    collection of statistical accumulators.
  * Exception: A library for transporting of arbitrary data in
    exception objects, and transporting of exceptions
    between threads.
  * Units: Zero-overhead dimensional analysis and unit/quantity
    manipulation and conversion.
  * Unordered: Unordered associative containers.
  Updated Libraries
  * Asio:
    o Added support for serial ports.
    o Added support for UNIX domain sockets.
    o Added support for raw sockets and ICMP.
    o Added wrappers for POSIX stream-oriented file descriptors
    (excluding regular files).
    o Added support for reactor-style operations using a new
    null_buffers type.
    o Added an iterator type for bytewise traversal of buffer
    sequences.
    o Added new read_until() and async_read_until() overloads that
    take a user-defined function object for locating message
    boundaries.
    o Added an experimental two-lock queue (enabled by defining
    BOOST_ASIO_ENABLE_TWO_LOCK_QUEUE) that may provide better
    io_service scalability across many processors.
    o Various fixes, performance improvements, and more complete
    coverage of the custom memory allocation support.
  * Assign:list_of() (and its variants) now has overloaded comparison
    operators. This allows you to write test code such as
    BOOST_CHECK_EQUAL(my_container,list_of(2)(3)(4)(5));.
  * Foreach:BOOST_FOREACH macro for easily iterating over the elements
    of a sequence.
    o New BOOST_REVERSE_FOREACH macro for iterating over a sequence
    in reverse.
  * Function:
    o Improved allocator support.
  * Hash: Minor updates and fixes, for more info see the change log.
  * Interprocess:
    o Added anonymous shared memory for UNIX systems.
    o Fixed missing move semantics on managed memory classes.
    o Added copy_on_write and open_read_only options for shared
    memory and mapped file managed classes.
    o shared_ptr is movable and supports aliasing.
  * Intrusive:
    o Added linear<> and cache_last<> options to singly linked lists.
    o Added optimize_multikey<> option to unordered container hooks.
    o Optimized unordered containers when store_hash option is used
    in the hook.
    o Implementation changed to avoid explicit use of try-catch
    blocks and be compilable with exceptions disabled.
  * Math:
    o Added new non-central Chi-Square, Beta, F and T distributions.
    o Added Exponential Integral and Zeta special functions.
    o Added Rounding, Truncation, and Unit-in-the-last-place
    functions.
    o Added support for compile time powers of a runtime base.
    o Added a few SSE2 based optimisations for the Lanczos
    approximations.
  * MPI:
    o Added support for non-blocking operations in Python
    o Added support for graph topologies.
  * Multi-index Containers: Minor additions and maintenance fixes.
    Consult the library release notes for
    further information.
  * PtrContainer: Support for a few more containers, and addition
    of insert iterators. For details see upgrading
    details.
  * Spirit: Integrated the "Classic" Spirit V1.8.x code base with
    Spirit V2, "The New Generation". See Change Log.
  * Thread:
    o New generic lock and try_lock functions for locking multiple
    mutexes at once.
    o Rvalue reference support for move semantics where the
    compilers supports it.
    o A few bugs fixed and missing functions added (including
    the serious win32 condition variable bug).
    o scoped_try_lock types are now backwards-compatible with
    Boost 1.34.0 and previous releases.
    o Support for passing function arguments to the thread
    function by supplying additional arguments to the thread
    constructor.
    o Backwards-compatibility overloads added for timed_lock and
    timed_wait functions to allow use of xtime for timeouts.
  * Wave:
    o Wave V2.0 is a new major release introducing some breaking
    API changes, preventing it to be used with Boost versions
    earlier than V1.36.0. Mainly, the API and hook interface
    have been streamlined for more consistency.
    o Fixed a couple of bugs, improved regression test system to
    include testing of the preporcessing hooks interface
    (for details see: Changelog).
  * Xpressive:
    o Regular expressions that can be written as strings or as
    expression templates, and that can refer to each other and
    themselves recursively with the power of context-free
    grammars.
    o skip() for specifying which parts of the input sequence
    to ignore when matching it against a regex.
    o regex_replace() accepts formatter objects and formatter
    expressions in addition to format strings.
    o Range-based regex_replace() algorithm.
    o Fix crash when semantic actions are placed in look-aheads,
    look-behinds or independent sub-expressions.
* Mon Jun 23 2008 pth@suse.de
- Qualify name to avoid clash (bnc#401964)
* Fri Jun 20 2008 schwab@suse.de
- Fix ppc atomic ops.
* Thu Apr 10 2008 ro@suse.de
- added baselibs.conf file to build xxbit packages
  for multilib support
* Mon Jan 28 2008 schwab@suse.de
- Remove obsolete patch again.
* Fri Jan 18 2008 pth@suse.de
- Fix CVE-2008-0171 and CVE-2008-0171 (bugzilla #353180)
- Qualify special_values_parser (bugzilla #353897)
* Thu Jan 17 2008 schwab@suse.de
- Remove obsolete patch.
* Mon Jan 14 2008 pth@suse.de
- Move 1.34.1 from BS to Autobuild
- Add patch for critical bug in Boost.Function.
- Include C headers where necessary.
- Make the tests for ULONG_MAX more readable 64.
* Wed Oct 24 2007 rguenther@suse.de
- Use -fpermissive in addition to -O2 for building.
- Add patch to enable building wave with GCC 4.3.
* Mon Aug 20 2007 pth@suse.de
- Only use fdupes from 10.3 onwards.
* Sat Aug 11 2007 aj@suse.de
- Fix spec file to build again.
* Thu Aug  9 2007 pth@suse.de
- Add man pages (made for 1.33.1).
- Package html documentation differently.
- Check all links and add missing files that do exist.
- Use %%%%fdupes
- Add patch by rschiele@gmail.com to pass compiler flags into
  Boost.build.
- Update to 1.34.1 and use .spec file from bkoz@redhat.com as
  a basis.
  Changes 1.33.1 -> 1.34.0:
  New Libraries:
  * Foreach Library: BOOST_FOREACH macro for easily iterating over
    the elements of a sequence,
  * Statechart Library: Arbitrarily complex finite state machines
    can be implemented in easily readable and
    maintainable C++ code,
  * TR1 Library: An implementation of the C++ Technical Report on Standard
    Library Extensions, from John Maddock. This library does
    not itself implement the TR1 components, rather it's a
    thin wrapper that will include your standard library's
    TR1 implementation (if it has one), otherwise it will
    include the Boost Library equivalents, and import them
    into namespace std::tr1. Highlights include: Reference
    Wrappers, Smart Pointers, result_of, Function Object
    Binders, Polymorphic function wrappers, Type Traits,
    Random Number Generators and Distributions, Tuples, Fixed
    Size Array, Hash Function Objects, Regular Expressions,
    and Complex Number Additional Algorithms.
  * Typeof Library: Typeof operator emulation, from Arkadiy Vertleyb
    and Peder Holt.
  * Xpressive Library: Regular expressions that can be written as strings
    or as expression templates, and that can refer to
    each other and themselves recursively with the
    power of context-free grammars, from Eric Niebler.
    Updated Libraries:
  * Assign Library:
    o Support for ptr_map<key,T> via the new function ptr_map_insert()
    o Support for initialization of Pointer Containers when the
    containers hold pointers to an abstract base class.
  * Date_time library:
    o Support for new US/Canada timezone rules and other bug fixes.
    See Change History for details.
  * Filesystem Library: Major upgrade in preparation for submission to the
    C++ Standards Committee for TR2. Changes include:
    o Internationalization, provided by class templates basic_path,
    basic_filesystem_error, basic_directory_iterator, and
    basic_directory_entry.
    o Simplification of the path interface by eliminating special
    constructors to identify native formats.
    o Rationalization of predicate function design, including the
    addition of several new functions.
    o Clearer specification by reference to POSIX, the ISO/IEEE Single
    Unix Standard, with provisions for Windows and other operating
    systems.
    o Preservation of existing user code whenever possible.
    o More efficient directory iteration.
    o Addition of a recursive directory iterator.
  * Function Library: Boost.Function now implements a small buffer
    optimization, which can drastically improve the
    performance when copying or constructing
    Boost.Function objects storing small function
    objects. For instance, bind(&X:foo, &x, _1, _2)
    requires no heap allocation when placed into a
    Boost.Function object.
  * Functional/Hash Library
    o Use declarations for standard classes, so that the library
    doesn't need to include all of their headers
    o Deprecated the <boost/functional/hash/*.hpp> headers.
    o Add support for the BOOST_HASH_NO_EXTENSIONS macro, which
    disables the extensions to TR1
    o Minor improvements to the hash functions for floating point numbers.
  * Graph Library:
    o edmonds_maximum_cardinality_matching,
    o lengauer_tarjan_dominator_tree,
    o compressed_sparse_row_graph,
    o sorted_erdos_renyi_iterator,
    o biconnected_components now supports a visitor and named
    parameters,
    o adjacency_matrix now models the Bidirectional Graph concept.
    o dijkstra_shortest_paths now calls vis.initialize_vertex for each
    vertex during initialization.
    o Note: the name of the compiled library for the GraphViz reader has
    changed to boost_graph (from bgl-viz) to match Boost conventions.
    o See the complete revision history for more information.
  * MultiArray Library: Boost.MultiArray now by default provides
    range-checking for operator[]. Range checking can
    be disabled by defining the macro
    BOOST_DISABLE_ASSERTS before including
    multi_array.hpp. A bug in multi_array::resize()
    related to storage orders was fixed.
  * Multi-index Containers Library:
    o New random access indices.
    o Non key-based indices feature new rearrange facilities.
    o This version also includes a number of optimizations and usage
    improvements. For a complete list of changes, see the library
    release notes.
  * Optional Library:
    o boost::none_t and boost::none now added to Optional's
    documentation
    o Relational operators now directly support arguments of type
    'T' and 'none_t'
    o operator->() now also works with reference types.
    o Helper functions make_optional(val), make_optional(cond,val)
    and get_optional_value_or(opt,alternative_value) added.
    o Constructor taking a boolean condition (as well as a value)
    added.
    o Member function get_value_or(alternative_value) added.
    o Incompatbility bug with mpl::apply<> fixed.
    o Converting assignment bug with uninitialized lvalues fixed.
  * Parameter Library:
    o Every ArgumentPack is now a valid MPL Forward Sequence.
    o Support for unnamed arguments (those whose keyword is
    deduced from their types) is added.
    o Support for named and unnamed template arguments is added.
    o New overload generation macros solve the forwarding problem
    directly.
    o See also the Python library changes, below.
  * Pointer Container Library:
    o Support for serialization via Boost.Serialization.
    o Exceptions can be disabled by defining the macro
    BOOST_PTR_CONTAINER_NO_EXCEPTIONS before including any header.
    This macro is defined by default if BOOST_NO_EXCEPTIONS is defined.
    o Additional std::auto_ptr<T> overloads added s.t. one can also
    pass std::auto_ptr<T> instead of only T* arguments to member
    functions.
    o transfer() now has weaker requirements s.t. one can transfer
    objects from ptr_container<Derived> to ptr_container<Base>,
  * Python Library:
    o Boost.Python now automatically appends C++ signatures to
    docstrings. The new docstring_options.hpp header is available to
    control the content of docstrings.
    o stl_input_iterator, for turning a Python iterable object into an
    STL input iterator, from Eric Niebler.
    o Support for void* conversions is added.
    o Integrated support for wrapping C++ functions built with the
    parameter library; keyword names are automatically known to
    docsstrings.
    o Enhancements to the API for better embedding support
    (boost::python::import(), boost::python::exec(), and
    boost::python::exec_file()).
  * Signals Library: More improvements to signal invocation performance.
  * Smart Pointers Library:
    o Allocator support as proposed in N1851 (162 Kb PDF).
    o pointer_cast and pointer_to_other utilities to allow
    pointer-independent code,
  * String Algorithm Library:
    o lexicographical_compare
    o join
    o New comparison predicates is_less, is_not_greater.
    o Negative indexes support (like Perl) in various algorihtms
    (*_head/tail, *_nth).
  * Wave Library:
    o Wave now correctly recognizes pp-number tokens as mandated by
    the C++ Standard, which are converted to C++ tokens right before
    they are returned from the library.
    o Several new preprocessing hooks have been added. For a complete
    description please refer to the related documentation page: The
    Context Policy.
    o Shared library (dll) support has been added for the generated
    Wave libraries.
    o The overall error handling has been improved. It is now possible
    to recover and continue after an error or a warning was issued.
    o Support for optional comment and/or full whitespace
    preservation in the generated output stream has been added.
    o The Wave library now performs automatic include guard
    detection to avoid accessing header files more than once, if
    appropriate.
    o Full interactive mode has been added to the Wave tool. Now the
    Wave tool can be used just like Python or Perl for instance to
    interactively try out your BOOST_PP macros. Additionally it is
    now possible to load and save the current state of an
    interactive session (macro tables et.al.).
    o The overall performance has been improved by upto 40-60%%,
    depending on the concrete files to process.
    o Support for new pragmas has been added allowing to control
    certain library features from inside the preprocessed sources
    (partial output redirection, control of generated whitespace
    and #line directives).
    o Optional support for #pragma message "..." has been added.
    o This version also includes a number of bug fixes and usage
    improvements. For a complete list of changes, see the
    libraries change log.
  Fixes in 1.34.1:
  * Fixes for build on IBM pSeries for AIX and Linux
  * gcc-4.2 atomicity.h location fixed
  * [iostreams] zlib_compressor memory leaks in 1.34.0
  * filtering ostream problem... pushing zlib_compressor works in 1_33,
    dies in 1_34
  * [doc] The "Getting Started" page mentions incorrect library names
  * [filesystem] missing documentation or bad links
  * add missing docs for boost.python API enhancements.
  * Entire iostreams library outdated in 1.34.0
  * numeric_limits specializations in limits.hpp are incorrect
  * Updated ICU support in Boost.Regex
  * Make boost.python compatible with python 2.5
  * ::boost::detail::empty_base improved
  * Fix failing uild of libs/python/example/quickstart.
  * Fix problems when building Python modules on boost 1.34.0
  * Patches to allow boost 1.34.0 to compile with stricter warning
    checking under mac OS and gcc
  * Unable to compile Python example, tutorial, or quickstart with
    Boost 1_34_0
  * Improper overflow handling in shortest paths algorithms
  * Multiple include paths for Python
  * Add documentation for the iter_find/split algorithms
  * regex_token_iterator crashes
  * regex_error exception when quantifying some non-capturing groups
  * read_write_mutex docs don't clearly specify that the functionality
    is not present
- Remove patches not needed anymore.
- Replace file dupes by symlinks.
- Add rpmlintrc to suppress rpmlint warnings for things that won't be
  changed.
* Sun Jul 15 2007 schwab@suse.de
- Fix reference to atomicity.h.
* Sat Mar 24 2007 aj@suse.de
- Add libbz2-devel to BuildRequires.
* Fri Sep 22 2006 pth@suse.de
- Apply patch from community to build with Python 2.5
* Fri Jul 14 2006 sf@suse.de
- fixed wrong usage of visit_each() (Bug #192116 )
* Thu Jul 13 2006 sf@suse.de
- fixed link creation to libboost_thread.so, using %%_lib instead
  of lib
* Mon Jun 19 2006 jw@suse.de
- added a libboost_thread.so as a symlink to libboost_thread-mt.so
* Tue Apr  4 2006 pth@suse.de
- Add libboost_wave.a to file list
* Tue Apr  4 2006 pth@suse.de
- Use explicit file names instead of wildcards to detect libraries
  that weren't built.
* Wed Feb  8 2006 schwab@suse.de
- Fix broken assembler constraints [#148429].
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Jan 18 2006 schwab@suse.de
- Don't strip binaries.
* Wed Dec  7 2005 pth@suse.de
- Fix cases of type-punning in boost::python
- Compile without -fno-strict-aliasing again.
- Remove unnecessary type attributes in forward declarations.
* Tue Dec  6 2005 pth@suse.de
- Update to 1.33.1.
- Fix use of uninitialized variable.
- Compile with -fno-strict-aliasing.
- Update NEWS file
* Thu Aug 25 2005 pth@suse.de
- Incorporate fixes that are bound to be in 1.33.1
- Build boost.regex with unicode support.
* Fri Aug 19 2005 pth@suse.de
- Add a NEWS file.
* Thu Aug 18 2005 pth@suse.de
- Update to 1.33.0 with 5 new libraries. See NEWS for specifics.
- Fix use of uninitialized class member (matz@suse.de)
- Compile with -O2 instead of -O3
- Make build process use %%optflags
* Thu Mar 10 2005 pth@suse.de
- Update to 1.32.0
* Fri May  7 2004 pth@suse.de
- Add convenience symlinks (#38491)
* Sun Apr 25 2004 coolo@suse.de
- build with several jobs
* Fri Mar  5 2004 pth@suse.de
- Update to 1.31.0.
- Make building boost work on Linux platforms where gcc does not
  define _REENTRANT when passed -pthread. Patch was done by
  Robert Schiele.
* Sat Jan 10 2004 adrian@suse.de
- add %%run_ldconfig
* Wed Aug 20 2003 pthomas@suse.de
- Update to 1.30.2, a bugfix release
* Wed Jul 23 2003 pthomas@suse.de
- Initial package, based on the work by Robert Schiele.
- Fix building with Python 2.3
