import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, IntSlider, IntRangeSlider

def plot_signal_with_spikes(
    filtered_signal,
    unique_positive_spikes,
    unique_negative_spikes,
    positive_fdr,
    negative_fdr,
):
    def plot(x_range):
        x_min, x_max = x_range
        plt.figure(figsize=(12, 6))
        plt.plot(filtered_signal, color="lightblue", label="Filtered Signal")

        if not np.isnan(positive_fdr):
            plt.axhline(
                positive_fdr,
                color="green",
                linestyle="--",
                label="Positive FDR Threshold",
            )
        if not np.isnan(negative_fdr):
            plt.axhline(
                negative_fdr,
                color="purple",
                linestyle="--",
                label="Negative FDR Threshold",
            )

        # Positive spikes
        plt.scatter(
            [spike["peak_index"] for spike in unique_positive_spikes],
            [spike["peak"] for spike in unique_positive_spikes],
            color="red",
            label="Positive Spike"
            if "Positive Spike" not in plt.gca().get_legend_handles_labels()[1]
            else "",
        )

        # Negative spikes
        plt.scatter(
            [spike["peak_index"] for spike in unique_negative_spikes],
            [spike["peak"] for spike in unique_negative_spikes],
            color="blue",
            label="Negative Spike"
            if "Negative Spike" not in plt.gca().get_legend_handles_labels()[1]
            else "",
        )

        plt.xlim(0, len(filtered_signal))
        plt.title("Interactive Signal with Detected Spikes")
        plt.xlabel("Sample Index")
        plt.ylabel("Amplitude (µV)")
        plt.legend(loc="lower left", fontsize=8)
        plt.grid()
        plt.tight_layout()
        plt.show()

    x_slider = IntRangeSlider(
        value=[0, len(filtered_signal)],
        min=0,
        max=len(filtered_signal),
        step=100,
        description="X Range:",
        continuous_update=False,
    )

    interact(plot, x_range=x_slider)
