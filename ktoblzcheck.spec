%define name ktoblzcheck
%define version 1.28
%define release %mkrel 1
%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d %name
Name: %{name}
Summary: A library to check account numbers and bank codes of German banks
Version: %{version}
Release: %{release}
Source: http://prdownloads.sourceforge.net/ktoblzcheck/%{name}-%{version}.tar.gz
Group: System/Libraries
License: LGPLv2+
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
%py_requires -d

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

%package -n %develname
Group: Development/C++
Summary:A library to check account numbers and bank codes of German banks
Requires: %libname = %version
Provides: lib%name-devel = %version-%release
Obsoletes: %mklibname -d %name 1

%description -n %develname
KtoBLZCheck is a library to check account numbers and bank codes of
German banks. Both a library for other programs as well as a short
command-line tool is available. It is possible to check pairs of
account numbers and bank codes (BLZ) of German banks, and to map bank
codes (BLZ) to the clear-text name and location of the bank.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root,0755)
%{_libdir}/libktoblzcheck.so.%{major}*

%files -n %develname
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
