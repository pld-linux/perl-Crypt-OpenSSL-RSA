#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-RSA
Summary:	Crypt::OpenSSL::RSA - RSA encoding and decoding, using the OpenSSL libraries
Summary(pl.UTF-8):	Crypt::OpenSSL::RSA - kodowanie i dekodowanie RSA przy użyciu OpenSSL
Name:		perl-Crypt-OpenSSL-RSA
Version:	0.28
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	86217a5036fc63779c30420b5fd84129
URL:		http://search.cpan.org/dist/Crypt-OpenSSL-RSA/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-OpenSSL-Random
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::RSA provides the ability to RSA encrypt strings which
are somewhat shorter than the block size of a key.  It also allows for
decryption, signatures and signature verification.

%description -l pl.UTF-8
Moduł Crypt::OpenSSL::RSA udostępnia możliwość kodowania algorytmem
RSA łańcuchów, które są krótsze niż rozmiar bloku klucza. Pozwala
także na odszyfrowywanie oraz weryfikację podpisów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

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
%{perl_vendorarch}/Crypt/OpenSSL/RSA.pm
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/RSA
%{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/*.al
%{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/*.so
%{_mandir}/man3/Crypt::OpenSSL::RSA.3pm*
