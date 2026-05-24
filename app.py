import streamlit as st
from filters import load_data, apply_filters
from charts import (chart1_pie, chart2_histogram, chart3_line,
                    chart4_bar, chart5_scatter, chart6_box,
                    chart7_heatmap, chart8_area, chart9_countplot,
                    chart10_violin)

st.set_page_config(page_title="NFL 2023 Dashboard", layout="wide")

st.title("NFL 2023 Play-by-Play Dashboard")
st.markdown("Analyzing 49,000+ plays from the 2023 NFL season")

df_raw = load_data()
df = apply_filters(df_raw)

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Plays", f"{len(df):,}")
col2.metric("Avg Yards Gained", f"{df['yards_gained'].mean():.2f}")
col3.metric("Total Touchdowns", f"{int(df['touchdown'].sum())}")
col4.metric("Total Interceptions", f"{int(df['interception'].sum())}")

st.markdown("---")

st.subheader("Play Distribution and Yards")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(chart1_pie(df))
with col2:
    st.pyplot(chart2_histogram(df))

st.markdown("---")

st.subheader("Weekly Trends")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(chart3_line(df))
with col2:
    st.pyplot(chart8_area(df))

st.markdown("---")

st.subheader("Team and Play Analysis")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(chart4_bar(df))
with col2:
    st.pyplot(chart9_countplot(df))

st.markdown("---")

st.subheader("Statistical Analysis")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(chart5_scatter(df))
with col2:
    st.pyplot(chart6_box(df))

st.markdown("---")

st.subheader("Correlations and Distributions")
col1, col2 = st.columns(2)
with col1:
    st.pyplot(chart7_heatmap(df))
with col2:
    st.pyplot(chart10_violin(df))