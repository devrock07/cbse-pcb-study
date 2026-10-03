# PCB Boardroom

A free, offline-friendly CBSE Class 12 Physics, Chemistry and Biology study webpage.

## Open it

Download **[PCB-Boardroom.html](PCB-Boardroom.html)** using GitHub’s download button, then open the downloaded file in Chrome, Edge or another browser. No installation, account or local server is needed. The webpage itself works offline; original-paper links need internet access.

The repository is public. The downloaded HTML also works without hosting.

## Deploy on Vercel

Import this repository with the Root Directory left at the repository root. The included `vercel.json` selects the static-site preset, skips installation/build commands, and serves `dist/`, where `index.html` and its assets live. A connected GitHub project redeploys when changes are pushed; otherwise redeploy the latest commit from the Vercel dashboard.

## What is inside

- 133 independently written worked selections across all 37 current PCB chapters.
- 69 groups of related PYQs, with specific year, set and question references.
- Subject/chapter navigation, search, year filters, collapsible answers, revision flags and printing.
- A study plan aimed at improving written answers and working toward 90%; no selection can guarantee a score.
- Current-syllabus notes and original-paper/marking-scheme links.

## Scope and limits

The source pool contains one representative paper per subject for **2016–2020 and 2022–2026**: 30 source papers across ten exam years. **2022 covers Term II only.** The cancelled 2021 annual exam is not counted. The 2019 papers are third-party reproductions; other source links point to CBSE archives. The selected 2016 Physics/Chemistry sets carry `/C` in their codes.

This is a **curated selection**, not all questions, all regional sets, a complete solutions book or a statistical prediction. Some entries deliberately select one branch or subpart. Questions are paraphrased. Related groups demonstrate recurring concepts/methods; the displayed number of years refers to listed examples, not an exhaustive recurrence frequency.

Explanations are study solutions, **not official CBSE marking-scheme quotations or allocations**. Check the matching original paper and marking scheme for full wording, diagrams, alternatives and marks. The syllabus check uses CBSE’s **2026–27** documents. A few questions per chapter do not replace NCERT, complete syllabus coverage or timed full papers.

Progress is stored only in the browser’s local storage. It is not synced to GitHub or sent anywhere. Clearing browser data or changing browser/location may reset the log.

## Files

- `PCB-Boardroom.html`: single-file offline webpage.
- `dist/`: editable static HTML, CSS, JavaScript and study data.
- `scripts/build_offline.py`: rebuilds the single-file version using standard Python.

Run `python scripts/build_offline.py` after editing `dist/`.

## Sources

- [CBSE question-paper archive](https://www.cbse.gov.in/cbsenew/question-paper.html)
- [CBSE marking-scheme archive](https://www.cbse.gov.in/cbsenew/marking-scheme.html)
- [CBSE 2026–27 curriculum](https://cbseacademic.nic.in/curriculum_2027.html)

Specific archives, PDF filenames and question references are available inside the webpage under **Papers, syllabus & coverage**. Original exam archives are linked, not republished in this repository. Research checked on 3 October 2026.
