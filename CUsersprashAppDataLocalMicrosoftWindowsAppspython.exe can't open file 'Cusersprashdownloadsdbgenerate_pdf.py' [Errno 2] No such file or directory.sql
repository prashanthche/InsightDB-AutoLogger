from fpdf import FPDF

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 18)
pdf.cell(0, 10, "InsightDB Auto Logger – Portfolio Guide", ln=True, align='C')
pdf.ln(5)

# Section 1: Overview
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 8, "1. Project Overview", ln=True)
pdf.set_font("Arial", '', 12)
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
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 8, "2. Database Setup", ln=True)
pdf.set_font("Arial", '', 12)
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
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 8, "3. Python Script", ln=True)
pdf.set_font("Arial", '', 12)
python_script = """File: insightdb_autologger.py

- Logs system metrics + fake visitors every 60 seconds
- Creates tables automatically if not exists
- Trims long strings to avoid DB errors

Run manually:
python insightdb_autologger.py

Output:
🚀 InsightDB Auto Logger Started — collecting live data every 60 seconds...
[HH:MM:SS] System -> CPU:16.2% RAM:45.1%
"""
pdf.multi_cell(0, 6, python_script)
pdf.ln(3)

# Section 4: Automation
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 8, "4. Automation (Windows Startup)", ln=True)
pdf.set_font("Arial", '', 12)
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

# Section 5: Live Dashboard
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 8, "5. Live Dashboard", ln=True)
pdf.set_font("Arial", '', 12)
dashboard_text = """Option A – DBeaver
- System Metrics Query: SELECT recorded_at, cpu_usage, ram_usage FROM system_metrics ORDER BY recorded_at DESC LIMIT 100;
- Web Visitors Query: SELECT visited_at, ip_address, device FROM web_visitors ORDER BY visited_at DESC LIMIT 100;
- Use Line Chart for CPU/RAM, Bar Chart for visitors
- Auto-refresh: 60 seconds

Option B – Grafana
- PostgreSQL datasource → metrics
- CPU/RAM Query: SELECT recorded_at AS "time", cpu_usage, ram_usage FROM system_metrics ORDER BY recorded_at;
- Visitors Query: SELECT date_trunc('minute', visited_at) AS "time", COUNT(*) AS visitors FROM web_visitors GROUP BY 1 ORDER BY 1;
- Dashboard refresh: 30–60 seconds
"""
pdf.multi_cell(0, 6, dashboard_text)
pdf.ln(3)

# Section 6: Recruiter Demo
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 8, "6. Recruiter Demo (2 Minutes)", ln=True)
pdf.set_font("Arial", '', 12)
demo_text = """1. Show live data in DBeaver or Grafana
2. Highlight continuous logging of CPU, RAM, uptime, visitors
3. Show automation via Task Scheduler
4. Optional: Show insightdb.log → proves 24×7 operation

Placeholders for Screenshots:
- [DBeaver table updates]
- [Grafana dashboard]
- [Task Scheduler task]
"""
pdf.multi_cell(0, 6, demo_text)

# Save PDF
pdf.output("InsightDB_Portfolio_Guide.pdf")
print("✅ PDF generated: InsightDB_Portfolio_Guide.pdf")
