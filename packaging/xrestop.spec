Name:           xrestop
Version:        0.4
Release:        0
License:        GPL-2.0+
Summary:        X Resource Monitor
Url:            http://www.freedesktop.org/Software/xrestop
Group:          Development/Tools
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xres)

%description
A utility to monitor application usage of X resources in the X Server, and
display them in a manner similar to 'top'.  This is a very useful utility
for tracking down application X resource usage leaks.

%prep
%setup -q

%build
%reconfigure
make %{?_smp_mflags}
# SUBDIRS=

%install
%make_install

%remove_docs

%files
%defattr(-,root,root,-)
%license  COPYING
%{_bindir}/xrestop
