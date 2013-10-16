%define major	1
%define libname	%mklibname %{name} %major
%define devname	%mklibname -d %{name}

Summary:	A library to check account numbers and bank codes of German banks
Name:		ktoblzcheck
Version:	1.43
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://ktoblzcheck.sourceforge.net
Source0:	https://sourceforge.net/projects/ktoblzcheck/files/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)

%description 
KtoBLZCheck is a library to check account numbers and bank codes of
German banks. Both a library for other programs as well as a short
command-line tool is available. It is possible to check pairs of
account numbers and bank codes (BLZ) of German banks, and to map bank
codes (BLZ) to the clear-text name and location of the bank.

%package -n python-%{name}
Group:		Development/Python
Summary:	A library to check account numbers and bank codes of German banks
Requires:	%{name} = %{version}

%description -n python-%{name}
KtoBLZCheck is a library to check account numbers and bank codes of
German banks. Both a library for other programs as well as a short
command-line tool is available. It is possible to check pairs of
account numbers and bank codes (BLZ) of German banks, and to map bank
codes (BLZ) to the clear-text name and location of the bank.

%package -n %{libname}
Group:		System/Libraries
Summary:	A library to check account numbers and bank codes of German banks
Suggests:	%{name} >= %{version}

%description -n %{libname}
KtoBLZCheck is a library to check account numbers and bank codes of
German banks. Both a library for other programs as well as a short
command-line tool is available. It is possible to check pairs of
account numbers and bank codes (BLZ) of German banks, and to map bank
codes (BLZ) to the clear-text name and location of the bank.

%package -n %{devname}
Group:		Development/C++
Summary:	A library to check account numbers and bank codes of German banks
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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
%makeinstall_std

%files
%doc README COPYING ChangeLog
%{_bindir}/ktoblzcheck
%{_datadir}/ktoblzcheck/*
%{_mandir}/man1/ktoblzcheck.1*

%files -n %{libname}
%{_libdir}/libktoblzcheck.so.%{major}*

%files -n %{devname}
%{_libdir}/libktoblzcheck.so
%{_includedir}/iban.h
%{_includedir}/ktoblzcheck.h
%{_libdir}/pkgconfig/ktoblzcheck.pc

%files -n python-%{name}
%{py_puresitedir}/*.py*


