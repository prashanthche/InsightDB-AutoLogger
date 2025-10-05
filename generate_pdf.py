import pyautogui
from fpdf import FPDF
import time
import os

# Create folder for screenshots
screenshot_folder = "screenshots"
os.makedirs(screenshot_folder, exist_ok=True)

# Capture DBeaver screenshot
print("Switch to DBeaver... 5 seconds to prepare")
time.sleep(5)
dbeaver_path = os.path.join(screenshot_folder, "dbeaver.png")
pyautogui.screenshot(dbeaver_path)
print("✅ DBeaver screenshot saved")

# Capture Grafana screenshot
print("Switch to Grafana... 5 seconds to prepare")
time.sleep(5)
grafana_path = os.path.join(screenshot_folder, "grafana.png")
pyautogui.screenshot(grafana_path)
print("✅ Grafana screenshot saved")

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Add Unicode-safe fonts
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf", uni=True)

# Title
pdf.set_font("DejaVu", "B", 18)
pdf.cell(0, 10, "InsightDB Auto Logger - Portfolio Guide", ln=True, align='C')
pdf.ln(5)

# Section 1: Project Overview
pdf.set_font("DejaVu", "B", 14)
pdf.cell(0, 8, "1. Project Overview", ln=True)
pdf.set_font("DejaVu", "", 12)
overview = """Goal: Continuous logging of system metrics and web visitors with live dashboards.

Tech Stack:
- PostgreSQL (metrics)
- Python: psycopg2, psutil, faker
- Dashboard: DBeaver / Grafana
- Automation: Windows Task Scheduler

Features:
- Logs CPU, RAM, uptime every 60 seconds
- Logs fake web visitors automatically
- Creates tables if missing
- Runs 24×7 in background
- Live dashboard visualization
"""
pdf.multi_cell(0, 6, overview)
pdf.ln(3)

# Section 2: Database Setup
pdf.set_font("DejaVu", "B", 14)
pdf.cell(0, 8, "2. Database Setup", ln=True)
pdf.set_font("DejaVu", "", 12)
db_setup = """Create Database:
CREATE DATABASE metrics;

Create Tables:

-- System Metrics
CREATE TABLE IF NOT EXISTS system_metrics (
    id SERIAL PRIMARY KEY,
    recorded_at TIMESTAMP NOT NULL,
    cpu_usage NUMERIC(5,2),
    ram_usage NUMERIC(5,2),
    uptime BIGINT
);

-- Web Visitors
CREATE TABLE IF NOT EXISTS web_visitors (
    id SERIAL PRIMARY KEY,
    visited_at TIMESTAMP NOT NULL,
    ip_address VARCHAR(50),
    device VARCHAR(500),
    referrer VARCHAR(200)
);
"""
pdf.multi_cell(0, 6, db_setup)
pdf.ln(3)

# Section 3: Python Script
pdf.set_font("DejaVu", "B", 14)
pdf.cell(0, 8, "3. Python Script", ln=True)
pdf.set_font("DejaVu", "", 12)
python_script = """File: insightdb_autologger.py

- Logs system metrics + fake visitors every 60 seconds
- Creates tables automatically if not exists
- Trims long strings to avoid DB errors

Run manually:
python insightdb_autologger.py

Output:
Starting InsightDB Auto Logger - collecting live data every 60 seconds...
[HH:MM:SS] System -> CPU:16.2% RAM:45.1%
"""
pdf.multi_cell(0, 6, python_script)
pdf.ln(3)

# Section 4: Automation
pdf.set_font("DejaVu", "B", 14)
pdf.cell(0, 8, "4. Automation (Windows Startup)", ln=True)
pdf.set_font("DejaVu", "", 12)
automation_text = """Task Scheduler Setup:
- Action → Create Task
- General → Run with highest privileges
- Trigger → At log on
- Action → Start program:
  Program: C:\\Users\\prash\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe
  Arguments: "C:\\users\\prash\\downloads\\db\\insightdb_autologger.py"
  Start in: C:\\users\\prash\\downloads\\db
- Settings → Allow task on demand, restart if failed

Optional: Use .bat to run hidden & log output:
python "C:\\users\\prash\\downloads\\db\\insightdb_autologger.py" >> "C:\\users\\prash\\downloads\\db\\insightdb.log" 2>&1
"""
pdf.multi_cell(0, 6, automation_text)
pdf.ln(3)

# Section 5: Live Dashboard Screenshots
pdf.set_font("DejaVu", "B", 14)
pdf.cell(0, 8, "5. Live Dashboard Screenshots", ln=True)
pdf.set_font("DejaVu", "", 12)
pdf.multi_cell(0, 6, "DBeaver Table Snapshot:")
pdf.image(dbeaver_path, w=180)
pdf.ln(5)
pdf.multi_cell(0, 6, "Grafana Dashboard Snapshot:")
pdf.image(grafana_path, w=180)
pdf.ln(5)

# Section 6: Recruiter Demo
pdf.set_font("DejaVu", "B", 14)
pdf.cell(0, 8, "6. Recruiter Demo (2 Minutes)", ln=True)
pdf.set_font("DejaVu", "", 12)
demo_text = """1. Show live data in DBeaver or Grafana
2. Highlight continuous logging of CPU, RAM, uptime, visitors
3. Show automation via Task Scheduler
4. Optional: Show insightdb.log → proves 24×7 operation

Placeholders for additional screenshots if needed.
"""
pdf.multi_cell(0, 6, demo_text)

# Save PDF
pdf.output("InsightDB_Portfolio_Visual.pdf")
print("✅ PDF with live screenshots generated successfully!")
