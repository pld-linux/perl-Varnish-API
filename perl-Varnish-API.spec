#
# Conditional build:
%bcond_with	tests		# perform testing. needs running varnishd

%include	/usr/lib/rpm/macros.perl
%define		pdir	Varnish
%define		pnam	API
Summary:	Varnish::API - Perl extension for accessing varnish stats and logs
Name:		perl-Varnish-API
Version:	1.99_1
Release:	1
# Same as Perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AB/ABERGMAN/Varnish-API-%{version}.tar.gz
# Source0-md5:	d0acd25bc23f28fb74ff4d355a206db8
URL:		http://search.cpan.org/dist/Varnish-API/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows access to the data that varnishlog and varnishstats
can read.

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

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Varnish/*.pm
%dir %{perl_vendorarch}/auto/Varnish/API
%{perl_vendorarch}/auto/Varnish/API/*.bs
%{perl_vendorarch}/auto/Varnish/API/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Varnish/API/*.so
%{_mandir}/man3/*
