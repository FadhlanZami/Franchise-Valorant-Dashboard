# Valorant Champions Tour 2023-2024 Franchise Player Performance Dashboard

This interactive dashboard built using **Streamlit** provides an in-depth analysis and visualization of player performance in the **Valorant Champions Tour 2023-2024**. The dashboard allows users to explore player clustering data, compare team performance, and predict player clusters based on their performance metrics.

## Key Features
- **Cluster View**: Analyze players' performance based on clusters of similar characteristics. You can view average statistics, feature distributions, and make comparisons across clusters.
- **Team View**: Explore player performance across different tournaments for each team. Compare players’ stats in various metrics and tournaments.
- **Predict Cluster**: Input data from a new player and predict which performance cluster they belong to, using a pre-trained machine learning model.

## Technologies Used
- **Streamlit**: For building the interactive web application.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib** and **Seaborn**: For data visualization.
- **Joblib**: For loading and saving the machine learning prediction model.

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine by running the following command:

```bash
git clone https://github.com/username/valorant-dashboard.git
cd valorant-dashboard
```

### Step 2: Install Dependencies
Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 3 : Run the Application
Once all dependencies are installed, run the application using the following command:

```bash
streamlit run app.py
```

### Step 4 : Access the Application
After the application is running, open your browser and access the application at:
```bash
(http://localhost:8501)
```


## Features

### 1. **Overall View**

In the **Overall View**, users can explore player performance data based on clusters. Each cluster represents a group of players who exhibit similar characteristics in their tournament performances. You can analyze and compare different clusters and view:

- **Player Data in Cluster**: View detailed performance data of players in a selected cluster and tournament.
- **Cluster Statistics**: Calculate the average and median statistics of players in the selected cluster. This helps in understanding general trends of players in each cluster.
- **Feature Distributions**: Analyze the distribution of various player statistics (e.g., average combat score, kills/deaths ratio) for each cluster.
- **Scatter Plot**: Visualize the relationship between two player performance features. This scatter plot helps in identifying patterns and trends across different clusters and tournaments.

### 2. **Team View**

The **Team View** provides insights into individual and overall team performance. This feature allows users to:

- **Team Performance Data**: View detailed statistics for all players within a specific team. This includes tournament-specific performance data for each player.
- **Team Statistics**: Access a summary of team-wide performance data, including statistical analysis of player performance across different metrics.
- **Player Performance**: Select a specific player within the team to see their performance over time in selected metrics (e.g., average damage per round).
- **Team Performance Comparison**: Compare the performance of all players within the team over multiple tournaments. This helps to assess how well each player contributed to the team's success.

### 3. **Predict Cluster**

The **Predict Cluster** feature allows you to predict the performance cluster of a new player based on their tournament data. By entering a player's performance metrics (e.g., Average Combat Score, Kills:Deaths ratio, Average Damage Per Round), you can:

- **Predict Cluster**: Use a machine learning model to predict which cluster the new player would belong to, based on their statistics.
- **User Input**: Input the performance data of a player to predict the cluster. This helps teams and analysts to classify a player’s performance into one of the predefined clusters.
