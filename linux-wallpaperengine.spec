Name: linux-wallpaperengine
Version: 0.0.1
Release: 1%{?dist}
License: GPLv3
Summary: Wallpaper engine on Linux
Url: https://github.com/Almamu/linux-wallpaperengine
Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: git
BuildRequires: glm-devel
BuildRequires: SDL2-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: wayland-devel
BuildRequires: libX11-devel
BuildRequires: glew-devel
BuildRequires: freeglut-devel
BuildRequires: zlib-ng-compat-devel
BuildRequires: mpv-devel
BuildRequires: lz4-devel

Requires: ffmpeg
Requires: freeglut
Requires: glew
Requires: glfw
Requires: pulseaudio-libs
Requires: lz4
Requires: mpv

%description
Bring Wallpaper Engine-style live wallpapers to Linux! This project allows you to run animated wallpapers from Steam’s Wallpaper Engine right on your desktop.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
ls
ls "%{_sourcedir}"
mkdir build
cd build
cmake ..
make

%install
DESTDIR="%{buildroot}" cmake --install build

#-- FILES ---------------------------------------------------------------------#
%files
%license LICENSE
%{_bindir}/linux-wallpaperengine

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Wed Jun 11 2025 Moon 0.0.1-1
- new package built with tito




