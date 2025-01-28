# Neuroscience Spike Detection Project

This project focuses on detecting, characterizing, and visualizing neural spikes from extracellular recordings.

## Project Structure

- `src/`: Contains all main Python modules for preprocessing, detection, characterization, and visualization.
- `tests/`: Contains unit tests for validating the functionality of each module.
- `main.py`: Entry point to run the project.
- `requirements.txt`: Lists required Python packages.

## How to Run

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate


2. Install dependencies:
   pip install -r requirements.txt
pip install ipympl ipywidgets  # For interactive plotting
jupyter nbextension enable --py widgetsnbextension


3. Run the main script:
   python main.py

### Data Distribution Analysis

The distribution of signal values was analyzed to validate the assumption of normality, which supports the use of the FDR test. To visualize the distribution of your signal values, run the following script:

```bash
python plot_distribution.py

## Interactive Plotting
When using Jupyter Notebook, enable interactive plotting by running the following command inside a notebook cell:

   %matplotlib widget
This enables interactive features like zooming and panning for your plots.

## Testing
Run unit tests to validate functionality:
   python -m pytest
Ensure that the tests/ directory contains all required test cases.

## Research Question

The goal of this project is to analyze neural signals by detecting action potentials (spikes), characterizing their properties, and visualizing the results.
