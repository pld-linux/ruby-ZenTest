Summary:	Ruby Testing framework
Summary(pl):	Szkielet do testów dla jêzyka Ruby
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
ZenTest skanuje cel oraz kod testów jednostkowych i pisze brakuj±cy
kod w oparciu o proste regu³y nazywania, pozwalaj±c na du¿y szybsze
XP. ZenTest dzia³a tylko z Rubym i Test::Unit.

Dla potrzeb audytu ZenTest dostarcza ¶wietne ¶rodki znajdowania metod
wy¶lizguj±cych siê z procesu testowania. Autor uruchamia³ je na
w³asnym oprogramowaniu i znalaz³, ¿e wiele pomin±³ w dobrze
przetestowanym pakiecie. Napisanie tych testów znalaz³o 4 b³êdy, o
których istnieniu autor nie mia³ pojêcia.

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
