"""Split a prose explanation into 'why the answer is right' and 'why each other option is wrong'.
Shared by the AIF-C01 and SAA-C03 simulators (kept as a plain module so build scripts can import it)."""
import re

REF = re.compile(r"\(([A-F](?:(?:,|, and| and|&)\s*[A-F])*)\)")                 # "(A)", "(A, C)", "(A and B)"
LEAD = re.compile(r"^(?:Options?\s+)?([A-F](?:(?:,|, and| and|&)\s*[A-F])*)(?=\s+(?:[a-z]|—|-|:)|\s*:)")   # "A states…", "C and D describe…", "Option B: …"
ABBR = [("e.g.", "e§g§"), ("i.e.", "i§e§"), ("vs.", "vs§"), ("etc.", "etc§"), ("approx.", "approx§")]

def _letters(s): return re.findall(r"[A-F]", s)

def _sentences(line):
    for a, b in ABBR: line = line.replace(a, b)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])|;\s+", line)
    out = []
    for p in parts:
        for a, b in ABBR: p = p.replace(b, a)
        p = p.strip()
        if p: out.append(p[0].upper() + p[1:] + ("" if p[-1] in ".!?\"')" else "."))
    return out

def structure(text, answer, correct_text=""):
    text = re.sub(r"\s*\*?\(Domain \d\)\*?\s*$", "", text.strip())
    text = re.sub(r"^Domain \d\.\s*", "", text)
    text = text.replace("*", "")
    why, others = [], []
    first = True
    for line in [l.strip() for l in text.split("\n") if l.strip()]:
        line = re.sub(r"^•\s*", "", line)
        for s in _sentences(line):
            # the opening sentence usually just restates the correct option; drop it when it does
            if first:
                first = False
                if correct_text and len(s) < 160 and correct_text.lower()[:20] in s.lower():
                    continue
            letters = []
            m = LEAD.match(s)
            if m: letters = _letters(m.group(1))
            else:
                for r in REF.findall(s): letters += _letters(r)
            wrong = [l for l in dict.fromkeys(letters) if l not in answer]
            if wrong and not any(l in answer for l in letters):
                if m:  # the chip already shows the letter(s), so drop them from the sentence
                    s = s[m.end():].lstrip(" :—-–")
                    s = s[0].upper() + s[1:]
                others.append({"l": wrong, "t": s})
            else:
                why.append(s)
    return why, others
