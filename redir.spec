Summary:	Redirect TCP connections
Name:		redir
Version:	2.2.1
Release:	14
Group:		Networking/Other
License:	GPLv2+
Url:		http://sammy.net/~sammy/hacks/
Source0:	http://sammy.net/~sammy/hacks/%{name}-%{version}.tar.gz
BuildRequires:	tcp_wrappers-devel

#Include Debian Patches
Patch0:		01_fix_max_bandwidth_docs.dpatch
Patch1:		02_use_ntohs.dpatch
Patch2:		03_fix_tcp_wrappers.dpatch
Patch3:		04_fix_timeouts.dpatch
Patch4:		05_pedantic.dpatch
Patch5:		06_fix_shaper_buffer.dpatch
Patch6:		07_cosmetics.dpatch
Patch7:		08_add_wrappers.dpatch
Patch8:		09_add_linux_software_map.dpatch
Patch9:		15_deb_cosmetics.dpatch
Patch10:	20_do_not_strip.dpatch
Patch11:	25_fix_setsockopt.dpatch
Patch12:	30_fix_manpage.dpatch
#end of debian patches

Patch13:	redir_gcc4.4-signedness.patch
Patch14:	31_fix_transproxy_location.patch

%description
A port redirector, used to forward incoming connections to somewhere else.
by far the cleanest piece of code here, because someone else liked it
enough to fix it.

%prep
%setup -q

# Fix docs and --help to show --max_bandwidth instead of --maxbandwidth
%patch0 -p1

#use ntohs() to generate comprehensible debug()s and syslog()s
%patch1 -p1

#fix calls to tcp wrappers
%patch2 -p1

# fix and make timeout more verbose
%patch3 -p1

#changes to make clean up compilation, include missing time.h include
%patch4 -p1

#properly allocate copyloop buffer
%patch5 -p1

#cosmestic only patch
%patch6 -p1

#add tcp_wrapper support
%patch7 -p1

#description of redir
%patch8 -p1

#comestic only patch
%patch9 -p1

# do not stripping needed for debug-info package
%patch10 -p1

#make usage os setsockopt more verbose
%patch11 -p1

#Clean up questionable formatting in man page
%patch12 -p1

#fix compile warning with gcc 4.4
%patch13 -p2

# fix location of transproxy.txt
%patch14 -p2

# Convert to utf-8
for file in CHANGES; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{optflags}"

%install
install -Dp -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README CHANGES COPYING trans*.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

