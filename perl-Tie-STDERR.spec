#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	STDERR
Summary:	Tie::STDERR - send output of your STDERR to a process or mail
Summary(pl):	Tie::STDERR - wysy³anie standardowego wyj¶cia b³êdu do procesu lub poczt±
Name:		perl-Tie-STDERR
Version:	0.26
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2071204c4b6a6d22af14a46ceab586e7
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

%description -l pl
Ten modu³ przesy³a ca³e wyj¶cie, jakie zwykle posz³oby na standardowe
wyj¶cie b³êdu (STDERR) poczt± do administratora albo do pliku lub
procesu, albo wywo³uje funkcjê na koñcu skryptu. Ten sposób pozwala
³atwo zmieniæ przeznaczenie komunikatów b³êdów z wnêtrza skryptu.
Poczta mo¿e byæ wys³ana poleceniem systemowym lub funkcj± Perla
uruchomion± tylko w przypadku, kiedy co¶ siê pojawi na wyj¶ciu -
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
