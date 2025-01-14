import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Function to load data
def load_data(file_name):
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        st.error(f"File '{file_name}' not found. Please upload the correct file.")
        return None

# Function to load prediction model
def load_model(file_name):
    try:
        return joblib.load(file_name)
    except FileNotFoundError:
        st.error("Prediction model not found. Please upload the correct model file.")
        return None

# Load data
df = load_data("clustered_players.csv")

# Page configuration
st.set_page_config(page_title="Valorant Dashboard", layout="wide")

# Add header decoration image
st.title("Valorant Champions Tour 2023-2024 Franchise Player Performance Dashboard")

st.markdown("""
<div style="text-align: justify; font-size: 14px;">
Welcome to the performance analytics dashboard of Valorant Champions Tour 2023-2024 franchise players. 
Use the menu below to explore player clustering data, team performance, and predict the cluster for new players.
</div>
""", unsafe_allow_html=True)

# Navigation tabs
tabs = st.tabs([" Overall View", "🏆 Team View", "🔍 Predict Cluster"])

# Cluster View
if df is not None:
    with tabs[0]:
        st.header(" Overall View")
        st.markdown("---")
        st.markdown("""
        **Overall View** allows you to analyze player performance based on their clusters. 
        Each cluster represents groups of players with similar characteristics based on their performance during the tournament.
        You can also view average statistics and feature data distributions for specific clusters.
        """)

        # Cluster and Tournament Filters
        col1, col2 = st.columns(2)
        with col1:
            cluster = st.selectbox("Select Performance Cluster", df['Cluster'].unique())
        with col2:
            cluster_data = df[df['Cluster'] == cluster]
            tournament = st.selectbox("Select Tournament", cluster_data['Tournament'].unique())

        cluster_tournament_data = cluster_data[cluster_data['Tournament'] == tournament]
        tournament_data = df[df['Tournament'] == tournament]
        st.subheader(f"Player Data in Cluster {cluster} - Tournament {tournament}")
        st.write(f"**Number of Players:** {len(cluster_tournament_data)}")
        st.dataframe(cluster_tournament_data)

        # Cluster Statistics
        st.markdown("### Cluster Statistics")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Average")
            mean_stats = cluster_tournament_data.mean(numeric_only=True)
            st.dataframe(mean_stats)
        with col2:
            st.markdown("#### Median")
            median_stats = cluster_tournament_data.median(numeric_only=True)
            st.dataframe(median_stats)

        # Scatter Plot of All Players
        st.markdown("### Scatter Plot of All Players")
        col1, col2 = st.columns([2, 1])
        with col2:
            feature_x = st.selectbox("Select Feature X", df.columns[8:24], key="all_players_x")
            feature_y = st.selectbox("Select Feature Y", df.columns[8:24], key="all_players_y")
        with col1:
            plt.figure(figsize=(12, 6))
            sns.scatterplot(
                data=tournament_data,
                x=feature_x,
                y=feature_y,
                hue="Cluster",
                palette="tab10",
                s=100,
                alpha=0.8
            )
            plt.title(f"Scatter Plot: {feature_x} vs {feature_y} (Tournament {tournament})")
            plt.xlabel(feature_x)
            plt.ylabel(feature_y)
            plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.grid(True, linestyle="--", alpha=0.7)
            st.pyplot(plt)

        # Feature Distribution Visualization
        st.markdown("### Feature Distribution")
        col1, col2 = st.columns([3, 1])
        with col2:
            feature = st.selectbox("Select Feature for Distribution", cluster_tournament_data.columns[8:24])
        with col1:
            plt.figure(figsize=(12, 6))
            sns.histplot(cluster_tournament_data[feature], kde=True, bins=15, color="skyblue")
            plt.title(f"Distribution of {feature} in Cluster {cluster} - Tournament {tournament}")
            plt.xlabel(feature)
            plt.ylabel("Number of Players")
            st.pyplot(plt)

