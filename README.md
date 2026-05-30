# Python Learning — Week 4 Review

A review and consolidation of the first three weeks of Python learning.

---

## What I Reviewed

### Projects
- **To-Do List** — CLI task manager with add, complete, and delete features
- **String Utils** — Utility library with `reverse_words`, `count_vowels`, and `is_palindrome`
- **BMI Calculator** — Calculates BMI from user input and saves records to a JSON file

---

### Key Concepts Practiced

**Data Structures & Error Handling**
- Dictionary and List operations
- `try/except` exception handling

**JSON File I/O**
- Reading and writing JSON files
- Loading and saving structured data with `json.load()` and `json.dump()`

**Git Branch Workflow**
- Creating a new branch and making changes on it
- Merging the branch back into `main`
- Pushing local code to GitHub

---

## Git Workflow Used

```bash
git checkout -b feature/branch-name   # Create new branch
git add .
git commit -m "feat: ..."             # Commit changes
git checkout main
git merge feature/branch-name         # Merge back to main
git push origin main                  # Push to GitHub
```

---

## Tech Stack

- Python 3.14
- `json`, `os` — built-in modules
- `pytest` — test framework
