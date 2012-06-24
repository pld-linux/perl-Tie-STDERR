%define	pdir	Tie
%define	pnam	STDERR
%include	/usr/lib/rpm/macros.perl
Summary:	Tie-STDERR perl module
Summary(pl):	Modu� perla Tie-STDERR
Name:		perl-Tie-STDERR
Version:	0.26
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-STDERR perl module.

%description -l pl
Modu� perla Tie-STDERR.

%prep
%setup -q -n Tie-STDERR-%{version}

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
