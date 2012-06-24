Summary:	sdparm - listing and changing SCSI disk parameters
Summary(pl):	sdparm - wy�wietlanie i zmiana parametr�w dysk�w SCSI
Name:		sdparm
Version:	0.99
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://sg.torque.net/sg/p/%{name}-%{version}.tgz
# Source0-md5:	2b5f555adff8a672a2d0f6f71dc023a3
URL:		http://sg.torque.net/sg/sdparm.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sdparm is a utility for listing and potentially changing SCSI disk
parameters. More generally it can be used on any device that uses a
SCSI command set. Apart from SCSI disks, examples of devices that use
SCSI command sets are ATAPI CD/DVD drives, SCSI and ATAPI tape drives
and SCSI enclosures.

%description -l pl
sdparm to narz�dzie do wy�wietlania i ewentualnej zmiany parametr�w
dysk�w SCSI. Bardziej og�lnie mo�e by� u�ywane z ka�dym urz�dzeniem
u�ywaj�cym zestawu polece� SCSI. Opr�cz dysk�w SCSI przyk�adami takich
urz�dze� mog� by� nap�dy CD/DVD ATAPI, nap�dy ta�mowe SCSI i ATAPI
oraz zewn�trzne macierze SCSI.

%prep
%setup -q

%build
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
