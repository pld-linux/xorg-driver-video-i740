Summary:	X.org video driver for Intel i740 video adapters
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Intel i740
Name:		xorg-driver-video-i740
Version:	1.0.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-i740-%{version}.tar.bz2
# Source0-md5:	eb88ec9afb3c1b84a7bda762ea32bc6c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for video adapters based on Intel i740 chip.

%description -l pl
Sterownik obrazu X.org dla kart graficznych opartych na uk³adzie Intel
i740.

%prep
%setup -q -n xf86-video-i740-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/i740_drv.so
%{_mandir}/man4/i740.4x*
