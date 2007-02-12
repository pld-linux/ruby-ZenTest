Summary:	Ruby Testing framework
Summary(pl.UTF-8):   Szkielet do testów dla języka Ruby
Name:		ruby-ZenTest
Version:	3.0.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/9048/ZenTest-%{version}.tar.gz
# Source0-md5:	cef297906ffad7e024737727df9ea0fe
Patch0:	%{name}-nogems.patch
URL: http://www.zenspider.com/ZSS/Products/ZenTest/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	rake
BuildRequires:	sed >= 4.0
%{?ruby_mod_ver_requires_eq}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZenTest scans your target and unit-test code and writes your missing
code based on simple naming rules, enabling XP at a much quicker pace.
ZenTest only works with Ruby and Test::Unit.

For auditing, ZenTest provides an excellent means of finding methods
that have slipped through the testing process. I've run it against my
own software and found I missed a lot in a well tested package.
Writing those tests found 4 bugs I had no idea existed.

%description -l pl.UTF-8
ZenTest skanuje cel oraz kod testów jednostkowych i pisze brakujący
kod w oparciu o proste reguły nazywania, pozwalając na duży szybsze
XP. ZenTest działa tylko z Rubym i Test::Unit.

Dla potrzeb audytu ZenTest dostarcza świetne środki znajdowania metod
wyślizgujących się z procesu testowania. Autor uruchamiał je na
własnym oprogramowaniu i znalazł, że wiele pominął w dobrze
przetestowanym pakiecie. Napisanie tych testów znalazło 4 błędy, o
których istnieniu autor nie miał pojęcia.

%prep
%setup -q -n ZenTest-%{version}
find . -name '*.rb' | xargs sed -i -e '1s,#!.*local/bin/ruby,#!%{_bindir}/ruby,'
find bin -type f | xargs sed -i -e '1s,#!.*local/bin/ruby,#!%{_bindir}/ruby,'
%patch0 -p1

%build
rake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_rubylibdir}}

install bin/* $RPM_BUILD_ROOT%{_bindir}
install lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*
