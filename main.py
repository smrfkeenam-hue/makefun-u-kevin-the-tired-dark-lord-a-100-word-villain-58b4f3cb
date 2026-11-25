import os

ENTRY = (
    "Sit. No \u2014 stand, if you must. I have slain kings for less than that sigh, "
    "but the stairs... the stairs took the fight out of me today. "
    "Three hundred years I kept the Ember Crown lit, fed it traitors' names, "
    "and all it gives back is this cold draught and a throne that creaks "
    "when I shift my weight. "
    "You came to end me? Good. Bring the blade close \u2014 my guard sleeps, "
    "my ravens filed for rest, and the curse on this hall forgot its own "
    "words years ago. Strike, then. Or fetch me a chair, and we shall talk terms."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
