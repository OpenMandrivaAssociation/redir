Summary:	Redirect TCP connections
Name:		redir
Version:	3.3
Release:	2
Group:		Networking/Other
License:	GPLv2+
Url:		https://sammy.net/~sammy/hacks/
Source0:	https://github.com/troglobit/redir/archive/v%{version}.tar.gz
BuildRequires:	tcp_wrappers-devel

%description
A port redirector, used to forward incoming connections to somewhere else.
by far the cleanest piece of code here, because someone else liked it
enough to fix it.

%prep
%setup -q

%build
autoreconf -fiv
%configure
%make CFLAGS="%{optflags}" LDFLAGS="%{optflags}"

%install
%makeinstall

%files
%doc README.md COPYING trans*.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

