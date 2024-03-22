#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.02.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		akonadi-calendar-tools
Summary:	Akonadi Calendar Tools
Name:		ka6-%{kaname}
Version:	24.02.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d4947700f98c6eb4738b4af344a01524
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka6-calendarsupport-devel >= %{kdeappsver}
BuildRequires:	ka6-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka6-libkdepim-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Console applications and utilities for managing calendars in Akonadi.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/calendarjanitor
%attr(755,root,root) %{_bindir}/konsolekalendar
%{_desktopdir}/konsolekalendar.desktop
%{_iconsdir}/hicolor/128x128/apps/konsolekalendar.png
%{_iconsdir}/hicolor/16x16/apps/konsolekalendar.png
%{_iconsdir}/hicolor/22x22/apps/konsolekalendar.png
%{_iconsdir}/hicolor/32x32/apps/konsolekalendar.png
%{_iconsdir}/hicolor/48x48/apps/konsolekalendar.png
%{_datadir}/qlogging-categories6/console.categories
%{_datadir}/qlogging-categories6/console.renamecategories
