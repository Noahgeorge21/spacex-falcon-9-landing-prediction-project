🚀 Winning the Space Race with Data Science
SpaceX Falcon 9 Landing Prediction Project
📌 Project Overview

This project analyzes historical SpaceX Falcon 9 launch data to identify the key factors influencing launch and landing success. Using an end-to-end data science workflow, the project combines data collection, data wrangling, exploratory data analysis (EDA), interactive visualization, and machine learning to predict mission outcomes and uncover operational insights.

The final deliverable includes predictive models and an interactive dashboard that allows users to explore how payload mass, launch site, booster version, orbit type, and time affect launch success.

🎯 Key Objectives

Identify which factors most strongly influence launch success

Analyze trends across launch sites, payload mass, booster versions, and orbits

Build and evaluate machine learning models to predict launch outcomes

Develop interactive visual tools for exploratory analysis

Select a final model balancing performance, interpretability, and robustness

🧠 Methodology
1️⃣ Data Collection

Retrieved historical SpaceX launch data using a REST API

Supplemented API data with public datasets for geographic and launch-site context

Web-scraped additional launch records using BeautifulSoup

Stored raw data in Pandas DataFrames for processing

2️⃣ Data Wrangling & Feature Engineering

Removed duplicates and irrelevant records

Handled missing and inconsistent values

Converted and standardized data types

Encoded categorical variables for modeling

Produced clean, analysis-ready datasets

3️⃣ Exploratory Data Analysis (EDA)

Conducted EDA using Python (Matplotlib, Seaborn) and SQL

Analyzed:

Launch success by site and booster version

Payload mass vs. launch outcome

Orbit type and mission reliability

Success trends over time

Validated Python findings using SQL aggregation queries

4️⃣ Interactive Visual Analytics

Built Folium maps to visualize launch site locations and spatial relationships

Developed a Plotly Dash dashboard with:

Launch-site filters

Payload mass range sliders

Interactive pie charts and scatter plots

Dynamic success/failure visualizations

5️⃣ Predictive Modeling

Trained and evaluated classification models:

K-Nearest Neighbors (KNN)

Logistic Regression

Support Vector Machine (SVM)

Tuned hyperparameters and evaluated models using:

Accuracy

Confusion matrices

Logistic Regression selected as final model due to:

Comparable performance

Strong interpretability

Lower overfitting risk

📊 Key Results & Insights

Launch success varies significantly by launch site

Payload mass shows a strong relationship with mission outcome

Certain booster versions demonstrate more consistent success

Launch reliability improves steadily over time

All three ML models performed similarly, with Logistic Regression providing the best balance of accuracy and interpretability

🖥️ Interactive Dashboard

The dashboard allows users to:

Filter launches by site

Adjust payload mass ranges

Explore success vs. failure distributions

Analyze booster performance visually

To run locally:

python dash_interactive.py

🛠️ Technologies Used

Python: Pandas, NumPy, Scikit-learn

Visualization: Matplotlib, Seaborn, Plotly, Folium

Databases: SQLite, SQL

Web Scraping: BeautifulSoup

Dashboards: Plotly Dash

APIs: REST APIs (JSON parsing)
