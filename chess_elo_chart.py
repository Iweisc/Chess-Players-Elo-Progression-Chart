import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator, MultipleLocator
from matplotlib.patches import Rectangle
import matplotlib.patheffects as path_effects
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.gridspec as gridspec

# Data for some of the greatest chess players and their approximate ELO ratings at different ages
# Note: Historical ELO data is approximate, especially for older players
# Format: [age, rating]
players_data = {
    'Garry Kasparov': [
        (12, 2200), (13, 2250), (14, 2300), (15, 2350), (16, 2400), (17, 2450), (18, 2500), (19, 2545), 
        (20, 2595), (21, 2630), (22, 2665), (23, 2690), (24, 2700), (25, 2725), (26, 2750), (27, 2775), 
        (28, 2800), (29, 2815), (30, 2830), (31, 2840), (32, 2851), (33, 2851), (34, 2850), (35, 2850), 
        (36, 2849), (37, 2840), (38, 2830), (39, 2820), (40, 2812), (41, 2812), (42, 2812), (43, 2812),
        (44, 2812), (45, 2812), (46, 2812), (47, 2812), (48, 2812), (49, 2812), (50, 2812), (51, 2812), 
        (52, 2812), (53, 2812), (54, 2812), (55, 2812), (56, 2812), (57, 2812), (58, 2812), (59, 2812)
    ],
    'Magnus Carlsen': [
        (10, 2000), (11, 2150), (12, 2300), (13, 2350), (14, 2400), (15, 2500), (16, 2570), (17, 2650), 
        (18, 2700), (19, 2750), (20, 2800), (21, 2815), (22, 2835), (23, 2850), (24, 2870), (25, 2875), 
        (26, 2878), (27, 2880), (28, 2882), (29, 2881), (30, 2875), (31, 2870), (32, 2864), (33, 2855), 
        (34, 2847)
    ],
    'Bobby Fischer': [
        (11, 2000), (12, 2200), (13, 2300), (14, 2400), (15, 2500), (16, 2580), (17, 2600), (18, 2620), 
        (19, 2640), (20, 2660), (21, 2690), (22, 2720), (23, 2740), (24, 2760), (25, 2770), (26, 2775), 
        (27, 2780), (28, 2785), (29, 2785), (30, 2785), (31, 2780), (32, 2780), (33, 2780), (34, 2780), 
        (35, 2780), (36, 2780), (37, 2780), (38, 2780), (39, 2780), (40, 2780)
    ],
    'Anatoly Karpov': [
        (15, 2400), (16, 2450), (17, 2500), (18, 2550), (19, 2600), (20, 2660), (21, 2670), (22, 2680), 
        (23, 2690), (24, 2700), (25, 2705), (26, 2710), (27, 2720), (28, 2725), (29, 2730), (30, 2740), 
        (31, 2745), (32, 2750), (33, 2745), (34, 2740), (35, 2735), (36, 2730), (37, 2730), (38, 2730), 
        (39, 2730), (40, 2730), (41, 2725), (42, 2715), (43, 2705), (44, 2700), (45, 2690), (46, 2680), 
        (47, 2675), (48, 2670), (49, 2665), (50, 2660), (51, 2655), (52, 2650), (53, 2640), (54, 2630), 
        (55, 2625), (56, 2620), (57, 2615), (58, 2610), (59, 2605), (60, 2600)
    ],
    'Viswanathan Anand': [
        (15, 2400), (16, 2450), (17, 2500), (18, 2525), (19, 2550), (20, 2600), (21, 2625), (22, 2650), 
        (23, 2675), (24, 2700), (25, 2710), (26, 2720), (27, 2735), (28, 2750), (29, 2755), (30, 2760), 
        (31, 2765), (32, 2770), (33, 2775), (34, 2780), (35, 2785), (36, 2790), (37, 2792), (38, 2795), 
        (39, 2798), (40, 2800), (41, 2803), (42, 2805), (43, 2808), (44, 2810), (45, 2805), (46, 2795), 
        (47, 2785), (48, 2780), (49, 2775), (50, 2770), (51, 2765), (52, 2760), (53, 2755), (54, 2750), 
        (55, 2745), (56, 2740)
    ],
    'Jose Raul Capablanca': [
        (15, 2350), (16, 2400), (17, 2425), (18, 2450), (19, 2500), (20, 2550), (21, 2575), (22, 2600), 
        (23, 2625), (24, 2650), (25, 2660), (26, 2675), (27, 2690), (28, 2700), (29, 2705), (30, 2710), 
        (31, 2715), (32, 2720), (33, 2725), (34, 2730), (35, 2730), (36, 2730), (37, 2725), (38, 2725), 
        (39, 2720), (40, 2720), (41, 2715), (42, 2710), (43, 2705), (44, 2700), (45, 2695), (46, 2690), 
        (47, 2685), (48, 2680), (49, 2670), (50, 2665), (51, 2660), (52, 2650)
    ],
    'Mikhail Tal': [
        (16, 2400), (17, 2450), (18, 2500), (19, 2550), (20, 2600), (21, 2650), (22, 2700), (23, 2750),
        (24, 2780), (25, 2785), (26, 2780), (27, 2775), (28, 2770), (29, 2765), (30, 2760), (31, 2755),
        (32, 2750), (33, 2745), (34, 2740), (35, 2735), (36, 2730), (37, 2725), (38, 2720), (39, 2715),
        (40, 2710), (41, 2705), (42, 2700), (43, 2695), (44, 2690), (45, 2685), (46, 2680), (47, 2675),
        (48, 2670), (49, 2665), (50, 2660), (51, 2655), (52, 2650), (53, 2645), (54, 2640), (55, 2630)
    ],
    'Emanuel Lasker': [
        (20, 2500), (22, 2550), (24, 2600), (26, 2650), (28, 2700), (30, 2720), (32, 2730), (34, 2740),
        (36, 2750), (38, 2760), (40, 2760), (42, 2755), (44, 2750), (46, 2745), (48, 2740), (50, 2735),
        (52, 2730), (54, 2720), (56, 2710), (58, 2700), (60, 2690), (62, 2680), (64, 2670), (66, 2660),
        (68, 2650), (70, 2640), (72, 2630)
    ]
}

