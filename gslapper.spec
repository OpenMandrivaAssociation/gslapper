Name:		gslapper
Version:	1.5.0
Release:        1
Summary:	A wallpaper utility that handles static images and videos
License:	GPL-3.0-only
URL:	https://github.com/Nomadcxx/gSlapper
Source0:	https://github.com/Nomadcxx/gSlapper/archive/refs/tags/v1.4.0.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-gl-1.0)
BuildRequires:	pkgconfig(gstreamer-video-1.0)
BuildRequires:	pkgconfig(wayland-protocols)

BuildSystem:	meson

Requires:	gstreamer1.0-libav
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-ugly

%description
gSlapper is a Wayland wallpaper utility that plays both videos and 
static images. Uses GStreamer instead of libmpv, which fixes 
memory leaks on NVIDIA systems

%install -a
## delete files related to wiki formatting
rm docs/index.md docs/README.md docs/*/index.md
rm -r docs/assets* docs/css

## install systemd service files
mkdir -p %{buildroot}%{_unitdir}/user
install -Dm644 *.service %{buildroot}%{_unitdir}/user/

%files
%license LICENSE
%doc docs README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-holder
%{_unitdir}/user/*.service
