%include	/usr/lib/rpm/macros.perl
%define		pdir	Search
%define		pnam	Xapian
%define		basever	1.0.4
Summary:	Search::Xapian - Perl XS frontend to the Xapian C++ search library
Name:		perl-Search-Xapian
Version:	%{basever}.0
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Search/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	71012cee4819d80ad1da82c5bf6f3136
URL:		http://search.cpan.org/dist/Search-Xapian/
BuildRequires:	libstdc++-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	xapian-core-devel = %{basever}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module wraps most methods of most Xapian classes. The missing
classes and methods should be added in the future. It also provides a
simplified, more 'perlish' interface to some common operations, as
demonstrated above.

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
%{perl_vendorarch}/Search/*.pm
%dir %{perl_vendorarch}/Search/Xapian
%{perl_vendorarch}/Search/Xapian/*.pm
%dir %{perl_vendorarch}/Search/Xapian/MSet
%{perl_vendorarch}/Search/Xapian/MSet/Tied.pm
%dir %{perl_vendorarch}/auto/Search/Xapian
%{perl_vendorarch}/auto/Search/Xapian/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Search/Xapian/*.so

%{_mandir}/man3/Search::Xapian*

%{_examplesdir}/%{name}-%{version}
