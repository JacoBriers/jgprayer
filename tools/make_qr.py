#!/usr/bin/env python3
"""Regenerate the printable QR code for the Sunday Prayer landing page.

Usage:
    pip install segno
    python3 tools/make_qr.py

Writes qr.png and qr.svg at the repo root. If the site ever moves to a
custom domain, change URL below, re-run, and reprint anything already
distributed -- the old QR will point at the old address.
"""
import pathlib
import segno

URL = "https://jacobriers.github.io/jgprayer/"
DARK = "#1d3b64"  # --jg-navy
LIGHT = "#ffffff"

root = pathlib.Path(__file__).resolve().parent.parent

# error='h' -> 30% error correction, so the code still scans when a print
# is smudged, folded, or partly covered.
qr = segno.make(URL, error="h")

qr.save(root / "qr.png", scale=24, border=4, dark=DARK, light=LIGHT)
qr.save(root / "qr.svg", scale=24, border=4, dark=DARK, light=LIGHT)

print(f"encoded : {URL}")
print(f"version : {qr.version}  error: {qr.error.upper()}")
print(f"wrote   : {root / 'qr.png'}")
print(f"wrote   : {root / 'qr.svg'}")
