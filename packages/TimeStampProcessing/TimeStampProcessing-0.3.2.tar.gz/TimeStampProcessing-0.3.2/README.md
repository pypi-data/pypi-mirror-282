# TimeStampProcessing

`TimeStampProcessing` is a Python package designed to simplify and enhance operations involving timestamps and time series data. This package includes a wide range of utilities for parsing, comparing, and manipulating timestamps, which can be particularly useful in time-sensitive data analysis tasks.

## Features
- **Time Series Resampling**: Resample time series data in a DataFrame to specified intervals with linear interpolation, simplifying data analysis and visualization.

- **Statistical Analysis**: Compute and retrieve specific statistics such as max, min, mean, and various percentiles from a single-column DataFrame, enhancing data-driven insights.

- **Column Sum Comparison**: Identify columns with the maximum and minimum sums within a specified time range in a DataFrame, aiding in financial and operational analysis.

- **Conditional Time Range Identification**: Determine periods when specified conditions between two DataFrame columns hold true, useful for comparative data analysis.

- **Sunrise and Sunset Calculation**: Calculate exact times of sunrise and sunset for given coordinates and dates, supporting planning and research activities that depend on daylight.

- **Leap Year Checker**: Determine whether a specified year is a leap year, crucial for accurate date and time calculations in scheduling and calendaring systems.

- **Daylight Saving Time Checker**: Assess if a specific datetime falls within Daylight Saving Time for US time zones, essential for time-sensitive scheduling and operations.

- **DateTime Formatting**: Convert datetime objects into custom-formatted strings, allowing for flexible presentation of date and time information across various applications.

- **Data Integrity Tools**: Functions like finding non-missing timestamps and merging close ranges help maintain and ensure the integrity of time series data.

- **Advanced Data Filtering**: Includes functions to find missing timestamps and assess time overlaps, aiding in thorough data audits and integrity checks.

## Installation

You can install `TimeStampProcessing` using pip:

```bash
pip install TimeStampProcessing
```

## Setup
Import the package once and use the alias tsp to access all functionalities:
```python
import timestampprocessing as tsp
```

## Usage Examples

Each function available in the TimeStampProcessing package is demonstrated below with an example.

### Formatting DateTime Objects

The `format_datetime` function is designed to format a datetime object into a custom string format. This utility is essential for applications requiring date and time display in various formats, such as reporting systems, user interfaces, or logging activities where date and time information needs to be presented in a specific style.

**Functionality**

This function converts datetime objects into strings based on custom formatting instructions, allowing for flexible presentation of date and time information. It supports a wide range of format options to accommodate different regional formats, special formatting needs, or user preferences.

**Parameters**

- **dt (datetime)**: The datetime object to format.
- **format_str (str)**: The custom format string where tokens like 'YYYY' or 'YY' for the year, 'MM' or 'M' for the month, 'DD' or 'D' for the day, 'hh' or 'h' for the hour, 'mm' or 'm' for the minute, and 'ss' or 's' for the second are used to specify the format.

**Example Usage**

Suppose you need to display the current time in a user interface where the date format should include the full year, month, and day, and the time should be in hours and minutes:

```python
import datetime
import timestampprocessing as tsp

# Current datetime
current_datetime = datetime.datetime.now()

# Format the datetime into a more readable format
formatted_date = tsp.format_datetime(current_datetime, "YYYY-MM-DD hh:mm")
print(f"Formatted DateTime: {formatted_date}")
```

### Sorting Dictionary Keys by Datetime Format

The `sort_dict_keys` function is designed to sort the keys of a dictionary where the keys are strings formatted as datetime. This function is useful for organizing data chronologically when working with time-based key values in dictionaries.

**Functionality**

This function sorts the keys of a dictionary based on the datetime format provided. It can sort in both ascending and descending order, making it versatile for various data processing needs.

**Parameters**

- **dictionary (dict)**: A dictionary whose keys are datetime strings that need sorting.
- **format (str)**: The datetime format of the keys, which tells the function how to interpret the datetime strings.
- **order (int)**: Determines the sort order. Use `0` for ascending order or `1` for descending order.

**Example Usage**

Suppose you have a dictionary with event names as keys and descriptions as values, and you want to sort these events by their datetime keys.

```python
import timestampprocessing as tsp

events = {
    "2023-12-25-15-30-00": "Christmas Party",
    "2023-10-31-19-00-00": "Halloween Bash",
    "2023-11-24-20-00-00": "Thanksgiving Dinner"
}

# Sort the dictionary keys in ascending order
sorted_events = tsp.sort_dict_keys(events, format="%Y-%m-%d-%H-%M-%S", order=0)
print("Events sorted by datetime:")
for event in sorted_events:
    print(f"{event}: {events[event]}")
```

