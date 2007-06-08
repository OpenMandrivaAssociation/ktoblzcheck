%define name ktoblzcheck
%define version 1.8
%define release %mkrel 2
%define major 1
%define libname %mklibname %name %major
Name: %{name}
Summary: A library to check account numbers and bank codes of German banks
Version: %{version}
Release: %{release}
Source: http://prdownloads.sourceforge.net/ktoblzcheck/%{name}-%{version}.tar.bz2
Patch: ktoblzcheck-1.8-gcc4.1.patch.bz2
Group: System/Libraries
License: LGPL
URL: http://ktoblzcheck.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: python-devel

%description 
KtoBLZCheck is a library to check account numbers and bank codes of
German banks. Both a library for other programs as well as a short
command-line tool is available. It is possible to check pairs of
account numbers and bank codes (BLZ) of German banks, and to map bank
codes (BLZ) to the clear-text name and location of the bank.

%package -n python-%name
Group: Development/Python
Summary:A library to check account numbers and bank codes of German banks
Requires: %name = %version

%description -n python-%name
KtoBLZCheck is a library to check account numbers and bank codes of
German banks. Both a library for other programs as well as a short
command-line tool is available. It is possible to check pairs of
account numbers and bank codes (BLZ) of German banks, and to map bank
codes (BLZ) to the clear-text name and location of the bank.


%package -n %libname
Group: System/Libraries
Summary:A library to check account numbers and bank codes of German banks
Requires: %name >= %version

%description -n %libname
KtoBLZCheck is a library to check account numbers and bank codes of
German banks. Both a library for other programs as well as a short
command-line tool is available. It is possible to check pairs of
account numbers and bank codes (BLZ) of German banks, and to map bank
codes (BLZ) to the clear-text name and location of the bank.

%package -n %libname-devel
Group: Development/C++
Summary:A library to check account numbers and bank codes of German banks
Requires: %libname = %version
Provides: lib%name-devel = %version-%release

%description -n %libname-devel
KtoBLZCheck is a library to check account numbers and bank codes of
German banks. Both a library for other programs as well as a short
command-line tool is available. It is possible to check pairs of
account numbers and bank codes (BLZ) of German banks, and to map bank
codes (BLZ) to the clear-text name and location of the bank.

%prep
%setup -q
%patch -p1

%build
%configure2_5x
%make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root,0755)
%{_libdir}/libktoblzcheck.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root,0755)
%{_libdir}/libktoblzcheck.so
%{_libdir}/libktoblzcheck.la
%{_includedir}/iban.h
%{_includedir}/ktoblzcheck.h
%{_libdir}/pkgconfig/ktoblzcheck.pc

%files -n python-%name
%defattr(-,root,root,0755)
%{py_sitedir}/*.py*

%files
%defattr(-,root,root,0755)
%doc README TODO COPYING ChangeLog
%{_bindir}/ktoblzcheck
%{_datadir}/ktoblzcheck/*
%{_mandir}/man1/ktoblzcheck.1*
