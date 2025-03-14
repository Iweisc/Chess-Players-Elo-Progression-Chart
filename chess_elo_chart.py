import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator
import matplotlib.gridspec as gridspec
from matplotlib.colors import LinearSegmentedColormap, Normalize
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator

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

# Create a highly detailed GitHub-style contribution chart for chess ELO ratings
plt.style.use('dark_background')
plt.rcParams['font.family'] = 'monospace'
plt.rcParams['figure.facecolor'] = '#0d1117'  # GitHub dark mode background
plt.rcParams['axes.facecolor'] = '#0d1117'
plt.rcParams['text.color'] = '#c9d1d9'  # GitHub text color
plt.rcParams['axes.labelcolor'] = '#c9d1d9'
plt.rcParams['xtick.color'] = '#c9d1d9'
plt.rcParams['ytick.color'] = '#c9d1d9'

# Create figure with subplots (higher resolution)
fig = plt.figure(figsize=(24, 18), dpi=150)
gs = gridspec.GridSpec(3, 2, height_ratios=[5, 1, 1], width_ratios=[5, 1])

# Main heatmap plot
ax_main = plt.subplot(gs[0, 0])
ax_legend = plt.subplot(gs[0, 1])
ax_info = plt.subplot(gs[1, :])
ax_timeline = plt.subplot(gs[2, :])

# Create a more detailed pandas DataFrame with interpolated data points
# Generate data at monthly intervals instead of yearly
all_ages = np.linspace(10, 75, 781)  # Monthly data points from age 10 to 75
df = pd.DataFrame(index=all_ages, columns=players_data.keys())

# Fill the DataFrame with ratings and interpolate for smoother transitions
for player, data in players_data.items():
    ages, ratings = zip(*data)
    
    # Create a function to interpolate between known data points
    from scipy.interpolate import interp1d
    f = interp1d(ages, ratings, kind='cubic', bounds_error=False, fill_value=(ratings[0], ratings[-1]))
    
    # Fill in interpolated values
    for age in all_ages:
        df.loc[age, player] = f(age)

# Create an enhanced GitHub-style colormap with more gradations
github_colors = ['#0e1117', '#0e4429', '#006d32', '#26a641', '#39d353']
# Add intermediate colors for smoother transitions
enhanced_colors = []
for i in range(len(github_colors)-1):
    # Add 3 intermediate colors between each pair
    for j in range(4):
        r1, g1, b1 = int(github_colors[i][1:3], 16), int(github_colors[i][3:5], 16), int(github_colors[i][5:7], 16)
        r2, g2, b2 = int(github_colors[i+1][1:3], 16), int(github_colors[i+1][3:5], 16), int(github_colors[i+1][5:7], 16)
        
        # Calculate intermediate color
        r = r1 + (r2 - r1) * j / 4
        g = g1 + (g2 - g1) * j / 4
        b = b1 + (b2 - b1) * j / 4
        
        enhanced_colors.append(f'#{int(r):02x}{int(g):02x}{int(b):02x}')

github_cmap = LinearSegmentedColormap.from_list('github_enhanced', enhanced_colors, N=256)

# Define the rating ranges for color mapping with finer granularity
min_rating = 2000
max_rating = 2900
norm = Normalize(vmin=min_rating, vmax=max_rating)

# Cell size and spacing (smaller cells for more detail)
cell_size = 0.15
cell_spacing = 0.05
total_cell_size = cell_size + cell_spacing

