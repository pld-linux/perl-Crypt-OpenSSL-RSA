%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-RSA
Summary:	Crypt-Primes perl module
Summary(pl):	Modu³ perla Crypt-Primes
Name:		perl-Crypt-OpenSSL-RSA
Version:	0.14
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	openssl-devel
BuildRequires:	perl-devel >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::RSA perl module.

%description -l pl
Modu³ perla Crypt::OpenSSL::RSA.

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
%dir %{perl_sitearch}/Crypt/OpenSSL
%{perl_sitearch}/Crypt/OpenSSL/RSA.pm
%dir %{perl_sitearch}/auto/Crypt/OpenSSL/
%dir %{perl_sitearch}/auto/Crypt/OpenSSL/RSA
%{perl_sitearch}/auto/Crypt/OpenSSL/RSA/*
%{_mandir}/man3/*
