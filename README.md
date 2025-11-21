SpendSense — Automated Transaction Categorizer

SpendSense is a lightweight prototype that automatically categorizes financial transactions using simple keyword-based rules.
It allows users to upload a CSV file or type a single transaction description to receive instant categorization.
🔗 Demo Video

YouTube / Google Drive Link:
👉 https://drive.google.com/file/d/1rLMX0iis_zOPpN_MgrOJ96x8WVGoXQKM/view?usp=sharing

🔗 Project Report (PDF)

PDF Link:
👉 https://www.canva.com/design/DAG4vfBAGi4/_u6v7xcGCOeYZs0e3vRfvQ/edit?utm_content=DAG4vfBAGi4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
🚀 Features

Upload CSV and categorize transactions instantly

Single-line text categorization

Simple rules-based prototype

Fully offline (Flask backend)

Clean, responsive UI

🛠 Technology Stack

Python (Flask) — Backend

HTML / CSS — Frontend

Pandas — CSV handling

Keyword Rules — Categorization logic

📊 System Architecture
User (CSV Upload / Text Input)
          ↓
Flask Backend (API: /categorize)
          ↓
Categorizer (Keyword Rules)
          ↓
Outputs (CSV / JSON / HTML)

📁 Sample CSV Format
description,amount
Paid Uber to airport,450
Walmart groceries,1200
Dominos pizza order,650

▶ How to Run the Project Locally

Create environment

python -m venv venv


Activate

.\venv\Scripts\activate


Install

pip install -r requirements.txt


Run

python app.py


Open

http://127.0.0.1:5000