# Draw the highly detailed GitHub-style contribution grid
for i, player in enumerate(df.columns):
    player_data = df[player].dropna()
    
    # Sample data points to avoid overcrowding (show every 2 weeks)
    sampled_data = [(age, rating) for j, (age, rating) in enumerate(player_data.items()) if j % 2 == 0]
    
    for j, (age, rating) in enumerate(sampled_data):
        # Calculate cell position
        x = age
        y = i * total_cell_size
        
        # Determine cell color based on rating
        if pd.isna(rating):
            color = '#161b22'  # Empty cell color in GitHub dark mode
        else:
            color = github_cmap(norm(rating))
        
        # Draw the cell as a rounded rectangle with subtle 3D effect
        rect = patches.Rectangle((x - cell_size/2, y - cell_size/2), 
                                cell_size, cell_size, 
                                linewidth=0.5, edgecolor='#30363d',
                                facecolor=color, alpha=0.95, zorder=3,
                                angle=0, capstyle='round')
        ax_main.add_patch(rect)
        
        # Add subtle highlight to top-left edge for 3D effect
        if not pd.isna(rating) and rating > min_rating + 100:
            highlight = patches.Rectangle((x - cell_size/2, y - cell_size/2), 
                                        cell_size/3, cell_size/3, 
                                        linewidth=0, facecolor='white', 
                                        alpha=0.1, zorder=4)
            ax_main.add_patch(highlight)
        
        # Add world championship indicator (only for integer ages to avoid overcrowding)
        if player in world_champion_periods and abs(age - round(age)) < 0.01:
            for start_year, end_year in world_champion_periods[player]:
                birth_year = 0  # Approximate
                if start_year - birth_year <= age <= end_year - birth_year:
                    # Add a gold crown marker
                    ax_main.plot(x, y, marker='$♔$', markersize=6, 
                                color='gold', zorder=5)
        
        # Add notable achievement indicator
        if player in notable_events:
            for event_age, event in notable_events[player]:
                if abs(age - event_age) < 0.1:  # Allow small tolerance for matching
                    # Add a star marker
                    ax_main.plot(x, y, marker='*', markersize=8, 
                                color='gold', markeredgecolor='#30363d', 
                                markeredgewidth=0.5, zorder=6)
                    
                    # Add tooltip-style annotation
                    tooltip = ax_main.annotate(event,
                                xy=(x, y), xytext=(15, 0),
                                textcoords='offset points',
                                fontsize=8, color='#c9d1d9',
                                bbox=dict(boxstyle="round,pad=0.3", fc='#161b22', ec='#30363d', alpha=0.9),
                                arrowprops=dict(arrowstyle="->", color='#30363d'),
                                zorder=7, visible=False)
                    
                    # Create hover effect (simulated with always-visible for key events)
                    if "World Champion" in event or "highest" in event:
                        tooltip.set_visible(True)
    
    # Add rating trend line
    trend_ages = [age for age, _ in sampled_data]
    trend_ratings = [rating for _, rating in sampled_data]
    ax_main.plot(trend_ages, [y] * len(trend_ages), '-', color='#8b949e', 
                alpha=0.3, linewidth=0.5, zorder=2)

# Add player labels on y-axis with custom styling
ax_main.set_yticks([i * total_cell_size for i in range(len(df.columns))])
player_labels = []
for player in df.columns:
    # Add player name with peak rating
    peak_rating = max([rating for _, rating in players_data[player]])
    player_labels.append(f"{player} ({peak_rating})")
ax_main.set_yticklabels(player_labels, fontsize=10)

# Style the y-tick labels
for tick in ax_main.yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

# Set x-axis to show ages with more detail
ax_main.set_xticks(range(10, 76, 5))
ax_main.set_xticklabels(range(10, 76, 5), fontsize=9)
# Add minor ticks for each year
ax_main.set_xticks(range(10, 76, 1), minor=True)
ax_main.tick_params(axis='x', which='minor', length=2, color='#30363d')

# Remove spines
for spine in ax_main.spines.values():
    spine.set_visible(False)

# Add grid lines with more detail
ax_main.grid(True, linestyle='--', alpha=0.1, color='#30363d', which='major')
ax_main.grid(True, linestyle=':', alpha=0.05, color='#30363d', which='minor', axis='x')
ax_main.set_axisbelow(True)

