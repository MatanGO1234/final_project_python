import numpy as np
from scipy.signal import butter, filtfilt


# Function for filtering
def band_pass_filter(signal, lowcut, highcut, sampling_rate=60000):
    """Apply a band-pass filter to the signal."""
    nyquist = 0.5 * sampling_rate
    b, a = butter(2, [lowcut / nyquist, highcut / nyquist], btype="band")
    return filtfilt(b, a, signal)
