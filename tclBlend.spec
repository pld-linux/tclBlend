#
# Conditional build:
%bcond_with	javac	# use javac instead of jikes+kaffe
#
Summary:	Tcl Blend - Java access for Tcl system
Summary(pl):	Tcl Blend - dostêp do Javy w systemie Tcl
Name:		tclBlend
Version:	1.2.6
Release:	0.1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	ftp://ftp.tcl.tk/pub/tcl/java/%{name}%{version}.tar.gz
# Source0-md5:	96ba50d8c9af7c37caae60b1b77c9650
Patch0:		%{name}-build.patch
URL:		http://www.tcl.tk/software/java/
BuildRequires:	autoconf
%{?with_javac:BuildRequires:	jdk}
%{!?with_javac:BuildRequires:	jikes}
%{!?with_javac:BuildRequires:	kaffe-devel}
BuildRequires:	tcl-devel >= 8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
Tcl Blend wnosi dwie nowe mo¿liwo¶ci do systemu Tcl. Po pierwsze
dostarcza klasy Javy udostêpniaj±ce kluczowe fragmenty interfejsów,
które s± dostêpne pisz±cym rozszerzenia aktualnie u¿ywaj±cym C. Przy
u¿yciu tych klas autorzy rozszerzeñ mog± tworzyæ nowe polecenia dla
interpretera Tcl. Ponadto Tcl Blend udostêpnia polecenia umo¿liwiaj±ce
pisz±cym skrypty bezpo¶rednie manipulowanie na obiektach Javy bez
konieczno¶ci pisania ¿adnego kodu w Javie. Klasy odzwierciedlaj±ce w
Javie umo¿liwiaj± wywo³ywanie metod z tymi mo¿liwo¶ciami w celu
udostêpnienia dynamicznego interfejsu do Javy.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%build
cd unix
%{__autoconf}
%configure \
	%{?with_javac:--without-jikes} \
	--with-tcl=/usr/lib
%{__make} \
	%{?with_javac:JAVAC_FLAGS="-g -source 1.4"}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C unix install \
	TCLSH=/usr/bin/tclsh \
	BIN_INSTALL_DIR=$RPM_BUILD_ROOT%{_bindir} \
	LIB_INSTALL_DIR=$RPM_BUILD_ROOT%{_libdir} \
	XP_LIB_INSTALL_DIR=$RPM_BUILD_ROOT%{_javadir} \
	TCLBLEND_LIBRARY=$RPM_BUILD_ROOT%{_prefix}/lib/tclblend

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changes.txt diffs.txt known_issues.txt license.*
%attr(755,root,root) %{_bindir}/jtclsh
%attr(755,root,root) %{_bindir}/jwish
%attr(755,root,root) %{_libdir}/libtclblend.so
%{_prefix}/lib/tclblend
%{_javadir}/tclblend.jar
# XXX: dup with jacl?
%{_javadir}/tcljava.jar