# Set axis limits
ax_main.set_xlim(9.5, 73.5)
ax_main.set_ylim(-0.5, len(df.columns) * total_cell_size - 0.5)

# Add titles and labels with enhanced styling
title = ax_main.set_title('Chess Grandmasters ELO Rating Progression (Detailed GitHub-style Contribution Chart)', 
                fontsize=18, fontweight='bold', pad=20, color='#c9d1d9')
# Add subtle glow effect to title
title.set_path_effects([path_effects.withStroke(linewidth=3, foreground='#161b22')])

ax_main.set_xlabel('Age', fontsize=14, labelpad=10, color='#c9d1d9', fontweight='bold')

# Create an enhanced color legend in the separate axis
ax_legend.axis('off')

# Add rating level legend with more detailed gradations
legend_title = ax_legend.text(0.5, 0.95, "Rating Levels", 
                            ha='center', va='top', fontsize=12, 
                            fontweight='bold', color='#c9d1d9')
legend_title.set_path_effects([path_effects.withStroke(linewidth=2, foreground='#161b22')])

# Create more detailed rating level boxes (10 levels instead of 5)
step = (max_rating - min_rating) / 10
rating_levels = []
for i in range(10):
    start = min_rating + i * step
    end = min_rating + (i+1) * step
    # Get color from our enhanced colormap
    color_val = i / 10
    color = github_cmap(color_val)
    rating_levels.append({
        "label": f"{int(start)}-{int(end)}" if i < 9 else f"> {int(start)}",
        "color": color
    })

# Draw the rating level boxes in a grid (2 columns x 5 rows)
for i, level in enumerate(rating_levels):
    col = i // 5
    row = i % 5
    x_pos = 0.1 + col * 0.5
    y_pos = 0.85 - (row * 0.1)
    
    # Add color box with 3D effect
    rect = patches.Rectangle((x_pos, y_pos-0.03), 0.08, 0.06, 
                           facecolor=level["color"], edgecolor='#30363d',
                           linewidth=0.5)
    ax_legend.add_patch(rect)
    
    # Add subtle highlight for 3D effect
    if i > 0:  # Skip the darkest box
        highlight = patches.Rectangle((x_pos, y_pos-0.03), 0.03, 0.03, 
                                    linewidth=0, facecolor='white', alpha=0.1)
        ax_legend.add_patch(highlight)
    
    # Add label
    ax_legend.text(x_pos + 0.1, y_pos, level["label"], fontsize=8, 
                  va='center', color='#c9d1d9')

# Add indicators legend with enhanced styling
indicator_title = ax_legend.text(0.5, 0.3, "Indicators", ha='center', va='top', 
                               fontsize=12, fontweight='bold', color='#c9d1d9')
indicator_title.set_path_effects([path_effects.withStroke(linewidth=2, foreground='#161b22')])

# World champion indicator with enhanced styling
ax_legend.plot(0.15, 0.2, marker='$♔$', markersize=10, color='gold')
ax_legend.text(0.25, 0.2, "World Champion", fontsize=10, va='center', color='#c9d1d9',
              path_effects=[path_effects.withStroke(linewidth=1, foreground='#161b22')])

# Notable achievement indicator with enhanced styling
ax_legend.plot(0.15, 0.1, marker='*', markersize=10, color='gold', 
              markeredgecolor='#30363d', markeredgewidth=0.5)
ax_legend.text(0.25, 0.1, "Notable Achievement", fontsize=10, va='center', color='#c9d1d9',
              path_effects=[path_effects.withStroke(linewidth=1, foreground='#161b22')])

# Add statistics section
stats_title = ax_legend.text(0.5, -0.05, "Statistics", ha='center', va='top', 
                           fontsize=12, fontweight='bold', color='#c9d1d9')
stats_title.set_path_effects([path_effects.withStroke(linewidth=2, foreground='#161b22')])

