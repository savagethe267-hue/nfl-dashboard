# NFL 2023 Play-by-Play Dashboard

## Project Overview
This dashboard analyzes 49,665 plays from the 2023 NFL season.
Built for the Exploratory Data Analysis course project.

## Dataset
- File: play_by_play_2023.csv
- Rows: 49,665
- Columns: 372
- Source: NFL Play-by-Play 2023

## How to Install

Open terminal in the project folder and run:

    pip install -r requirements.txt

## How to Run

    streamlit run app.py

Dashboard will open at: http://localhost:8501

## Charts Included
1. Pie Chart        - Play Type Distribution
2. Histogram        - Yards Gained Distribution
3. Line Chart       - Average Yards Gained per Week
4. Bar Chart        - Top 10 Teams by Avg Yards Gained
5. Scatter Plot     - Yards to Go vs Yards Gained
6. Box Plot         - Yards Gained by Play Type
7. Heatmap          - Feature Correlation Matrix
8. Area Chart       - Total Touchdowns per Week
9. Count Plot       - Number of Plays per Quarter
10. Violin Plot     - Yards Gained Distribution Pass vs Run

## Filters Available
- Date Range Filter
- Season Type Filter
- Play Type Multi-Select
- Week Range Slider
- Team Search Filter
- Reset All Filters Button

## Key Insights
- Pass plays are more common than run plays in 2023
- Average yards gained per play is around 5-6 yards
- Touchdowns peak in middle weeks of the season
- EPA (Expected Points Added) strongly correlates with yards gained

## Tools Used
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

## Instructor
Ali Hassan Sherazi

## Course
Exploratory Data Analysis

## Submission Date
05-June-2026