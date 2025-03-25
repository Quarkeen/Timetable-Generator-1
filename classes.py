import pandas as pd

# Corrected file path using a raw string to avoid escape character issues
file_path = r"C:\Users\HP\Downloads\timetable_structure.xlsx"  # Replace with your actual file path

# Load the Excel file
excel_data = pd.ExcelFile(file_path)

# Print all sheet names
print("Sheet names:", excel_data.sheet_names)

# Load a specific sheet into a DataFrame (you can change 'Sheet1' to your actual sheet name)
df = excel_data.parse('Sheet1')

# Display the first few rows
print("Data from Sheet1:")
print(df.head())

# Reading specific columns (replace 'Name' and 'Age' with your actual column names)
print("\nReading specific columns:")
print(df[['Course Code', 'Course Title','Credits (L-T-P-S-C)']])

# Accessing a specific cell (replace row index and column name as needed)
print("\nSpecific Cell (row 1, column 'Name'):")
print(df.at[0, 'Course Code'])

# Get statistical summary
print("\nStatistical Summary:")
print(df.describe())

class timing:
    def __init__(self,starting_time,ending_time):
        self.starting_time = starting_time
        self.ending_time = ending_time
        