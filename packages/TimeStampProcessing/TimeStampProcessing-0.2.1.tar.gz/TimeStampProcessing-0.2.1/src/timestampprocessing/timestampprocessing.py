from datetime import datetime, timedelta, time, date
import pandas as pd
import pytz
import os
from tqdm import tqdm
from astral.sun import sun
from astral import LocationInfo

def __parse_time_to_hms(time_str):
    '''
    Parse a string in the format "H-M-S" to a time object, and formatted to hh:mm:ss.
    Parameters:
        - time_str (str): A string in the format "H-M-S".
    Returns:
        - time: A time object representing the input string.
    '''
    h, m, s = map(int, time_str.split('-'))
    return datetime.strptime(f"{h}:{m}:{s}", "%H:%M:%S").time()

def __format_time_to_HHMM(time_str):
    '''
    Format a string in the format "H-M" to a time object.
    Parameters:
        - time_str (str): A string in the format "H-M".
    Returns:
        - time: A time object representing the input string.
    '''
    return datetime.strptime(time_str, "%H-%M").time()

def __parse_date_and_time(date_str, time_str):
    '''
    Parse a date and time string into a datetime object.
    Parameters:
        - date_str (str): A string representing the date.
        - time_str (str): A string representing the time.
    Returns:
        - datetime: A datetime object representing the input date and time.'''
    return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H-%M-%S")

def sort_dict_keys(dictionary, format = "%Y-%m-%d-%H-%M-%S", order = 0):
    '''
    Sorts the keys of a dictionary in ascending order, assuming the keys are in datetime format.
    Parameters:
        dictionary (dict): The dictionary to be sorted.
        format (str): The format of the keys in the dictionary.
        order (int): The order in which the keys should be sorted. 0 for ascending, 1 for descending.
    Returns:
        list: A list of sorted keys.
        
    '''
    # Convert string keys to datetime objects
    date_keys = [datetime.strptime(key, format) for key in dictionary.keys()]
    # Sort the datetime objects
    sorted_dates = sorted(date_keys)
    # Convert sorted datetime objects back to strings
    sorted_date_strings = [date.strftime(format) for date in sorted_dates]
    if order == 0:
        return sorted_date_strings
    else:
        return sorted_date_strings[::-1]
    
def time_difference(datetime_str1, datetime_str2, format1 = "%Y-%m-%d-%H-%M-%S", format2 = "%Y-%m-%d-%H-%M-%S"):
    '''
    Calculates the time difference between two datetime strings, the output unit is second.
    Parameters:
        datetime_str1 (str): The first datetime string.
        datetime_str2 (str): The second datetime string.
        format1 (str): The format of the first datetime string.
        format2 (str): The format of the second datetime string.
    Returns:
        timedelta: The time difference between the two datetime strings.
    '''
    # Convert the strings to datetime objects
    datetime_obj1 = datetime.strptime(datetime_str1, format1)
    datetime_obj2 = datetime.strptime(datetime_str2, format2)

    # Calculate the time difference
    difference = datetime_obj1 - datetime_obj2
    # You can format the difference as needed, here it's returned as days, seconds, and microseconds
    return difference

def get_first_last_dates(series, format = '%04d-%02d-%02d'):
    """
    Returns the first and last date of a pandas Series with datetime index.
    
    Parameters:
    - series: pandas Series object with a datetime index.
    - format: Format string to format the date. This should contain three placeholders for the year, month, and day.
    Returns:
    - Tuple containing the first and last date of the series index.
    """
    if not isinstance(series.index, pd.DatetimeIndex):
        raise ValueError("The series index must be a DatetimeIndex.")
        
    first_date = series.index.min()
    last_date = series.index.max()
    
    return format%(first_date.year, first_date.month, first_date.day), format%(last_date.year, last_date.month, last_date.day)

def add_seconds_to_timestamp(timestamp_str, seconds, timestamp_format = '%Y-%m-%d-%H-%M-%S'):
    '''
    Adds a specified number of seconds to a timestamp string.
    Parameters:
        timestamp_str (str): The timestamp string.
        seconds (int): The number of seconds to add.
        timestamp_format (str): The format of the timestamp string.
    Returns:
        str: The new timestamp string after adding the specified number of seconds of the same format.
    '''
    # Convert the timestamp string to a datetime object
    timestamp = datetime.strptime(timestamp_str, timestamp_format)
    
    # Add the specified number of seconds to the datetime object
    new_timestamp = timestamp + timedelta(seconds=seconds)
    
    # Convert the new datetime object back to a string in the specified format
    new_timestamp_str = new_timestamp.strftime(timestamp_format)
    
    return new_timestamp_str

