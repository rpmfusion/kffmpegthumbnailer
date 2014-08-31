Name:           kffmpegthumbnailer
Version:        1.1.0
Release:        8%{?dist}
Summary:        A video thumbnailer for kde based on ffmpegthumbnailer

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://code.google.com/p/ffmpegthumbnailer/
Source0:        http://ffmpegthumbnailer.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ffmpegthumbnailer-devel, kdelibs-devel
Requires:       kdebase-workspace


%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }

%description
This video thumbnailer can be used to create thumbnails for your video files. 
The thumbnailer uses ffmpeg to decode frames from the video files.


%prep
%setup -q
chmod -x INSTALL

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf $RPM_BUILD_ROOT
make install/fast DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYRIGHT README Changelog
%{_kde4_datadir}/kde4/services/kffmpegthumbnailer.desktop
%{_kde4_libdir}/kde4/kffmpegthumbnailer.so

%changelog
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
