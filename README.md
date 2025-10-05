# InsightDB Auto Logger

A complete **system metrics & web visitor logger** with live dashboards and recruiter-ready PDF reports.

---

## Features
- Logs CPU, RAM, uptime every 60 seconds
- Logs fake web visitors for testing
- Creates PostgreSQL tables automatically
- Runs 24×7 on Windows
- Generates recruiter-ready PDF with screenshots

---

## Tech Stack
- **Database:** PostgreSQL
- **Language:** Python 3.12
- **Libraries:** psycopg2, psutil, faker, fpdf, pyautogui, pillow
- **Dashboard:** DBeaver & Grafana

---

## Setup Instructions

1. Install Python libraries:
```bash
pip install psycopg2 psutil faker fpdf pyautogui pillow
