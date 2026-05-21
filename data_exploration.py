import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("  MODULE 1: Gradient Boosting for Purchase Prediction")
print("  Step 1: Data Exploration & Understanding")
print("=" * 60)

# ==========================================
# [1] LOADING DATASETS
# ==========================================
print("\n[1] Loading datasets...")

# TODO: Load 'data/events.csv' using pandas
events = None 

# TODO: Load the two item properties datasets ('data/item_properties_part1.csv' and 'data/item_properties_part2.csv')
props1 = None
props2 = None

# TODO: Combine props1 and props2 vertically into a single dataframe named 'item_props'
# Hint: Use pd.concat and remember to ignore the original indexes so they form a continuous sequence
item_props = None

print(f"    Events shape      : {events.shape if events is not None else 'Not Implemented'}")
print(f"    Item props shape  : {item_props.shape if item_props is not None else 'Not Implemented'}")


# ==========================================
# [2] EVENT TYPE DISTRIBUTION
# ==========================================
print("\n[2] Event type distribution:")

# TODO: Compute the raw count of each unique value in the 'event' column of the events dataframe
event_counts = None
print(event_counts.to_string() if event_counts is not None else "    Not Implemented")

print("\n    As % of total events:")
# TODO: Calculate the percentage distribution of the event types, rounded to 2 decimal places
# Hint: Divide the event_counts by the total length of the events dataframe and multiply by 100
event_percentages = None
print(event_percentages.to_string() if event_percentages is not None else "    Not Implemented")


# ==========================================
# [3] DATA QUALITY & TIMESTAMP PARSING
# ==========================================
print("\n[3] Data quality check:")

# TODO: Calculate the total number of missing/null values for each column in the events dataframe
null_counts = None
print(f"    Null values in events:\n{null_counts}")

# TODO: The 'timestamp' column is in milliseconds. Convert it to a readable datetime format.
# Hint: Use pd.to_datetime and specify the unit as 'ms'
events['datetime'] = None

print(f"\n    Events date range:")
# TODO: Find and print the minimum and maximum dates in your new 'datetime' column
print(f"    Start : {None}")
print(f"    End   : {None}")


# ==========================================
# [4] USER BEHAVIOR SUMMARY STATISTICS
# ==========================================
print("\n[4] User behavior summary:")

# TODO: Calculate the total number of unique users (visitorid) and unique items (itemid)
unique_users = None
unique_items = None
total_events = None

print(f"    Unique users  : {unique_users}")
print(f"    Unique items  : {unique_items}")
print(f"    Total events  : {total_events}")

# TODO: Group the events dataframe by 'visitorid' and calculate the total number of actions/events per user
events_per_user = None

# TODO: From the events_per_user data, calculate the mean, median, and maximum values
avg_events = None
median_events = None
max_events = None

print(f"\n    Avg events/user  : {avg_events}")
print(f"    Median           : {median_events}")
print(f"    Max              : {max_events}")


# ==========================================
# [5] GENERATING VISUALIZATIONS
# ==========================================
print("\n[5] Generating visualizations...")

# TODO: Set up a figure with 1 row and 2 columns of subplots with a figure size of (14, 5)
fig, axes = None

# TODO: Add a main bold title to the figure: "Retailrocket Dataset - Exploratory Analysis"
# Hint: Use fig.suptitle with a suitable fontsize and fontweight


# --- Left Subplot: Bar Chart of Event Counts ---
colors = ['#4C72B0', '#DD8452', '#55A868']
# TODO: Plot a bar chart on axes[0] showing the counts of each event type
# Hint: Use event_counts index for x-axis and values for y-axis


# TODO: Customize axes[0] by setting its Title ("Event Type Distribution"), X-label ("Event Type"), and Y-label ("Count")


# TODO: (Optional/Bonus challenge for students): 
# Loop through the bars and add a text label displaying the raw count value slightly above each bar
# Hint: Use axes[0].text() with alignment settings


# --- Right Subplot: Histogram of Events per User ---
# TODO: Plot a histogram on axes[1] representing the distribution of events_per_user values
# Hint: Set bins to 50, choose a solid color, and use an edge color to separate bars


# TODO: Customize axes[1] by setting its Title ("Events per User Distribution"), X-label ("Number of Events"), and Y-label ("Number of Users")


# TODO: Because a few users have massive amounts of events, change the Y-axis scale of axes[1] to logarithmic
# Hint: Use axes[1].set_yscale()


# --- Save and Render ---
# TODO: Adjust the subplot layout automatically to prevent overlap text, save to 'output/01_eda_overview.png' with 150 DPI, and display the plot
# Hint: use plt.tight_layout(), plt.savefig(), and plt.show()


print("    Saved -> output/01_eda_overview.png")
