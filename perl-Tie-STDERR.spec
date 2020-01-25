#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Tie
%define		pnam	STDERR
Summary:	Tie::STDERR - send output of your STDERR to a process or mail
Summary(pl.UTF-8):	Tie::STDERR - wysyłanie standardowego wyjścia błędu do procesu lub pocztą
Name:		perl-Tie-STDERR
Version:	0.122
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	65bdd4f54c4e6a06cd7444e885c05f22
URL:		http://search.cpan.org/dist/Tie-STDERR/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sends all output that would otherwise go to STDERR either by email to
root or whoever is responsible, or to a file or a process, or calls
your function at the end of the script. This way you can easily change
the destination of your error messages from inside of your script. The
mail will be sent or the system command or Perl function run only if
there actually is some output detected - something like cron would do.

%description -l pl.UTF-8
Ten moduł przesyła całe wyjście, jakie zwykle poszłoby na standardowe
wyjście błędu (STDERR) pocztą do administratora albo do pliku lub
procesu, albo wywołuje funkcję na końcu skryptu. Ten sposób pozwala
łatwo zmienić przeznaczenie komunikatów błędów z wnętrza skryptu.
Poczta może być wysłana poleceniem systemowym lub funkcją Perla
uruchomioną tylko w przypadku, kiedy coś się pojawi na wyjściu -
podobnie, jak robi to cron.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tie/STDERR.pm
%{_mandir}/man3/*
