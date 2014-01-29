%bcond_with x

Name:           xrestop
Version:        0.4
Release:        0
License:        GPL-2.0+
Summary:        X Resource Monitor
Url:            http://www.freedesktop.org/Software/xrestop
Group:          Development/Tools
Source0:        %{name}-%{version}.tar.gz
Source1001: 	xrestop.manifest

BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xres)

%if !%{with x}
ExclusiveArch:
%endif

%description
A utility to monitor application usage of X resources in the X Server, and
display them in a manner similar to 'top'.  This is a very useful utility
for tracking down application X resource usage leaks.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure
make %{?_smp_mflags}
# SUBDIRS=

%install
%make_install

%remove_docs

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license  COPYING
%{_bindir}/xrestop