def is_time_ahead(timestamp_str1, timestamp_str2, timestamp_format = '%Y-%m-%d-%H-%M-%S'):
    '''
    Checks if one timestamp is ahead of another.
    Parameters:
        timestamp_str1 (str): The first timestamp string.
        timestamp_str2 (str): The second timestamp string.
        timestamp_format (str): The format of the timestamp strings.
    Returns:
        bool: True if the first timestamp is ahead of the second, False otherwise.
    '''
    # Convert the timestamp strings to datetime objects
    timestamp1 = datetime.strptime(timestamp_str1, timestamp_format)
    timestamp2 = datetime.strptime(timestamp_str2, timestamp_format)
    
    # Compare the two datetime objects
    return timestamp1 > timestamp2

def convert_utc_to_central(timestamp_str, timestamp_format = '%Y-%m-%d-%H-%M-%S'):
    '''
    Converts a timestamp from UTC to Central Time.
    Parameters:
        timestamp_str (str): The timestamp string in UTC.
        timestamp_format (str): The format of the timestamp string.
    Returns:
        str: The timestamp string converted to Central Time.
    '''
    
    # Create a datetime object from the input timestamp string
    utc_time = datetime.strptime(timestamp_str, timestamp_format)
    
    # Define the UTC and Central Time zones
    utc_zone = pytz.utc
    central_zone = pytz.timezone('US/Central')
    
    # Localize the datetime object to UTC
    utc_time = utc_zone.localize(utc_time)
    
    # Convert the datetime object from UTC to Central Time
    central_time = utc_time.astimezone(central_zone)
    
    # Return the datetime object in the desired format
    return central_time.strftime(timestamp_format)

def adjust_timestamp(timestamp_str, interval_seconds, check_before, timestamp_format = '%Y-%m-%d-%H-%M-%S'):
    '''
    Adjusts a timestamp by adding or subtracting a specified number of seconds.
    Parameters:
        timestamp_str (str): The timestamp string to adjust.
        interval_seconds (int): The number of seconds to add or subtract.
        check_before (bool): If True, subtract the interval; if False, add the interval.
        timestamp_format (str): The format of the timestamp string.
    Returns:
        str: The adjusted timestamp string in the same format.
    '''
    # Convert the timestamp string to a datetime object
    timestamp = datetime.strptime(timestamp_str, timestamp_format)
    
    # Adjust the timestamp based on the dummy variable
    if check_before:
        new_timestamp = timestamp - timedelta(seconds=interval_seconds)
    else:
        new_timestamp = timestamp + timedelta(seconds=interval_seconds)
    
    # Return the new timestamp as a string in the same format
    return new_timestamp.strftime(timestamp_format)

