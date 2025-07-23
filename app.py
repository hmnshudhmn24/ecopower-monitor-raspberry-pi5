from flask import Flask, render_template_string
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from monitor import read_power_data
from ai_tips import generate_tips

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>🔋 EcoPower Monitor</title>
    <style>
        body { font-family: Arial; padding: 20px; background-color: #f4f4f4; }
        h1 { color: green; }
    </style>
</head>
<body>
    <h1>🔋 EcoPower Monitor</h1>
    <h2>📊 Live Power Usage</h2>
    <img src="data:image/png;base64,{{ plot_url }}"/>
    <h2>🧠 AI Suggestions</h2>
    <ul>
    {% for tip in tips %}
        <li>{{ tip }}</li>
    {% endfor %}
    </ul>
</body>
</html>
'''

@app.route('/')
def dashboard():
    df = pd.read_csv("usage_log.csv")
    plt.figure()
    df.tail(20).plot(x="Time", y="Power(W)", kind="line")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plot_url = base64.b64encode(buf.read()).decode('utf-8')
    tips = generate_tips(df)
    return render_template_string(TEMPLATE, plot_url=plot_url, tips=tips)

if __name__ == '__main__':
    app.run(debug=True)