# Calculate and display some statistics
total_cells = sum(len(player_data) for player in df.columns for player_data in [df[player].dropna()])
ax_legend.text(0.1, -0.15, f"Total Data Points: {total_cells:,}", fontsize=9, color='#c9d1d9')
ax_legend.text(0.1, -0.2, f"Date Range: Ages 10-75", fontsize=9, color='#c9d1d9')
ax_legend.text(0.1, -0.25, f"Rating Range: {min_rating}-{max_rating}", fontsize=9, color='#c9d1d9')

# Create enhanced rating categories section in info panel
ax_info.axis('off')
info_title = ax_info.set_title('Rating Categories and Historical Context', 
                             fontsize=14, fontweight='bold', color='#c9d1d9')
info_title.set_path_effects([path_effects.withStroke(linewidth=2, foreground='#161b22')])

# Create a grid for the info panel with 3 columns for more detail
info_grid = gridspec.GridSpecFromSubplotSpec(1, 3, subplot_spec=gs[1, :])

# Rating categories section with enhanced styling
ax_categories = fig.add_subplot(info_grid[0, 0])
ax_categories.axis('off')

# Add a background panel
ax_categories.add_patch(
    patches.Rectangle((0.02, 0.02), 0.96, 0.96, 
                     facecolor='#161b22', edgecolor='#30363d',
                     linewidth=1, alpha=0.7, zorder=1)
)

# Add a title for the section
cat_title = ax_categories.text(0.5, 0.95, "FIDE Rating Categories", 
                             fontsize=12, fontweight='bold', color='#c9d1d9',
                             ha='center', va='top', zorder=2)
cat_title.set_path_effects([path_effects.withStroke(linewidth=2, foreground='#161b22')])

# Create a GitHub-style table for rating categories with enhanced styling
category_data = [[cat['name'], f"{cat['min']}-{cat['max']}"] for cat in rating_categories]

for i, (name, range_text) in enumerate(category_data):
    y_pos = 0.85 - (i * 0.08)
    # Category name with color indicator
    color = rating_categories[i]['color']
    ax_categories.add_patch(
        patches.Rectangle((0.05, y_pos-0.03), 0.03, 0.06, 
                         facecolor=color, edgecolor='#30363d',
                         linewidth=0.5, alpha=0.7, zorder=2)
    )
    ax_categories.text(0.1, y_pos, name, fontsize=9, color='#c9d1d9', 
                      ha='left', va='center', zorder=2,
                      path_effects=[path_effects.withStroke(linewidth=1, foreground='#161b22')])
    
    # Rating range
    ax_categories.text(0.7, y_pos, range_text, fontsize=9, color='#c9d1d9', 
                      ha='left', va='center', zorder=2)
    
    # Add separator line
    if i < len(category_data) - 1:
        ax_categories.axhline(y=y_pos-0.04, xmin=0.05, xmax=0.95, 
                             color='#30363d', linestyle='-', linewidth=0.5, zorder=2)

# Historical context section with enhanced styling
ax_history = fig.add_subplot(info_grid[0, 1])
ax_history.axis('off')

# Add a background panel
ax_history.add_patch(
    patches.Rectangle((0.02, 0.02), 0.96, 0.96, 
                     facecolor='#161b22', edgecolor='#30363d',
                     linewidth=1, alpha=0.7, zorder=1)
)

# Add a title for the section
hist_title = ax_history.text(0.5, 0.95, "Historical Context", 
                           fontsize=12, fontweight='bold', color='#c9d1d9',
                           ha='center', va='top', zorder=2)
hist_title.set_path_effects([path_effects.withStroke(linewidth=2, foreground='#161b22')])

historical_notes = [
    "• FIDE rating system introduced in 1970",
    "• Pre-1970 ratings are retroactively calculated",
    "• 2700+ considered 'super-grandmaster' level",
    "• 2800+ achieved by only 15 players in history",
    "• 2882 (Carlsen, 2014) is the highest official rating",
    "• Ratings inflation: ~1-3 points per year"
]

