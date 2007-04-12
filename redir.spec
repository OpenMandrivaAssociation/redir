%define name redir
%define version 2.2.1
%define release %mkrel 5

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



* Sat Aug 28 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.2.1-4mdk
- rebuild because changelog size does matter

* Mon Aug 04 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.2.1-3mdk
- rebuild
- cosmetics
- fix filename of man page
- compile with $RPM_OPT_FLAGS

* Fri Dec 27 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.2.1-2mdk
- rebuild for rpm and glibc

* Mon Nov 11 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.2.1-1mdk
- by Tibor Pittich <Tibor.Pittich@phuture.sk>
	- initial import into Cooker from PLD
	- remove PLD patches
	- new version 2.2.1
- remove packager and vendor tag
- make rpmlint happy
