%define		module	tasklib
Summary:	Python Task Warrior library
Name:		python3-%{module}
Version:	2.3.0
Release:	3
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/t/tasklib/%{module}-%{version}.tar.gz
# Source0-md5:	4e2523982b161214551286fdbcc7fda0
URL:		https://github.com/robgolding/tasklib
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python3-modules >= 1:3.5
Requires:	taskwarrior
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tasklib is a Python library for interacting with taskwarrior
databases, using a queryset API similar to that of Django’s ORM.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-%{module}
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py3*.egg-info
