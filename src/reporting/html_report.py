from jinja2 import Template
from pathlib import Path

REPORT_PATH = Path("data") / "output" / "report.html"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>BI Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #2c3e50; }
        .kpi { margin: 10px 0; font-size: 18px; }
    </style>
</head>
<body>
    <h1>Business Intelligence Report</h1>

    <div class="kpi">Total Revenue: <strong>{{ total_revenue }}</strong></div>
    <div class="kpi">Conversion Rate: <strong>{{ conversion_rate }}</strong></div>
    <div class="kpi">Unique Customers: <strong>{{ unique_customers }}</strong></div>
    <div class="kpi">Transactions: <strong>{{ transactions }}</strong></div>

</body>
</html>
"""

def generate_html_report(kpis: dict):
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    template = Template(HTML_TEMPLATE)
    html = template.render(**kpis)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    return REPORT_PATH
