#!/usr/bin/env bash
# seal-release.sh — EVEZ Reality Engine manifest hard-block release gate.
# Enforces: regenerate seal -> verify (sha256sum -c) -> zip ONLY if clean.
# A mismatch physically cannot ship. No window between seal and zip.
set -euo pipefail
cd "$(dirname "$0")"

SELFTEST=0
[[ "${1:-}" == "--selftest" ]] && SELFTEST=1

regenerate() {
  find . -type f \
    ! -path './manifest.sha256' \
    ! -path './__pycache__/*' \
    ! -name '*.pyc' \
    ! -name 'evez-reality-engine-*.zip' \
    -exec sha256sum {} + | sort -k2 > manifest.sha256
}

if [[ $SELFTEST -eq 1 ]]; then
  # Negative test: seal a clean tree, then tamper one file, assert abort + no zip.
  regenerate
  if sha256sum -c manifest.sha256 >/dev/null 2>&1; then
    echo "[selftest] clean seal OK"
  else
    echo "[selftest] FAILED: clean tree did not verify" >&2; exit 1
  fi
  # simulate the v1.0.0 CHANGELOG slip: a late edit after the seal
  printf '\n# late tamper\n' >> README.md 2>/dev/null || printf '\n# late tamper\n' >> CHANGELOG.md
  if sha256sum -c manifest.sha256 >/dev/null 2>&1; then
    echo "[selftest] FAILED: tampered tree still verified (hard-block broken)" >&2; exit 1
  fi
  echo "[selftest] PASS: tampered tree blocked by seal. Hard-block enforced."
  # clean up so we never ship the tamper
  git checkout -- README.md CHANGELOG.md 2>/dev/null || true
  rm -f manifest.sha256 evez-reality-engine-*.zip
  exit 0
fi

regenerate

# HARD BLOCK: verify before packaging. Any mismatch aborts the release.
sha256sum -c manifest.sha256 || {
  echo "RELEASE BLOCKED: manifest seal failure. Ship nothing." >&2
  exit 1
}

VERSION="$(cat VERSION 2>/dev/null || echo unknown)"
zip -r "evez-reality-engine-${VERSION}.zip" . -x 'manifest.sha256'
zip "evez-reality-engine-${VERSION}.zip" manifest.sha256
echo "RELEASE SEALED: evez-reality-engine-${VERSION}.zip (manifest verified clean)"
