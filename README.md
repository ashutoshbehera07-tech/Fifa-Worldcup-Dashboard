
# FIFA World Cup Analytics Dashboard

The **FIFA World Cup Analytics Dashboard** is a professional, interactive web application for exploring and visualizing the rich history of the FIFA World Cup. Built with **Python**, **Streamlit**, and **Plotly**, this dashboard empowers users to analyze team and player performance, goal trends, referee and disciplinary patterns, and the impact of match locations across all tournaments from 1930 to the present.

---

## 📑 Table of Contents

- [Overview](#fifa-world-cup-analytics-dashboard)
- [Features](#features)
- [Dashboard Action](#Dashboard-Action)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Dashboard](#running-the-dashboard)
- [Data Sources](#data-sources)
- [Dashboard Structure](#dashboard-structure)
- [Research Questions Addressed](#research-questions-addressed)
- [File Structure](#file-structure)
- [Customization](#customization)
- [Conclusion](#conclusion)
- [Acknowledgments & License](#acknowledgments--license)
- [Contact](#contact)

---
## DashBoard Video
[Watch the video](https://drive.google.com/file/d/1duWCICEg5TFpHvn14YhGkCrLszZNj6Sy/view?usp=sharing)

---
## 🚀 Features

✅ **Interactive Tournament and Team Selection**  
Filter and explore data by tournament year and team.

✅ **Consistent High Performance Analysis**  
Visualize team rankings over time and identify top-performing players.

✅ **Temporal Goal Patterns**  
Analyze when goals are scored (by half, extra time, penalties) and penalty shootout outcomes.

✅ **Referee & Disciplinary Trends**  
Explore cards by team, referee nationalities, and disciplinary patterns.

✅ **Country Improvement/Decline**  
Track team performance across tournaments and see the impact of hosting.

✅ **Location & Stadium Analysis**  
Examine how city, country, and stadium capacity relate to team performance.

✅ **Modern, Responsive UI**  
Clean layout with sidebar navigation, expanders, and interactive charts.

✅ **Data Table Exports**  
View and export match-level data for further analysis.

---

## 🎥 Dashbord Action

To see the dashboard in action, run it locally as described below.  
You can also add a video walkthrough or animated GIF in this section.

---

## 🏃 Getting Started

### ✅ Prerequisites

- Python 3.8 or higher
- The following Python packages:
  - `streamlit`
  - `pandas`
  - `plotly`

### 📦 Installation

1. Clone or download this repository:
   ```bash
   git clone (https://github.com/ashutoshbehera07-tech/Fifa-Worldcup-Dashboard.git)
   cd Fifa-Worldcup-Dashboard
   ```

2. Install dependencies:
   ```bash
   pip install streamlit pandas plotly
   ```

3. Place all required CSV data files in the same directory as `fifa_dashboard.py`.

### ▶️ Running the Dashboard

Open a terminal and navigate to the project directory:

```bash
streamlit run fifa_dashboard.py
```

The dashboard will open in your default web browser at [http://localhost:8501](http://localhost:8501).

---

## 📊 Data Sources

**Fjelstul World Cup Database**: Comprehensive, structured datasets covering all FIFA World Cups from 1930 to 2018, including teams, players, matches, goals, stadiums, referees, and more.

**Files Used:**
- `players.csv`
- `teams.csv`
- `tournament_standings.csv`
- `award_winners.csv`
- `goals.csv`
- `bookings.csv`
- `tournaments.csv`
- `penalty_kicks.csv`
- `referee_appointments.csv`
- `matches.csv`
- `stadiums.csv`
- `referees.csv`

_All data is used under the terms of the original dataset’s license. See the dataset documentation for details._

---

## 📂 Dashboard Structure

| Section                          | Description                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------|
| Consistent High Performance      | Bump chart of top teams’ rankings, top players by appearances, recent award winners     |
| Temporal Patterns of Goal Scoring | Bar chart of goals by match period, donut chart of penalty shootout outcomes           |
| Referee & Disciplinary Trends    | Card metrics for yellow/red cards, bar chart by team, radar chart of referee nationalities |
| Country Improvement or Decline   | Line chart of team performance over time, host country context                          |
| Match Location & Stadium Performance | Table of matches by location, bar chart by city, violin plot of stadium capacity vs. result |

---

## ❓ Research Questions Addressed

- Which teams and players have demonstrated consistent high performance or improvement over multiple World Cups?
- What are the temporal patterns of goal scoring—by half, extra time, and penalties—across tournaments and teams?
- How do referee assignments and decisions (e.g., cards, penalties awarded) influence match outcomes and disciplinary trends?
- Which countries have shown the greatest improvement or decline in performance over time, and what contextual factors (e.g., hosting, investment) explain these trends?
- What is the relationship between match location (city, country, stadium, capacity) and team performance?

Each section of the dashboard is designed to answer one or more of these questions with interactive, visual analytics.

---

## 🗂️ File Structure

```
fifa_dashboard.py
players.csv
teams.csv
tournament_standings.csv
award_winners.csv
goals.csv
bookings.csv
tournaments.csv
penalty_kicks.csv
referee_appointments.csv
matches.csv
stadiums.csv
referees.csv
FIFA-World-Cup_image.jpg
README.md
```

---

## 🎨 Customization

- **Add new research questions:** Duplicate a section and adjust the data queries/visualizations.
- **Change color themes:** Modify `color_discrete_sequence` or `color_continuous_scale` in Plotly charts.
- **Deploy online:** Use Streamlit Community Cloud or similar services for public sharing.
- **Update data:** Replace CSVs with newer versions as needed.

---

## ✅ Conclusion

The **FIFA World Cup Analytics Dashboard** provides a powerful, interactive platform for exploring the history and data of the world’s most celebrated football tournament. Whether you are a data scientist, football analyst, or passionate fan, this dashboard enables you to:

- Discover long-term trends in team and player performance
- Analyze when and how goals are scored
- Investigate the impact of referees and disciplinary actions
- Track the rise and fall of national teams
- Explore the influence of match locations and stadiums

With its modular design and open-source code, the dashboard can be easily extended to answer new research questions or incorporate future World Cup data. Dive in, explore, and uncover the stories behind the stats!

---

## 🙌 Acknowledgments & License

**Data:** Fjelstul World Cup Database (CC-BY-SA 4.0). Please credit Joshua C. Fjelstul, Ph.D., and include the dataset link if redistributing.

**Libraries:** Streamlit, Plotly, Pandas

**Dashboard Author:** Ashutosh Behera

---

## 📬 Contact

For questions, suggestions, or contributions, please contact:

**Name:** Ashutosh Behera  
**Email:** [ashutoshbehera470@gmail.com]  
**GitHub:** [ashutoshbeheratech-07](https://github.com/ashutoshbehera07-tech)

---

*This README provides all the information needed to understand, run, and extend the FIFA World Cup Analytics Dashboard. For further details, see the code comments and in-app tooltips.*
=======
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jEmd1PJR)
>>>>>>> 6e25b682ee9433f41085e36094eec3edd7ec1809
