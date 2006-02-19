Summary:	A data viewing program for KDE
Summary(pl):	Program do przegl±dania danych pod KDE
Name:		kst
Version:	1.2.0
Release:	0.1
License:	GPL
Group:		Applications/Math
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/scientific/%{name}-%{version}.tar.gz
# Source0-md5:	789aac131edb24cdefbb90634cbb4b56
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

%description -l pl
Kst to narzêdzie do przegl±dania danych i rysowania wykresów w czasie
rzeczywistym z podstawowymi funkcjami analizy danych.

%package devel
Summary:	kst header files
Summary(pl):	Pliki nag³ówkowe do kst
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel >= 9:3.1

%description devel
kst files for developing applications.

%description devel -l pl
Pliki nag³ówkowe potrzebne przy tworzeniu innych aplikacji.

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
