%define name redir
%define version 2.2.1
%define release %mkrel 9

Summary:	Redirect TCP connections
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
Source0:	http://sammy.net/~sammy/hacks/%{name}-%{version}.tar.bz2
BuildRequires:	tcp_wrappers-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://sammy.net/~sammy/hacks

%description
Redir redirects tcp connections coming in to a local port to a
specified address/port combination.

%prep
%setup  -q

%build
%make EXTRA_CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install %{name} -D $RPM_BUILD_ROOT%{_sbindir}/%{name}
install %{name}.man -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README trans*.txt
%attr(755,root,root) %{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.2.1-9mdv2010.0
+ Revision: 433089
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.2.1-8mdv2009.0
+ Revision: 260205
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.2.1-7mdv2009.0
+ Revision: 248331
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.2.1-5mdv2008.1
+ Revision: 140744
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - kill changelog left by repsys


* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-07-14 19:29:14 (41143)
- %%mkrel and rebuild

* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-07-14 19:27:30 (41142)
- Import redir

* Sat Aug 28 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.2.1-4mdk
- rebuild because changelog size does matter

* Mon Aug 04 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.2.1-3mdk
- rebuild
- cosmetics
- fix filename of man page
- compile with $RPM_OPT_FLAGS

