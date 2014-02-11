%bcond_with    nonfree
%bcond_without x264
#bcond_without dirac
%bcond_without speex
%bcond_without v4l
%bcond_without openjpeg
%bcond_without libva
%bcond_without frei0r
%bcond_without opencv
%bcond_without libvpx

%lib_package avutil 52
%lib_package avcodec 54
%lib_package avformat 54
%lib_package avdevice 54
%lib_package avfilter 3
%lib_package swscale 2
%lib_package swresample 0
%lib_package postproc 52

Summary: Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Name: ffmpeg
Version: 2.0 
Release: 1%{?dist}
License: GPLv3
Group: System Environment/Libraries
Source: http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2
#Source: http://www.ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2
URL: http://ffmpeg.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: imlib2-devel, SDL-devel, freetype-devel, zlib-devel, bzip2-devel
BuildRequires: a52dec-devel
BuildRequires: libdc1394-devel, libraw1394-devel
# because pkg-config --libs dirac needs libstdc++
%{?with_dirac:BuildRequires: libstdc++-devel}
%{?with_nonfree:BuildRequires: faac-devel}
BuildRequires: faad2-devel
BuildRequires: gsm-devel
BuildRequires: lame-devel
BuildRequires: libnut-devel
BuildRequires: libtheora-devel, libvorbis-devel
BuildRequires: xvidcore-devel
%{?with_x264:BuildRequires: x264-devel}
%{?with_openjpeg:BuildRequires: openjpeg-devel}
%{?with_dirac:BuildRequires: dirac-devel, schroedinger-devel}
%{?with_speex:BuildRequires: speex-devel}
BuildRequires: opencore-amr-devel
BuildRequires: libvdpau-devel
BuildRequires: yasm
%{?with_libva:BuildRequires: libva-devel}
%{?with_frei0r:BuildRequires: frei0r-plugins-devel}
%{?with_opencv:BuildRequires: opencv-devel}
BuildRequires: rtmpdump-devel >= 2.2.f, openssl-devel
%{?with_libvpx:BuildRequires: libvpx-devel >= 0.9.6}
BuildRequires: xavs-devel

Obsoletes: ffmpeg-libs <= %{evr}
%lib_dependencies

%description
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.
The command line interface is designed to be intuitive, in the sense that
ffmpeg tries to figure out all the parameters, when possible. You have
usually to give only the target bitrate you want. FFmpeg can also convert
from any sample rate to any other, and resize video on the fly with a high
quality polyphase filter.

%devel_extra_Requires zlib-devel, libX11-devel, libXext-devel
%devel_extra_Requires a52dec-devel
%devel_extra_Requires libdc1394-devel, libraw1394-devel
%{?with_nonfree:%devel_extra_Requires faac-devel}
%devel_extra_Requires faad2-devel
%devel_extra_Requires gsm-devel
%devel_extra_Requires lame-devel
%devel_extra_Requires libvorbis-devel, libtheora-devel
%devel_extra_Requires xvidcore-devel
%{?with_x264:%devel_extra_Requires x264-devel}

%prep
%setup -q
test -f version.h || echo "#define FFMPEG_VERSION \"%{evr}\"" > version.h

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} \
            --shlibdir=%{_libdir} --mandir=%{_mandir} \
	--enable-shared \
	--enable-runtime-cpudetect \
	--enable-gpl \
	--enable-version3 \
	%{?with_nonfree:--enable-nonfree} \
	--enable-postproc \
	--enable-avfilter \
	--enable-pthreads \
	--enable-x11grab \
	--enable-vdpau \
	\
	--disable-avisynth \
	%{?with_frei0r:--enable-frei0r} \
	%{?with_opencv:--enable-libopencv} \
	--enable-libdc1394 \
	%{?with_dirac:--enable-libdirac} \
	%{?with_nonfree:--enable-libfaac} \
	--enable-libgsm \
	--enable-libmp3lame \
	--enable-libnut \
	--enable-libopencore-amrnb --enable-libopencore-amrwb \
	%{?with_openjpeg:--enable-libopenjpeg} \
	--enable-librtmp \
	%{?with_dirac:--enable-libschroedinger} \
	%{?with_speex:--enable-libspeex} \
	--enable-libtheora \
	--enable-libvorbis \
	%{?with_libvpx:--enable-libvpx} \
	%{?with_x264:--enable-libx264} \
	--enable-libxavs \
	--enable-libxvid \
%ifarch %ix86
	--extra-cflags="%{optflags}" \
%else
	--extra-cflags="%{optflags} -fPIC" \
%endif
	--disable-stripping \
	%{!?with_v4l:--disable-demuxer=v4l --disable-demuxer=v4l2 --disable-indev=v4l --disable-indev=v4l2} \

make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} incdir=%{buildroot}%{_includedir}/ffmpeg
#mkdir %{buildroot}%{_includedir}/postproc
#ln %{buildroot}%{_includedir}/ffmpeg/postprocess.h %{buildroot}%{_includedir}/postproc

