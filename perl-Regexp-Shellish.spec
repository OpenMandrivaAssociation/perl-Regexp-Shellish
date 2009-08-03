%define upstream_name	 Regexp-Shellish
%define upstream_version 0.93

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Shell-like regular expressions for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Regexp/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This perl module allows you to use shell-like regular expressions, 
instead of using perl regular expressions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
