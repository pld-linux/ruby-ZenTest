Summary:	Ruby Testing framework
Summary(pl):	Szkielet do testów dla jêzyka Ruby
Name:		ruby-ZenTest
Version:	2.3.0
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/1944/ZenTest-%{version}.tar.gz
# Source0-md5:	f94eed12075025c3e7090520b95e8eab
BuildRequires:	ruby-modules
BuildRequires:	sed >= 4.0
Requires:	ruby-modules
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
find . -name '*.rb' | xargs sed -i -e '1s,#!.*local/bin/ruby#!%{_bindir}/ruby#'

%build
%{__make}

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