# Remove from the included docs
rm -f doc/Makefile

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/lib64/libavcodec.so.55
/usr/lib64/libavcodec.so.55.18.102
/usr/lib64/libavdevice.so.55
/usr/lib64/libavdevice.so.55.3.100
/usr/lib64/libavformat.so.55
/usr/lib64/libavformat.so.55.12.100
%doc COPYING* CREDITS README doc/
%{_bindir}/*
#%{_libdir}/vhook
%{_datadir}/ffmpeg
%{_mandir}/man1/ff*.1*


%changelog
* Fri Jul 19 2013 Vicente Dominguez <vicente.dominguez@viewmetric.com> - 2.0-1
- Update to 2.0.

* Fri May 10 2013 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.1-59
- Update to 1.2.1.

* Fri May 10 2013 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.1.4-58
- Update to 1.1.4.

* Fri May 10 2013 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.0.6-57
- Update to 1.0.6.

* Fri May 10 2013 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.11.3-56
- Update to 0.11.3.

* Fri May 10 2013 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.10.7-55
- Update to 0.10.7.

* Mon Mar 19 2012 Paulo Roma <roma@lcg.ufrj.br> - 0.10.2-54
- Update to 0.10.2

* Fri Feb 10 2012 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.10-53
- Update to 0.10.

* Tue Jan  3 2012 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.9-52
- Update to 0.9.

* Tue Jan  3 2012 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.9-51
- Update to 0.8.9.

* Sat Nov 26 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.7-50
- Update to 0.8.7.

* Sat Nov 12 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.6-49
- Update to 0.8.6.

* Fri Sep 23 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.4-48
- Update to 0.8.4.

* Mon Jul 25 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8-47
- Update to 0.8.

* Mon Jul 25 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.7.1-46
- Update to 0.7.1.

* Thu Jun  2 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6.3-43
- Update to 0.6.3.

* Fri Mar 25 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6.1-42_git20110322
- Update to latest git master.

* Mon Mar 14 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6.1-39_git20110314
- Update to latest git master.

* Sat Jan 15 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6.1-38_git20110115
- Update to latest git master.

* Sun Oct 24 2010 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6-37_git20101024
- Update to latest git master.

* Thu Jul 22 2010 Paulo Roma <roma@lcg.ufrj.br> - 0.6-35
- Added BR libva-devel.

* Tue Jul 20 2010 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6-34
- Update to 0.6.

* Sun Apr  4 2010 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.5-32_git20100404
- Update to latest git.

* Fri Nov 20 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.5-31_git20091120
- Update to latest git.

* Sun Jan 18 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9-29_r16671
- Update to latest svn version.

* Sun Nov 16 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9-28_r15845
- ffmpeg-libs from a 3rd party repo generates conflicts.

* Sun Nov  9 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9-27_r15797
- Update to latest svn version.

* Mon Feb 18 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9-26_r12135
- Update to latest svn version.

* Sat Jan 12 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9-25_r11517
- Update to latest svn version.
- libdca nd libogg are not (directly) needed anymore.

* Sat Oct 27 2007 Paulo Roma <roma@lcg.ufrj.br> - 0.4.9-24_r8743
- Compiling with --enable-liba52 for vob->avi using AC3.
- Added --enable-libaad.
- Added libnut-devel as a conditional BuildRequires.
- Using libdc1394-1.2.2, because version 2 does not work.

* Mon Apr 23 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9-23_r8743
- Add some more dependencies (#1172).

* Sun Apr 22 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9-21_r8743
- Add some dependencies on the devel package (#1172).

* Sun Apr 15 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9-20_r8742
- Update to latest svn version.

* Wed Jan  3 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9_19_r7407
- Update to latest svn version.

* Fri Oct 27 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9-18_r6524
- Add faac support.

* Mon Oct  2 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9-17_r6524
- Update to latest svn version.
- Fix revision in release tag.

* Wed Sep  6 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.4.9-15_r19707
- Update to latest svn version.

* Wed Mar  1 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs20060301.
- Fix bug #752.

* Mon Feb 27 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Move compatibility provides to devel package (bug #750).

* Wed Feb 15 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs20060215.

* Sun Jun 12 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs20050612.

* Tue May 17 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs 20050517.

* Mon Apr 18 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs 20050418.

* Tue Nov 23 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.4.9-pre1.

* Thu Oct 16 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.4.8.

* Tue Jul  1 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to a CVS snapshot as videolan-client 0.6.0 needs it.
- Enable faad, imlib2 and SDL support.
- Disable mmx until it doesn't make the build fail anymore :-/

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.
- Hardcode provides in order to get it right :-/

* Tue Feb 25 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Moved libavcodec.so to the main package to fix dependency problems.

* Wed Feb 19 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Major spec file updates, based on a very nice Mandrake spec.
- Revert to the 0.4.6 release as CVS snapshots don't build.

* Tue Feb  4 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.

