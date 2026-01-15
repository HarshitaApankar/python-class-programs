Pandas Practice Programs (Day 01)

This repository contains my **Day 01 practice programs** using the **pandas** library in Python.  
Each program demonstrates a basic but important operation on a DataFrame.

---

Programs Included

1. dataframe.py  
Description: 
- Creates a dictionary with `name`, `age`, and `city`
- Converts it into a pandas DataFrame
- Prints the DataFrame  

Concepts Used:  
- pandas DataFrame  
- Basic data representation  

---

2. dataframe_index.py  
Description: 
- Demonstrates how to update or set an index in a DataFrame  

Concepts Used: 
- `set_index()`  
- DataFrame indexing  

---

3. check_missing_values.py  
Description:  
- Checks missing (null) values in a DataFrame
- isnull(): It return true for nan (missing) values and false otherwise
- notnull(): It returns the opposite , true for non-missing values and false for nan values.

Concepts Used: 
- `isnull()`  
- `notnull()`  

---

4. fill_missing_values.py  
Description: 
- Fills missing values in a DataFrame using different methods
- fillna(): replace missing values with constants or statistics
- replace(): replace specific values including nan
- interpolate(): estimate missing value based on surrounding data  

Concepts Used: 
- `fillna()`  
- `replace()`  
- `interpolate()`  

---

5. missing_values_dropna.py  
Description:
- Removes rows containing missing values from a DataFrame  

**Concepts Used:**  
- `dropna()`  

---
🛠️ Tools & Technologies
- Python 3
- pandas
- VS Code
- GitHub

---

Learning Objective
The goal of these programs is to understand:
- How pandas handles missing data
- Different ways to check, fill, and remove null values
- Basic DataFrame operations

---

✔️ Day 01 Completed  
More programs will be added as learning continues.