### Calculating Time Difference

The `time_difference` function calculates the difference between two datetime strings, providing the result as a `timedelta` object which represents the difference in time between the two specified points.

**Functionality**

This function is essential for applications requiring time duration calculations between two timestamps, useful in fields such as event planning, logging, and time-series analysis.

**Parameters**

- **datetime_str1 (str)**: The first datetime string, representing the start time.
- **datetime_str2 (str)**: The second datetime string, representing the end time.
- **format1 (str)**: The datetime format of the first string, specifying how to interpret the datetime string.
- **format2 (str)**: The datetime format of the second string, specifying how to interpret the datetime string.

**Example Usage**

Suppose you want to calculate the time difference between two specific events:

```python
import timestampprocessing as tsp

# Define datetime strings
start_time = "2023-01-01-10-00-00"
end_time = "2023-01-01-15-00-00"

# Calculate the time difference
time_diff = tsp.time_difference(end_time, start_time, format1="%Y-%m-%d-%H-%M-%S", format2="%Y-%m-%d-%H-%M-%S")
print(f"Time Difference: {time_diff}")
```

### Getting First and Last Dates from a Series

The `get_first_last_dates` function is designed to extract the first and last date from a pandas Series that has a datetime index. This function is particularly useful for time series analysis, where determining the range of data coverage is essential.

**Functionality**

This function simplifies the process of identifying the start and end points of datasets, facilitating easier assessment of the time span covered by the data.

**Parameters**

- **series (pandas.Series)**: A pandas Series object equipped with a datetime index.
- **format (str)**: A string specifying the output format for the dates. It should contain placeholders for the year (`%04d`), month (`%02d`), and day (`%02d`).

**Example Usage**

Consider you have a pandas Series representing daily sales data, and you want to find out the date range covered by this dataset:

```python
import pandas as pd
from timestampprocessing as tsp

# Create a pandas Series with a datetime index
data = {
    pd.Timestamp('2023-01-01'): 100,
    pd.Timestamp('2023-01-02'): 110,
    pd.Timestamp('2023-01-03'): 120
}
series = pd.Series(data)

# Get the first and last date
first_date, last_date = tsp.get_first_last_dates(series)
print(f"First Date: {first_date}, Last Date: {last_date}")
```

### Adding Seconds to a Timestamp

The `add_seconds_to_timestamp` function allows users to add (or subtract) a specified number of seconds to a given timestamp, effectively modifying the time accordingly. This utility is useful in scenarios where time adjustments are needed, such as scheduling future events or calculating expiration times.

**Functionality**

This function enhances the flexibility of time manipulation by allowing precise control over time adjustments, supporting both positive and negative adjustments.

**Parameters**

- **timestamp_str (str)**: The initial timestamp string formatted according to the specified datetime format.
- **seconds (int)**: The number of seconds to add to the timestamp. Negative values will subtract seconds.
- **timestamp_format (str)**: The format of the timestamp string, which dictates how the string is parsed into a datetime object.

**Example Usage**

Suppose you have a starting timestamp representing the beginning of an event, and you need to find the exact time 30 minutes (1800 seconds) later:

```python
import timestampprocessing as tsp

# Initial timestamp
timestamp_str = "2023-10-01-12-00-00"

# Adding 1800 seconds to the timestamp
new_timestamp = tsp.add_seconds_to_timestamp(timestamp_str, 1800, "%Y-%m-%d-%H-%M-%S")
print(f"New Timestamp: {new_timestamp}")
```

### Checking if One Timestamp is Ahead of Another

The `is_time_ahead` function determines whether one timestamp occurs chronologically before another. This utility is crucial for applications that require temporal comparisons, such as scheduling systems, logging mechanisms, or any condition-based triggers dependent on time ordering.

**Functionality**

This function offers a straightforward method to compare two timestamps to assess which one is earlier, aiding in making decisions based on time sequences.

**Parameters**

- **timestamp_str1 (str)**: The first timestamp string to compare. Typically, this is the timestamp you want to check if it occurs earlier.
- **timestamp_str2 (str)**: The second timestamp string to compare against the first.
- **timestamp_format (str)**: The format in which both timestamp strings are provided. This ensures accurate parsing and comparison.

**Example Usage**

Assuming you have two events and you need to verify if the first event happens before the second:

