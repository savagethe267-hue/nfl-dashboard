import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv('data/play_by_play_2023.csv', low_memory=False)
    df['game_date'] = pd.to_datetime(df['game_date'], errors='coerce')
    df['down'] = df['down'].fillna(0).astype(int)
    df['week'] = df['week'].astype(int)
    cols = [
        'game_date','week','season_type','home_team','away_team',
        'posteam','defteam','play_type','yards_gained','qtr','down',
        'ydstogo','score_differential','touchdown','interception',
        'sack','pass_attempt','rush_attempt','epa','wp',
        'pass_length','pass_location','run_location','field_goal_result',
        'home_score','away_score','roof','stadium','qb_epa'
    ]
    df = df[cols].copy()
    df['yards_gained'] = df['yards_gained'].fillna(0)
    df['score_differential'] = df['score_differential'].fillna(0)
    df['epa'] = df['epa'].fillna(0)
    df['wp'] = df['wp'].fillna(0)
    df = df.dropna(subset=['play_type','posteam'])
    return df

def apply_filters(df):
    st.sidebar.header("Filters")

    min_date = df['game_date'].min().date()
    max_date = df['game_date'].max().date()
    date_range = st.sidebar.date_input('Date Range',
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date)
    if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
        df = df[(df['game_date'] >= pd.Timestamp(date_range[0])) &
                (df['game_date'] <= pd.Timestamp(date_range[1]))]

    season_types = sorted(df['season_type'].dropna().unique().tolist())
    selected_season = st.sidebar.selectbox('Season Type', ['All'] + season_types)
    if selected_season != 'All':
        df = df[df['season_type'] == selected_season]

    play_types = sorted(df['play_type'].dropna().unique().tolist())
    selected_plays = st.sidebar.multiselect('Play Type(s)', play_types, default=play_types)
    if selected_plays:
        df = df[df['play_type'].isin(selected_plays)]

    week_min = int(df['week'].min())
    week_max = int(df['week'].max())
    week_range = st.sidebar.slider('Week Range',
        min_value=week_min, max_value=week_max,
        value=(week_min, week_max))
    df = df[(df['week'] >= week_range[0]) & (df['week'] <= week_range[1])]

    team_search = st.sidebar.text_input('Search Team (e.g. KC, SF, BUF)')
    if team_search.strip():
        q = team_search.strip().upper()
        df = df[df['posteam'].str.upper().str.contains(q, na=False) |
                df['defteam'].str.upper().str.contains(q, na=False)]

    if st.sidebar.button('Reset All Filters'):
        st.rerun()

    return df