%global bmdsdk_path /tmp/Blackmagic_DeckLink_SDK_10.1.1
# you need to unzip Blackmagic_DeckLink_SDK_10.1.1.zip Blackmagic_DeckLink_SDK_10.1.1 dir name in /tmp


Name:           bmdtools-n3
Version:        0.0.3
Release:        1%{?dist}
Summary:        Basic capture and play programs for Blackmagic Design Decklink

Group:          Applications/Multimedia
License:        GPL
URL:            https://github.com/lu-zero/bmdtools
Source0:        %{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildRequires:  desktopvideo >= 10.1.1  
BuildRequires:  ffmpeg-devel make

Requires: ffmpeg mesa-libGL libvdpau desktopvideo >= 10.1.1

%description
Capture and play applications for Blackmagic Design DeckLink cards running under Linux
From: luca.barbato@luminem.it (commit 19a2d131a6)

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}

make %{?_smp_mflags} VERBOSE=1 SDK_PATH="%{bmdsdk_path}/Linux/include"
make -C %{bmdsdk_path}/Linux/Samples/DeviceList/

install -m 755 %{_builddir}/%{name}-%{version}/bmdcapture %{buildroot}%{_bindir}/
install -m 755 %{_builddir}/%{name}-%{version}/bmdgenlock %{buildroot}%{_bindir}/
install -m 755 %{_builddir}/%{name}-%{version}/bmdplay %{buildroot}%{_bindir}/
install -m 755 %{bmdsdk_path}/Linux/Samples/DeviceList/DeviceList %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%{_bindir}/bmdcapture
%{_bindir}/bmdgenlock
%{_bindir}/bmdplay
%{_bindir}/DeviceList

%post 

%postun 

%changelog
* Tue Dec 20 2015 Vicente Dominguez <vicente.dominguez@enetres.net> - 0.0.3
- last commit a122199f0cb10249256f4008a4e0d6a87d82d6c1
* Fri Aug 08 2014 Vicente Dominguez <vicente.dominguez@viewmetric.com> - 0.0.2
- DeviceList tool added
* Fri Jul 25 2014 Vicente Dominguez <vicente.dominguez@viewmetric.com> - 0.0.1
- initial package

