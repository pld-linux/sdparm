# NOTE: beta versions are versioned with just new version number,
#       so check URL for final releases
Summary:	sdparm - listing and changing SCSI disk parameters
Summary(pl.UTF-8):	sdparm - wyświetlanie i zmiana parametrów dysków SCSI
Name:		sdparm
Version:	1.06
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://sg.danny.cz/sg/p/%{name}-%{version}.tgz
# Source0-md5:	5e19913658bb4f9849ddd909e0f47cde
URL:		http://sg.danny.cz/sg/sdparm.html
BuildRequires:	autoconf
BuildRequires:	automake
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
%attr(755,root,root) %{_bindir}/sdparm
%{_mandir}/man8/sdparm.8*
