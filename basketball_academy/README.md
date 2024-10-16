# Data Cleaning and Transformation Script Documentation (Anonymize.ipynb)

## Overview
This Python script utilizes the Pandas library to clean and transform participant information stored in a DataFrame. The script performs various operations such as renaming columns, filling in missing data, standardizing school names, creating student IDs, and exporting the modified data to a CSV file.

## Steps Overview
1. **Import Necessary Libraries and function script:**
   - Pandas
   - 'utils.py' 

2. **Read Data and Initial Processing:**
   - Read the participant information from a CSV file into a Pandas DataFrame.
   - Initial data processing includes removing unnecessary rows from the DataFrame.

3. **Rename Columns:**
   - Map original column names to desired column names using a dictionary.
   - Use the `rename` method in Pandas to update the column names in the DataFrame.

4. **Remove Unnecessary Columns:**
   - Identify and remove columns that contain sensitive information or are not needed.

5. **Fill in Missing Data:**
   - Fill in missing information for specific rows, such as names, attendance, gender, date of birth, age, and school details.

6. **Standardize School Names:**
   - Standardize school names using a predefined mapping dictionary to ensure consistency.

7. **Create Student IDs:**
   - Generate unique student IDs based on the initials of names, date of birth, and gender.
   - Utilize a custom function to create student IDs for each participant.

8. **Export Data to CSV:**
   - Save the modified DataFrame to a CSV file for further analysis or sharing.

## Note
- The script includes comments at each step to explain the rationale behind the data cleaning and transformation operations.
- Custom utility functions like `generate_student_id` are used to enhance functionality and maintain code readability.

## Conclusion
By following this script, you can efficiently clean and transform participant information, ensuring data accuracy and consistency. The exported CSV file, containing anonymized data, can be used for analysis or reporting purposes.















Challenges Faced:
1. "Email Adresss" not found in columns when it is present
2. Missing DOB
