Summary:	A data viewing program for KDE
Summary(pl):	Program do przegl±dania danych pod KDE
Name:		kst
Version:	1.1.0
Release:	0.1
License:	GPL
Group:		Applications/Math
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/scientific/%{name}-%{version}.tar.gz
# Source0-md5:	bfd6e196850a8883b9c12553d9c7a910
URL:		http://kst.kde.org
BuildRequires:	kdelibs-devel
BuildRequires:	netcdf-devel
BuildRequires:	gsl-devel
BuildRequires:	cfitsio-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kst is a real-time data viewing and plotting tool with basic data
analysis functionality.

%prep
%setup -q

%build

kde_appsdir="%{_desktopdir}/kde"; export kde_appsdir
kde_htmldir="%{_kdedocdir}"; export kde_htmldir

%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_desktopdir}/kde/Applications/Sciences/* $RPM_BUILD_ROOT%{_desktopdir}/kde/
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{_datadir}/apps/kst/tutorial ./

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README 
%doc tutorial
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%dir %{_libdir}/kde3/kstplugins
%attr(755,root,root) %{_libdir}/kde3/kstplugins/*.so
%{_libdir}/kde3/kstplugins/*.xml
%{_libdir}/kde3/kstplugins/*.la
%{_desktopdir}/kde/*
%{_datadir}/apps/kconf_update/*
%{_datadir}/apps/kst
%{_datadir}/config/colors/*
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/*
%{_datadir}/mimelnk/application/*
%{_datadir}/services/kst
%{_datadir}/servicetypes/kst

#This is probably need for plugin development. Move to devel subpackage
%{_includedir}/*
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
