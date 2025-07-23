# 🔋 EcoPower Monitor - Raspberry Pi

🌱 A smart energy usage tracker built using a Raspberry Pi. It uses sensors to monitor real-time power consumption and provides AI-powered suggestions to save energy.


## 🚀 Features

- 📉 Real-time power monitoring using current/voltage sensors (ACS712/INA219)
- 📊 Live graph of power usage over time
- 🧠 AI-based energy-saving tips based on usage patterns
- 🔔 Alert system for power surges or wastage
- 📝 Daily and weekly usage logs
- 📡 Remote access via Flask-based web dashboard


## 📦 Requirements

- Raspberry Pi (any version with GPIO)
- ACS712 / INA219 current sensor
- Python 3.x
- Libraries:
  - `flask`
  - `matplotlib`
  - `smtplib` (optional for alerts)
  - `pandas`, `numpy`
  - `RPi.GPIO` or `gpiozero`

Install with:

```bash
pip install flask matplotlib pandas numpy
```


## 🧠 How It Works

1. Raspberry Pi reads current data from the ACS712 sensor.
2. Calculates power in real-time and logs it.
3. Displays live graph via a web dashboard.
4. AI component checks historical usage and generates tips like:
   - "Unplug idle devices"
   - "Usage spike detected at 2 PM — check appliances"


## 🖥️ Web Dashboard

Access it locally:

```bash
python app.py
# Then open http://localhost:5000
```

Live graph, daily report, and tips are shown.


## 📂 Project Structure

```
eco-power-monitor-raspberry-pi/
├── app.py                # Flask web server + live dashboard
├── monitor.py            # Sensor reading + logging
├── ai_tips.py            # AI logic for usage analysis
├── static/
│   └── style.css         # Optional styling
└── usage_log.csv         # Daily energy usage log
```


## 🤖 Future Ideas

- Add support for solar panel stats
- Export data to cloud (Google Sheets or Firebase)
- Integrate voice alerts with a speaker
- MQTT support for IoT integration

