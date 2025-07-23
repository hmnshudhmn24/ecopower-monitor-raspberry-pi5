def generate_tips(df):
    tips = []
    avg_power = df["Power(W)"].mean()
    max_power = df["Power(W)"].max()
    if max_power > 250:
        tips.append("⚠️ High power usage detected — check large appliances.")
    if avg_power < 100:
        tips.append("✅ Great job! Your average usage is efficient.")
    if "14:00:00" in df["Time"].values:
        tips.append("🔌 Unusual spike at 2 PM — investigate usage.")
    if len(df) > 20:
        tips.append("📈 You've logged over 20 entries — detailed analysis available.")
    return tips