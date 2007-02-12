Summary:	Tcl Blend - Java access for Tcl system
Summary(pl.UTF-8):	Tcl Blend - dostęp do Javy w systemie Tcl
Name:		tclBlend
Version:	1.4.0
Release:	0.1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcljava/%{name}%{version}.tar.gz
# Source0-md5:	c88f84fb6a72af4c951648295f0e02f0
URL:		http://www.tcl.tk/software/java/
BuildRequires:	autoconf >= 2.50
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	sed >= 4.0
BuildRequires:	tcl-devel >= 8.0
BuildRequires:	tcl-thread
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
Tcl Blend provides two new capabilities to the Tcl system. First, Tcl
Blend provides Java classes that expose key pieces of the interfaces
that are available to extension writers who currently use C. Using
these classes, extension writers can create new commands for the Tcl
interpreter. In addition, Tcl Blend provides commands that allow
script writers to directly manipulate Java objects without having to
write any Java code. The reflection classes in Java make it possible
to invoke methods and access fields on arbitrary objects. Tcl Blend
takes advantage of these capabilities to provide a dynamic interface
to Java.

%description -l pl.UTF-8
Tcl Blend wnosi dwie nowe możliwości do systemu Tcl. Po pierwsze
dostarcza klasy Javy udostępniające kluczowe fragmenty interfejsów,
które są dostępne piszącym rozszerzenia aktualnie używającym C. Przy
użyciu tych klas autorzy rozszerzeń mogą tworzyć nowe polecenia dla
interpretera Tcl. Ponadto Tcl Blend udostępnia polecenia umożliwiające
piszącym skrypty bezpośrednie manipulowanie na obiektach Javy bez
konieczności pisania żadnego kodu w Javie. Klasy odzwierciedlające w
Javie umożliwiają wywoływanie metod z tymi możliwościami w celu
udostępnienia dynamicznego interfejsu do Javy.

%prep
%setup -q -n %{name}%{version}

sed -i -e 's,TCLSH_LOC=\$TCL_BIN_DIR/tclsh,TCLSH_LOC=/usr/bin/tclsh,' tcljava.m4

%build
unset CLASSPATH || :
%{__autoconf}
%configure \
	--with-jdk="%{java_home}" \
	--with-tcl=/usr/lib \
	--with-thread=$(echo %{_libdir}/thread2.*)
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	TCLSH=/usr/bin/tclsh \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	BIN_INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir} \
	LIB_INSTALL_DIR=$RPM_BUILD_ROOT%{_libdir} \
	XP_LIB_INSTALL_DIR=$RPM_BUILD_ROOT%{_javadir} \
	TCLBLEND_LIBRARY=$RPM_BUILD_ROOT%{_prefix}/lib/tclblend \
	TCLJAVA_INSTALL_DIR=$RPM_BUILD_ROOT%{_libdir}/tcljava%{version} \
	XP_TCLJAVA_INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix}/lib/tcljava%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changes.txt diffs.txt known_issues.txt license.*
%attr(755,root,root) %{_bindir}/jtclsh
%attr(755,root,root) %{_bindir}/jwish
%dir %{_libdir}/tcljava%{version}
%attr(755,root,root) %{_libdir}/tcljava%{version}/libtclblend.so
%if "%{_libdir}" != "%{_prefix}/lib"
%dir %{_prefix}/lib/tcljava%{version}
%endif
%{_prefix}/lib/tcljava%{version}/pkgIndex.tcl
%{_prefix}/lib/tcljava%{version}/tclblend.jar
%{_prefix}/lib/tcljava%{version}/tclblendsrc.jar
%{_prefix}/lib/tcljava%{version}/tcljava.jar
%{_prefix}/lib/tcljava%{version}/tcljavasrc.jar
%{_prefix}/lib/xputils
