#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Search
%define		pnam	Xapian
%define		basever	1.2.24
Summary:	Search::Xapian - Perl XS frontend to the Xapian C++ search library
Summary(pl.UTF-8):	Search::Xapian - interfejs Perlowy XS do biblioteki wyszukiwania Xapian
Name:		perl-Search-Xapian
Version:	%{basever}.0
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/Search/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://oligarchy.co.uk/xapian/%{basever}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	01206bf2cc71c5b3a6258a01daabfc43
URL:		http://search.cpan.org/dist/Search-Xapian/
BuildRequires:	libstdc++-devel
%if %{with tests}
BuildRequires:	perl-Devel-Leak
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	xapian-core-devel >= %{basever}
Requires:	xapian-core-libs >= %{basever}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module wraps most methods of most Xapian classes. The missing
classes and methods should be added in the future. It also provides a
simplified, more 'perlish' interface to some common operations.

%description -l pl.UTF-8
Ten moduł obudowuje większość metod z większości klas Xapiana.
Brakujące klasy i metody powinny być dodane w przyszłości. Moduł
udostępnia także uproszczony, bardziej perlowy interfejs do niektórych
popularnych operacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

# NOTE: (this) Perl build system doesn't have CXX, but CC is used
%{__make} \
	CC="%{__cxx}" \
	OPTIMIZE="%{rpmcxxflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Search
%{perl_vendorarch}/Search/Xapian.pm
%dir %{perl_vendorarch}/Search/Xapian
%{perl_vendorarch}/Search/Xapian/*.pm
%dir %{perl_vendorarch}/Search/Xapian/MSet
%{perl_vendorarch}/Search/Xapian/MSet/Tied.pm
%dir %{perl_vendorarch}/auto/Search
%dir %{perl_vendorarch}/auto/Search/Xapian
%attr(755,root,root) %{perl_vendorarch}/auto/Search/Xapian/Xapian.so
%{_mandir}/man3/Search::Xapian*.3pm*
%{_examplesdir}/%{name}-%{version}
