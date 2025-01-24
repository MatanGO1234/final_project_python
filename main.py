from src.config import sampling_rate, refractory_period, min_distance, alpha
from source.preprocessing import band_pass_filter
from source.detection import apply_fdr, calculate_fdr_thresholds, enforce_refractory, sort_spikes_by_significance 
from source.characterization import calculate_spike_characteristics, filter_unique_spikes
from source.visualization import plot_signal_with_spikes
import numpy as np

# Load signal and preprocess
signal = np.load("C:\\test1\\matan_bootcamp_python\\bic13-ch259.npy")
filtered_signal = band_pass_filter(signal, 300, 10000)

# # Detect spikes using FDR
spikes_indices = apply_fdr(filtered_signal, alpha=0.05)
spikes_values = filtered_signal[spikes_indices]
positive_fdr, negative_fdr = calculate_fdr_thresholds(spikes_values)

# Sort and enforce refractory period
positive_indices_idx, negative_indices_idx = sort_spikes_by_significance(filtered_signal, positive_fdr, negative_fdr)
positive_spikes_idx = enforce_refractory(positive_indices_idx, min_distance)
negative_spikes_idx = enforce_refractory(negative_indices_idx, min_distance)

# Characterization
positive_spike_char = calculate_spike_characteristics(filtered_signal, positive_fdr, negative_fdr, mode="positive")
negative_spike_char = calculate_spike_characteristics(filtered_signal, positive_fdr, negative_fdr, mode="negative")
unique_positive_spikes = filter_unique_spikes(positive_spike_char)
unique_negative_spikes = filter_unique_spikes(negative_spike_char)

# Visualization
plot_signal_with_spikes(filtered_signal, unique_positive_spikes, unique_negative_spikes, positive_fdr, negative_fdr,)
 