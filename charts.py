import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='darkgrid')

def chart1_pie(df):
    play_counts = df['play_type'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 8))
    wedges, texts, autotexts = ax.pie(
        play_counts,
        autopct='%1.1f%%',
        colors=sns.color_palette('Set2', len(play_counts)),
        startangle=90,
        pctdistance=0.75,
        wedgeprops=dict(width=0.6)
    )
    for text in autotexts:
        text.set_fontsize(9)
    ax.legend(
        wedges,
        play_counts.index,
        title="Play Types",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=10
    )
    ax.set_title('Play Type Distribution', fontsize=14, fontweight='bold')
    plt.tight_layout()
    return fig

def chart2_histogram(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(df['yards_gained'], bins=50, color='steelblue', edgecolor='white')
    ax.set_title('Yards Gained Distribution', fontsize=14, fontweight='bold')
    ax.set_xlabel('Yards Gained')
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    return fig

def chart3_line(df):
    weekly = df.groupby('week')['yards_gained'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(weekly['week'], weekly['yards_gained'],
            marker='o', color='steelblue', linewidth=2)
    ax.set_title('Average Yards Gained per Week', fontsize=14, fontweight='bold')
    ax.set_xlabel('Week')
    ax.set_ylabel('Avg Yards')
    plt.tight_layout()
    return fig

def chart4_bar(df):
    top_teams = df.groupby('posteam')['yards_gained'].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    top_teams.plot(kind='bar', ax=ax, color=sns.color_palette('Set2', 10))
    ax.set_title('Top 10 Teams by Avg Yards Gained', fontsize=14, fontweight='bold')
    ax.set_xlabel('Team')
    ax.set_ylabel('Avg Yards')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    return fig

def chart5_scatter(df):
    sample = df[df['play_type'].isin(['pass','run'])].sample(min(2000, len(df)), random_state=42)
    fig, ax = plt.subplots(figsize=(10, 5))
    for ptype, color in zip(['pass','run'], ['steelblue','coral']):
        s = sample[sample['play_type'] == ptype]
        ax.scatter(s['ydstogo'], s['yards_gained'],
                   alpha=0.4, label=ptype, color=color, s=20)
    ax.set_title('Yards to Go vs Yards Gained', fontsize=14, fontweight='bold')
    ax.set_xlabel('Yards to Go')
    ax.set_ylabel('Yards Gained')
    ax.legend()
    plt.tight_layout()
    return fig

def chart6_box(df):
    box_data = df[df['play_type'].isin(['pass','run','punt','field_goal'])]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=box_data, x='play_type', y='yards_gained',
                palette='Set2', ax=ax)
    ax.set_title('Yards Gained by Play Type', fontsize=14, fontweight='bold')
    ax.set_xlabel('Play Type')
    ax.set_ylabel('Yards Gained')
    plt.tight_layout()
    return fig

def chart7_heatmap(df):
    cols = ['yards_gained','ydstogo','score_differential',
            'epa','wp','qb_epa','down','qtr']
    corr = df[cols].corr()
    fig, ax = plt.subplots(figsize=(10, 7))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
                ax=ax, linewidths=0.5)
    ax.set_title('Feature Correlation Heatmap', fontsize=14, fontweight='bold')
    plt.tight_layout()
    return fig

def chart8_area(df):
    weekly_tds = df.groupby('week')['touchdown'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.fill_between(weekly_tds['week'], weekly_tds['touchdown'],
                    color='steelblue', alpha=0.5)
    ax.plot(weekly_tds['week'], weekly_tds['touchdown'],
            color='steelblue', linewidth=2)
    ax.set_title('Total Touchdowns per Week', fontsize=14, fontweight='bold')
    ax.set_xlabel('Week')
    ax.set_ylabel('Touchdowns')
    plt.tight_layout()
    return fig

def chart9_countplot(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(data=df, x='qtr', palette='Set2', ax=ax)
    ax.set_title('Number of Plays per Quarter', fontsize=14, fontweight='bold')
    ax.set_xlabel('Quarter')
    ax.set_ylabel('Number of Plays')
    plt.tight_layout()
    return fig

def chart10_violin(df):
    violin_data = df[df['play_type'].isin(['pass','run'])]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.violinplot(data=violin_data, x='play_type', y='yards_gained',
                   palette='Set2', ax=ax)
    ax.set_title('Yards Gained Distribution - Pass vs Run', fontsize=14, fontweight='bold')
    ax.set_xlabel('Play Type')
    ax.set_ylabel('Yards Gained')
    plt.tight_layout()
    return fig