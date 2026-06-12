# Sales Data Automation Tool

This project is a tool designed to streamline sales data analysis, eliminating the operational burden of manually cleaning and processing files.

## 🛠 Problem
In business environments, reports often arrive with inconsistent formats, typos, and missing data. Processing this information manually in Excel is time-consuming and prone to human error.

## 💡 Solution
I developed a **Python** script using **Pandas** that:
1. **Automates Cleaning:** Detects and fixes format errors in prices and dates.
2. **Handles Missing Data:** Automatically filters out corrupt records to ensure analysis integrity.
3. **Generates Results:** Creates statistical summaries and visualizations in seconds.

## 🚀 Technologies Used
* **Python**
* **Pandas** (for data manipulation)
* **Matplotlib** (for data visualization)

## 📋 How to use
1. Ensure you have Python and pandas installed.
2. Run the script: `python CodigoAnalisis.py`.
3. Enter the name of your CSV file when prompted.
4. The program will automatically generate a `resumen_analisis.txt` file and display a bar chart with the average sales.
