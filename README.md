# Pandas Portfolio – Excel/CSV Automation Scripts

I'm a math & computing student building simple, accurate Python scripts using Pandas to clean, process, and summarize Excel/CSV data.  
These scripts are standalone .py files that clients can run easily (after `pip install pandas openpyxl`).

All scripts include:
- Basic error handling
- Clear comments
- Tested on sample data
- Export to new Excel file

### Scripts Overview

- **data_cleaner1.py**  
  Loads data and merges columns to handle duplicates or combine info.

- **data_cleaner2.py**  
  Adds new calculated columns (e.g., profit = sales - cost).

- **data_cleaner3.py**  
  Extra basic cleaning steps built on top of previous cleaners (e.g., type conversion, trimming).

- **data_cleaner4.py**  
  Removes duplicate rows and fills missing numeric values with averages.

- **data_cleaner5.py**  
  Computes summary statistics (mean, std, min, max) and saves report.

- **Task1.py**  
  Cleans sales data: removes duplicates, fills missing prices with average, adds profit column, saves cleaned file.

- **Task2.py**  
  Cleans student grades: fills missing scores with subject average, counts A/B/C/D grades per subject, saves summary report.

- **Task3.py**  
  Cleans inventory list: removes invalid/negative stock or blank items, groups by category, adds low-stock flags (<10), saves report with totals.

- **Titanic_analysis.ipynb**  
  Jupyter notebook exploring Titanic dataset (cleaning, grouping, basic stats with Pandas + NumPy).

### How to Use Any Script
1. Install requirements (one time):  
   `pip install pandas openpyxl`
2. Put your Excel/CSV file in the same folder as the .py file
3. Update the file name in the code if needed (e.g. change `'input.xlsx'`).
4. Run: `python script_name.py`
5. Check the new output file created.

Feel free to open issues or fork if you want to improve any script.

Last updated:  13 March 2026
