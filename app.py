import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Election Analytics", layout="wide")

# Title
st.title("🗳️ Election Commission of India - Interactive Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("india_election_data_large.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filter Data")
states = sorted(df['State'].unique())
years = sorted(df['Year'].unique())
parties = sorted(df['Party'].unique())

selected_state = st.sidebar.selectbox("Select State", states)
selected_year = st.sidebar.selectbox("Select Year", years)
selected_party = st.sidebar.multiselect("Select Party", parties, default=parties)

# Filtered Data
filtered_df = df[
    (df['State'] == selected_state) &
    (df['Year'] == selected_year) &
    (df['Party'].isin(selected_party))
]

# 🎯 Constituency-level results
st.subheader(f"📍 Results in {selected_state} ({selected_year})")
st.dataframe(filtered_df[['Constituency', 'Party', 'Candidate', 'Votes', 'Vote_Percentage', 'Winner']])

# 🏆 Top Candidates
st.subheader("🏆 Top 10 Candidates by Votes")
top_candidates = filtered_df.sort_values(by='Votes', ascending=False).head(10)
fig_top = px.bar(
    top_candidates,
    x='Candidate',
    y='Votes',
    color='Party',
    title="Top 10 Candidates by Votes",
    animation_frame='Constituency',
    template='plotly_dark'
)
st.plotly_chart(fig_top, use_container_width=True)

# 📊 Vote Share Pie Chart
st.subheader("📊 Vote Share Distribution")
party_votes = filtered_df.groupby('Party')['Votes'].sum().reset_index()
fig_pie = px.pie(
    party_votes,
    names='Party',
    values='Votes',
    title='Vote Share by Party',
    color_discrete_sequence=px.colors.qualitative.Set3
)
st.plotly_chart(fig_pie, use_container_width=True)

# 📈 Party Performance Bar Chart
st.subheader("📈 Party Performance in Selected State")
fig_bar = px.bar(
    party_votes,
    x='Party',
    y='Votes',
    color='Party',
    title=f"Party-wise Vote Totals in {selected_state}",
    text='Votes',
    template='plotly_white'
)
fig_bar.update_traces(textposition='outside')
st.plotly_chart(fig_bar, use_container_width=True)

# 📅 Year-over-Year Trends
st.subheader("📅 Year-over-Year Vote Trends (All India)")
trend_df = df[df['Party'].isin(selected_party)].groupby(['Year', 'Party'])['Votes'].sum().reset_index()
fig_line = px.line(
    trend_df,
    x='Year',
    y='Votes',
    color='Party',
    markers=True,
    title="Vote Trends Over Time",
    template='plotly_dark'
)
st.plotly_chart(fig_line, use_container_width=True)