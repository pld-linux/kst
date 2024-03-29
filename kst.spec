Summary:	A data viewing program for KDE
Summary(pl.UTF-8):	Program do przeglądania danych pod KDE
Name:		kst
Version:	1.3.1
Release:	0.1
License:	GPL
Group:		Applications/Math
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/scientific/%{name}-%{version}.tar.gz
# Source0-md5:	b18013223dc4cc2d1d0c8c4197bf8f97
URL:		http://kst.kde.org
BuildRequires:	cfitsio-devel
BuildRequires:	gsl-devel
BuildRequires:	kdelibs-devel >= 9:3.1
BuildRequires:	netcdf-devel
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kst is a real-time data viewing and plotting tool with basic data
analysis functionality.

%description -l pl.UTF-8
Kst to narzędzie do przeglądania danych i rysowania wykresów w czasie
rzeczywistym z podstawowymi funkcjami analizy danych.

%package devel
Summary:	kst header files
Summary(pl.UTF-8):	Pliki nagłówkowe do kst
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel >= 9:3.1

%description devel
kst files for developing applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne przy tworzeniu innych aplikacji.

%prep
%setup -q

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir

%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appsdir=%{_desktopdir}/kde

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{_datadir}/apps/kst/tutorial .

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README tutorial
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%dir %{_libdir}/kde3/kstplugins
%attr(755,root,root) %{_libdir}/kde3/kstplugins/*.so
%{_libdir}/kde3/kstplugins/*.la
%{_libdir}/kde3/kstplugins/*.xml
%{_datadir}/apps/kconf_update/*
%{_datadir}/apps/kst
%{_datadir}/config/colors/*
%{_datadir}/mimelnk/application/*
%{_datadir}/services/kst
%{_datadir}/servicetypes/kst
%{_desktopdir}/kde/*
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/kstwidgets.so
%{_libdir}/kde3/plugins/designer/kstwidgets.la
%{_includedir}/*
