%define realname	Regexp-Shellish

Name:		perl-%{realname}
Version:	0.93
Release: %mkrel 6

License:	GPL or Artistic
Group:		Development/Perl
Summary:	Shell-like regular expressions for perl
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Regexp/%{realname}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildArch:      noarch
%description
This perl module allows you to use shell-like regular expressions, 
instead of using perl regular expressions.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*

