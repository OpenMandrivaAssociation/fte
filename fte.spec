%define cvssnap 20180420

Summary:	Text Editor (programmer oriented)
Name:		fte
Epoch:		1
Version:	0.50
Release:	%mkrel 0.%{cvssnap}.9
Source0:	http://fte.sourceforge.net/fte/%{name}-cvs-%{cvssnap}.tar.xz
Patch2: 	fte-lib64.patch
License:	GPL
Group:		Editors
URL:		https://fte.sourceforge.net/
BuildRequires:	libgpm-devel
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(slang)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)

%description
FTE is a Text Mode text editor for xterm sessions.  Color syntax highlighting
for C/C++, REXX, HTML, IPF, PERL, Ada, Pascal, TEX.  Multiple file/window
editing, Column blocks, configurable menus and keyboard bindings, mouse
support, undo/redo, regular expression search and replace, folding, background
compiler execution.

%package x11
Summary:	X11 version of the FTE editor
Group:		Editors
Requires:	%{name} = %{EVRD}

%description x11
X11 version of the FTE editor

%prep
%setup -q -n fte
sed -i -e 's,^LIBDIR=.*,LIBDIR=\$(PREFIX)/%{_lib}/fte,g' Makefile
sed -i -e 's,^LIBDIR=.*,LIBDIR=\$PREFIX/%{_lib}/fte,g' install

%build
%make PREFIX=%{_prefix} OPTIMIZE="%{optflags}" CC="%{__cc}" CXX="%{__cxx}"

%install
%make_install INSTALL_NONROOT=1 PREFIX=%{buildroot}%{_prefix}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/org.openmandriva.%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=FTE Text Editor (programmer oriented)
Exec=%{name}
Icon=editors_section
Terminal=false
Type=Application
Categories=Utility;TextEditor;
EOF


%files 
%doc README COPYING Artistic TODO BUGS doc/*.html
%exclude %{_bindir}/xfte
%{_bindir}/*
%{_libdir}/fte

%files x11
%{_bindir}/xfte
%{_datadir}/applications/*
