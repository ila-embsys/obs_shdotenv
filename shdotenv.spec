#
# spec file for package shdotenv
#

Name:           shdotenv
Version:        1.2.3
Release:        1
Summary:        Dotenv loader and parser for POSIX-compliant shells
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/ko1nksm/shdotenv
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  sed
Requires:       /bin/sh
Requires:       awk
BuildArch:      noarch

%description
shdotenv is a dotenv loader and parser written in POSIX-compliant shell script
with embedded awk. It loads environment variables from .env files and can
export them or convert .env files to various formats (e.g. sh, csh, fish, json,
jsonl, yaml).

%prep
%autosetup -p1

%build
%make_build build

%install
install -D -p -m 0755 shdotenv %{buildroot}%{_bindir}/shdotenv

%check
./shdotenv --version
./shdotenv -d posix -f json < /dev/null

%files
%license LICENSE
%doc README.md docs/
%{_bindir}/shdotenv

%changelog
* Wed Oct 21 2026 ila <ila.embsys@gmail.com> - 0.14.0-0
- Initial package of shdotenv at latest upstream release tag
