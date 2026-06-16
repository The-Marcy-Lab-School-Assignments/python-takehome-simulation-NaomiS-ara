# NYC 311 Service Requests Analysis

## How to Run

1. Make sure you have Python 3 installed.
2. Navigate to this folder in your terminal.
3. Run the script:

python3 analysis.py

Output will be saved to `output.txt`. The console will confirm when the file has been written.

## What This Script Does

[Write 2-3 sentences describing what your script does in plain English.]

This script reads NYC 311 service request data from a CSV file and analyzes it to answer seven questions about request volume, complaint types, and resolution status. It counts and aggregates requests by borough and complaint type, calculates closure rates, and identifies top results (most common complaint, most open requests, top boroughs by volume). All results are formatted as readable text and written to output.txt.

## Dependencies

This script uses only Python's built-in libraries: `csv`.

## Notes

[Optional: anything you want to flag about your approach or assumptions.]

Boroughs and complaint types are counted using dictionaries built up while looping through the rows once. Closure rate is calculated as closed requests divided by total requests for each borough, multiplied by 100 and rounded to one decimal place. For Question 7, ties in total requests are broken alphabetically by borough name using a sort key of (-count, borough_name)
