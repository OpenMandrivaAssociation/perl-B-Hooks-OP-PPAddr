%define upstream_name    B-Hooks-OP-PPAddr
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Hook into opcode execution
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/B/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(parent)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a c api for XS modules to hook into the execution of
perl opcodes.

the ExtUtils::Depends manpage is used to export all functions for other XS
modules to use. Include the following in your Makefile.PL:

    my $pkg = ExtUtils::Depends->new('Your::XSModule', 'B::Hooks::OP::PPAddr');
    WriteMakefile(
        ... # your normal makefile flags
        $pkg->get_makefile_vars,
    );

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


