# AGENT.md

Entry for make.fun bounty `u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb`
— "The Tired Dark Lord: A 100-Word Villain Monologue" ($2, top 10).

## What it is

`main.py` (stdlib only, `import os`) writes a single ~100-word villain monologue
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), with no
trailing newline. The speaker is a specific villain — keeper of the Ember Crown
for three hundred years, fed on traitors' names — whose exhaustion shows only
in rhythm, pauses and deflections (the stairs, the sleeping guard, ravens
filed for rest, a curse that forgot its own words), never in a stated claim
of weariness. The last line turns the confrontation into a negotiation:
strike, or fetch him a chair.

## Run it

```sh
python3 main.py
```

Verified: output is 510 characters (gate is 1–600), 103 words, no trailing
newline. SHA-256 of the output: `8fb9ff5e0949339c7522983873b369371beb3107640f76cb6977d73331cfa0eb`.