# World Championship periods for each player
world_champion_periods = {
    'Garry Kasparov': [(1985, 2000)],
    'Magnus Carlsen': [(2013, 2023)],
    'Bobby Fischer': [(1972, 1975)],
    'Anatoly Karpov': [(1975, 1985), (1993, 1999)],
    'Viswanathan Anand': [(2007, 2013)],
    'Jose Raul Capablanca': [(1921, 1927)],
    'Mikhail Tal': [(1960, 1961)],
    'Emanuel Lasker': [(1894, 1921)]
}

# Notable achievements and tournaments
notable_events = {
    'Garry Kasparov': [
        (22, 'Becomes youngest World Champion'),
        (36, 'Highest classical rating in history (2851)'),
        (41, 'Retires from professional chess')
    ],
    'Magnus Carlsen': [
        (22, 'Becomes World Champion'),
        (28, 'Highest rating in history (2882)'),
        (32, 'Resigns World Championship title')
    ],
    'Bobby Fischer': [
        (15, 'Becomes youngest US Champion'),
        (29, 'Wins World Championship vs Spassky'),
        (32, 'Forfeits title to Karpov')
    ],
    'Anatoly Karpov': [
        (24, 'Becomes World Champion'),
        (30, 'First FIDE rating list #1')
    ],
    'Viswanathan Anand': [
        (37, 'Wins World Championship Tournament'),
        (43, 'Loses title to Carlsen')
    ],
    'Jose Raul Capablanca': [
        (33, 'Wins World Championship'),
        (39, 'Loses title to Alekhine')
    ]
}

# Rating categories
rating_categories = [
    {'name': 'Candidate Master', 'min': 2000, 'max': 2199, 'color': '#8dd3c7'},
    {'name': 'FIDE Master', 'min': 2200, 'max': 2299, 'color': '#ffffb3'},
    {'name': 'International Master', 'min': 2300, 'max': 2399, 'color': '#bebada'},
    {'name': 'Grandmaster', 'min': 2400, 'max': 2499, 'color': '#fb8072'},
    {'name': 'Super Grandmaster', 'min': 2500, 'max': 2599, 'color': '#80b1d3'},
    {'name': 'Elite Grandmaster', 'min': 2600, 'max': 2699, 'color': '#fdb462'},
    {'name': 'Super Elite', 'min': 2700, 'max': 2799, 'color': '#b3de69'},
    {'name': 'World Champion Level', 'min': 2800, 'max': 2899, 'color': '#fccde5'},
    {'name': 'All-Time Great', 'min': 2900, 'max': 3000, 'color': '#d9d9d9'}
]

