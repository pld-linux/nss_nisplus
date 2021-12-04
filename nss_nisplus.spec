Summary:	NIS+ NSS glibc module (DEPRECATED)
Summary(es.UTF-8):	Módulo NIS+ NSS de glibc
Summary(pl.UTF-8):	Moduł glibc NSS NIS+ (PRZESTARZAŁY)
Name:		nss_nisplus
Version:	1.3
Release:	1
Epoch:		7
License:	LGPL v2.1+
Group:		Base
#Source0Download: https://github.com/thkukuk/libnss_nisplus/releases
Source0:	https://github.com/thkukuk/libnss_nisplus/archive/libnss_nisplus-%{version}.tar.gz
# Source0-md5:	8e86cde0cb0abcd1387fd24aa8421698
Patch0:		%{name}-update.patch
URL:		https://github.com/thkukuk/libnss_nisplus
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	libnsl-devel < 2
BuildRequires:	libtirpc-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
glibc NSS (Name Service Switch) module for NIS+ databases access.

This code was formerly part of glibc, but is now standalone to be able
to link against TI-RPC for IPv6 support.

Note: the NIS+ stuff is deprecated and shouldn't be used anymore.

%description -l es.UTF-8
Módulo NSS de glibc para acceder las bases de datos NIS+.

%description -l pl.UTF-8
Moduł glibc NSS (Name Service Switch) dostępu do baz danych NIS+.

Ten kod wcześniej był częścią glibc, ale został wydzielony, aby mógł
używać TI-RPC w celu obsługi IPv6.

Uwaga: kod NIS+ jest przestarzały i nie powinien być już używany.

%prep
%setup -q -n libnss_nisplus-libnss_nisplus-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--libdir=/%{_lib} \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT/%{_lib}/libnss_nisplus.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) /%{_lib}/libnss_nisplus.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libnss_nisplus.so.2