```python
import timestampprocessing as tsp

# Define two timestamps
timestamp1 = "2023-10-01-14-00-00"
timestamp2 = "2023-10-01-15-00-00"

# Check if the first timestamp is ahead (earlier) than the second
is_ahead = tsp.is_time_ahead(timestamp1, timestamp2, "%Y-%m-%d-%H-%M-%S")
print(f"Is the first timestamp ahead of the second? {'Yes' if is_ahead else 'No'}")
```

### Checking Leap Year Status

The `is_leap_year` function determines whether a specified year is a leap year. This utility is crucial for applications that involve date calculations where leap year consideration is necessary, such as calendaring systems, scheduling applications, and any temporal data analysis that spans multiple years.

**Functionality**

This function checks if a given year qualifies as a leap year based on the Gregorian calendar rules. A leap year has 366 days and occurs every four years, except for years that are divisible by 100 and not divisible by 400.

**Parameters**

- **year (int)**: The year to check as an integer.

**Example Usage**

Suppose you are developing a feature that adjusts scheduling for leap years and need to verify if the current year is a leap year:

```python
import timestampprocessing as tsp

# Check if the year 2024 is a leap year
leap_year_status = tsp.is_leap_year(2024)
print(f"Is 2024 a leap year? {'Yes' if leap_year_status else 'No'}")
```


### Determining US Daylight Saving Time Status

The `is_US_summer_time` function checks whether a given datetime falls within the Daylight Saving Time (DST) period for a specified US timezone. This utility is crucial for applications involving time-sensitive scheduling, broadcasting, or any operations that need to adjust for DST changes in the US.

**Functionality**

This function determines if a specific datetime is subject to DST adjustments in various US time zones, such as 'US/Eastern', 'US/Central', 'US/Mountain', or 'US/Pacific'. It is particularly valuable for coordinating activities across states that observe DST, ensuring that timing remains consistent and accurate.

**Parameters**

- **time_str (str)**: The datetime as a string in 'YYYY-MM-DD HH:MM:SS' format.
- **timezone_str (str)**: The timezone string pertaining to a US timezone.

**Example Usage**

Suppose you are managing an application that schedules events across different US time zones and you need to determine if a particular event date in New York is during DST:

```python
import timestampprocessing as tsp

# Event datetime and timezone
event_datetime = "2023-11-05 02:00:00"  # Transition out of DST
timezone = 'US/Eastern'

# Check if the event time is during DST
is_dst = tsp.is_US_summer_time(event_datetime, timezone)
print(f"Is the event time during Daylight Saving Time? {'Yes' if is_dst else 'No'}")
```

### Calculating Sunrise and Sunset Times

The `sunrise_sunset_time` function calculates the exact times of sunrise and sunset for a given latitude, longitude, and date. This function is invaluable for applications related to astronomy, meteorology, photography, and any planning activities that depend on daylight hours.

**Functionality**

This function leverages the `astral` library to determine the sunrise and sunset times based on geographic coordinates and a specific date. It's perfect for scheduling events that align with daylight, understanding light conditions for photography shoots, or any use case requiring precise knowledge of daylight hours.

**Parameters**

- **latitude (float)**: The latitude of the location for which you want to calculate sunrise and sunset times. Positive values are north of the equator; negative values are south.
- **longitude (float)**: The longitude of the location for which you want to calculate sunrise and sunset times. Positive values are east of the Prime Meridian; negative values are west.
- **date_str (str)**: The date for which to calculate the times, formatted as 'YYYY-MM-DD'.

**Example Usage**

Suppose you are planning a photography event and need to know the sunrise and sunset times to capture the best natural lighting:

```python
import timestampprocessing as tsp

# Latitude and longitude for New York City
latitude = 40.7128
longitude = -74.0060

# Calculate sunrise and sunset times for October 1st, 2023
date_str = '2023-10-01'
sunrise, sunset = tsp.sunrise_sunset_time(latitude, longitude, date_str)
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")
```

### Converting UTC Time to Central Time

The `convert_utc_to_central` function is designed to convert a given UTC timestamp into Central Time (CT). This utility is particularly valuable for applications involving users or operations across different time zones, ensuring that time-sensitive data is correctly adjusted to local times.

**Functionality**

This function transforms a timestamp from Coordinated Universal Time (UTC) to Central Standard Time (CST) or Central Daylight Time (CDT), depending on daylight saving times.

**Parameters**

- **timestamp_str (str)**: The timestamp string in UTC that needs to be converted.
- **timestamp_format (str)**: The format of the timestamp string, which dictates how the string is parsed into a datetime object.

**Example Usage**

