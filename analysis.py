import csv

# Read the CSV into a list of dictionaries
rows = []
with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# ----- Question 1: How many requests are currently open? -----
open_count = 0
for row in rows:
    if row['resolution_status'] == 'Open':
        open_count += 1

q1_output = f"Open requests: {open_count}"

# ----- Question 2: What is the most common complaint type? -----
complaint_counts = {}
for row in rows:
    complaint = row['complaint_type']
    complaint_counts[complaint] = complaint_counts.get(complaint, 0) + 1

most_common_complaint = max(complaint_counts, key=complaint_counts.get)
most_common_count = complaint_counts[most_common_complaint]

q2_output = f"Most common complaint type: {most_common_complaint} ({most_common_count} requests)"

# ----- Question 3: How many requests were submitted per borough? -----
borough_counts = {}
for row in rows:
    borough = row['borough']
    borough_counts[borough] = borough_counts.get(borough, 0) + 1

q3_lines = ["Requests per borough:"]
for borough in sorted(borough_counts):
    q3_lines.append(f"- {borough}: {borough_counts[borough]}")
q3_output = "\n".join(q3_lines)

# ----- Question 4: Requests by complaint type, sorted highest to lowest -----
q4_lines = ["Requests by complaint type:"]
sorted_complaints = sorted(complaint_counts.items(), key=lambda x: x[1], reverse=True)
for complaint, count in sorted_complaints:
    q4_lines.append(f"- {complaint}: {count}")
q4_output = "\n".join(q4_lines)

# ----- Question 5: Which borough has the most open requests? -----
open_by_borough = {}
for row in rows:
    if row['resolution_status'] == 'Open':
        borough = row['borough']
        open_by_borough[borough] = open_by_borough.get(borough, 0) + 1

top_open_borough = max(open_by_borough, key=open_by_borough.get)
top_open_count = open_by_borough[top_open_borough]

q5_output = f"Borough with most open requests: {top_open_borough} ({top_open_count} open)"

# ----- Question 6: Closure rate by borough -----
closed_by_borough = {}
for row in rows:
    if row['resolution_status'] == 'Closed':
        borough = row['borough']
        closed_by_borough[borough] = closed_by_borough.get(borough, 0) + 1

q6_lines = ["Closure rate by borough:"]
for borough in sorted(borough_counts):
    total = borough_counts[borough]
    closed = closed_by_borough.get(borough, 0)
    rate = (closed / total) * 100
    q6_lines.append(f"- {borough}: {rate:.1f}%")
q6_output = "\n".join(q6_lines)

# ----- Question 7: Top 3 boroughs by total requests -----
sorted_boroughs = sorted(borough_counts.items(), key=lambda x: (-x[1], x[0]))
top_3 = sorted_boroughs[:3]

q7_lines = ["Top 3 boroughs by total requests:"]
for i, (borough, count) in enumerate(top_3, start=1):
    q7_lines.append(f"{i}. {borough} ({count} requests)")
q7_output = "\n".join(q7_lines)

# ----- Write everything to output.txt -----
all_output = "\n\n".join([
    q1_output,
    q2_output,
    q3_output,
    q4_output,
    q5_output,
    q6_output,
    q7_output
])

with open('output.txt', 'w') as f:
    f.write(all_output + "\n")

print("Output saved to output.txt")