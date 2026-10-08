Name:           oofree
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign memory auditor and kernel RAM/swap telemetry engine in pure openOODA.
License:        Apache-2.0
URL:            https://github.com/openOODA-tools/oofree
Source0:        oofree-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oofree is a sovereign, capability-bounded memory auditor and kernel RAM/swap
telemetry coordinator written in 100% pure native openOODA with zero ambient authority,
human-scaled unit conversions, commit charge tracking, and streaming Model Context Protocol (MCP) support.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oofree
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oofree-uninstall

%files
/usr/bin/oofree
/usr/bin/oofree-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign memory auditor and swap telemetry engine with streaming MCP
