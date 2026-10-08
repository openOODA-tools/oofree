# oofree: Sovereign MEMORY AUDITOR

<div align="center">

```
================================================================================
                                oofree
               Sovereign openOODA MEMORY AUDITOR
================================================================================
```

**Sovereign MEMORY AUDITOR**  
*Sovereign memory auditor and kernel RAM/swap telemetry engine in pure openOODA.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oofree/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oofree-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oofree/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oofree/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oofree-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oofree/uninstall.sh | bash
```

---

## 2. CLI Usage

```
oofree 0.2.0 (openOODA sovereign system & monitor)
usage: oofree [options]

Sovereign memory auditor and kernel RAM/swap telemetry engine.

Display & Unit Options:
  -b, --bytes         show output in bytes
  -k, --kibi          show output in kibibytes (default)
  -m, --mebi          show output in mebibytes
  -g, --gibi          show output in gibibytes
      --tera          show output in terabytes
      --kilo          show output in kilobytes (powers of 1000)
      --mega          show output in megabytes (powers of 1000)
      --giga          show output in gigabytes (powers of 1000)
  -h, --human         show human-readable output (powers of 1024)
      --si            use powers of 1000 not 1024
  -w, --wide          wide output (separate buffers and cache)
  -t, --total         show aggregate total for RAM + swap
  -j, --json          output structured metrics formatted as JSON
  -D, --demo          interactive multi-scenario memory showcase
      --test          execute internal subsystem verification suite
      --mcp           run as Model Context Protocol JSON-RPC stdio server
  -V, --version       output version information and exit
      --help          display this help and exit
```

---

## 3. Theming Integration (`oote`)

`oofree` synchronizes visual styles and status colors with [oote](https://github.com/openOODA-tools/oote):
* **Configuration:** Reads active palette from `~/.openooda/theme.oot`.
* **Environment Overrides:** Respects `$OODA_THEME` and `$NO_COLOR`.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oofree` runs a streaming JSON-RPC 2.0 stdio server exposing 5 tools for AI coding agents:
* `free_memory`: Query current system RAM and swap metrics formatted with unit conversions.
* `free_swap`: Query system swap space metrics, utilization percentage, and health status.
* `free_detailed`: Return comprehensive kernel memory counters including dirty pages, slab, and active/inactive splits.
* `free_pressure`: Analyze RAM, swap, and commit pressure with operational risk classification.
* `free_demo`: Run multi-scenario sovereign memory inspection showcase.

```bash
oofree --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`, `&McpCap`). Physical absence of ambient network or write leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
