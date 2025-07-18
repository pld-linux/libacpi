Summary:	A library for programs gathering ACPI data 
Summary(pl.UTF-8):	Biblioteka dla programów pobierających dane ACPI
Name:		libacpi
Version:	0.2
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://www.ngolde.de/download/%{name}-%{version}.tar.gz
# Source0-md5:	05b53dd7bead66dda35fec502b91066c
Patch0:		%{name}-Makefile.patch
URL:		http://www.ngolde.de/libacpi.html
ExclusiveArch:	%{ix86} %{x8664} x32 ia64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libacpi is a library for programs gathering ACPI data.

%description -l pl.UTF-8
libacpi jest biblioteką dla programów pobierających dane ACPI.

%package devel
Summary:	Header files for libacpi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libacpi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libacpi library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libacpi.

%package static
Summary:	Static libacpi library
Summary(pl.UTF-8):	Statyczna biblioteka libacpi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libacpi library.

%description static -l pl.UTF-8
Statyczna biblioteka libacpi.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README doc/html/*
%attr(755,root,root) %{_bindir}/test-libacpi
%attr(755,root,root) %{_libdir}/libacpi.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libacpi.so
%{_includedir}/libacpi.h
%{_mandir}/man3/libacpi.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libacpi.a
