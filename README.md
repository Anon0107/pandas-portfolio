# Pandas Portfolio – Excel/CSV Automation Scripts

I'm a math & computing student building simple, accurate Python scripts using Pandas to clean, process, and summarize Excel/CSV data.  
These scripts are standalone .py files that clients can run easily (after `pip install pandas openpyxl`).

All scripts include:
- Basic error handling
- Clear comments
- Tested on sample data
- Export to new Excel file

### Scripts Overview

- **sales_profit_adder.py**  
  Loads sales data, adds profit per item and total profits column, saves processed file.
  
- **sales_region_profit_summary.py**  
  Loads sales data, adds profit per item and total profits column, show total profits by region in console, removes product with no profits, saves cleaned file.

- **sales_data_cleaner.py**  
  Sales data cleaning: removes duplicates, fills missing prices with average, adds revenue column, saves cleaned file.

- **scores_data_cleaner_.py**  
  Basic score data cleaning: removes duplicates, fills missing data with mean, saves cleaned file

- **score_stats_counter.py**  
  Basic score data cleaning: removes duplicates, fills missing data.Computes basic statistics and grade counts for each subject, saves cleaned and processed files

- **score_subject_summary_report.py**  
  Score data cleaning: removes dupicates, fills missing scores with subject average, counts grades per subject, computes basic statistics, saves cleaned file and summary report.

- **stock_category_flag_report.py**  
  Stock data cleaning: removes duplicates, removes invalid/negative stock or blank items, groups by category, adds low-stock flags (<10), saves cleaned file and report with totals.
  
- **character_role_merger.py**  
  Loads charcter data, merge column Role1 and Role2 into new column Roles to handle missing values, saves processed file.
  
- **Titanic_analysis.ipynb(UNUSABLE)**  
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
