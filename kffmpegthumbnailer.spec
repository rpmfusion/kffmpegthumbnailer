%undefine __cmake_in_source_build
%global ff_version 2.2.2

Name:           kffmpegthumbnailer
Version:        1.1.0
Release:        20%{?dist}
Summary:        A video thumbnailer for kde based on ffmpegthumbnailer

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/dirkvdb/ffmpegthumbnailer
Source0:        %{url}/archive/%{ff_version}/ffmpegthumbnailer-%{ff_version}.tar.gz

BuildRequires:  ffmpegthumbnailer-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  kdelibs-devel


%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }

%description
This video thumbnailer can be used to create thumbnails for your video files. 
The thumbnailer uses ffmpeg to decode frames from the video files.


%prep
%autosetup -p1 -n ffmpegthumbnailer-%{ff_version}
chmod -x INSTALL

%build
cd %{name}
%{cmake_kde4} \
 -Wno-dev \
 -B %{_vpath_builddir} \
 -S .
%cmake_build


%install
cd %{name}
%cmake_install


%files
%doc kffmpegthumbnailer/README kffmpegthumbnailer/Changelog
%license kffmpegthumbnailer/COPYRIGHT
%{_kde4_datadir}/kde4/services/kffmpegthumbnailer.desktop
%{_kde4_libdir}/kde4/kffmpegthumbnailer.so

%changelog
* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Leigh Scott <leigh123linux@gmail.com> - 1.1.0-19
- Switch to maintained source

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 03 2016 Sérgio Basto <sergio@serjux.com> - 1.1.0-10
- Fix build on F23
- Add license tag
- Spec quick clean up

* Tue Aug 02 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-9
- remove requires kdebase-workspace (rfbz 3719)

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-7
- Mass rebuilt for Fedora 19 Features

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-6
- Rebuilt for c++ ABI breakage

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 29 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 1.1.0-4
- add BuildRequires kdelibs-devel
- remove BuildREquires qt-devel

* Mon Apr 26 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 1.1.0-3
- add requires qt-devel

* Mon Apr 12 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 1.1.0-2
- requires kdebase-workspace
- remove INSTALL from doc
- license change to GPLv2+

* Sun Apr 11 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 1.1.0-1
- initial build
