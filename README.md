# jgprayer

A shareable calendar event for **Sunday Prayer**, published on GitHub Pages so it
can be added to a phone by scanning a QR code.

**Live page:** https://jacobriers.github.io/jgprayer/

## The event

| | |
|---|---|
| Title | Sunday Prayer |
| When | Every Sunday, 15:30 – 15:45 (SAST, Africa/Johannesburg) |
| First | Sunday 20 September 2026 |
| Last | Sunday 26 December 2027 |
| Location | *(not set)* |

## What's here

| File | Purpose |
|---|---|
| `index.html` | Landing page the QR code points at. Offers download, Google Calendar, and subscribe. |
| `sunday-prayer.ics` | The calendar file itself (RFC 5545). |
| `qr.png` / `qr.svg` | Print-ready QR code for `https://jacobriers.github.io/jgprayer/`. |
| `tools/make_qr.py` | Regenerates the QR images. |
| `.gitattributes` | Keeps `.ics` line endings as CRLF — see below. |
| `.nojekyll` | Skips Jekyll processing on Pages. |

## Enabling GitHub Pages

**Settings → Pages → Source: Deploy from a branch → `main` / `/ (root)`.**
First deploy takes about a minute.

## Changing the event

Edit `sunday-prayer.ics`, then bump `SEQUENCE` so calendar apps recognise it as an
update rather than ignoring it.

Two things to watch:

1. **Line endings must stay CRLF.** RFC 5545 requires it, and GitHub Pages serves the
   blob exactly as stored in git. `.gitattributes` marks `*.ics` as `-text` so git
   never normalises it — but your editor still can. Verify after editing:

   ```sh
   python3 -c "d=open('sunday-prayer.ics','rb').read(); assert d.count(b'\n')==d.count(b'\r\n')"
   ```

2. **People who *added* the event keep their old copy.** Only those who used
   *Subscribe* will see edits. The QR code itself does not need reprinting — it
   points at the page, not at the file.

Keep `index.html` in step with the `.ics`; the visible times are written into the
page and into the Google Calendar link.

## Regenerating the QR code

```sh
pip install segno
python3 tools/make_qr.py
```

Only necessary if the URL changes — for example, moving to a custom domain.
**A new URL means every already-printed QR code is dead**, so decide on the domain
before printing anything.
