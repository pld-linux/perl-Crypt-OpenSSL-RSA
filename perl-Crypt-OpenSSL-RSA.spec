%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-RSA
Summary:	Crypt::OpenSSL::RSA Perl module
Summary(cs):	Modul Crypt::OpenSSL::RSA pro Perl
Summary(da):	Perlmodul Crypt::OpenSSL::RSA
Summary(de):	Crypt::OpenSSL::RSA Perl Modul
Summary(es):	Módulo de Perl Crypt::OpenSSL::RSA
Summary(fr):	Module Perl Crypt::OpenSSL::RSA
Summary(it):	Modulo di Perl Crypt::OpenSSL::RSA
Summary(ja):	Crypt::OpenSSL::RSA Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Crypt::OpenSSL::RSA ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Crypt::OpenSSL::RSA
Summary(pl):	Modu³ Perla Crypt::OpenSSL::RSA
Summary(pt):	Módulo de Perl Crypt::OpenSSL::RSA
Summary(pt_BR):	Módulo Perl Crypt::OpenSSL::RSA
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::RSA
Summary(sv):	Crypt::OpenSSL::RSA Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::RSA
Summary(zh_CN):	Crypt::OpenSSL::RSA Perl Ä£¿é
Name:		perl-Crypt-OpenSSL-RSA
Version:	0.16
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::RSA perl module.

%description -l cs
Modul Crypt::OpenSSL::RSA pro Perl.

%description -l da
Perlmodul Crypt::OpenSSL::RSA.

%description -l de
Crypt::OpenSSL::RSA Perl Modul.

%description -l es
Módulo de Perl Crypt::OpenSSL::RSA.

%description -l fr
Module Perl Crypt::OpenSSL::RSA.

%description -l it
Modulo di Perl Crypt::OpenSSL::RSA.

%description -l ja
Crypt::OpenSSL::RSA Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Crypt::OpenSSL::RSA ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul Crypt::OpenSSL::RSA.

%description -l pl
Modu³ perla Crypt::OpenSSL::RSA.

%description -l pt
Módulo de Perl Crypt::OpenSSL::RSA.

%description -l pt_BR
Módulo Perl Crypt::OpenSSL::RSA.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::RSA.

%description -l sv
Crypt::OpenSSL::RSA Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::RSA.

%description -l zh_CN
Crypt::OpenSSL::RSA Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Crypt/OpenSSL/RSA.pm
%dir %{perl_sitearch}/auto/Crypt/OpenSSL/RSA
%{perl_sitearch}/auto/Crypt/OpenSSL/RSA/*.al
%{perl_sitearch}/auto/Crypt/OpenSSL/RSA/*.bs
%{perl_sitearch}/auto/Crypt/OpenSSL/RSA/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/OpenSSL/RSA/*.so
%{_mandir}/man3/*