def find_closest_timestamps(timestamp_str, interval_seconds, timestamp_format = '%Y-%m-%d-%H-%M-%S'):
    '''
    Finds the closest lower and upper timestamps that are multiples of a specified interval.
    Parameters:
        timestamp_str (str): The timestamp string to find the closest timestamps for.
        interval_seconds (int): The interval in seconds.
        timestamp_format (str): The format of the timestamp string.
    Returns:
        Tuple: A tuple containing the lower and upper timestamps as strings.
    '''
    # Convert the timestamp string to a datetime object
    timestamp = datetime.strptime(timestamp_str, timestamp_format)
    
    # Calculate the number of seconds since the start of the day
    seconds_since_midnight = (timestamp - timestamp.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    
    # Find the closest lower multiple of the interval
    lower_multiplier = int(seconds_since_midnight // interval_seconds)
    lower_timestamp = timestamp.replace(hour=0, minute=0, second=0) + timedelta(seconds=lower_multiplier * interval_seconds)
    
    # Find the closest higher multiple of the interval
    upper_multiplier = lower_multiplier + 1
    upper_timestamp = timestamp.replace(hour=0, minute=0, second=0) + timedelta(seconds=upper_multiplier * interval_seconds)
    
    # If the upper timestamp is on the next day, adjust the date
    if upper_timestamp.day != timestamp.day:
        upper_timestamp = upper_timestamp.replace(day=timestamp.day) + timedelta(days=1)
    
    # Convert the lower and upper timestamps back to strings
    lower_timestamp_str = lower_timestamp.strftime(timestamp_format)
    upper_timestamp_str = upper_timestamp.strftime(timestamp_format)
    
    return lower_timestamp_str, upper_timestamp_str

def is_time_overlap(event_start, event_end, interval_start, interval_end):
    '''
    Checks if two time intervals overlap.
    Parameters:
        event_start (str): The start time of the first interval.
        event_end (str): The end time of the first interval.
        interval_start (str): The start time of the second interval.
        interval_end (str): The end time of the second interval.
    Returns:
        bool: True if the intervals overlap, False otherwise.
    '''
    return max(event_start, interval_start) < min(event_end, interval_end)

def get_time_range_histogram_data(entries, start_counting_time='00-00-00', end_counting_time='23-59-59', interval=30):
    '''
    This function generates a histogram of the number of events that overlap with each interval in a day.
    Parameters:
        entries (list): A list of dictionaries containing the start and end times of events.
        start_counting_time (str): The start time for counting events in the format "H-M-S".
        end_counting_time (str): The end time for counting events in the format "H-M-S".
        interval (int): The interval in minutes for the histogram.
    Returns:
        dict: A dictionary where the keys are time intervals and the values are the number of events that overlap with each interval.
    '''
    start_time = __parse_time_to_hms(start_counting_time)
    end_time = __parse_time_to_hms(end_counting_time)
    interval_delta = timedelta(minutes=interval)
    histogram = {}

    # Create interval ranges for a day
    intervals = []
    base_date = datetime.today().date()  # Use any arbitrary date
    current_time = datetime.combine(base_date, start_time)
    while current_time.time() < end_time:
        interval_start = current_time
        current_time += interval_delta
        intervals.append((interval_start, min(current_time, datetime.combine(base_date, end_time))))

    # Count overlaps for each interval
    for interval_start, interval_end in intervals:
        count = 0
        for entry in entries:
            event_start = datetime.strptime(entry['start_time'], '%Y-%m-%d-%H-%M-%S')
            event_end = datetime.strptime(entry['end_time'], '%Y-%m-%d-%H-%M-%S')

            # Ensure we compare datetime with datetime
            interval_start_time = datetime.combine(event_start.date(), interval_start.time())
            interval_end_time = datetime.combine(event_start.date(), interval_end.time())

            if is_time_overlap(event_start, event_end, interval_start_time, interval_end_time):
                count += 1
        
        histogram[f"{interval_start.time().strftime('%H:%M:%S')} - {interval_end.time().strftime('%H:%M:%S')}"] = count

    return histogram

def find_missing_timestamps(base_dir, start_time='08-00', end_time='18-00', interval=15, file_end = '-PW.jpg'):
    '''
    Find missing timestamps in a directory of images for each day. Assuming the file names are in the format "YYYY-MM-DD-HH-MM-SS{file_end}".
    Parameters:
        base_dir (str): The base directory containing the files.
        start_time (str): The start time for checking files in the format "H-M".
        end_time (str): The end time for checking files in the format "H-M".
        interval (int): The interval in seconds between files.
        file_end (str): The file extension to filter files.
    Returns:
        dict: A dictionary where the keys are dates and the values are lists of missing timestamps for each day.
    '''
    start_time = __format_time_to_HHMM(start_time)
    end_time = __format_time_to_HHMM(end_time)
    expected_images_per_hour = 3600 // interval
    missing_timestamps = {}  # Dictionary to store missing timestamps

    # List directories to estimate total progress accurately
    directories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    for folder_name in tqdm(directories, desc="Processing folders"):
        folder_path = os.path.join(base_dir, folder_name)
        all_images = [f for f in os.listdir(folder_path) if f.endswith(file_end)]
        image_times = set(datetime.strptime(img[:-7], '%Y-%m-%d-%H-%M-%S') for img in all_images)

        # Start and end datetime for the day
        day_date = datetime.strptime(folder_name, '%Y-%m-%d')
        start_datetime = datetime.combine(day_date, start_time)
        end_datetime = datetime.combine(day_date, end_time)

        # Prepare timestamps to progress over
        all_timestamps = []
        current_time = start_datetime
        while current_time < end_datetime:
            all_timestamps.append(current_time)
            current_time += timedelta(hours=1)

        missing_day = []  # List to collect missing timestamps for the day

        for current_time in tqdm(all_timestamps, desc=f"Checking {folder_name}", leave=False):
            hour_end = min(current_time + timedelta(hours=1), end_datetime)
            # Count images within this hour
            image_count = sum(1 for img_time in image_times if current_time <= img_time < hour_end)
            if image_count < expected_images_per_hour:
                # If fewer images than expected, check each timestamp
                while current_time < hour_end:
                    next_time = current_time + timedelta(seconds=interval)
                    if not any(current_time <= img_time < next_time for img_time in image_times):
                        missing_day.append(current_time.strftime('%Y-%m-%d-%H-%M-%S'))
                    current_time = next_time
            else:
                # Skip detailed checking if the hour is fully covered
                current_time = hour_end

        missing_timestamps[folder_name] = missing_day

    return missing_timestamps

def compare_timestamp_order(time1, time2, include = True):
    '''
    Compare the order of two timestamps.
    Parameters:
        time1 (str): The first timestamp in the format "H-M-S".
        time2 (str): The second timestamp in the format "H-M-S".
        include (bool): If True, include equality in the comparison.
    Returns:
        bool: True if the first timestamp is earlier or equal to the second, False otherwise.
    '''
    # Parse the time strings into datetime.time objects
    t1 = datetime.strptime(time1, "%H-%M-%S").time()
    t2 = datetime.strptime(time2, "%H-%M-%S").time()
    
    # Compare and print which is earlier or if they are the same
    if include:
        if t1 <= t2:
            return True
        else:
            return False
    else:
        if t1 < t2:
            return True
        else:
            return False

def find_missing_ranges(missing_timestamps, start_time='08-00-00', end_time='18-00-00', interval=15):
    """
    Finds and groups missing timestamp ranges for each day.
    
    Args:
    missing_timestamps (dict): Dictionary with days as keys and lists of missing timestamps as values.
    start_time (str): The start time of the active period each day.
    end_time (str): The end time of the active period each day.
    interval (int): The interval in seconds to determine breaks between missing timestamp groups.
    
    Returns:
    dict: Dictionary with days as keys and lists of tuple pairs indicating missing ranges.
    """
    missing_ranges = {}
    
    for day, times in missing_timestamps.items():
        full_day_start = __parse_date_and_time(day, "00-00-00")
        full_day_end = __parse_date_and_time(day, "23-59-59")
        daily_start_count_time, daily_end_count_time = __parse_date_and_time(day, start_time), __parse_date_and_time(day, end_time)
        # Convert recorded times to datetime objects and sort them
        recorded_times = sorted(__parse_date_and_time(day, time) for time in times)
        
        # Initialize list of ranges
        ranges = []
        if recorded_times:
            start_range = recorded_times[0]
            end_range = start_range

            # Group timestamps into ranges
            for time in recorded_times[1:]:
                if (time - end_range).total_seconds() > interval:
                    ranges.append((start_range, end_range))
                    start_range = time
                end_range = time
            ranges.append((start_range, end_range))  # Append the last range

        # Include entire period before and after if there are no timestamps
        if not recorded_times:
            
            ranges.append((full_day_start, daily_start_count_time - timedelta(seconds=1)))
            ranges.append((daily_end_count_time, full_day_end))
        elif ranges:
            # Append missing ranges before the first and after the last recorded timestamp
            day_start = __parse_date_and_time(day, start_time)
            day_end = __parse_date_and_time(day, end_time)
            if day_start < ranges[0][0]:
                ranges.insert(0, (full_day_start, day_start - timedelta(seconds=1)))
            elif day_start == ranges[0][0]:
                ranges[0] = (full_day_start, ranges[0][1])
            if day_end > ranges[-1][1]:
                ranges.append((day_end, full_day_end))
            elif day_end == ranges[-1][1]:
                ranges[-1] = (ranges[-1][0], full_day_end)
        missing_ranges[day] = ranges

    return missing_ranges

def generate_timestamps(start, end, interval_seconds):
    """
    Generates a list of timestamps from start to end at specified second intervals.

    Args:
    start (str): Start time in 'YYYY-MM-DD HH:MM:SS' format.
    end (str): End time in 'YYYY-MM-DD HH:MM:SS' format.
    interval_seconds (int): Interval in seconds between each timestamp.

    Returns:
    list: List of timestamps at the specified interval.
    """
    return pd.date_range(start=start, end=end, freq=f'{interval_seconds}S').tolist()

def merge_close_ranges(missing_ranges, merge_threshold=timedelta(seconds=2)):
    """
    Merges close or overlapping missing ranges.

    Args:
    missing_ranges (list of tuples): List of tuples, each containing start and end datetimes.
    merge_threshold (timedelta): Maximum gap between ranges to consider for merging.

    Returns:
    list of tuples: Merged list of missing ranges.
    """
    if not missing_ranges:
        return []

    # Sort ranges by the start time
    sorted_ranges = sorted(missing_ranges, key=lambda x: x[0])
    
    merged_ranges = [sorted_ranges[0]]
    
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged_ranges[-1]
        
        # Check if the current range overlaps or is very close to the last range
        if current_start <= last_end + merge_threshold:
            # Extend the last range
            merged_ranges[-1] = (last_start, max(last_end, current_end))
        else:
            # Add the current range as it is far enough from the last range
            merged_ranges.append((current_start, current_end))
    
    return merged_ranges

def find_non_missing_timestamps(total_start, total_end, missing_ranges, interval_seconds=60):
    """
    Finds non-missing timestamp ranges that are not within the specified missing ranges.
    
    Args:
    total_start (datetime): The start datetime of the total range.
    total_end (datetime): The end datetime of the total range.
    missing_ranges (list of tuples): Each tuple contains the start and end datetimes of a missing range.
    interval_seconds (int): The interval in seconds for generating timestamps within the total range.
    
    Returns:
    list: A list of tuples, each containing the start and end datetimes of non-missing ranges.
    """
    res = []
    if total_start < missing_ranges[0][0]:
        res.append((total_start, missing_ranges[0][0]))
    for i in range(len(missing_ranges) - 1):
        res.append((missing_ranges[i][1], missing_ranges[i+1][0]))
    if total_end > missing_ranges[-1][1]:
        res.append((missing_ranges[-1][1], total_end))
    return res

def interp_ts_vals(start_time, end_time, start_value, end_value, current_time):
    """
    Calculates the interpolated value at a given time between two points using linear interpolation.

    Args:
    start_time (str): The start time in any recognizable datetime format.
    end_time (str): The end time in any recognizable datetime format.
    start_value (float): The value at the start time.
    end_value (float): The value at the end time.
    current_time (str): The current time in any recognizable datetime format for which the value is to be interpolated.

    Returns:
    float: Interpolated value at the current time.
    """
    # Convert all input times to datetime objects
    start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    current_time = datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')

    # Calculate the total time difference and the elapsed time from start to current
    total_time_delta = (end_time - start_time).total_seconds()
    elapsed_time_from_start = (current_time - start_time).total_seconds()

    # Linear interpolation formula
    interpolated_value = start_value + (end_value - start_value) * (elapsed_time_from_start / total_time_delta)

    return interpolated_value

def is_leap_year(year):
    '''
    This function checks if a year is a leap year.
    Parameters:
        year (int): The year to check.
    Returns:
        bool: True if the year is a leap year, False otherwise.
    '''
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_US_summer_time(time_str, timezone_str):
    """
    Determines if the specified time in a given US timezone is during daylight saving time.

    Args:
    time_str (str): The datetime in 'YYYY-MM-DD HH:MM:SS' format.
    timezone_str (str): The timezone string (e.g., 'US/Eastern', 'US/Central', 'US/Mountain', 'US/Pacific').

    Returns:
    bool: True if the time is during daylight saving time, False otherwise.
    """
    # Create a timezone object based on the input
    timezone = pytz.timezone(timezone_str)
    
    # Parse the time string to a datetime object
    naive_datetime = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    
    # Localize the datetime to the specified timezone
    localized_datetime = timezone.localize(naive_datetime, is_dst=None)
    
    # Return whether the datetime is in daylight saving time
    return localized_datetime.dst() != datetime.timedelta(0)

def format_datetime(dt, format_str):
    """
    Formats a datetime object into a custom string format.

    Args:
    dt (datetime): The datetime object to format.
    format_str (str): The custom format string where 'YYYY' or 'YY' means year,
                      'MM' or 'M' means month, 'DD' or 'D' means day, 'hh' or 'h' means hour,
                      'mm' or 'm' means minute, 'ss' or 's' means second.

    Returns:
    str: The datetime formatted according to the custom format.
    """
    # Temporary tokens to avoid conflicts during replacements
    tokens = {
        'YYYY': '_0000_',
        'YY': '_0001_',
        'MM': '_0002_',
        'M': '_0003_',
        'DD': '_0004_',
        'D': '_0005_',
        'hh': '_0006_',
        'h': '_0007_',
        'mm': '_0008_',
        'm': '_0009_',
        'ss': '_0010_',
        's': '_0011_'
    }

    # Replace placeholders with tokens
    temp_format = format_str
    for key, token in tokens.items():
        temp_format = temp_format.replace(key, token)
    # print(temp_format)
    strftime_map = {
        '_0000_': '%Y', '_0001_': '%Y',
        '_0002_': '%m', '_0003_': '%m',
        '_0004_': '%d', '_0005_': '%d',
        '_0006_': '%H', '_0007_': '%H',
        '_0008_': '%M', '_0009_': '%M',
        '_0010_': '%S', '_0011_': '%S'
    }

    # Replace tokens with strftime formats
    strftime_format = temp_format
    for token, format_value in strftime_map.items():
        strftime_format = strftime_format.replace(token, format_value)
    # print(strftime_format)
    # Format the datetime
    return dt.strftime(strftime_format)

def sunrise_sunset_time(latitude, longitude, date_str):
    """
    Calculates the sunrise and sunset times in UTC for a given latitude, longitude, and date.

    Args:
    latitude (float): Latitude of the location.
    longitude (float): Longitude of the location.
    date_str (str): The date in 'YYYY-MM-DD' format.

    Returns:
    tuple: Sunrise and sunset times in UTC.
    """
    # Create a location object with the provided latitude and longitude
    location = LocationInfo(latitude=latitude, longitude=longitude)
    
    # Parse the provided date
    selected_date = date.fromisoformat(date_str)
    
    # Calculate sun information
    s = sun(location.observer, date=selected_date)
    
    # Extract sunrise and sunset times
    sunrise_utc = s['sunrise'].strftime('%Y-%m-%d %H:%M:%S UTC')
    sunset_utc = s['sunset'].strftime('%Y-%m-%d %H:%M:%S UTC')
    
    return (sunrise_utc, sunset_utc)

def resample_datetime_df(df, interval_seconds):
    """
    Resample a pandas DataFrame with a timestamp index.
    
    Args:
    df (pd.DataFrame): Input DataFrame with a timestamp index.
    interval_seconds (int): Resampling interval in seconds.
    
    Returns:
    pd.DataFrame: Resampled DataFrame with linear interpolation.
    """
    # Convert seconds to pandas frequency string
    freq_str = f'{interval_seconds}S'
    
    # Resample the DataFrame
    resampled_df = df.resample(freq_str).mean()
    
    # Interpolate missing data
    interpolated_df = resampled_df.interpolate(method='linear')
    
    return interpolated_df

def get_ts_statistic_value(df, statistic='max'):
    """
    Retrieve a specific statistic from a pandas DataFrame.
    
    Args:
    df (pd.DataFrame): Input DataFrame with a datetime index and one numerical column.
    statistic (str): Statistic to compute; defaults to 'max'. Options include 'max', 'min', 'mean', 
                     'middle', '25 percentile', '75 percentile', '10 percentile', 
                     '90 percentile', '95 percentile', '99 percentile', and 'most'.
    
    Returns:
    tuple: The datetime and value of the computed statistic.
    """
    # Mapping statistic to function
    if statistic == 'max':
        value = df.max()
    elif statistic == 'min':
        value = df.min()
    elif statistic == 'mean':
        value = df.mean()
    elif statistic == 'middle':
        value = df.median()
    elif statistic in ['25 percentile', '75 percentile', '10 percentile', 
                       '90 percentile', '95 percentile', '99 percentile']:
        percentile = float(statistic.split()[0])
        value = df.quantile(percentile/100)
    elif statistic == 'most':
        value = df.mode().iloc[0]  # takes the first mode in case of multiple modes
    else:
        raise ValueError("Invalid statistic. Please choose a valid option.")
    
    # Find the index of the value
    if statistic == 'most':  # mode might not be unique and may not directly exist in df
        idx = df[df == value].first_valid_index()
    else:
        idx = df[df == value[0]].first_valid_index()

    return (idx, value[0])
