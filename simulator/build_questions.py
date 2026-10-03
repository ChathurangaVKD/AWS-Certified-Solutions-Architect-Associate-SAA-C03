#!/usr/bin/env python3
"""Parse the practice-question markdown files into simulator/questions.js."""
import json, re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from explain_structure import structure
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent

def squash(s): return re.sub(r"\s+", " ", s).strip()

def clean_expl(s):
    s = re.sub(r"```.*?```", "", s, flags=re.S)
    s = re.sub(r"^\s*[-*] ", "• ", s, flags=re.M)
    s = re.sub(r"\*\*(.*?)\*\*", r"\1", s)
    return re.sub(r"\n{2,}", "\n", s).strip()

def options(text):
    parts = re.split(r"^([A-F])[\.\)] ", text, flags=re.M)
    return {parts[j]: squash(parts[j + 1]) for j in range(1, len(parts) - 1, 2)}

def stem_of(text):
    s = re.split(r"^\*\*Options:\*\*|^[A-F][\.\)] ", text, flags=re.M)[0]
    return re.sub(r"\n---\s*$", "", s).strip()

def module_parse(path):
    mod = re.sub(r"^\d+-", "", path.parent.name).replace("-", " ")
    out, skipped = [], []
    chunks = re.split(r"^#{3,4} Question (\d+)[^\n]*\n", path.read_text(), flags=re.M)
    for i in range(1, len(chunks) - 1, 2):
        n, body = int(chunks[i]), chunks[i + 1]
        am = re.search(r"\*\*Answers?:\s*([A-F](?:\s*(?:,|and|&)\s*[A-F])*)\b", body)
        opts = options(body.split("<details>")[0])
        ans = re.findall(r"[A-F]", am.group(1)) if am else []
        if not ans or len(opts) < 2 or not all(a in opts for a in ans):
            skipped.append((mod, n)); continue
        em = re.search(r"\*\*Explanation:?\*\*:?\s*(.*?)(?=\n\*\*(?:Key Points|References|Memory|Exam)|\n</details>|\Z)", body, re.S)
        out.append(dict(id=f"{path.parent.name[:2]}-{n}", q=stem_of(body.split("<details>")[0]), options=opts, answer=ans,
                        explanation=clean_expl(em.group(1)) if em else "", module=mod, multi=len(ans) > 1))
    return out, skipped

CAT = {"Auto Scaling & High Availability": "Compute", "Storage & Data Management": "Storage", "Databases": "Database",
       "Serverless & Containers": "Application Integration"}

def practice_parse(path):  # 14-Practice: "✓" marks the correct option, category = preceding "## " heading
    out, skipped, cat = [], [], ""
    for blk in re.split(r"^(?=## |### Question )", path.read_text(), flags=re.M):
        if blk.startswith("## "): cat = blk[3:].split("\n")[0].strip(); continue
        m = re.match(r"### Question (\d+)", blk)
        if not m: continue
        n = int(m.group(1)); head = blk.split("**Explanation:**")[0]
        opts, ans = {}, []
        for k, v in options(head).items():
            if "✓" in v: ans.append(k)
            opts[k] = v.replace("✓", "").strip()
        em = re.search(r"\*\*Explanation:\*\*\s*(.*?)(?=\n---|\Z)", blk, re.S)
        if not ans or len(opts) < 2: skipped.append((cat, n)); continue
        out.append(dict(id=f"14-{n}", q=stem_of(head.split("\n", 1)[1]), options=opts, answer=ans,
                        explanation=clean_expl(em.group(1)) if em else "", module=CAT.get(cat, cat), multi=len(ans) > 1))
    return out, skipped

allq, skipped = [], []
for p in sorted(ROOT.glob("[0-9][0-9]-*/PRACTICE-QUESTIONS.md")):
    q, s = (practice_parse if p.parent.name.startswith("14-") else module_parse)(p); allq += q; skipped += s
for q in allq:
    q["why"], q["others"] = structure(q["explanation"], q["answer"], q["options"][q["answer"][0]])
(pathlib.Path(__file__).parent / "questions.js").write_text("window.QUESTIONS = " + json.dumps(allq, indent=1, ensure_ascii=False) + ";\n")
print(len(allq), "questions;", sum(q["multi"] for q in allq), "multi; skipped", skipped)
print(sorted(Counter(q["module"] for q in allq).items()))
