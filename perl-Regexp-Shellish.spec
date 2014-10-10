%define upstream_name	 Regexp-Shellish
%define upstream_version 0.93

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Shell-like regular expressions for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Regexp/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This perl module allows you to use shell-like regular expressions, 
instead of using perl regular expressions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.930.0-2mdv2011.0
+ Revision: 658878
- rebuild for updated spec-helper

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.930.0-1mdv2010.0
+ Revision: 408044
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.93-8mdv2009.0
+ Revision: 241852
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 0.93-6mdv2008.0
+ Revision: 64195
- rebuild

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.93-5mdv2008.0
+ Revision: 25098
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.93-4mdk
- Fix According to perl Policy
	- Source URL
	- URL
- use mkrel

* Sat Feb 05 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.93-3mdk
- rebuild for new perl

* Tue Aug 31 2004 Michael Scherer <misc@mandrake.org> 0.93-2mdk 
- rebuild for new perl ( [DIRM] )

* Fri Apr 02 2004 Michael Scherer <misc@mandrake.org> 0.93-1mdk 
- First MandrakeSoft Package

