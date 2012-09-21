Name: mod_jk
Summary: The Apache Tomcat Connector
Version: 1.2.37
Release: el6.intesi.2
Group: System Environment/Daemons
License: ASL 2.0
URL: http://tomcat.apache.org/connectors-doc/
Packager: Emanuele Cisbani
Vendor: Intesi Group Spa
Exclusiveos: linux 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: %{_prefix}
Source: http://www.apache.org/dist/tomcat/tomcat-connectors/jk/tomcat-connectors-%{version}-src.tar.gz
Requires: httpd >= 2.0
BuildRequires: httpd-devel, gcc-c++, make

%description
This package provide the module used to connect the Tomcat servlet container 
with the web server Apache using the AJP protocol.

It provides:
	Advanced load balancer
	Advanced node failure detection
	Support for large AJP packet sizes

%prep
%setup -n tomcat-connectors-%{version}-src
cd native
./configure --with-apxs=/usr/sbin/apxs

%build
cd native
make
echo "install:
	echo nothing "> ../Makefile

%install
install --directory $RPM_BUILD_ROOT/usr/lib/httpd/modules
install -m 755 native/apache-2.0/mod_jk.so $RPM_BUILD_ROOT/usr/lib/httpd/modules/mod_jk.so

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, root)
/usr/lib/httpd/modules/mod_jk.so
%doc docs
%doc README.txt

#%pre

#%post

#%postun

%changelog
* Wed Jul 13 2012 Emanuele Cisbani - 1.2.37-el6.intesi.1
- Initial RPM release.
* Wed Jul 13 2012 Emanuele Cisbani - 1.2.37-el6.intesi.2
- fixed some rpmlint warnings
- packaged also documentation files