Suppose you have a UTC timestamp that represents the start time of an international virtual meeting, and you need to convert this time to Central Time for participants in that zone:

```python
import timestampprocessing as tsp

# UTC timestamp
utc_timestamp = "2023-12-15-18-00-00"

# Convert UTC to Central Time
central_time = tsp.convert_utc_to_central(utc_timestamp, "%Y-%m-%d-%H-%M-%S")
print(f"Central Time: {central_time}")
```

### Adjusting Timestamps

The `adjust_timestamp` function allows for the addition or subtraction of a specified number of seconds to or from a timestamp. This functionality is crucial for applications that need to manipulate time values dynamically, such as scheduling, reminders, or adjusting event times based on various conditions.

**Functionality**

This function is versatile in its ability to both advance and roll back timestamps, making it a valuable tool for time-sensitive operations where precise time adjustments are necessary.

**Parameters**

- **timestamp_str (str)**: The timestamp string to be adjusted.
- **interval_seconds (int)**: The number of seconds to add (positive value) or subtract (negative value).
- **check_before (bool)**: A boolean flag that indicates whether to subtract (True) or add (False) the interval to the timestamp.
- **timestamp_format (str)**: The format of the timestamp string, which ensures accurate parsing and formatting.

**Example Usage**

Suppose you are managing a project timeline and need to extend a deadline by 2 hours due to unforeseen circumstances:

```python
import timestampprocessing as tsp

# Original timestamp of the deadline
deadline = "2023-11-01-15-00-00"

# Adjust the deadline by adding 7200 seconds (2 hours)
new_deadline = tsp.adjust_timestamp(deadline, 7200, False, "%Y-%m-%d-%H-%M-%S")
print(f"Adjusted Deadline: {new_deadline}")
```

### Finding Closest Timestamps

The `find_closest_timestamps` function is designed to identify the closest timestamps before and after a given reference time that are multiples of a specified interval. This utility is particularly useful in time series analysis, event logging, or scheduling where aligning events to fixed intervals is required.

**Functionality**

This function calculates the nearest timestamps around a given reference point based on a regular time interval. It helps in aligning timestamps to a grid, which is useful for generating reports, setting up event triggers, or any application requiring standardized time intervals.

**Parameters**

- **timestamp_str (str)**: The reference timestamp string around which to find the closest timestamps.
- **interval_seconds (int)**: The interval in seconds to use for finding the closest timestamps.
- **timestamp_format (str)**: The format of the timestamp string, ensuring it is parsed and formatted correctly.

**Example Usage**

Assuming you need to schedule tasks that should run closest to regular 15-minute intervals, and you receive a timestamp that doesn't exactly align:

```python
import timestampprocessing as tsp

# Given timestamp that doesn't align with a 15-minute schedule
timestamp_str = "2023-08-01-12-07-35"

# Finding the closest timestamps before and after the given time
lower, upper = tsp.find_closest_timestamps(timestamp_str, 900, "%Y-%m-%d-%H-%M-%S")
print(f"Closest Lower Timestamp: {lower}")
print(f"Closest Upper Timestamp: {upper}")
```

### Checking Time Interval Overlap

The `is_time_overlap` function determines whether two specified time intervals overlap. This utility is crucial for scheduling systems, resource allocation tasks, and any application where it's necessary to avoid conflicts between events scheduled in the same timeframe.

**Functionality**

This function checks if the periods defined by two pairs of start and end times overlap, providing a boolean result. This is particularly useful in planning and logistics, where overlapping times can lead to conflicts or resource overbooking.

**Parameters**

- **event_start (str)**: The start time of the first interval.
- **event_end (str)**: The end time of the first interval.
- **interval_start (str)**: The start time of the second interval.
- **interval_end (str)**: The end time of the second interval.
- **timestamp_format (str, optional)**: The format of the timestamp strings, if not already datetime objects.

**Example Usage**

Assume you need to determine if a new meeting time conflicts with an already scheduled meeting:

```python
import timestampprocessing as tsp

# Scheduled meeting time
scheduled_start = "2023-10-05-09-00-00"
scheduled_end = "2023-10-05-10-00-00"

# New meeting time proposal
new_meeting_start = "2023-10-05-09:30-00"
new_meeting_end = "2023-10-05-10:30-00"

# Check if the new meeting overlaps with the scheduled one
overlap = tsp.is_time_overlap(scheduled_start, scheduled_end, new_meeting_start, new_meeting_end)
print(f"Do the meeting times overlap? {'Yes' if overlap else 'No'}")
```

### Generating Time Range Histogram Data

