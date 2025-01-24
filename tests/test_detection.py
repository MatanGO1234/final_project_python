import pytest
import numpy as np
import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
if src_path not in sys.path:
    sys.path.insert(0, src_path)
    
from src.detection import (
    apply_fdr,
    calculate_fdr_thresholds,
)

def test_apply_fdr():
    signal = np.random.normal(0, 1, 1000)
    alpha = 0.05
    indices = apply_fdr(signal, alpha)
    assert len(indices) > 0  # Ensure some spikes are detected

def test_calculate_fdr_thresholds():
    spikes_values = np.array([0.1, 0.2, -0.3, -0.1])
    positive_fdr, negative_fdr = calculate_fdr_thresholds(spikes_values)
    assert positive_fdr > 0
    assert negative_fdr < 0
