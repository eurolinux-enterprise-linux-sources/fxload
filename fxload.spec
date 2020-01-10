Name: fxload
Version: 2002_04_11
Release: 14%{?dist}
Summary: A helper program to download firmware into FX and FX2 EZ-USB devices

Group: System Environment/Kernel
License: GPLv2+
URL: http://linux-hotplug.sourceforge.net/
Source0: fxload-2002_04_11-noa3load.tar.gz
# The above file is derived from:
# http://downloads.sourceforge.net/linux-hotplug/fxload-2002_04_11.tar.gz
# This file contains code that is copyright Cypress Semiconductor Inc,
# and cannot be distributed. Therefore we use this script to remove the
# copyright code before shipping it. Download the upstream tarball and
# invoke this script while in the tarball's directory:
# ./fxload-generate-tarball.sh 2002_04_11
Source1: fxload-generate-tarball.sh
Patch0: fxload-header.patch
Patch1: fxload-noa3load.patch
Patch2: fxload-man.patch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: kernel-headers
Requires: udev
Conflicts: hotplug-gtk hotplug

%description 
This program is conveniently able to download firmware into FX and FX2
EZ-USB devices, as well as the original AnchorChips EZ-USB.  It is
intended to be invoked by udev scripts when the unprogrammed device
appears on the bus.

%prep
%setup -q 
%patch0 -p0 -b .fxload-header
%patch1 -p1 -b .fxload-noa3load
%patch2 -p1 -b .fxload-man

%build 
make

%install
rm -rf %{buildroot}
mkdir -p -m 755 %{buildroot}/sbin
install -m 755 fxload %{buildroot}/sbin
mkdir -p -m 755 %{buildroot}/%{_mandir}/man8/
install -m 644 fxload.8 %{buildroot}/%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc COPYING
%doc README.txt
%attr(0755, root, root) /sbin/fxload
%{_mandir}/*/*

%changelog
* Wed Jul 31 2013 Jaroslav Kysela <jkysela@redhat.com> - 2002_04_11-14
- Man page and usage updates
- rhbz#948527

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2002_04_11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2002_04_11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2002_04_11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2002_04_11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2002_04_11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2002_04_11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 9 2008 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2002_04_11-7
- Bump version to rebuild with gcc-4.3

* Sat Nov 16 2007 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2002_04_11-6
- Rework the spec file formatting to match templates from rpmdev
- Be explicit about file attributes, just in case

* Sat Nov 16 2007 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2002_04_11-5
- Updates after reading packaging guide-lines more thoroughly:
- Make license version more explicit
- Add generate-tarball.sh, and associated comments
- Added BuildRequires on kernel-headers
- Added COPYING as a doc
- Use dollar v.s. percent macros more consitently

* Fri Nov 15 2007 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2002_04_11-4
- Repackage the source tarball to remove a3load.hex
- Added instructions to spec file on how to do the above
- Remove reference to a3load.hex from the man page too

* Thu Nov 15 2007 Stephen Warren <s-t-rhbugzilla@wwwdotorg.org> - 2002_04_11-3
- Update BuildRoot per Fedora wiki
- Fixed rpmlint complaint about not cleaning buildroot
- Updated source patch file to match latest kernel file layout
- Add patch to remove reference to non-shipped non-free a3load.hex firmware

* Fri Dec 8 2006 Bart Vanbrabant <bart.vanbrabant@zoeloelip.be> - 2002_04_11-2
- Fixed some rpmlint complaints
- Added patch to fix an include header
- Added dist tag

* Wed Apr 12 2006 Bart Vanbrabant <bart.vanbrabant@zoeloelip.be> - 2002_04_11-1
- First version of fxload spec based on hotplug spec

