import numpy as np


def calculate_spike_characteristics(
    signal, spikes_indices, positive_fdr, negative_fdr, mode="positive"
):
    """
    Calculate characteristics of detected spikes.

    Parameters:
    -----------
    signal : array-like
        The input signal
    spikes_indices : array-like
        Indices of detected spikes
    positive_fdr : float
        Positive threshold for spike detection
    negative_fdr : float
        Negative threshold for spike detection
    mode : str, optional
        'positive' or 'negative' to specify spike direction (default: 'positive')

    Returns:
    --------
    list
        List of dictionaries containing spike characteristics
    """
    spike_characteristics = []
    buffer_size = 50

    for spike_idx in spikes_indices:
        # Define search window: 50 sampels before and after each spike
        start_spike = max(0, spike_idx - buffer_size)
        end_spike = min(len(signal), spike_idx + buffer_size)

        # sortings spikes to positive and negetive
        if mode == "positive":
            # backward search until finding value below threshold
            while start_spike > 0 and signal[start_spike] > positive_fdr:
                start_spike -= 1
            # foorwad search untill finding spike below threshold
            while end_spike < len(signal) and signal[end_spike] > positive_fdr:
                end_spike += 1
        else: # mode == negetive
            # same, but with negetive threshold
            while start_spike > 0 and signal[start_spike] < negative_fdr:
                start_spike -= 1
            while end_spike < len(signal) and signal[end_spike] < negative_fdr:
                end_spike += 1

        if start_spike >= end_spike:
            continue # if something go wrong, skip the spike

        

        spike_characteristics.append(
            {
                "peak_index": spike_idx,  # peak location
                "peak": signal[spike_idx],  # peak value
                "duration": end_spike - start_spike,  # duration of the spike
                "start_index": start_spike,  # starting point
                "end_index": end_spike,  # ending point
            }
        )

    # Filtering false indetification
    return filter_unique_spikes(spike_characteristics)


def filter_unique_spikes(spike_characteristics):
    """
    Filter out duplicate spikes based on their peak indices.

    Parameters:
    -----------
    spike_characteristics : list
        List of dictionaries containing spike characteristics

    Returns:
    --------
    list
        Filtered list with unique spikes
    """
    return list(
        {spike["peak_index"]: spike for spike in spike_characteristics}.values()
    )