# Set up the plot with a custom style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.facecolor'] = '#f8f9fa'
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['grid.color'] = '#cccccc'
plt.rcParams['grid.linestyle'] = ':'
plt.rcParams['grid.linewidth'] = 0.5

# Create figure with subplots
fig = plt.figure(figsize=(20, 16))
gs = gridspec.GridSpec(2, 2, height_ratios=[4, 1], width_ratios=[5, 1])

# Main plot
ax_main = plt.subplot(gs[0, 0])
ax_legend = plt.subplot(gs[0, 1])
ax_info = plt.subplot(gs[1, :])

# Add background color bands for rating categories
for category in rating_categories:
    ax_main.axhspan(category['min'], category['max'], alpha=0.1, color=category['color'], 
                   zorder=0, label=category['name'])

# Plot each player's data with enhanced styling
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']
markers = ['o', 's', '^', 'D', 'x', '*', 'p', 'h', 'v']
linestyles = ['-', '--', '-.', ':', '-', '--', '-.', ':', '-']

for i, (player, data) in enumerate(players_data.items()):
    ages, ratings = zip(*data)
    color = colors[i % len(colors)]
    
    # Plot the main line with enhanced styling
    line = ax_main.plot(ages, ratings, marker=markers[i % len(markers)], 
             linestyle=linestyles[i % len(linestyles)], linewidth=3, 
             label=player, color=color, markersize=8, markeredgewidth=1.5,
             markeredgecolor='white', zorder=5, alpha=0.9)
    
    # Add a subtle shadow effect to the line
    ax_main.plot(ages, ratings, linewidth=5, color=color, alpha=0.3, zorder=4)
    
    # Highlight world championship periods
    if player in world_champion_periods:
        for start_year, end_year in world_champion_periods[player]:
            # Find ages that correspond to championship years
            birth_year = 0  # This is approximate
            for age in ages:
                if start_year - birth_year <= age <= end_year - birth_year:
                    idx = ages.index(age)
                    if idx < len(ratings):
                        ax_main.plot(age, ratings[idx], 'o', markersize=12, 
                                    markerfacecolor='gold', markeredgecolor=color, 
                                    markeredgewidth=2, alpha=0.8, zorder=6)
    
    # Add notable achievements
    if player in notable_events:
        for age, event in notable_events[player]:
            if age in ages:
                idx = ages.index(age)
                if idx < len(ratings):
                    rating = ratings[idx]
                    # Add star marker
                    ax_main.plot(age, rating, marker='*', markersize=20, 
                                color='gold', markeredgecolor='black', 
                                markeredgewidth=1.5, zorder=7)
                    
                    # Add annotation with event description
                    text = ax_main.annotate(event, 
                                xy=(age, rating), 
                                xytext=(15, 15),
                                textcoords='offset points',
                                fontsize=9, fontweight='bold',
                                bbox=dict(boxstyle="round,pad=0.3", fc='white', ec=color, alpha=0.8),
                                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2", 
                                                color=color, lw=1.5),
                                zorder=8)
                    
                    # Add path effect to make text more readable
                    text.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])

# Add annotations for peak ratings with enhanced styling
for player, data in players_data.items():
    ages, ratings = zip(*data)
    max_rating = max(ratings)
    max_age = ages[ratings.index(max_rating)]
    
    # Create a more visible annotation for peak rating
    text = ax_main.annotate(f"Peak: {max_rating}", 
                 xy=(max_age, max_rating),
                 xytext=(0, 15),
                 textcoords='offset points',
                 ha='center',
                 fontsize=10,
                 fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.3", fc='white', ec='black', alpha=0.7))
    
    # Add path effect to make text more readable
    text.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])

# Enhance grid and ticks
ax_main.grid(True, linestyle='--', alpha=0.7, which='both')
ax_main.set_axisbelow(True)
ax_main.xaxis.set_major_locator(MultipleLocator(5))
ax_main.xaxis.set_minor_locator(MultipleLocator(1))
ax_main.yaxis.set_major_locator(MultipleLocator(100))
ax_main.yaxis.set_minor_locator(MultipleLocator(25))
ax_main.tick_params(axis='both', which='major', labelsize=12)

# Set axis limits with some padding
ax_main.set_xlim(9, 73)
ax_main.set_ylim(1950, 2950)

# Add titles and labels with enhanced styling
title = ax_main.set_title('ELO Rating Progression of Chess Grandmasters Throughout Their Careers', 
                        fontsize=22, fontweight='bold', pad=20)
