import numpy as np
import matplotlib.pyplot as plt

# Request user input for data file
file_path = input("Please enter the path to your data file (NumPy .npy format): ")

try:
    # Load the data from the provided file
    data = np.load(file_path)

    # Plot histogram
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=50, density=True, alpha=0.6, color="b")
    plt.title("Histogram of Signal Values")
    plt.xlabel("Signal Amplitude")
    plt.ylabel("Density")
    plt.grid(True)
    plt.show()

except Exception as e:
    print(
        f"Error: {e}\nPlease check the file path and ensure it is a valid NumPy .npy file."
    )