# Team View
with tabs[1]:
    st.header("🏆 Team View")
    st.markdown("---")
    st.markdown("""
    **Team View** provides an overall analysis of team performance. 
    You can view performance data for each player in the selected team and compare player performance 
    across metrics in various tournaments.
    """)

    # Team Selection
    team = st.selectbox("Select Team", df['Teams'].unique())
    team_data = df[df['Teams'] == team]

    # Team Data
    st.subheader(f"Team Performance Data: {team}")
    st.dataframe(team_data)

    # Team Statistics
    st.markdown("### Team Statistics")
    st.dataframe(team_data.describe())

    # Team Performance Scatter Plot
    st.markdown("### Team Performance Scatter Plot")
    col1, col2 = st.columns([2, 1])
    with col2:
        feature_x = st.selectbox("Select Feature X", team_data.columns[8:24], key="team_x")
        feature_y = st.selectbox("Select Feature Y", team_data.columns[8:24], key="team_y")
    with col1:
        plt.figure(figsize=(12, 6))
        sns.scatterplot(
            data=team_data,
            x=feature_x,
            y=feature_y,
            hue="Player",
            palette="tab10",
            s=100
        )
        plt.title(f"Scatter Plot: {feature_x} vs {feature_y} (Team: {team})")
        plt.xlabel(feature_x)
        plt.ylabel(feature_y)
        plt.legend(title="Player", bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(plt)

    # Player Performance
    st.markdown("### Player Performance")
    selected_player = st.selectbox("Select Player", team_data['Player'].unique())
    performance_metric = st.selectbox("Select Performance Metric", team_data.columns[8:24])

    # Individual Player Performance Plot
    st.subheader(f"**Performance of {selected_player} in {performance_metric}**")
    plt.figure(figsize=(12, 6))
    player_data = team_data[team_data['Player'] == selected_player]
    sns.lineplot(
        data=player_data,
        x='Tournament',
        y=performance_metric,
        marker='o',
        label=selected_player
    )
    plt.title(f"Performance of {selected_player}")
    plt.xlabel("Tournament")
    plt.xticks(rotation=30)
    plt.ylabel(performance_metric)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title="Player", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(plt)

    # Team Performance Comparison Plot
    st.subheader(f"**Performance of All Players in the Team ({performance_metric})**")
    plt.figure(figsize=(12, 6))
    for player in team_data['Player'].unique():
        player_data = team_data[team_data['Player'] == player]
        sns.lineplot(
            data=player_data,
            x='Tournament',
            y=performance_metric,
            marker='o',
            label=player,
            alpha=0.8
        )
    plt.title(f"Team {team} Performance")
    plt.xlabel("Tournament")
    plt.ylabel(performance_metric)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title="Player", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(plt)

# Predict Cluster
with tabs[2]:
    st.header("🔍 Predict Cluster")
    st.markdown("---")
    st.markdown("""
    **Predict Cluster** allows you to predict the cluster of a new player based on their performance data.
    Enter the player's data below to see the predicted cluster.
    """)

    # Input Player Data
    st.subheader("Enter New Player Data")
    input_data = {
        "Average Combat Score": st.number_input("Average Combat Score", 0, 500, step=1),
        "Kills:Deaths": st.number_input("Kills:Deaths Ratio", 0.0, 5.0, step=0.1),
        "Average Damage Per Round": st.number_input("Average Damage Per Round", 0, 500, step=1)
    }
    
    # Predict Cluster
    if st.button("Predict Cluster"):
        model = load_model("player_performance_model.pkl")
        if model:
            prediction = model.predict(pd.DataFrame([input_data]))
            st.success(f"Predicted cluster for the new player: **{prediction[0]}**")

# Footer
st.markdown("""
<hr style="border: 1px solid #e1e1e1;">
<div style="text-align: center; font-size: 12px; color: #555;">
© 2024 Valorant Analytics Dashboard | Built with Streamlit
</div>
""", unsafe_allow_html=True)
