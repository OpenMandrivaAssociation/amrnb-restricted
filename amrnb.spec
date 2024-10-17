%define major 3
%define libname %mklibname amrnb %{major}
%define develname %mklibname -d amrnb
%define distsuffix plf

Name:		amrnb
Version:	7.0.0.2
Release:	%mkrel 3
Summary:	AMR NarrowBand speech codec
License:	Distributable
Group:		System/Libraries
URL:		https://www.penguin.cz/~utx/amr
Source:		http://ftp.penguin.cz/pub/users/utx/amr/amrnb-%{version}.tar.bz2
Source1:	http://www.3gpp.org/ftp/Specs/archive/26_series/26.104/26104-700.zip

%description
AMR-NB is a narrowband speech codec used in mobile phones.

This package is in restricted as it may violate some patents.

%package -n %{libname}
Summary:	AMR NarrowBand speech codec development files
Group:		System/Libraries

%description -n %{libname}
AMR-NB is a narrowband speech codec used in mobile phones development files.

%package -n %{develname}
Summary:	AMR NarrowBand speech codec development files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
AMR-NB is a narrowband speech codec used in mobile phones development files.

%prep
%setup -q
cp %{SOURCE1} .

%build
%configure2_5x --enable-static
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README AUTHORS TODO COPYING
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root,0755)
%{_libdir}/libamrnb.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,0755)
%{_includedir}/amrnb/
%{_libdir}/libamrnb.a
%{_libdir}/libamrnb.la
%{_libdir}/libamrnb.so

%changelog
* Fri Aug 19 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 7.0.0.2-3plf2011.0
- Port from PLF to restricted
- Little spec clean up

* Mon Nov 29 2010 Götz Waschk <goetz@zarb.org> 7.0.0.2-2plf2011.0
- fix file list

* Thu Jun 26 2008 Götz Waschk <goetz@zarb.org> 7.0.0.2-1plf2009.0
- new version

* Fri Apr 25 2008 Götz Waschk <goetz@zarb.org> 7.0.0.1-1plf2009.0
- new version

* Thu Jan 17 2008 Götz Waschk <goetz@zarb.org> 7.0.0.0-1plf2008.1
- new major
- new devel name
- new version

* Tue May 29 2007 Götz Waschk <goetz@zarb.org> 6.1.0.3-1plf2008.0
- new version

* Thu Mar 22 2007 Götz Waschk <goetz@zarb.org> 6.1.0-1plf2007.1
- add conflict with old devel package
- major 2
- don't download 3GPP reference code at build time, include it in the srpm
- new version from a new maintainer

* Fri Dec  8 2006 Götz Waschk <goetz@zarb.org> 0.0.1-1plf2007.1
- initial package
