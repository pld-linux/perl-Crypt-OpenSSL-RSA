#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-RSA
Summary:	Crypt::OpenSSL::RSA - RSA encoding and decoding, using the OpenSSL libraries
Summary(pl):	Crypt::OpenSSL::RSA - kodowanie i dekodowanie RSA przy u¿yciu OpenSSL
Name:		perl-Crypt-OpenSSL-RSA
Version:	0.19
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	87a308bf752ffd74b8034a906184e116
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Crypt-OpenSSL-Random
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::RSA provides the ability to RSA encrypt strings which
are somewhat shorter than the block size of a key.  It also allows for
decryption, signatures and signature verification.

%description -l pl
Modu³ Crypt::OpenSSL::RSA udostêpnia mo¿liwo¶æ kodowania algorytmem
RSA ³añcuchów, które s± krótsze ni¿ rozmiar bloku klucza. Pozwala
tak¿e na odszyfrowywanie oraz weryfikacjê podpisów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/OpenSSL/RSA.pm
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/RSA
%{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/*.al
%{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/*.bs
%{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/*.so
%{_mandir}/man3/*
