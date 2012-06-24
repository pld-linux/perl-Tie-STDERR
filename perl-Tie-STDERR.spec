%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	STDERR
Summary:	Tie::STDERR - Send output of your STDERR to a process or mail
Summary(pl):	Tie::STDERR - wysy�anie standardowego wyj�cia b��du do procesu lub poczt�
Name:		perl-Tie-STDERR
Version:	0.26
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sends all output that would otherwise go to STDERR either by email to
root or whoever is responsible, or to a file or a process, or calls
your function at the end of the script. This way you can easily change
the destination of your error messages from inside of your script. The
mail will be sent or the system command or Perl function run only if
there actually is some output detected - something like cron would do.

%description -l pl
Ten modu� przesy�a ca�e wyj�cie, jakie zwykle posz�oby na standardowe
wyj�cie b��du (STDERR) poczt� do administratora albo do pliku lub
procesu, albo wywo�uje funkcj� na ko�cu skryptu. Ten spos�b pozwala
�atwo zmieni� przeznaczenie komunikat�w b��d�w z wn�trza skryptu.
Poczta mo�e by� wys�ana poleceniem systemowym lub funkcj� Perla
uruchomion� tylko w przypadku, kiedy co� si� pojawi na wyj�ciu -
podobnie, jak robi to cron.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Tie/STDERR.pm
%{_mandir}/man3/*
