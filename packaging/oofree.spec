Name:           oofree
Version:        0.1.0
Release:        1%{?dist}
Summary:        Displays total, free, cached, buffers, and swap memory with unit conversions.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oofree
Source0:        oofree-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oofree is a sovereign, capability-bounded MEMORY AUDITOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oofree
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oofree-uninstall

%files
/usr/bin/oofree
/usr/bin/oofree-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
