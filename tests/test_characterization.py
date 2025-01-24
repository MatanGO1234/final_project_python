import unittest
import sys
import os
import numpy as np
import pytest
# Manually add the 'src' folder to sys.path so Python can find and import its modules.
#src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
#if src_path not in sys.path:
    #sys.path.insert(0, src_path)

from src.characterization import calculate_spike_characteristics


class TestCharacterization(unittest.TestCase):
    """
    Tests for the function 'calculate_spike_characteristics' in 'src/characterization.py'.
    """

    def test_calculate_spike_characteristics(self):
        """
        Test that with a signal containing a few spikes,
        the function returns the correct number of spike entries and correct indices.
        """
        signal = np.array([0, 0, 1, 5, 2, 0, -1, -3, -2, 0])
        spikes_indices = np.array([3, 8])
        positive_fdr = 2.5
        negative_fdr = -2.5
        result = calculate_spike_characteristics(
            signal, spikes_indices, positive_fdr, negative_fdr, mode="positive"
        )
        self.assertEqual(len(result), len(spikes_indices))
        self.assertEqual(result[0]["peak_index"], spikes_indices[0])
        self.assertEqual(result[1]["peak_index"], spikes_indices[1])

    def test_empty_spikes(self):
        """
        Test that if there are no spikes, the function returns an empty list.
        """
        signal = np.random.normal(0, 1, 1000)
        spikes_indices = np.array([])
        result = calculate_spike_characteristics(
            signal, spikes_indices, 0.5, -0.5, mode="positive"
        )
        self.assertEqual(result, [])

    def test_no_duplicate_peaks(self):
        """
        Test that the function does not return duplicate peaks
        when given a simple signal with two distinct spikes.
        """
        signal = [0.1, 0.2, 0.3, 0.4]
        spikes_indices = [0, 2]
        positive_fdr = 0.3
        negative_fdr = -0.3
        result = calculate_spike_characteristics(
            signal, spikes_indices, positive_fdr, negative_fdr, mode="positive"
        )
        unique_peaks = set(item["peak_index"] for item in result)
        self.assertEqual(len(result), len(unique_peaks))


if __name__ == "__main__":
    unittest.main()
