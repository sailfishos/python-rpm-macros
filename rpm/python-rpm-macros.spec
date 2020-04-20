Name:           python-rpm-macros
Version:        3.8
Release:        1
Summary:        The common Python RPM macros

License:        MIT and Python
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
# For %%python3_pkgversion used in %%python_provide
Requires:       python-srpm-macros

%description
This package contains the unversioned Python RPM macros, that most
implementations should rely on.

You should not need to install this package manually as the various
python?-devel packages require it. So install a python-devel package instead.

%package -n python-srpm-macros
Summary:        RPM macros for building Python source packages

%description -n python-srpm-macros
RPM macros for building Python source packages.

%package -n python2-rpm-macros
Summary:        RPM macros for building Python 2 packages
Requires:       python-srpm-macros

%description -n python2-rpm-macros
RPM macros for building Python 2 packages.

%package -n python3-rpm-macros
Summary:        RPM macros for building Python 3 packages
Requires:       python-srpm-macros

%description -n python3-rpm-macros
RPM macros for building Python 3 packages.


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
# We don't package macros.pybytecompile and compileall2.py
# as we are using RPM's version of pybytecompile
install -m 644 macros.python macros.python-srpm macros.python2 macros.python3 \
  %{buildroot}%{_rpmmacrodir}/

%files
%{_rpmmacrodir}/macros.python

%files -n python-srpm-macros
%{_rpmmacrodir}/macros.python-srpm

%files -n python2-rpm-macros
%{_rpmmacrodir}/macros.python2

%files -n python3-rpm-macros
%{_rpmmacrodir}/macros.python3
