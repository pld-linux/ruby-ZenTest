Summary:	Ruby Testing framework
Summary(pl):	Szkielet do test�w dla j�zyka Ruby
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
