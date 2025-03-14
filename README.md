# Chess Grandmasters ELO Progression Chart

A data visualization tool that charts the ELO rating progression of some of the greatest chess players throughout their careers.

![Chess ELO Chart Preview](chess_grandmasters_elo_progression.png)

## Overview

This project creates a detailed visualization of ELO rating progression for legendary chess players including:

- Hikaru Nakamura
- Garry Kasparov
- Magnus Carlsen
- Bobby Fischer
- Anatoly Karpov
- Viswanathan Anand
- Jose Raul Capablanca
- Mikhail Tal
- Emanuel Lasker

The chart shows how their ratings evolved with age, highlighting world championship periods and notable achievements.

## Features

- **Rating Progression**: Visualizes ELO rating changes throughout each player's career
- **World Championship Periods**: Highlighted with gold markers
- **Notable Achievements**: Key moments in each player's career marked with gold stars
- **Rating Categories**: Color-coded bands showing different rating levels (Candidate Master to All-Time Great)

## Requirements

- Python 3.6+
- matplotlib
- numpy
- pandas

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/chess-elo-chart.git
cd chess-elo-chart

# Install dependencies
pip install matplotlib numpy pandas
```

## Usage

```bash
python chess_elo_chart.py
```

This will generate a PNG file named `chess_grandmasters_elo_progression.png` in the current directory.

## Data Sources

The ELO ratings used in this visualization are approximate, especially for players from earlier eras before the official FIDE rating system was established in 1970. For pre-1970 players, ratings are estimated based on tournament performances and historical analyses.

## Customization

You can modify the `players_data`, `world_champion_periods`, and `notable_events` dictionaries in the script to:

- Add more players
- Update rating information
- Add or modify notable achievements
- Change the visual style of the chart

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
