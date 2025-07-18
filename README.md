# Mood Logger CLI 🧠  
A simple yet powerful command-line tool to log, filter, and analyze moods using `argparse`, `datetime`, and `csv`.  
Built as part of a personal 12-week Python relearning journey — inspired by the need for emotional journaling and self-reflection.

---

## 🚀 Features

- Log moods using `--name` and `--mood`
- Filter entries by `--name`, `--mood`, and `--date`
- View all logged moods (`--view`)
- Analyze mood frequency stats (`--stats`)
- Built entirely using standard Python libraries — no external dependencies
- Clean and extendable structure for future journaling, tagging, or visualization upgrades

---

## 🖥️ Usage Examples

```bash
# Log a mood
python mood_logger.py --name honestgpt --mood happy

# View full mood history
python mood_logger.py --view

# View frequency stats
python mood_logger.py --stats

# Filter logs by name and mood
python mood_logger.py --filter --name pyaradox --mood happy

# Filter by date (YYYY-MM-DD format)
python mood_logger.py --filter --date 2025-07-11

# Combine filters
python mood_logger.py --filter --name honestgpt --mood calm --date 2025-07-11
```

---

## 📂 File Structure

```plaintext
mood_logger.py       # Main CLI script
mood_log.csv         # Auto-generated log file storing entries (timestamp, name, mood)
README.md            # This file
```

---

## 🔧 Tech Stack

- Python 3.x
- `argparse` — for command-line interface
- `csv` — for lightweight file-based storage
- `datetime` — for logging and filtering by date
- `collections.Counter` — for simple mood frequency analytics

---

## 🌱 Why This Project?

This project wasn't just about Python — it was about rebuilding discipline, confidence, and clarity. Logging moods felt like a small but symbolic act of taking ownership over time and self-awareness. It also helped refine CLI skills, string parsing, and input validation in a personal way.

> _"Sometimes, the best tool you build is the one that understands you.” _ — Param

---

## ✅ Future Plans

- Add support for mood tags (e.g. `--tags grateful, focused`)
- Export filtered data to JSON or Markdown
- Weekly mood summaries (analytics)
- GUI version with Tkinter or Streamlit
- AI-assisted pattern detection (future concept)

---

## 🧠 Lessons Learned

- Small tools matter when built with heart
- CLI apps teach real-world thinking: input, validation, structure
- Working with CSV manually boosts your control over data

---

## 📜 License

This project is licensed under the MIT License.
