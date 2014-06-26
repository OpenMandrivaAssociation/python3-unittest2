%define oname unittest2



Name:           python3-%{oname}
Version:        0.5.1
Release:        1
Url:            http://pypi.python.org/pypi/unittest2
Summary:        Backport ofunittest2 to Python3
License:        BSD
Group:          Development/Python
Source:         http://pypi.python.org/packages/source/u/unittest2py3k/%{oname}py3k-%{version}.tar.gz
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3egg(setuptools)
Requires:       python3
BuildArch:	noarch



%description
unittest2 is a backport of the new features added to the unittest
testing framework in Python 2.7. It has been tested to on Python 2.4 -
2.6.

To use unittest2 instead of unittest simply replace ``import
unittest`` with ``import unittest2``.

Classes in unittest2 derive from the equivalent classes in unittest,
so it should be possible to use the unittest2 test running infra-
structure without having to switch all your tests to using unittest2
immediately. Similarly, you can use the new assert methods on
``unittest2.TestCase`` with the standard unittest test running
infrastructure. Not all of the new features in unittest2 will work
with the standard unittest test loaders and runners, however.
This is python3 module.

%prep
%setup -qn %{oname}py3k-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

# rename py3 binaries for coexsistance
mv %{buildroot}%{_bindir}/unit2 %{buildroot}%{_bindir}/unit2-python%{py3_ver}
mv %{buildroot}%{_bindir}/unit2.py %{buildroot}%{_bindir}/unit2-python%{py3_ver}.py


%files
%doc README.txt
%{_bindir}/unit2-python%{py3_ver}*
%{py3_puresitedir}/unittest2/
%{py3_puresitedir}/unittest2py3k-%{version}-py%{py3_ver}.egg-info

