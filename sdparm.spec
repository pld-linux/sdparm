Summary:	sdparm - listing and changing SCSI disk parameters
Summary(pl.UTF-8):	sdparm - wyświetlanie i zmiana parametrów dysków SCSI
Name:		sdparm
Version:	1.09
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://sg.danny.cz/sg/p/%{name}-%{version}.tar.xz
# Source0-md5:	76b53e2be4c5b85e4af0887ce838c955
Patch0:		%{name}-am.patch
URL:		http://sg.danny.cz/sg/sdparm.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# for scsi_ch_swp
Suggests:	blockdev
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sdparm is a utility for listing and potentially changing SCSI disk
parameters. More generally it can be used on any device that uses a
SCSI command set. Apart from SCSI disks, examples of devices that use
SCSI command sets are ATAPI CD/DVD drives, SCSI and ATAPI tape drives
and SCSI enclosures.

%description -l pl.UTF-8
sdparm to narzędzie do wyświetlania i ewentualnej zmiany parametrów
dysków SCSI. Bardziej ogólnie może być używane z każdym urządzeniem
używającym zestawu poleceń SCSI. Oprócz dysków SCSI przykładami takich
urządzeń mogą być napędy CD/DVD ATAPI, napędy taśmowe SCSI i ATAPI
oraz zewnętrzne macierze SCSI.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING CREDITS ChangeLog README
%attr(755,root,root) %{_bindir}/sas_disk_blink
%attr(755,root,root) %{_bindir}/scsi_ch_swp
%attr(755,root,root) %{_bindir}/sdparm
%{_mandir}/man8/sas_disk_blink.8*
%{_mandir}/man8/scsi_ch_swp.8*
%{_mandir}/man8/sdparm.8*
