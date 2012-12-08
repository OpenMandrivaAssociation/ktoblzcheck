%define name ktoblzcheck
%define version 1.39
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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

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
%{_includedir}/iban.h
%{_includedir}/ktoblzcheck.h
%{_libdir}/pkgconfig/ktoblzcheck.pc

%files -n python-%name
%defattr(-,root,root,0755)
%{py_sitedir}/*.py*

%files
%defattr(-,root,root,0755)
%doc README COPYING ChangeLog
%{_bindir}/ktoblzcheck
%{_datadir}/ktoblzcheck/*
%{_mandir}/man1/ktoblzcheck.1*


%changelog
* Tue Jun 14 2011 Funda Wang <fwang@mandriva.org> 1.33-1mdv2011.0
+ Revision: 685114
- new version 1.33

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.31-2
+ Revision: 666055
- mass rebuild

* Tue Mar 01 2011 Götz Waschk <waschk@mandriva.org> 1.31-1
+ Revision: 641100
- new version

* Sat Feb 05 2011 Götz Waschk <waschk@mandriva.org> 1.28-1
+ Revision: 636198
- update to new version 1.28

* Mon Nov 01 2010 Götz Waschk <waschk@mandriva.org> 1.24-2mdv2011.0
+ Revision: 591586
- rebuild for new python 2.7

* Sun Jan 31 2010 Götz Waschk <waschk@mandriva.org> 1.24-1mdv2010.1
+ Revision: 498734
- update to new version 1.24

* Sat Jun 20 2009 Götz Waschk <waschk@mandriva.org> 1.22-1mdv2010.0
+ Revision: 387517
- update to new version 1.22

* Mon Feb 09 2009 Götz Waschk <waschk@mandriva.org> 1.21-1mdv2009.1
+ Revision: 338967
- update to new version 1.21

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 1.20-2mdv2009.1
+ Revision: 319424
- rebuild for new python

* Fri Nov 14 2008 Götz Waschk <waschk@mandriva.org> 1.20-1mdv2009.1
+ Revision: 303115
- update to new version 1.20

* Tue Aug 12 2008 Götz Waschk <waschk@mandriva.org> 1.19-1mdv2009.0
+ Revision: 271238
- new version
- update license

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.18-2mdv2009.0
+ Revision: 264768
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 18 2008 Götz Waschk <waschk@mandriva.org> 1.18-1mdv2009.0
+ Revision: 208784
- new version

* Sat Mar 01 2008 Götz Waschk <waschk@mandriva.org> 1.17-1mdv2008.1
+ Revision: 177442
- new version

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 1.16-1mdv2008.1
+ Revision: 174607
- new version

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.15-2mdv2008.1
+ Revision: 150434
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 05 2007 Götz Waschk <waschk@mandriva.org> 1.15-1mdv2008.0
+ Revision: 79987
- new version
- drop patch
- new devel name

* Fri Jun 08 2007 Götz Waschk <waschk@mandriva.org> 1.8-2mdv2008.0
+ Revision: 37223
- Import ktoblzcheck



* Wed Jun  7 2006 Götz Waschk <waschk@mandriva.org> 1.8-2mdv2007.0
- fix build

* Tue Dec  6 2005 Götz Waschk <waschk@mandriva.org> 1.8-1mdk
- initial package