y_pos = 0.85
for note in historical_notes:
    ax_history.text(0.05, y_pos, note, fontsize=9, va='top', ha='left', 
                   color='#c9d1d9', zorder=2)
    y_pos -= 0.15

# Add player achievements section
ax_achievements = fig.add_subplot(info_grid[0, 2])
ax_achievements.axis('off')

# Add a background panel
ax_achievements.add_patch(
    patches.Rectangle((0.02, 0.02), 0.96, 0.96, 
                     facecolor='#161b22', edgecolor='#30363d',
                     linewidth=1, alpha=0.7, zorder=1)
)

# Add a title for the section
ach_title = ax_achievements.text(0.5, 0.95, "Notable Achievements", 
                               fontsize=12, fontweight='bold', color='#c9d1d9',
                               ha='center', va='top', zorder=2)
ach_title.set_path_effects([path_effects.withStroke(linewidth=2, foreground='#161b22')])

# List some key achievements
achievements = [
    "• Kasparov: Longest time as world #1 (255 months)",
    "• Carlsen: Highest classical rating (2882)",
    "• Fischer: 20 consecutive wins against top players",
    "• Tal: Known for brilliant sacrificial attacks",
    "• Capablanca: Went 8 years without losing a game",
    "• Lasker: Held World Championship for 27 years"
]

y_pos = 0.85
for achievement in achievements:
    ax_achievements.text(0.05, y_pos, achievement, fontsize=9, va='top', ha='left', 
                        color='#c9d1d9', zorder=2)
    y_pos -= 0.15

# Create an enhanced timeline of chess history in the bottom panel
ax_timeline.axis('off')
timeline_title = ax_timeline.set_title('Timeline of Chess History', 
                                     fontsize=14, fontweight='bold', color='#c9d1d9')
timeline_title.set_path_effects([path_effects.withStroke(linewidth=2, foreground='#161b22')])

# Add a background panel
ax_timeline.add_patch(
    patches.Rectangle((0.02, 0.05), 0.96, 0.9, 
                     facecolor='#161b22', edgecolor='#30363d',
                     linewidth=1, alpha=0.7, zorder=1)
)

# Create more detailed timeline events
timeline_events = [
    {"year": 1886, "event": "First official World Championship (Steinitz)", "importance": "major"},
    {"year": 1894, "event": "Lasker defeats Steinitz", "importance": "minor"},
    {"year": 1921, "event": "Capablanca defeats Lasker", "importance": "minor"},
    {"year": 1924, "event": "FIDE founded", "importance": "major"},
    {"year": 1927, "event": "Alekhine defeats Capablanca", "importance": "minor"},
    {"year": 1935, "event": "Euwe defeats Alekhine", "importance": "minor"},
    {"year": 1948, "event": "First FIDE World Championship Tournament", "importance": "major"},
    {"year": 1958, "event": "Botvinnik-Tal rivalry begins", "importance": "minor"},
    {"year": 1970, "event": "FIDE rating system introduced", "importance": "major"},
    {"year": 1972, "event": "Fischer-Spassky 'Match of the Century'", "importance": "major"},
    {"year": 1975, "event": "Fischer forfeits title to Karpov", "importance": "minor"},
    {"year": 1985, "event": "Kasparov becomes youngest World Champion", "importance": "major"},
    {"year": 1993, "event": "PCA/FIDE split", "importance": "minor"},
    {"year": 1996, "event": "Kasparov vs Deep Blue", "importance": "major"},
    {"year": 2000, "event": "Kramnik defeats Kasparov", "importance": "minor"},
    {"year": 2006, "event": "FIDE/PCA reunification match", "importance": "minor"},
    {"year": 2013, "event": "Carlsen becomes World Champion", "importance": "major"},
    {"year": 2018, "event": "AlphaZero defeats Stockfish", "importance": "minor"},
    {"year": 2023, "event": "Ding Liren becomes World Champion", "importance": "major"}
]

