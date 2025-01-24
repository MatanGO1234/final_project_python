sampling_rate = 30000  # Hz
refractory_period = 0.002  # 1 ms
min_distance = int(refractory_period * sampling_rate) # preventing detect the same spikes twice
alpha = 0.05
