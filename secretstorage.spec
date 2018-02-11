#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD6FE710363F85DD3 (mitya57@gmail.com)
#
Name     : secretstorage
Version  : 2.3.1
Release  : 11
URL      : http://pypi.debian.net/SecretStorage/SecretStorage-2.3.1.tar.gz
Source0  : http://pypi.debian.net/SecretStorage/SecretStorage-2.3.1.tar.gz
Source99 : http://pypi.debian.net/SecretStorage/SecretStorage-2.3.1.tar.gz.asc
Summary  : Python bindings to FreeDesktop.org Secret Service API
Group    : Development/Tools
License  : BSD-3-Clause
Requires: secretstorage-python3
Requires: secretstorage-python
Requires: cryptography
BuildRequires : cryptography
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://api.travis-ci.org/mitya57/secretstorage.svg
:target: https://travis-ci.org/mitya57/secretstorage
:alt: Travis CI status

%package python
Summary: python components for the secretstorage package.
Group: Default
Requires: secretstorage-python3

%description python
python components for the secretstorage package.


%package python3
Summary: python3 components for the secretstorage package.
Group: Default
Requires: python3-core

%description python3
python3 components for the secretstorage package.


%prep
%setup -q -n SecretStorage-2.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518380236
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
