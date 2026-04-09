import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ta import add_all_ta_features

# Find Demand Zones

# Function to identify demand zones

def find_demand_zones(data, threshold=0.03):
    high = data['High'].max()
    low = data['Low'].min()
    demand_zones = []
    for price in data['Close']:
        if price < low + threshold * (high - low):
            demand_zones.append(price)
    return list(set(demand_zones))

# Find Supply Zones

# Function to identify supply zones

def find_supply_zones(data, threshold=0.03):
    high = data['High'].max()
    low = data['Low'].min()
    supply_zones = []
    for price in data['Close']:
        if price > high - threshold * (high - low):
            supply_zones.append(price)
    return list(set(supply_zones))

# Chart Pattern Recognition

# Function to detect Head and Shoulders pattern

def detect_head_and_shoulders(data):
    # Implementation of pattern detection logic here
    pass

# Function to detect Triangle pattern

def detect_triangle_pattern(data):
    # Implementation of pattern detection logic here
    pass

# Function to detect Flag pattern

def detect_flag_pattern(data):
    # Implementation of pattern detection logic here
    pass

# Technical Indicators

# Function to calculate RSI

def calculate_rsi(data, window=14):
    delta = data['Close'].diff()  
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Function to calculate MACD

def calculate_macd(data):
    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal

# Function to calculate Moving Averages

def calculate_moving_average(data, window=14):
    return data['Close'].rolling(window=window).mean()

# Function to calculate Bollinger Bands

def calculate_bollinger_bands(data, window=14):
    rolling_mean = data['Close'].rolling(window=window).mean()
    rolling_std = data['Close'].rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * 2)
    lower_band = rolling_mean - (rolling_std * 2)
    return upper_band, lower_band