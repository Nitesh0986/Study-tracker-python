import pandas as pd
import matplotlib.pyplot as plt

# Take input
days = []
hours = []

for i in range(5):
    d = input("Enter day: ")
    h = int(input("Enter hours: "))
    days.append(d)
    hours.append(h)

# Create DataFrame
df = pd.DataFrame({
    "Days": days,
    "Hours": hours
})

# Analysis
print("Average:", df["Hours"].mean())
print("Max:", df["Hours"].max())
print("Min:", df["Hours"].min())

# Save data
df.to_csv("study.csv", index=False)

# Plot
plt.plot(df["Days"], df["Hours"], marker='o')
plt.title("Study Tracker")
plt.show()