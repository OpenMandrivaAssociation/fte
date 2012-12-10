%define cvssnap 20040412

Summary:	FTE Text Editor (programmer oriented)
Name:		fte
Epoch:		1
Version:	0.50
Release:	%mkrel 0.%{cvssnap}.9
Source:		http://fte.sourceforge.net/fte/%{name}-cvs-%{cvssnap}.tar.bz2
Patch0: 	fte-20040412-rpmopt.patch
Patch1: 	fte-slang2_compat.patch
Patch2: 	fte-lib64.patch
License:	GPL
Group:		Editors
URL:		http://fte.sourceforge.net/
BuildRequires:	libgpm-devel
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(slang)
BuildRequires:	pkgconfig(x11)

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


%files 
%defattr(0755,root,root,0755)
%{_bindir}/*
%defattr(0644,root,root,0755)
%doc README COPYING Artistic CHANGES HISTORY TODO BUGS doc/*.html
%{_libdir}/fte
%{_datadir}/applications/*


%changelog
* Fri Jan 21 2011 Funda Wang <fwang@mandriva.org> 1:0.50-0.20040412.8mdv2011.0
+ Revision: 632034
- simplify BR
- rediff patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1:0.50-0.20040412.7mdv2009.0
+ Revision: 218423
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - do not harcode icon extension

* Tue Aug 28 2007 Funda Wang <fwang@mandriva.org> 1:0.50-0.20040412.7mdv2008.0
+ Revision: 72330
- fix menu entry comment

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags

  + Herton Ronaldo Krzesinski <herton@mandriva.com.br>
    - Fixed build when libdir = /usr/lib64 (x86_64).
    - Bunzip patches.
    - Rebuild with slang2: replaced slang patch with slang2_compat patch,
      needed as workaround for new slang.
    - Import fte



* Thu Aug 10 2006 Lenny Cartier <lenny@mandriva.com> 1:0.50-0.20040412.4mdv2007.0
- rebuild

* Sun Jul 25 2004 Marcel Pol <mpol@mandrake.org> 0.50-0.20040412.3mdk
- patch1: build against new slang

* Thu Jun 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.50-0.20040412.2mdk
- REbuild

* Mon Apr 12 2004 Michael Reinsch <mr@uue.org> 0.50-0.20040412.1mdk
- cvs snapshot 20040412
- rediffed patch to use $(RPM_OPT_FLAGS)
- spec cleanups

* Tue Apr 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 20020318-4mdk
- buildrequires

* Fri Jan 17 2003 Lenny Cartier <lenny@mandrakesoft.com> 20020318-3mdk
- rebuild

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 20020318-2mdk
- rebuild

* Thu Jun 06 2002 Lenny Cartier <lenny@mandrakesoft.com> 20020318-1mdk
- 20020318

* Sat Jan 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.49.13-7mdk
- Fix menu entry
- Add missing files

* Tue Jul 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.49.13-6mdk
- rebuild

* Tue Jan 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.49.13-5mdk
- rebuild

* Tue Aug 31 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.49.13-4mdk
- menu

* Thu Aug  3 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.49.13-3mdk
- macros
- fix docs

* Wed Apr 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.49.13-2mdk
- fix group
- bzip2 patch

* Tue Feb 29 2000 Vincent Danen <vdanen@linux-mandrake.com>
- initial specfile
- bzip sources
- patchfile for RPM optimization and proper location of binaries
