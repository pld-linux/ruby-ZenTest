Summary:	Ruby Testing framework
Summary(pl):	Szkielet do test�w dla j�zyka Ruby
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

%description -l pl
ZenTest skanuje cel oraz kod test�w jednostkowych i pisze brakuj�cy
kod w oparciu o proste regu�y nazywania, pozwalaj�c na du�y szybsze
XP. ZenTest dzia�a tylko z Rubym i Test::Unit.

Dla potrzeb audytu ZenTest dostarcza �wietne �rodki znajdowania metod
wy�lizguj�cych si� z procesu testowania. Autor uruchamia� je na
w�asnym oprogramowaniu i znalaz�, �e wiele pomin�� w dobrze
przetestowanym pakiecie. Napisanie tych test�w znalaz�o 4 b��dy, o
kt�rych istnieniu autor nie mia� poj�cia.

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
