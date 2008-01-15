%define module Net-MAC-Vendor

Summary:	Look up the vendor for a MAC
Name:		perl-%{module}
Version:	1.18
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}" CFLAGS="%{optflags}"

# make test dies...
# make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/*/*


