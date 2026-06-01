import streamlit as st
from filters import load_data, apply_filters
from charts import (chart1_pie, chart2_histogram, chart3_line,
                    chart4_bar, chart5_scatter, chart6_box,
                    chart7_heatmap, chart8_area, chart9_countplot,
                    chart10_violin)

st.set_page_config(page_title="NFL 2023 Dashboard", layout="wide", page_icon="🏈")

st.markdown("""
    <h1 style='text-align: center; color: #1a1a2e;'>🏈 NFL 2023 Play-by-Play Dashboard</h1>
    <p style='text-align: center; color: gray; font-size: 16px;'>
    Analyzing 49,000+ plays from the 2023 NFL Season</p>
    <hr>
""", unsafe_allow_html=True)

df_raw = load_data()
df = apply_filters(df_raw)

st.markdown("### 📊 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("🏈 Total Plays", f"{len(df):,}")
col2.metric("📏 Avg Yards Gained", f"{df['yards_gained'].mean():.2f}")
col3.metric("🏆 Total Touchdowns", f"{int(df['touchdown'].sum())}")
col4.metric("⚠️ Total Interceptions", f"{int(df['interception'].sum())}")

st.markdown("<hr>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Trends & Distribution",
    "🏟️ Team Analysis",
    "📉 Statistical Analysis",
    "🔥 Correlations & Density"
])

with tab1:
    st.markdown("### 📈 Trends & Distribution")
    st.markdown("---")

    st.markdown("#### 🥧 Play Type Distribution")
    st.markdown("Shows the proportion of each play type used during the season.")
    st.pyplot(chart1_pie(df))

    st.markdown("---")

    st.markdown("#### 📊 Yards Gained Distribution")
    st.markdown("Frequency distribution of yards gained per play.")
    st.pyplot(chart2_histogram(df))

    st.markdown("---")

    st.markdown("#### 📈 Average Yards Gained per Week")
    st.markdown("Weekly trend of average yards gained throughout the season.")
    st.pyplot(chart3_line(df))

    st.markdown("---")

    st.markdown("#### 🏔️ Total Touchdowns per Week")
    st.markdown("Cumulative touchdown trend across all weeks of the season.")
    st.pyplot(chart8_area(df))

with tab2:
    st.markdown("### 🏟️ Team Analysis")
    st.markdown("---")

    st.markdown("#### 🥇 Top 10 Teams by Average Yards Gained")
    st.markdown("Ranking of top offensive teams based on average yards per play.")
    st.pyplot(chart4_bar(df))

    st.markdown("---")

    st.markdown("#### 🔢 Number of Plays per Quarter")
    st.markdown("Count of plays executed in each quarter of the game.")
    st.pyplot(chart9_countplot(df))

with tab3:
    st.markdown("### 📉 Statistical Analysis")
    st.markdown("---")

    st.markdown("#### 🎯 Yards to Go vs Yards Gained")
    st.markdown("Scatter plot showing relationship between yards needed and yards gained for pass and run plays.")
    st.pyplot(chart5_scatter(df))

    st.markdown("---")

    st.markdown("#### 📦 Yards Gained by Play Type")
    st.markdown("Box plot showing spread, median and outliers of yards gained across different play types.")
    st.pyplot(chart6_box(df))

with tab4:
    st.markdown("### 🔥 Correlations & Density")
    st.markdown("---")

    st.markdown("#### 🌡️ Feature Correlation Heatmap")
    st.markdown("Heatmap showing how strongly different numerical features are correlated with each other.")
    st.pyplot(chart7_heatmap(df))

    st.markdown("---")

    st.markdown("#### 🎻 Yards Gained Distribution - Pass vs Run")
    st.markdown("Violin plot comparing the distribution and density of yards gained for pass and run plays.")
    st.pyplot(chart10_violin(df))

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
    <p style='text-align: center; color: gray; font-size: 13px;'>
    NFL 2023 Dashboard | Exploratory Data Analysis Project | Instructor: Ali Hassan Sherazi
    </p>
""", unsafe_allow_html=True)