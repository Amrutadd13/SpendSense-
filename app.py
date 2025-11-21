from flask import Flask, render_template, request, jsonify
import pandas as pd, csv, io
from werkzeug.utils import secure_filename

app = Flask(__name__)

CATEGORIES = {
    "Food & Dining": ["restaurant","cafe","pizza","domino"],
    "Groceries": ["supermarket","grocery","store"],
    "Travel": ["uber","ola","bus","train","flight"],
    "Bills & Utilities": ["bill","electricity","internet","mobile"],
    "Shopping": ["amazon","flipkart","myntra"],
    "Entertainment": ["netflix","prime","movie","ticket"],
    "Salary": ["salary","payroll","credit"],
    "Others": []
}

def categorize(desc):
    d = desc.lower()
    for cat, keys in CATEGORIES.items():
        for k in keys:
            if k in d:
                return cat
    return "Others"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categorize', methods=['POST'])
def categorize_route():
    if 'file' in request.files and request.files['file'].filename:
        f = request.files['file']
        content = f.read().decode('utf-8', errors='ignore')
        reader = csv.DictReader(io.StringIO(content))
        out = []
        for r in reader:
            desc = r.get('description') or ''
            amt = r.get('amount') or ''
            out.append({"description": desc, "amount": amt, "category": categorize(desc)})
        return jsonify(out)
    text = request.form.get('text','')
    return jsonify({"description": text, "category": categorize(text)})

if __name__ == "__main__":
    app.run(debug=True)
