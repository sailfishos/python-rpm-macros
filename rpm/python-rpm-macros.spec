Name:           python-rpm-macros
Version:        3.11
Release:        1
Summary:        The common Python RPM macros

License:        MIT and Python
Source0:        %{name}-%{version}.tar.gz
Patch1:         0001-Use-meego-paths-in-scripts-and-some-comments.patch
Patch2:         0002-brp-python-bytecompile-Ensure-reproducibility-of-inv.patch

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
install -m 644 macros.python macros.python-srpm macros.python3 \
  %{buildroot}%{_rpmmacrodir}/

mkdir -p %{buildroot}%{_rpmluadir}/fedora/srpm
install -p -m 644 -t %{buildroot}%{_rpmluadir}/fedora/srpm python.lua

mkdir -p %{buildroot}%{_rpmconfigdir}/meego
install -p -m 755 -t %{buildroot}%{_rpmconfigdir}/meego \
  brp-fix-pyc-reproducibility \
  brp-python-bytecompile \
  brp-python-hardlink \
  %{nil}

%files
%{_rpmmacrodir}/macros.python

%files -n python-srpm-macros
%{_rpmmacrodir}/macros.python-srpm
%{_rpmluadir}/fedora/srpm/python.lua
%{_rpmconfigdir}/meego/brp-fix-pyc-reproducibility
%{_rpmconfigdir}/meego/brp-python-bytecompile
%{_rpmconfigdir}/meego/brp-python-hardlink

%files -n python3-rpm-macros
%{_rpmmacrodir}/macros.python3
