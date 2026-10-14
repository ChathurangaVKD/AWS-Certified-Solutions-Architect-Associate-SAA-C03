# Module 14: Practice & Exam Prep

## Overview
This module is where you turn what you learned in Modules 1-13 into exam readiness. It collects the exam format, practice questions, flashcards, study notes, a results tracker and the final-week cheat sheets in one place, and points you to the full practice-test reviews and the online exam simulator.

> **⚠️ Disclaimer:** All questions in this repository are **original practice questions** written for study purposes. They are **not** real exam questions. Exam details below come from this repo's own notes, so confirm them on the [official AWS exam page](https://aws.amazon.com/certification/certified-solutions-architect-associate/) before you book.

## Learning Objectives
- Know the SAA-C03 exam format, domains and question types
- Practice with scenario-based questions and learn the elimination strategy
- Find your weak areas and fix them with focused review
- Run timed practice exams and track your scores over time
- Finish with a final-week checklist and exam-day plan

---

## 1. Exam at a Glance (SAA-C03)

| Item | Detail |
|------|--------|
| **Questions** | 65 (50 scored + 15 unscored, unmarked) |
| **Time** | 130 minutes |
| **Formats** | Multiple choice (1 of 4) and multiple response (2+ of 5+) |
| **Passing score** | 720 / 1000 |
| **Validity** | 3 years |

| Exam domain | Weight | Main modules |
|-------------|:------:|--------------|
| 1. Design **Secure** Architectures | 30% | [02 IAM](../02-IAM/README.md), [07 Security](../07-Security/README.md), [06 Networking](../06-Networking/README.md) |
| 2. Design **Resilient** Architectures | 26% | [08 Application Integration](../08-Application-Integration/README.md), [12 Architecture Patterns](../12-Architecture-Patterns/README.md), [05 Database](../05-Database/README.md) |
| 3. Design **High-Performing** Architectures | 24% | [03 Compute](../03-Compute/README.md), [04 Storage](../04-Storage/README.md), [11 Analytics](../11-Analytics/README.md) |
| 4. Design **Cost-Optimized** Architectures | 20% | [13 Cost Optimization](../13-Cost-Optimization/README.md) |

The module mapping is a guide, not a rule: most real questions mix services from several modules.

---

## 2. What's in This Folder

| File | Use it for | Time |
|------|-----------|------|
| [ULTRA-FAST-LEARN.md](ULTRA-FAST-LEARN.md) | Exam format, key topics and tactics on one cheat sheet | 15 min |
| [FAST-LEARN.md](FAST-LEARN.md) | Question-type strategies, the elimination method, must-memorize facts, final checklist | 30-45 min |
| [PRACTICE-QUESTIONS.md](PRACTICE-QUESTIONS.md) | 15 mixed scenario questions with answers and explanations | 20-30 min |
| [FLASHCARDS.md](FLASHCARDS.md) | Quick recall of key services and best practices | 10-15 min |
| [STUDY-NOTES.md](STUDY-NOTES.md) | Consolidated notes, common mistakes and corrections | 20 min |
| [SERVICE-QUESTION-MAPPING.md](SERVICE-QUESTION-MAPPING.md) | Which module's practice questions cover which AWS service (draft) | lookup |
| [TEST-RESULTS-TRACKER.md](TEST-RESULTS-TRACKER.md) | Template for logging practice-test scores and weak areas | ongoing |

Each module also has its own `PRACTICE-QUESTIONS.md`, so you can drill one topic at a time.

---

## 3. Recommended Practice Workflow

1. **Finish the modules** you are weakest in first ([Module 1-13](../README.md)).
2. **Warm up** with [PRACTICE-QUESTIONS.md](PRACTICE-QUESTIONS.md) and the per-module question files.
3. **Take a full timed practice test** (65 questions, 130 minutes, no notes). Use the [online exam simulator](https://chathurangavkd.github.io/AWS-Certified-Solutions-Architect-Associate-SAA-C03/simulator/) or any practice-test provider you prefer.
4. **Review every question**, including the ones you got right by guessing. Write down *why* each wrong option is wrong.
5. **Log the result** in the [tracker](TEST-RESULTS-TRACKER.md) and note which domain or service lost points.
6. **Fix the weak areas** with the module's FAST-LEARN and [STUDY-NOTES.md](STUDY-NOTES.md), then repeat from step 3.
7. **Final week:** use [FLASHCARDS.md](FLASHCARDS.md), the [ULTRA-FAST-LEARN](ULTRA-FAST-LEARN.md) sheet and the checklist in [FAST-LEARN.md](FAST-LEARN.md).

A reasonable readiness target is scoring **75-80% or better on several full practice tests in a row** before you sit the real exam.

---

## 4. Elimination Strategy (Short Version)

1. Read the question **twice** and identify what problem it is actually asking you to solve.
2. Highlight the **constraints**: MOST / LEAST, cost, availability, performance, compliance, "least operational overhead".
3. Remove options that **break a constraint** or use the wrong service for the job.
4. Between the last two, prefer the **managed, simpler, AWS-native** option unless the question says otherwise.
5. Flag it and move on if you are stuck after about 2 minutes. You can return to it.

The full version, with examples and common traps, is in [FAST-LEARN.md](FAST-LEARN.md).

---

## 5. Deeper Review Material

- [Practice-test reviews](../exam-reviews/START-HERE.md): detailed write-ups of past practice attempts, with condensed versions and quick-reference sheets
- [Study progress tracker](../exam-reviews/STUDY-PROGRESS-TRACKER.md): longer-term tracking across attempts
- [Study guides](../docs/study-guides/STUDY-ROADMAP.md): roadmap, flashcards and quick-study notes

---

## Next Steps
- Take a timed practice test and record your score in the [tracker](TEST-RESULTS-TRACKER.md)
- Revisit the module for your lowest domain, then test again
- Back to the [course overview](../README.md)
