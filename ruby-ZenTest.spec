Summary:	Ruby Testing framework
Name:		ruby-ZenTest
Version:	2.3.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/1944/ZenTest-%{version}.tar.gz
# Source0-md5:	f94eed12075025c3e7090520b95e8eab
BuildRequires: perl
Requires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZenTest scans your target and unit-test code and writes your missing code based on simple naming rules, enabling XP at a much quicker pace. ZenTest only works with Ruby and Test::Unit.

For auditing, ZenTest provides an excellent means of finding methods that have slipped through the testing process. I've run it against my own software and found I missed a lot in a well tested package. Writing those tests found 4 bugs I had no idea existed.

%prep
%setup -q -n ZenTest-%{version}

%build
make
find . -name '*.rb' | xargs perl -pi -e "s#local/bin/ruby#bin/ruby#"


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install ZenTest.rb $RPM_BUILD_ROOT%{_bindir}/ZenTest
install unit_diff.rb $RPM_BUILD_ROOT%{_bindir}/unit_diff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
