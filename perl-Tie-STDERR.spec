%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	STDERR
Summary:	Tie::STDERR - Send output of your STDERR to a process or mail
Name:		perl-Tie-STDERR
Version:	0.26
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sends all output that would otherwise go to STDERR either by email to
root or whoever is responsible, or to a file or a process, or calls
your function at the end of the script. This way you can easily change
the destination of your error messages from B<inside> of your script.
The mail will be sent or the system command or Perl function run only
if there actually is some output detected -- something like cron would do.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tie/STDERR.pm
%{_mandir}/man3/*
