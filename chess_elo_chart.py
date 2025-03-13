import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator

# Data for some of the greatest chess players and their approximate ELO ratings at different ages
# Note: Historical ELO data is approximate, especially for older players
# Format: [age, rating]
players_data = {
    'Garry Kasparov': [
        (12, 2200), (16, 2400), (20, 2595), (24, 2700), 
        (28, 2800), (32, 2851), (36, 2849), (40, 2812),
        (44, 2812), (48, 2812), (52, 2812), (56, 2812)
    ],
    'Magnus Carlsen': [
        (12, 2300), (16, 2570), (20, 2800), (24, 2870),
        (28, 2882), (32, 2864), (34, 2847)
    ],
    'Bobby Fischer': [
        (12, 2200), (14, 2400), (16, 2580), (20, 2660),
        (24, 2760), (28, 2785), (32, 2780), (36, 2780),
        (40, 2780)
    ],
    'Anatoly Karpov': [
        (16, 2450), (20, 2660), (24, 2700), (28, 2725),
        (32, 2750), (36, 2730), (40, 2730), (44, 2700),
        (48, 2670), (52, 2650), (56, 2620), (60, 2600)
    ],
    'Viswanathan Anand': [
        (16, 2450), (20, 2600), (24, 2700), (28, 2750),
        (32, 2770), (36, 2790), (40, 2800), (44, 2810),
        (48, 2780), (52, 2760), (56, 2740)
    ],
    'Jose Raul Capablanca': [
        (16, 2400), (20, 2550), (24, 2650), (28, 2700),
        (32, 2720), (36, 2730), (40, 2720), (44, 2700),
        (48, 2680), (52, 2650)
    ]
}

# Set up the plot
plt.figure(figsize=(12, 8))
plt.title('ELO Rating Progression of Chess Grandmasters', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('ELO Rating', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

# Plot each player's data
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
markers = ['o', 's', '^', 'D', 'x', '*']

for i, (player, data) in enumerate(players_data.items()):
    ages, ratings = zip(*data)
    plt.plot(ages, ratings, marker=markers[i % len(markers)], 
             linestyle='-', linewidth=2, label=player, color=colors[i % len(colors)])

# Add legend and set axis limits
plt.legend(loc='lower right', fontsize=12)
plt.xlim(10, 60)
plt.ylim(2100, 2950)

# Set integer ticks for age axis
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

# Add annotations for peak ratings
for player, data in players_data.items():
    ages, ratings = zip(*data)
    max_rating = max(ratings)
    max_age = ages[ratings.index(max_rating)]
    plt.annotate(f"{max_rating}", 
                 xy=(max_age, max_rating),
                 xytext=(0, 10),
                 textcoords='offset points',
                 ha='center',
                 fontsize=9)

# Add a note about data approximation
plt.figtext(0.5, 0.01, "Note: Historical ELO ratings are approximate, especially for players from earlier eras.", 
            ha="center", fontsize=10, style='italic')

# Save the chart
plt.tight_layout()
plt.savefig('chess_grandmasters_elo_progression.png', dpi=300)
plt.show()