The `get_time_range_histogram_data` function creates a histogram of the number of events that overlap with each interval in a specified time range. This utility is particularly useful for analyzing the distribution and frequency of events over time, such as in traffic flow management, resource usage monitoring, or attendance tracking.

**Functionality**

This function calculates how many events occur within predefined intervals throughout a day or other time period. It's valuable for statistical analysis and planning, providing insights into peak times or identifying potential scheduling conflicts.

**Parameters**

- **entries (list of dict)**: A list of dictionaries, each representing an event with start and end times.
- **start_counting_time (str)**: The start time for counting events in the format "H-M-S", typically "00-00-00" for starting at midnight.
- **end_counting_time (str)**: The end time for counting events in the format "H-M-S", typically "23-59-59" for ending at midnight.
- **interval (int)**: The interval in minutes for which to count overlapping events.

**Example Usage**

Suppose you want to analyze traffic flow by counting the number of cars that pass a checkpoint every 30 minutes:

```python
import timestampprocessing as tsp

# Sample data representing car passing times
entries = [
    {'start_time': '2023-07-01-12-00-00', 'end_time': '2023-07-01-12-05-00'},
    {'start_time': '2023-07-01-12-15-00', 'end_time': '2023-07-01-12-20-00'},
    {'start_time': '2023-07-01-12-25-00', 'end_time': '2023-07-01-12-35-00'}
]

# Generate a histogram for the 12 PM to 1 PM range with 30-minute intervals
histogram_data = tsp.get_time_range_histogram_data(entries, '12-00-00', '13-00-00', 30)
print("Histogram of traffic flow:")
for interval, count in histogram_data.items():
    print(f"{interval}: {count} cars passed")
```

### Finding Missing Timestamps in a Directory

The `find_missing_timestamps` function is designed to identify gaps or missing timestamps in a sequence of files within a directory, typically used for monitoring data completeness in time-series data collected at regular intervals, such as sensor data or surveillance footage.

**Functionality**

This function scans through files in a specified directory, each named with a timestamp, and checks for expected intervals between timestamps. It's particularly useful for ensuring data integrity and completeness in automated data collection systems.

**Parameters**

- **base_dir (str)**: The base directory containing timestamped files.
- **start_time (str)**: The start time for checking files in the format "H-M", which determines when the expected sequence begins each day.
- **end_time (str)**: The end time for checking files in the format "H-M", which marks when the expected sequence should end each day.
- **interval (int)**: The expected interval in seconds between files, used to determine what counts as a missing timestamp.
- **file_end (str)**: The file extension or ending pattern to identify relevant files in the directory.

**Example Usage**

Suppose you are monitoring a weather station that saves sensor readings every 15 minutes, and you need to verify data completeness for a particular day:

```python
import timestampprocessing as tsp

# Path to the directory containing sensor data files
base_dir = "/path/to/sensor/data"

# Finding missing timestamps
missing_ts = tsp.find_missing_timestamps(base_dir, '00-00', '23-45', 900, '-data.log')
print("Missing timestamps:")
for date, timestamps in missing_ts.items():
    print(f"{date}: {timestamps}")
```

### Comparing Timestamp Order

The `compare_timestamp_order` function assesses the chronological order of two timestamps. This utility is crucial for systems where event sequence validation is necessary, such as in workflow management, event logging, or conditional process triggering based on time criteria.

**Functionality**

This function compares two given timestamps to determine if one occurs before the other. It is designed to support both strict (exclusive) and non-strict (inclusive) comparisons, making it versatile for various use cases where precision in time ordering impacts the logic flow.

**Parameters**

- **time1 (str)**: The first timestamp string to compare, typically representing the start or earlier time.
- **time2 (str)**: The second timestamp string to compare, typically representing the end or later time.
- **include (bool)**: Specifies whether the comparison is inclusive (True) of the exact timestamp or strictly before (False).

**Example Usage**

Suppose you need to determine if a task started on time based on scheduled and actual start times:

```python
import timestampprocessing as tsp

# Scheduled and actual start times of a task
scheduled_start = "10-00-00"
actual_start = "10-00-00"

# Check if the task started on or before the scheduled time
on_time = tsp.compare_timestamp_order(actual_start, scheduled_start, include=True)
print(f"Did the task start on time? {'Yes' if on_time else 'No'}")
```

### Finding Missing Timestamp Ranges

The `find_missing_ranges` function identifies ranges of missing timestamps in a sequence, based on provided lists of missing timestamps for each day. It is particularly useful in applications requiring continuous monitoring or data collection, such as environmental sensing, healthcare monitoring, or manufacturing process control.

