import pandas as pd
import matplotlib.pyplot as plt

# Load sample data (or read from CSV)
data = {
    'Month': ['Jan-25', 'Feb-25', 'Mar-25', 'Apr-25', 'May-25', 'Jun-25', 'Jul-25', 'Aug-25'],
    'Productivity_Increase_Pct': [30, 32, 33, 34, 35, 35, 34, 35],
    'Meeting_Time_Reduction_Pct': [18, 19, 20, 20, 21, 20, 19, 20],
    'Tech_Fatigue_Pct': [12, 13, 14, 15, 15, 16, 16, 15]
}
df = pd.DataFrame(data)

# Plot the chart
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Productivity_Increase_Pct'], label='Productivity Increase (%)', color='green', marker='o')
plt.plot(df['Month'], df['Meeting_Time_Reduction_Pct'], label='Meeting Time Reduction (%)', color='orange', marker='o')
plt.plot(df['Month'], df['Tech_Fatigue_Pct'], label='Tech Fatigue (%)', color='red', marker='o')

# Add trend lines (simple linear regression for demo)
from scipy.stats import linregress
for col, color in zip(['Productivity_Increase_Pct', 'Meeting_Time_Reduction_Pct', 'Tech_Fatigue_Pct'], ['green', 'orange', 'red']):
    slope, intercept, _, _, _ = linregress(range(len(df)), df[col])
    plt.plot(df['Month'], [slope * i + intercept for i in range(len(df))], color=color, linestyle='--')

plt.title('AI Impact on Remote Work Productivity, 2025')
plt.xlabel('Month')
plt.ylabel('Percentage')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('ai_remote_work_chart.png')  # Save for LinkedIn or GitHub
plt.show()