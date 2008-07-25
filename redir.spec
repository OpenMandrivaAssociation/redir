%define name redir
%define version 2.2.1
%define release %mkrel 7

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