**Functionality**

This function analyzes a dictionary of missing timestamps and calculates contiguous missing ranges, helping users understand prolonged gaps in data collection or event logging.

**Parameters**

- **missing_timestamps (dict)**: A dictionary with days as keys and lists of missing timestamps (in strings) as values. Each list should contain timestamps where data is absent.
- **start_time (str)**: The start time for the day, indicating when monitoring or data collection begins.
- **end_time (str)**: The end time for the day, indicating when monitoring or data collection ends.
- **interval (int)**: The interval in seconds, used to determine the threshold for grouping close timestamps into a single range.

**Example Usage**

Suppose you are managing a telemetry system that collects data every minute, and you need to identify any significant data collection gaps over a specific day:

```python
import timestampprocessing as tsp

# Example missing timestamps reported by the system
missing_timestamps = {
    '2023-10-01': ['2023-10-01-00:15:00', '2023-10-01-00:16:00', '2023-10-01-05:00:00', '2023-10-01-05:01:00']
}

# Find missing ranges considering a 60-second interval for closeness
missing_ranges = tsp.find_missing_ranges(missing_timestamps, '00-00-00', '23-59-59', 60)
for day, ranges in missing_ranges.items():
    print(f"Day: {day}")
    for start, end in ranges:
        print(f"Missing from {start} to {end}")
```

### Generating Timestamps

The `generate_timestamps` function is designed to create a list of timestamps at specified second intervals between a given start and end time. This utility is especially useful for applications that require scheduled tasks, simulations, or time-series analysis where consistent time intervals are necessary.

**Functionality**

This function generates a series of timestamps, ensuring that events or data points are evenly spaced over a defined period. It's valuable for setting up simulations, scheduling in industrial automation, or any scenario where precise timing between events is crucial.

**Parameters**

- **start (str)**: The start time in 'YYYY-MM-DD HH:MM:SS' format.
- **end (str)**: The end time in 'YYYY-MM-DD HH:MM:SS' format.
- **interval_seconds (int)**: The interval in seconds between each generated timestamp.

**Example Usage**

Suppose you are setting up a simulation that requires data points every 30 minutes over a 24-hour period starting from midnight:

```python
import timestampprocessing as tsp

# Define the start and end times
start = "2023-10-01 00:00:00"
end = "2023-10-02 00:00:00"

# Generate timestamps at 30-minute intervals
timestamps = tsp.generate_timestamps(start, end, 1800)  # 1800 seconds = 30 minutes
print("Generated Timestamps:")
for timestamp in timestamps:
    print(timestamp)
```

### Finding Non-Missing Timestamp Ranges

The `find_non_missing_timestamps` function identifies continuous ranges of time that are not covered by the specified missing ranges. This utility is crucial for applications where it is important to understand when data or events are consistently present, such as in operational monitoring, quality control processes, or in ensuring compliance with expected service or operational standards.

**Functionality**

This function calculates the intervals within a total specified range that are not accounted for by a list of known missing periods. It's invaluable for filling gaps in schedules, ensuring coverage in surveillance or monitoring systems, and optimizing operational plans based on availability.

**Parameters**

- **total_start (datetime)**: The start datetime of the total range to be examined.
- **total_end (datetime)**: The end datetime of the total range to be examined.
- **missing_ranges (list of tuples)**: A list of tuples, each containing the start and end datetimes of a missing range.
- **interval_seconds (int)**: The granularity in seconds for checking the presence within the total range, affecting the precision of the identified non-missing ranges.

**Example Usage**

Suppose you are managing a factory that operates 24/7, and you have identified certain periods when equipment was down. You need to determine when the equipment was operational:

```python
import timestampprocessing as tsp
from datetime import datetime

# Define the overall operational period
total_start = datetime(2023, 10, 1)
total_end = datetime(2023, 10, 2)

# List known downtimes
downtimes = [
    (datetime(2023, 10, 1, 2, 0), datetime(2023, 10, 1, 3, 0)),
    (datetime(2023, 10, 1, 5, 0), datetime(2023, 10, 1, 6, 0))
]

# Find operational periods
operational_periods = tsp.find_non_missing_timestamps(total_start, total_end, downtimes)
print("Operational Periods:")
for start, end in operational_periods:
    print(f"From {start} to {end}")
```

### Merging Close or Overlapping Time Ranges

The `merge_close_ranges` function is designed to merge time ranges that are close to each other or overlapping, based on a specified threshold. This is particularly useful in scenarios where you need to consolidate event durations that may have small gaps or overlaps between them.

**Functionality**

