
import csv
import matplotlib.pyplot as plt
from pathlib import Path

# Find the project folder and input/output files
project_folder = Path(__file__).resolve().parent
csv_file = project_folder / "docs" / "Classification_Summary.csv"
output_file = project_folder / "evidence" / "Classification_Summary_Chart.png"

# Read classification counts from the CSV
labels = []
counts = []

with csv_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        labels.append(row["sensitivity_level"])
        counts.append(int(row["column_count"]))

# Create the chart
plt.figure(figsize=(8, 5))
bars = plt.bar(labels, counts)

plt.title("Data Classification Summary")
plt.xlabel("Sensitivity Level")
plt.ylabel("Number of Columns")
plt.bar_label(bars, padding=3)
plt.ylim(0, max(counts) + 15)
plt.tight_layout()

# Save the chart
output_file.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_file, dpi=200)
plt.close()

print(f"Chart created successfully: {output_file}")
