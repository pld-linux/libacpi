Summary:	a library for programs gathering ACPI data 
Summary(pl.UTF-8):	biblioteka dla programów pobierających dane ACPI
Name:		libacpi
Version:	0.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.ngolde.de/download/%{name}-%{version}.tar.gz
# Source0-md5:	49ecbeae66c3dc2588cd08328c6b759a
Patch0:		%{name}-Makefile.patch
URL:		http://www.ngolde.de/libacpi.html
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
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README doc/html/*
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.0
%{_includedir}/%{name}.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