This function takes a list of time range tuples (each tuple consists of a start and an end datetime) and a `merge_threshold`, which is a `timedelta` object specifying how close the time ranges need to be to consider them for merging.

**Parameters**

- **missing_ranges (list of tuples)**: List of tuples, where each tuple contains start and end datetime objects representing individual time ranges.
- **merge_threshold (timedelta)**: A `timedelta` object that specifies the maximum gap between ranges that should be considered for merging. Ranges closer than this threshold will be merged together.

**Returns**

- **list of tuples**: Returns a list of tuples, where each tuple represents a merged time range.

**Example Usage**

Here's how you can use the `merge_close_ranges` function to merge time ranges that are within two seconds of each other:

```python
from datetime import datetime, timedelta
import timestampprocessing as tsp

# Example list of time ranges
time_ranges = [
    (datetime(2021, 7, 15, 12, 0, 0), datetime(2021, 7, 15, 12, 30, 0)),
    (datetime(2021, 7, 15, 12, 30, 1), datetime(2021, 7, 15, 13, 0, 0)),
    (datetime(2021, 7, 15, 14, 0, 0), datetime(2021, 7, 15, 14, 30, 0))
]

# Setting the merge threshold to 2 seconds
merge_threshold = timedelta(seconds=2)

# Merging close or overlapping ranges
merged_ranges = tsp.merge_close_ranges(time_ranges, merge_threshold)

for start, end in merged_ranges:
    print(f"Range from {start} to {end}")
```

### Interpolating Timestamp Values

The `interp_ts_vals` function calculates interpolated values at specific times based on linear interpolation between two known data points. This function is ideal for applications such as data imputation, sensor data analysis, and financial forecasting where precise intermediate values are needed between two known data points.

**Functionality**

This function employs linear interpolation to estimate values at a given timestamp, based on the values at two bounding timestamps. It is particularly useful for filling gaps in datasets, enhancing the granularity of sparse data, or any situation where data points are missing or expected at times between recorded values.

**Parameters**

- **start_time (str)**: The start time as a string in any recognizable datetime format, representing the first data point.
- **end_time (str)**: The end time as a string in any recognizable datetime format, representing the second data point.
- **start_value (float)**: The data value at the start time.
- **end_value (float)**: The data value at the end time.
- **current_time (str)**: The time at which the value needs to be interpolated, formatted as a string in the same format as the start and end times.

**Example Usage**

Suppose you have sensor data measuring temperature every hour, but you need to estimate the temperature at a half-hour mark:

```python
import timestampprocessing as tsp

# Known temperature readings at 1:00 PM and 2:00 PM
start_time = '2023-07-01 13:00:00'
end_time = '2023-07-01 14:00:00'
start_value = 22.0  # Temperature in degrees Celsius
end_value = 24.0    # Temperature in degrees Celsius

# Time for which you need an estimated temperature
current_time = '2023-07-01 13:30:00'

# Interpolate the temperature at 1:30 PM
interpolated_value = tsp.interp_ts_vals(start_time, end_time, start_value, end_value, current_time)
print(f"Interpolated Temperature at {current_time}: {interpolated_value:.2f}°C")
```

### Resampling a DataFrame with Linear Interpolation

The `resample_datetime_df` function resamples a pandas DataFrame that has a timestamp index to a specified interval in seconds, and fills any resulting gaps using linear interpolation. This function is highly valuable for processing time series data where uniform sampling intervals are required for analysis or visualization.

**Functionality**

This function adjusts the frequency of time series data by resampling the data to a new, specified frequency. It calculates the mean of the data within each new interval and applies linear interpolation to fill in any missing data points, ensuring a continuous set of data without gaps.

**Parameters**

- **df (pandas.DataFrame)**: The input DataFrame which must have a datetime index.
- **interval_seconds (int)**: The interval, in seconds, to which the DataFrame's data should be resampled.

**Example Usage**

Suppose you have environmental sensor data recorded at irregular intervals and you need to analyze it at regular 10-minute intervals:

```python
import pandas as pd
import numpy as np
import timestampprocessing as tsp
# Creating a sample DataFrame with irregular time intervals
times = pd.to_datetime(['2023-01-01 12:00', '2023-01-01 12:05', '2023-01-01 12:19', '2023-01-01 12:33', '2023-01-01 12:47', '2023-01-01 12:58'])
data = np.random.rand(6, 1)  # Random data
df = pd.DataFrame(data, index=times, columns=['Sensor_Reading'])

# Resample the DataFrame to every 10 minutes
resampled_df = tsp.resample_datetime_df(df, 600)  # 600 seconds = 10 minutes
print(resampled_df)
```

