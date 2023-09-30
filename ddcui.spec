%define		qt_ver	5.5

Summary:	Graphical user interface for ddcutil
Name:		ddcui
Version:	0.4.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://github.com/rockowitz/ddcui/releases
Source0:	https://github.com/rockowitz/ddcui/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	09c18396b9610b0978b82b2897d85505
URL:		http://www.ddcutil.com/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Help-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.10
BuildRequires:	ddcutil-devel >= 2.0.0
BuildRequires:	glib2-devel >= 1:2.40
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	glib2 >= 1:2.40
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ddcui is a graphical user interface for ddcutil, implemented using Qt.

%prep
%setup -q

: > validate_CMAKE_BUILD_TYPE.cmake

%build
install -d build
cd build
%cmake .. \
	-DUSE_CCACHE:BOOL=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS {CHANGELOG,NEWS,README}.md
%attr(755,root,root) %{_bindir}/ddcui
%{_mandir}/man1/ddcui.1*
%{_desktopdir}/ddcui.desktop
%{_iconsdir}/hicolor/*/apps/ddcui.png
%{_datadir}/metainfo/ddcui.appdata.xml
