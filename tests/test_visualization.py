import sys
import os
import pytest
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from src.visualization import plot_signal_with_spikes


def test_visualization_dummy():
   
    assert plot_signal_with_spikes is not None