# Draw enhanced timeline with decorative elements
timeline_start = 1880
timeline_end = 2025
ax_timeline.axhline(y=0.5, xmin=0.05, xmax=0.95, color='#30363d', linewidth=3, zorder=2)

# Add decade markers
for decade in range(1880, 2030, 10):
    x_pos = 0.05 + 0.9 * (decade - timeline_start) / (timeline_end - timeline_start)
    # Add tick mark
    ax_timeline.plot([x_pos, x_pos], [0.48, 0.52], '-', color='#8b949e', linewidth=1, zorder=3)
    # Add decade label
    ax_timeline.text(x_pos, 0.43, str(decade), fontsize=8, ha='center', va='top', 
                    color='#8b949e', zorder=3)

# Calculate position on timeline and add events
timeline_length = timeline_end - timeline_start
for event in timeline_events:
    x_pos = 0.05 + 0.9 * (event["year"] - timeline_start) / timeline_length
    
    # Add marker with different styling based on importance
    if event["importance"] == "major":
        marker_size = 10
        marker_color = '#39d353'
        text_size = 9
        text_weight = 'bold'
    else:
        marker_size = 7
        marker_color = '#26a641'
        text_size = 8
        text_weight = 'normal'
    
    # Add marker with 3D effect
    ax_timeline.plot(x_pos, 0.5, 'o', markersize=marker_size, color=marker_color, 
                    markeredgecolor='#30363d', markeredgewidth=1, zorder=4)
    
    # Add year label
    ax_timeline.text(x_pos, 0.4, str(event["year"]), fontsize=8, 
                    ha='center', va='top', color='#c9d1d9', zorder=3)
    
    # Add event description (alternating above/below)
    if timeline_events.index(event) % 2 == 0:
        y_text = 0.7
        va = 'bottom'
    else:
        y_text = 0.3
        va = 'top'
    
    # Add text with custom styling
    event_text = ax_timeline.text(x_pos, y_text, event["event"], fontsize=text_size, 
                                ha='center', va=va, color='#c9d1d9', fontweight=text_weight,
                                bbox=dict(boxstyle="round,pad=0.2", fc='#161b22', ec='#30363d', alpha=0.8),
                                zorder=4)
    
    # Add subtle glow effect for major events
    if event["importance"] == "major":
        event_text.set_path_effects([path_effects.withStroke(linewidth=1, foreground='#161b22')])

# Add connecting lines between events and timeline
for event in timeline_events:
    x_pos = 0.05 + 0.9 * (event["year"] - timeline_start) / timeline_length
    
    # Determine if event is above or below timeline
    if timeline_events.index(event) % 2 == 0:
        y_text = 0.65  # Adjust to connect to the text box
        ax_timeline.plot([x_pos, x_pos], [0.5, y_text], '--', color='#30363d', 
                        linewidth=0.5, alpha=0.7, zorder=2)
    else:
        y_text = 0.35  # Adjust to connect to the text box
        ax_timeline.plot([x_pos, x_pos], [0.5, y_text], '--', color='#30363d', 
                        linewidth=0.5, alpha=0.7, zorder=2)

# Add a watermark
watermark = ax_main.text(0.5, 0.5, "CHESS ELO", fontsize=100, color='#161b22',
                        ha='center', va='center', alpha=0.1, zorder=1,
                        fontweight='bold', rotation=30)

# Add metadata and credits
fig.text(0.01, 0.01, "Created with matplotlib • Data source: FIDE and historical records • © 2025",
        fontsize=8, color='#8b949e', ha='left')

# Adjust layout and save with higher resolution
plt.tight_layout()
fig.subplots_adjust(hspace=0.3, wspace=0.05)
plt.savefig('chess_grandmasters_github_style_detailed.png', dpi=300, bbox_inches='tight', 
           facecolor='#0d1117', pad_inches=0.2)
plt.show()
