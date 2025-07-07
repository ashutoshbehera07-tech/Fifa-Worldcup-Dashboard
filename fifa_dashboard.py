import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration

st.set_page_config(
    page_title="🏆 FIFA World Cup Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Inserting the Image into the Dashboard
import os

print("Exists?", os.path.exists(r"C:/Fifa_worldcup_dashboard/FIFA-World-Cup_image.jpg"))

st.image(r"C:/Fifa_worldcup_dashboard/FIFA-World-Cup_image.jpg", width=500)


# Load the data and Merge the data

@st.cache_data
def load_data():
    players = pd.read_csv("C:/Fifa_worldcup_dashboard/players.csv")
    teams = pd.read_csv("C:/Fifa_worldcup_dashboard/teams.csv")
    standings = pd.read_csv("C:/Fifa_worldcup_dashboard/tournament_standings.csv")
    awards = pd.read_csv("C:/Fifa_worldcup_dashboard/award_winners.csv")
    goals = pd.read_csv("C:/Fifa_worldcup_dashboard/goals.csv")
    bookings = pd.read_csv("C:/Fifa_worldcup_dashboard/bookings.csv")
    tournaments = pd.read_csv("C:/Fifa_worldcup_dashboard/tournaments.csv")
    penalty_kicks = pd.read_csv("C:/Fifa_worldcup_dashboard/penalty_kicks.csv")
    referee_appointments = pd.read_csv("C:/Fifa_worldcup_dashboard/referee_appointments.csv")
    matches = pd.read_csv("C:/Fifa_worldcup_dashboard/matches.csv")
    stadiums = pd.read_csv("C:/Fifa_worldcup_dashboard/stadiums.csv")
    referees = pd.read_csv("C:/Fifa_worldcup_dashboard/referees.csv")
    return (players, teams, standings, awards, goals, bookings, tournaments, penalty_kicks,
            referee_appointments, matches, stadiums, referees)

(players, teams, standings, awards, goals, bookings, tournaments, penalty_kicks,
 referee_appointments, matches, stadiums, referees) = load_data()

# Merge Referee Data  (with suffixes)

referee_appointments_merged = referee_appointments.merge(
    referees[['referee_id', 'country_name', 'confederation_name', 'family_name']],
    on='referee_id',
    how='left',
    suffixes=('', '_ref')
)

# Side Bar Configuration

st.sidebar.title("🏆 FIFA Dashboard")
selected_tournament = st.sidebar.selectbox("🌍 Select Tournament", tournaments['tournament_name'].unique())
selected_tournament_id = tournaments[tournaments['tournament_name'] == selected_tournament]['tournament_id'].values[0]

# TITLE

st.title("⚽ FIFA World Cup Analytics Dashboard")

# Q1: Which teams and players have demonstrated consistent high performance or improvement over multiple World Cups?

st.header("1. Consistent High Performance")
team_performance = standings.groupby(['team_name', 'tournament_name'])['position'].min().reset_index()
top_teams = team_performance.groupby('team_name')['position'].mean().sort_values().head(5).index.tolist()
bump_data = team_performance[team_performance['team_name'].isin(top_teams)].copy()
# Ensure tournaments are in chronological order
tournament_order = sorted(bump_data['tournament_name'].unique())
bump_data['tournament_name'] = pd.Categorical(
    bump_data['tournament_name'],
    categories=tournament_order,
    ordered=True
)
bump_data = bump_data.sort_values(['team_name', 'tournament_name'])

# Create the bump chart
fig_bump = px.line(
    bump_data,
    x='tournament_name',
    y='position',
    color='team_name',
    markers=True,
    text='position',
    line_shape='linear',
    title="Top 5 Teams' Rankings Over Tournaments (Bump Chart)",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig_bump.update_traces(textposition='top center')
fig_bump.update_yaxes(
    autorange='reversed',
    title='Position (1 = Winner)',
    tickmode='linear',
    tick0=1,
    dtick=1
)
fig_bump.update_xaxes(title='Tournament')
fig_bump.update_layout(
    height=600,
    legend_title='Team',
    hovermode='x unified'
)
st.plotly_chart(fig_bump, use_container_width=True)




# Q2 : What are the temporal patterns of goal scoring—by half, extra time, and penalties—across tournaments and teams?

st.header("⚽ 2. Temporal Patterns of Goal Scoring")
col1, col2 = st.columns(2)
goals_tournament = goals[goals['tournament_id'] == selected_tournament_id]
period_counts = goals_tournament['match_period'].value_counts().reset_index()
period_counts.columns = ['Match Period', 'Goals']
fig_goals = px.bar(
    period_counts,
    x='Match Period', y='Goals', text_auto=True,
    title="⏱️ Goals by Match Period",
    color='Goals',
    color_continuous_scale='Blues'
)
col1.plotly_chart(fig_goals, use_container_width=True)

# Filter penalty kicks for the selected tournament
penalties_tournament = penalty_kicks[penalty_kicks['tournament_id'] == selected_tournament_id]
penalty_summary = penalties_tournament['converted'].value_counts().rename({1: "Scored", 0: "Missed"})

# Create an interactive donut chart
fig_donut = px.pie(
    names=penalty_summary.index,
    values=penalty_summary.values,
    title="🥅 Penalty Shootout Outcomes",
    hole=0.5,  # This makes it a donut chart
    color_discrete_sequence=px.colors.qualitative.Set3
)
fig_donut.update_traces(
    textinfo='percent+label',
    pull=[0.05, 0],  # Slightly pull out the first slice for emphasis
    hovertemplate='%{label}: %{value} (%{percent})<extra></extra>'
)
fig_donut.update_layout(
    showlegend=True,
    legend_title_text='Outcome'
)

st.plotly_chart(fig_donut, use_container_width=True)


# Q3 : How do referee assignments and decisions (e.g., cards, penalties awarded) influence match outcomes and disciplinary trends?

st.header("🟥 3. Referee & Disciplinary Trends")
yellow_cards = bookings[bookings['tournament_id'] == selected_tournament_id]['yellow_card'].sum()
red_cards = bookings[bookings['tournament_id'] == selected_tournament_id]['red_card'].sum()
col1, col2 = st.columns(2)
col1.metric("🟨 Yellow Cards", int(yellow_cards))
col2.metric("🟥 Red Cards", int(red_cards))

cards_by_team = bookings[bookings['tournament_id'] == selected_tournament_id].groupby('team_name')[['yellow_card', 'red_card']].sum().reset_index()
fig_cards = px.bar(
    cards_by_team, x='team_name', y=['yellow_card', 'red_card'],
    barmode='group',
    title="📊 Cards by Team",
    color_discrete_sequence=px.colors.qualitative.Pastel
)
st.plotly_chart(fig_cards, use_container_width=True)

# Top Referee Nationalities Across Tournaments 

st.subheader(" Top Referee Nationalities Across Tournaments")
# Prepare data for radar chart

top_countries = referee_appointments_merged['country_name_ref'].value_counts().head(5).index.tolist()
radar_data = referee_appointments_merged[referee_appointments_merged['country_name_ref'].isin(top_countries)]
radar_df = radar_data.groupby(['tournament_name', 'country_name_ref']).size().reset_index(name='count')
radar_pivot = radar_df.pivot(index='tournament_name', columns='country_name_ref', values='count').fillna(0)

radar_long = radar_pivot.reset_index().melt(id_vars='tournament_name', var_name='country', value_name='count')

# Plotting the chart

fig_radar = px.line_polar(
    radar_long,
    r='count',
    theta='tournament_name',
    color='country',
    line_close=True,
    title='Top 5 Referee Nationalities Across Tournaments'
)
fig_radar.update_traces(fill='toself')
st.plotly_chart(fig_radar, use_container_width=True)

# Q4 : Which countries have shown the greatest improvement or decline in performance over time, and what contextual factors (e.g., hosting, investment) explain these trends?

st.header("📈 4. Country Improvement or Decline")
country_trends = standings.groupby(['team_name', 'tournament_name'])['position'].min().reset_index()
selected_team = st.selectbox("Select a Team", sorted(standings['team_name'].unique()))
team_trend = country_trends[country_trends['team_name'] == selected_team]
fig_trend = px.line(
    team_trend, x='tournament_name', y='position', markers=True,
    title=f"📉 {selected_team} World Cup Performance",
    color_discrete_sequence=['#636EFA']
)
fig_trend.update_yaxes(autorange="reversed", title='Position (1 = Winner)')
st.plotly_chart(fig_trend, use_container_width=True)

hosted = tournaments[tournaments['host_country'] == selected_team]
if not hosted.empty:
    st.info(f"🏠 {selected_team} hosted: {', '.join(hosted['tournament_name'])}")

# Q5: What is the relationship between match location (city, country, stadium, capacity) and team performance?

st.header("📍 5. Match Location & Stadium Performance")
col1, col2 = st.columns(2)
with col1:
    selected_tournament_match = st.selectbox("Select Tournament", matches['tournament_name'].unique(), key="matches_tournament")
    matches_tournament = matches[matches['tournament_name'] == selected_tournament_match]
    team_list = sorted(set(matches_tournament['home_team_name']).union(set(matches_tournament['away_team_name'])))
with col2:
    selected_team_match = st.selectbox("Select Team", team_list, key="matches_team")
    team_matches = matches_tournament[
        (matches_tournament['home_team_name'] == selected_team_match) |
        (matches_tournament['away_team_name'] == selected_team_match)
    ]
    team_matches = team_matches.merge(
        stadiums[['stadium_id', 'stadium_name', 'city_name', 'country_name', 'stadium_capacity']],
        on=['stadium_id', 'stadium_name', 'city_name', 'country_name'],
        how='left'
    )

with st.expander(f"📋 Matches for {selected_team_match} in {selected_tournament_match}"):
    st.dataframe(team_matches[['match_date', 'stadium_name', 'city_name', 'country_name', 'stadium_capacity',
                              'home_team_name', 'away_team_name', 'home_team_score', 'away_team_score', 'result']],
                 height=300)

city_counts = team_matches['city_name'].value_counts().reset_index()
city_counts.columns = ['City', 'Matches']
fig_city = px.bar(
    city_counts, x='City', y='Matches',
    title=f"🏙️ Matches by City: {selected_team_match}",
    color='Matches',
    color_continuous_scale='Teal'
)
st.plotly_chart(fig_city, use_container_width=True)

fig_violin = px.violin(
    team_matches,
    x='result',
    y='stadium_capacity',
    color='result',
    box=True,  # Show box plot inside the violin
    points='all',  # Show all data points
    title=f"Stadium Capacity Distribution by Match Result: {selected_team_match}",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig_violin.update_layout(
    yaxis_title='Stadium Capacity',
    xaxis_title='Match Result',
    showlegend=False
)
st.plotly_chart(fig_violin, use_container_width=True)

# FOOTER 
st.markdown("""
---
📊 **Data Source:** Fjelstul World Cup Database  
👨💻 **Dashboard by:** [Ashutosh Behera]
""")



