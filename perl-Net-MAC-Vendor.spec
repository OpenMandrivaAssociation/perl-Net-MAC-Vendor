%define upstream_name    Net-MAC-Vendor
%define upstream_version 1.1901

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.1901
Release:	2

Summary:	Look up the vendor for a MAC
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Net/Net-MAC-Vendor-1.1901.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Institute of Electrical and Electronics Engineers (IEEE) assigns an
Organizational Unique Identifier (OUI) to manufacturers of network interfaces.
Each interface has a Media Access Control (MAC) address of six bytes. The first
three bytes are the OUI.

This module allows you to take a MAC address and turn it into the OUI and
vendor information.  You can, for instance, scan a network, collect MAC
addresses, and turn those addresses into vendors.  With vendor information, you
can often guess at what what you are looking at (e.g. an Apple product).

You can use this as a module as its individual functions, or call it as a
script with a list of MAC addresses as arguments. The module can figure it out.

This module tries to persistently cache with DBM::Deep the OUI information so
it can avoid using the network. If it cannot load DBM::Deep, it uses a normal
hash (which is lost when the process finishes). You can preload this cache with
the load_cache() function. So far, the module looks in the current working
directory for a file named mac_oui.db to find the cache. I need to come up with
a way to let the user set that location.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}" CFLAGS="%{optflags}"

# make test dies...
# make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.180.0-2mdv2011.0
+ Revision: 655141
- rebuild for updated spec-helper

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.180.0-1mdv2011.0
+ Revision: 404096
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.18-6mdv2009.0
+ Revision: 258055
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.18-5mdv2009.0
+ Revision: 246157
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.18-3mdv2008.1
+ Revision: 152222
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.18-2mdv2008.1
+ Revision: 152221
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2008.1
+ Revision: 104563
- update to new version 1.18


* Tue Mar 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.17-1mdv2007.1
+ Revision: 143145
- Import perl-Net-MAC-Vendor

* Tue Mar 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.17-1mdv2007.1
- initial Mandriva package


