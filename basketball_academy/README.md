# Basketball Academy Data Analysis Report README

## Overview

Welcome to the Basketball Camp Data Analytics Project!

This project serves as a showcase of my data analytics and data science skills, focusing on extracting valuable insights from the data collected from our customers at the basketball camp. The primary goal of this project is to demonstrate my proficiency in handling and analyzing real-world data to derive meaningful conclusions and actionable insights.

One unique aspect of this project is the deliberate introduction of dirty data, intentionally included to highlight my expertise in data cleaning and manipulation using Pandas. By working with imperfect data, I aim to showcase my ability to preprocess and transform datasets effectively.

Through this project, I aim to not only reveal interesting patterns and trends within the basketball camp data but also demonstrate my capability to tackle data challenges and extract valuable information that can drive informed decision-making.
## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Data Overview](#data-overview)
- [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Key Findings](#key-findings)
- [Statistical Analysis](#statistical-analysis)
- [Data Visualizations](#data-visualizations)
- [Key Metrics and KPIs](#key-metrics-and-kpis)
- [Predictive Analysis](#predictive-analysis)
- [Recommendations](#recommendations)
- [Limitations](#limitations)
- [Conclusion](#conclusion)
- [References](#references)
- [Appendix](#appendix)

## Introduction

Company X, a basketball academy in Hong Kong, collects data on camp attendees to understand their demographics and behaviors. This report aims to explore this dataset to drive business insights and improvements.

## Methodology

Explain the data sources, collection methods, tools, and techniques used for analysis.

The dataset is from a camp in Hong Kong. The analysis includes demographic visualizations, customer turnout rates, attendance patterns, correlations, and a Hong Kong district heatmap that visualizes where our kids attend school. Insights will be used to inform business decisions.

### Data Overview
The dataset comprises information related to student registrations for a series of events from August 19 to August 23, 2024. Each entry includes details such as timestamps of when students signed up on the google form, student IDs, event attendance flags for each day, payment status, jersey sizes, payment dates, dates of birth, age, gender, school attended, payment acknowledgment, injury liability waiver, and photograph release agreement.

```
Basketball_Academy/
├── data/
│   ├── HK_District/
│   │   ├── HKDistrict18.cpg
│   │   ├── HKDistrict18.dbf
│   │   ├── HKDistrict18.prj
│   │   ├── HKDistrict18.shp
│   │   ├── HKDistrict18.shp.xml
│   │   └── HKDistrict18.shx
│   ├── Additional_Columns.csv
│   ├── Anonymized_Data.csv
│   ├── Cleaned_Data.csv
│   ├── merged_df.csv
│   └── Raw_Camp_Data.csv
├── Anonymize.ipynb
├── Data_Cleaning.ipynb
├── Old_and_new.ipynb
├── Analysis & Insights.ipynb
├── README.md
└── utils.py
```
# Column Names: Basketball_Academy/data 

## merged_df 
- **Timestamp:** Date and time of registration (datetime)
- **Student ID:** Unique identifier for each student (string)
- **Aug 19 - Aug 23:** Attendance status for each event day (boolean)
- **Payment Received:** The total amount paid by student (integer)
- **Jersey Sizes:** Sizes chosen for jerseys (integer)
- **Payment Date:** Date payment was made (datetime)
- **Date of Birth:** Birthdate of the student (datetime)
- **Age:** Age of the student at the time of registration (integer)
- **Gender:** Gender of the student (string)
- **School:** School where the student is enrolled (string)
- **Payment Instruction Acknowledgement:** Acknowledgement of payment instructions (boolean)
- **Injury Liability Waiver:** Agreement to waive liability for injuries (boolean)
- **Photograph Release Agreement:** Agreement for photograph release (boolean)


## Additional_Columns 

- **Student ID:** Unique identifier for each student (string)
- **Returning Customer:** Indicates if the student is a returning customer (boolean)
- **Elite Team Status:** Indicates if the student is part of the elite team (boolean)
- **Weekend Academy Status:** Indicates if the student is part of the weekend academy (boolean)
- **School Geographic Region:** Geographic region of the school attended by the student (string)


_This dataset provides a comprehensive view of student registrations, payment statuses, and participant details for the specified events, allowing for further analysis and insights into attendance patterns, demographic information, and compliance with payment and liability agreements._
## Data Cleaning and Preprocessing

The original dataset came with many issues to fix. These were the issues and fixes:

- ### Anonymized Names
  Creating Student ID's in place of full names
- ### Removing Sensitive Information
- ### Column Name Mapping
- ### Data Correction and completion
- ### Standardizing School Names
- ### Converting Data Types
- ### Merging Datasets

## Exploratory Data Analysis (EDA)
Patterns, trends, and relationships within the data will be explored.

## Key Findings
Important insights and discoveries from the analysis will be summarized.

## Statistical Analysis
Details on statistical tests, correlations, and models used in the analysis will be provided.

## Data Visualizations
Graphs, charts, and visual representations will aid in understanding the data.

## Key Metrics and KPIs
Performance indicators relevant to the business will be highlighted.

## Recommendations
Actionable insights and suggestions to enhance business performance will be provided.

## Limitations
Any constraints in the analysis that might affect the validity of the findings will be discussed.

## Conclusion
Main findings and their implications for the business will be summarized.




