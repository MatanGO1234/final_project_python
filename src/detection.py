import numpy as np
from statsmodels.stats.multitest import fdrcorrection
from scipy.stats import norm

def apply_fdr(filtered_signal, alpha):
    """Apply FDR correction to identify significant spikes."""
    p_values = 2 * (1 - norm.cdf(np.abs(filtered_signal / np.std(filtered_signal))))
    spikes_indices, _ = fdrcorrection(p_values, alpha=alpha)
    return spikes_indices


def calculate_fdr_thresholds(spikes_values):
    """Calculate FDR thresholds for positive and negative spikes."""
    if np.any(spikes_values > 0):
        positive_fdr = np.min(spikes_values[spikes_values > 0])
    else:
        positive_fdr = np.nan

    if np.any(spikes_values < 0):
        negative_fdr = np.max(spikes_values[spikes_values < 0])
    else:
        negative_fdr = np.nan

    return positive_fdr, negative_fdr


def enforce_refractory(spikes_indices, min_distance):
    """Enforce a refractory period to remove closely spaced spikes."""
    final_spikes = []
    last_spike = -np.inf
    for spike in spikes_indices:
        if spike - last_spike > min_distance:
            final_spikes.append(spike)
            last_spike = spike
    return np.array(final_spikes)


def sort_spikes_by_significance(filtered_signal, positive_fdr, negative_fdr):
    """Sort spikes into positive and negative categories based on thresholds."""
    positive_indices_idx = np.where(
        (filtered_signal >= positive_fdr) & (filtered_signal > 0)
    )[0]
    negative_indices_idx = np.where(
        (filtered_signal <= negative_fdr) & (filtered_signal < 0)
    )[0]
    return positive_indices_idx, negative_indices_idx
