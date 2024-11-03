# CSAS 2025 Data Challenge
[Reference](https://statds.org/events/csas2025/challenge.html)

[Background](https://technology.mlblogs.com/introducing-statcast-2023-high-frame-rate-bat-and-biomechanics-tracking-3844890264a6)

## Requirements
- Python 3.11.6

### Challenge Summary
The goal is to use data on bat speed and swing length to analyze some aspects of the pitcher/batter interaction.

Pitch-level data from Baseball Savant for 346250 Major League Baseball plate appearances from 4/2/2024 to 6/30/2024.

The analysis should involve bat speed and swing length to study any topic related to the batter, pitcher, or batter-pitcher interaction.

### Judging Criteria

- How original is the analysis?
- How applicable is the analysis?
- How appropriate were the methods used?
- How well did you communicate your findings? This includes both written text and visualizations. How did the use of facts, data-supported narratives, anecdotes etc. enhance your storytelling?

### Navigation
- A data dictionary is located at [glossary/data_dictionary.md](https://github.com/jonmontg/CSAS_Data_Challenge/blob/main/glossary/data_dictionary.md)
- Documentation generation utilities are located in [lib/documentation.py](https://github.com/jonmontg/CSAS_Data_Challenge/blob/main/lib/documentation.py)
- Data is read and processed in [lib/data_util.py](https://github.com/jonmontg/CSAS_Data_Challenge/blob/main/lib/data_util.py)

### Data Transformations
- integer-type columns are downsized to minimum storage size
- game_date column is converted from a string to a date
- columns with no information are dropped
- any plate appearance with a "swing event" and no recorded bat speed or swing length is dropped. The following events are considered 'swing events':
  - hit_into_play
  - foul
  - foul_tip
  - swinging_strike
  - swinging_strike_blocked
  - foul_bunt
  - missing_bunt
  - bunt_foul_tip


### Ideas

1. Swing Speed vs. Play Outcome Analysis
Objective: Identify how swing speed correlates with play outcomes (e.g., hits, home runs, strikeouts).
Analysis:
Examine whether higher swing speeds lead to more successful outcomes, such as extra-base hits or home runs.
Explore potential thresholds (e.g., "optimal" swing speeds) that maximize the likelihood of certain outcomes.
Use logistic regression or classification models to predict successful outcomes based on swing speed.
2. Swing Speed and Bat Length Impact on Ball Exit Velocity
Objective: Evaluate how swing speed and bat length interact to influence exit velocity.
Analysis:
Conduct a multivariate analysis to understand the combined impact of swing speed and bat length on exit velocity.
Determine if a certain range of swing speeds with specific bat lengths maximizes exit velocity, which can translate into stronger, farther hits.
3. Consistency in Swing Mechanics and Player Performance
Objective: Assess the variability in swing speed and bat length across multiple at-bats to understand consistency in player mechanics.
Analysis:
Measure consistency in swing speed and length and correlate it with player performance. Are players with consistent swing mechanics more successful?
Track patterns across games or seasons to gauge if players’ consistent swing mechanics lead to sustained performance.
4. Swing Speed and Pitch Physics Correlation
Objective: Determine if players adjust swing speed based on pitch type, speed, or other physical attributes of the pitch.
Analysis:
Evaluate how swing speed and bat length vary depending on the physics of the pitch, such as fastballs vs. curveballs.
Insights here could be valuable to teams for strategy, as they reveal how players respond to different pitches.
5. Impact of Swing Speed and Bat Length on Strikeout Rates
Objective: Identify whether swing mechanics (speed and length) influence strikeout tendencies.
Analysis:
Investigate if players with faster or shorter swings have lower strikeout rates.
This insight could be useful to betting markets and teams, highlighting players likely to connect or miss based on swing mechanics.
6. Benchmarking Players Using Swing Speed and Bat Length
Objective: Rank players based on their swing metrics and performance to highlight key players in terms of power or accuracy.
Analysis:
Create player profiles or "swing archetypes" based on their swing speed and bat length.
Use clustering to segment players into different types, which can help news outlets narrate player strengths or weaknesses in swing mechanics.
7. Predictive Modeling for Betting Markets
Objective: Build models that use swing speed and bat length to predict the likelihood of specific at-bat outcomes, valuable for betting predictions.
Analysis:
Use machine learning to predict outcomes like hits, home runs, or strikeouts based on swing speed and bat length.
Analyze whether swing metrics can offer predictive value in specific game contexts, adding granularity to betting odds.
Each of these directions would offer a narrative or actionable insight for different stakeholders and could highlight how bat mechanics impact performance in baseball.
