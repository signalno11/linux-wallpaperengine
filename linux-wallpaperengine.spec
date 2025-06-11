Name: linux-wallpaperengine
Version: 0.0.0
Release: 0%{?dist}
License: GPLv3
Summary: Wallpaper engine on Linux
Url: https://github.com/Almamu/linux-wallpaperengine
Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: git
BuildRequires: glm-devel
BuildRequires: SDL2-devel

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
cmake -B build -S "%{_sourcedir}/%{name}-%{version}" -DCMAKE_BUILD_TYPE='Release' -DCMAKE_INSTALL_PREFIX="/usr/bin/%{name}" -DCMAKE_CXX_FLAGS="-ffat-lto-objects -Wno-builtin-macro-redefined" -DCMAKE_C_FLAGS="-Wno-builtin-macro-redefined"
cmake --build build

%install
DESTDIR="%{buildroot}" cmake --install build

#-- FILES ---------------------------------------------------------------------#
%files
%license LICENSE
%{_bindir}/linux-wallpaperengine

#-- CHANGELOG -----------------------------------------------------------------#
%changelog



