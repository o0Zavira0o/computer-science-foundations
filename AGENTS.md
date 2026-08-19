# Repository Agent Instructions

For any curriculum or educational change:

1. Read `AI_INSTRUCTIONS.md`.
2. Read `SYSTEM.json`.
3. Follow `docs/LEARNING_SYSTEM.md`.
4. Treat canonical JSON as source of truth and generated Markdown as views.
5. Use targeted retrieval in normal sessions; reserve recursive scans for explicit audits.
6. Run `python scripts/csf.py sync` and `python scripts/csf.py audit` after canonical changes when execution is available.
