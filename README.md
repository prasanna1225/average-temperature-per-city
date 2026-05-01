# 📊 City Temperature Analysis

## 📌 Project Description
This Python program processes a CSV file containing city-wise temperature records and calculates the **average temperature for each city**.

The program reads data from `citytemp.csv`, converts temperatures from Celsius to Fahrenheit when required, groups records by city, and computes the average temperature. The final results are displayed in a clean, formatted output.

---

## ⚙️ What It Does
- Reads temperature data from a CSV file  
- Parses each record into **city, temperature, and unit**  
- Converts temperatures from **Celsius to Fahrenheit** for consistency  
- Groups data by city (assuming sorted input)  
- Calculates the **average temperature per city**  
- Prints the result rounded to **2 decimal places**  

---

## 🧠 Key Concepts Used
- File Handling (`open`, `readline`, file iteration)  
- String Manipulation (`split`, `rstrip`)  
- Conditional Logic  
- Looping and Aggregation  
- Basic Data Processing  

---

## 📂 Example Input
```csv
Hyderabad,30,C
Hyderabad,32,C
Delhi,95,F
Delhi,36,C

## 📊 Example Output
Hyderabad 89.60
Delhi 96.80
