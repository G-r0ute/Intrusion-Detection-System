import pandas as pd
import numpy as np

def extract_features(packet_df):
    packet_df['time_diff'] = packet_df['time'].diff().fillna(0)
    packet_df['packet_size'] = packet_df['len']

    features =packet_df[['time_diff', 'packet_size', 'proto']]
    return features

df = pd.read_csv('packets.csv')
features = extract_features(df)
features.to_csv('features.csv', index = False)