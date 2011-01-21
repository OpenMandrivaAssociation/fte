%define cvssnap 20040412

Summary:	FTE Text Editor (programmer oriented)
Name:		fte
Epoch:		1
Version:	0.50
Release:	%mkrel 0.%{cvssnap}.8
Source:		http://fte.sourceforge.net/fte/%{name}-cvs-%{cvssnap}.tar.bz2
Patch0: 	fte-20040412-rpmopt.patch
Patch1: 	fte-slang2_compat.patch
Patch2: 	fte-lib64.patch
License:	GPL
Group:		Editors
URL:		http://fte.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgpm-devel
BuildRequires:	libncurses-devel
BuildRequires:	libslang-devel
BuildRequires:	libx11-devel

%description
FTE is a Text Mode text editor for xterm sessions.  Color syntax highlighting
for C/C++, REXX, HTML, IPF, PERL, Ada, Pascal, TEX.  Multiple file/window
editing, Column blocks, configurable menus and keyboard bindings, mouse
support, undo/redo, regular expression search and replace, folding, background
compiler execution.

%prep
%setup -q -n fte
%patch0 -p0 -b .rpmopt
%patch1 -p1 -b .slang2_compat
%if %{_lib} == lib64
%patch2 -p1 -b .lib64
%endif

%build
make PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std INSTALL_NONROOT=1 PREFIX=%{buildroot}%{_prefix}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=FTE Text Editor (programmer oriented)
Exec=%{name}
Icon=editors_section
Terminal=false
Type=Application
Categories=Utility;TextEditor;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files 
%defattr(0755,root,root,0755)
%{_bindir}/*
%defattr(0644,root,root,0755)
%doc README COPYING Artistic CHANGES HISTORY TODO BUGS doc/*.html
%{_libdir}/fte
%{_datadir}/applications/*