title.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])

ax_main.set_xlabel('Age', fontsize=18, fontweight='bold', labelpad=15)
ax_main.set_ylabel('ELO Rating', fontsize=18, fontweight='bold', labelpad=15)

# Create a custom legend in the separate axis
ax_legend.axis('off')
legend_elements = []

# Add player legend entries
for i, player in enumerate(players_data.keys()):
    color = colors[i % len(colors)]
    marker = markers[i % len(markers)]
    linestyle = linestyles[i % len(linestyles)]
    
    # Create custom legend entry
    legend_elements.append(plt.Line2D([0], [0], color=color, marker=marker, 
                                     linestyle=linestyle, linewidth=3, markersize=10,
                                     markerfacecolor=color, markeredgecolor='white',
                                     label=player))

# Add world champion indicator to legend
legend_elements.append(plt.Line2D([0], [0], marker='o', color='white', 
                                 markerfacecolor='gold', markersize=12, 
                                 markeredgecolor='black', markeredgewidth=1.5,
                                 label='World Champion Period'))

# Add notable achievement indicator to legend
legend_elements.append(plt.Line2D([0], [0], marker='*', color='white', 
                                 markerfacecolor='gold', markersize=15, 
                                 markeredgecolor='black', markeredgewidth=1.5,
                                 label='Notable Achievement'))

# Create the legend with enhanced styling
legend = ax_legend.legend(handles=legend_elements, loc='center left', 
                         fontsize=14, frameon=True, framealpha=0.95,
                         edgecolor='black', fancybox=True, shadow=True)

# Add rating category legend to the info panel
ax_info.axis('off')
ax_info.set_title('Rating Categories and Historical Context', fontsize=16, fontweight='bold')

# Create a grid for the info panel
info_grid = gridspec.GridSpecFromSubplotSpec(2, 4, subplot_spec=gs[1, :])

# Rating categories section
ax_categories = fig.add_subplot(info_grid[0, :2])
ax_categories.axis('off')

# Create a table for rating categories
category_data = [[cat['name'], f"{cat['min']}-{cat['max']}"] for cat in rating_categories]
category_colors = [cat['color'] for cat in rating_categories]

table = ax_categories.table(cellText=category_data, 
                           colLabels=['Rating Category', 'ELO Range'],
                           loc='center', cellLoc='center',
                           colWidths=[0.6, 0.4])
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 1.5)

# Color the rows according to category colors
for i, color in enumerate(category_colors):
    for j in range(2):
        table[(i+1, j)].set_facecolor(color)
        table[(i+1, j)].set_alpha(0.3)

# Historical context section
ax_history = fig.add_subplot(info_grid[0, 2:])
ax_history.axis('off')

historical_notes = [
    "• FIDE rating system introduced in 1970",
    "• Pre-1970 ratings are retroactively calculated",
    "• 2700+ considered 'super-grandmaster' level",
    "• 2800+ achieved by only 15 players in history",
    "• 2882 (Carlsen, 2014) is the highest official rating"
]

y_pos = 0.9
for note in historical_notes:
    ax_history.text(0.05, y_pos, note, fontsize=12, va='top', ha='left')
    y_pos -= 0.2

# Add data source and methodology notes
ax_notes = fig.add_subplot(info_grid[1, :])
ax_notes.axis('off')

methodology_text = """
Data Methodology: Historical ELO ratings are approximate, especially for players from earlier eras before the official FIDE rating system.
For pre-1970 players, ratings are estimated based on tournament performances and historical analyses.
World Championship periods are highlighted with gold markers. Notable achievements are marked with gold stars.
"""

ax_notes.text(0.5, 0.5, methodology_text, fontsize=12, va='center', ha='center', 
             wrap=True, style='italic', bbox=dict(boxstyle="round,pad=0.5", 
                                                 fc='#f8f9fa', ec='#cccccc'))

# Add a subtle chess-themed watermark
ax_main.text(0.5, 0.5, '♚', fontsize=300, color='#f0f0f0', 
            ha='center', va='center', alpha=0.2, zorder=0,
            transform=ax_main.transAxes)

# Adjust layout and save with high resolution
plt.tight_layout()
fig.subplots_adjust(hspace=0.2, wspace=0.05)
plt.savefig('chess_grandmasters_elo_progression_detailed.png', dpi=600, bbox_inches='tight')
plt.show()