### Retrieving Statistical Values from Time Series Data

The `get_ts_statistic_value` function calculates and retrieves specific statistical measures from a pandas DataFrame that has a datetime index and one numerical column. This function is ideal for data analysis applications where insights into data distributions, such as maximum, minimum, mean, and various percentiles, are required.

**Functionality**

This function provides a flexible way to compute various statistical measures from a single-column DataFrame indexed by datetime. It supports a range of statistical calculations including max, min, mean, median (middle), various percentiles, and mode (most), facilitating detailed and specific data analysis tasks.

**Parameters**

- **df (pandas.DataFrame)**: The input DataFrame, which must have a datetime index and exactly one numerical column.
- **statistic (str)**: The specific statistic to compute. Default is 'max'. Options include 'max', 'min', 'mean', 'middle', '25 percentile', '75 percentile', '10 percentile', '90 percentile', '95 percentile', '99 percentile', and 'most'.

**Example Usage**

Suppose you are analyzing temperature data and need to find the maximum temperature recorded along with its corresponding datetime:

```python
import pandas as pd
import numpy as np
import timestampprocessing as tsp
# Create a sample DataFrame with datetime index and temperature data
idx = pd.date_range('2023-01-01', periods=100, freq='D')
data = np.random.normal(20, 5, size=(100,))  # Simulated temperature data
df = pd.DataFrame(data, index=idx, columns=['Temperature'])

# Get the maximum temperature and its datetime
max_temp_date, max_temp = tsp.get_ts_statistic_value(df, 'max')
print(f"The maximum temperature was {max_temp}°C on {max_temp_date}")
```

### Comparing Column Sums in a DataFrame

The `compare_ts_column_sums` function evaluates the sums of columns within a specified time range in a pandas DataFrame and identifies the columns with the maximum and minimum sums.

**Functionality**

This function is useful for data analysis scenarios where understanding column-wise aggregation over a specific interval is crucial, such as financial reporting, resource usage, or any cumulative measurements.

**Parameters**

- **df (pandas.DataFrame)**: The DataFrame to analyze, which must have a datetime index and numeric columns.
- **start_time (str or pd.Timestamp)**: The start of the time range for the analysis.
- **end_time (str or pd.Timestamp)**: The end of the time range for the analysis.

**Example Usage**

Suppose you have a DataFrame containing daily sales data for multiple products and you want to determine which product had the highest and lowest total sales in the first quarter:

```python
import timestampprocessing as tsp
import pandas as pd

# Sample DataFrame with sales data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=90, freq='D'),
    'Product_A': pd.np.random.randint(1, 100, size=90),
    'Product_B': pd.np.random.randint(1, 100, size=90)
}
df = pd.DataFrame(data).set_index('Date')

# Compare column sums for the first quarter
max_col, min_col = tsp.compare_ts_column_sums(df, '2023-01-01', '2023-03-31')
print(f"Product with maximum sales: {max_col}, Product with minimum sales: {min_col}")
```

### Analyzing Conditional Time Ranges

The find_time_ranges_with_condition function identifies periods within a pandas DataFrame where a specified condition between two columns holds true. This is particularly useful in operational monitoring, scientific experiments, or financial analysis where conditions between data streams need to be compared over time.

**Functionality**

This function examines two columns of a DataFrame to find continuous time ranges where a given relational condition (like greater than, less than, equals, etc.) is true.

**Parameters**

- **df (pandas.DataFrame)**: The DataFrame to analyze, which must have a datetime index and numeric columns.
- **col_indices (list)**: Indices of the two columns to compare.
- **operator (str)**: The comparison operator to use ('>', '>=', '<', '<=', '==', '!=').

**Example Usage**

Consider a DataFrame with temperature readings from two sensors, and you need to find when Sensor 1's readings were higher than Sensor 2's:

```python
import timestampprocessing as tsp
import pandas as pd
# Sample DataFrame with sensor readings
data = {
    'Date': pd.date_range(start='2023-01-01', periods=24, freq='H'),
    'Sensor_1': pd.np.random.randint(20, 35, size=24),
    'Sensor_2': pd.np.random.randint(20, 35, size=24)
}
df = pd.DataFrame(data).set_index('Date')

# Find time ranges where Sensor 1 readings are greater than Sensor 2
time_ranges = tsp.find_time_ranges_with_condition(df, [0, 1], '>')
print("Time ranges where Sensor 1 > Sensor 2:")
for start, end in time_ranges:
    print(f"From {start} to {end}")
```