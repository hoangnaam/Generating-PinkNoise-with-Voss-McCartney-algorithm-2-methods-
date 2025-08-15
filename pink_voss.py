# pink_voss.py
# -------------------------------------------------------------
# Two implementations of pink noise using the Voss–McCartney algorithm.
# Function bodies are kept exactly as provided by the author.
#
# Requirements:
#   pip install numpy pandas thinkdsp matplotlib
#
# Run:
#   python pink_voss.py
#
# This script will generate a power spectrum plot for each method.
# -------------------------------------------------------------

import numpy as np
import pandas as pd
import thinkdsp
from thinkdsp import decorate
import matplotlib.pyplot as plt

loglog = dict(xscale='log', yscale='log')

# ---------------
# Original snippet (kept verbatim in function body)
def PinkNoiseVoss(nrows, ncols):
  arrays = np.empty((ncols, nrows))
  arrays.fill(np.nan) # the dimensions are reversed
  arrays[:,0] = np.random.random(ncols)
  arrays[0,:] = np.random.random(nrows)
  counter = 1
  
  available_divided_number = array_of_divided_number(nrows)
  for i in range(ncols):
    if i == 0:
      continue
    else:
      for j in range(len(available_divided_number)):
        divided_num = available_divided_number[j]
        if counter % divided_num == 0:
          arrays[counter,divided_num-1] = np.random.random()
      counter += 1

  df = pd.DataFrame(arrays)
  df.fillna(method='ffill', axis=0, inplace=True)
  total = df.sum(axis=1)
  return total.values

# Helper the original snippet expects
def array_of_divided_number(nrows):
  array = []
  for i in range(nrows+1):
    array.append(i)
  array.pop(0)
  array.pop(0)
  return array

# ---------------
# Reference-style implementation (from the linked article idea; function body unchanged)
def voss(nrows, ncols=10):
    """Generates pink noise using the Voss-McCartney algorithm.
    
    nrows: number of values to generate
    rcols: number of random sources to add
    
    returns: NumPy array
    """
    array = np.empty((nrows, ncols))
    array.fill(np.nan)
    array[0, :] = np.random.random(ncols)
    array[:, 0] = np.random.random(nrows)
    
    # the total number of changes is nrows
    n = nrows
    cols = np.random.geometric(0.5, n)
    cols[cols >= ncols] = 0
    rows = np.random.randint(nrows, size=n)
    array[rows, cols] = np.random.random(n)

    df = pd.DataFrame(array)
    df.fillna(method='ffill', axis=0, inplace=True)
    total = df.sum(axis=1)

    return total.values

if __name__ == "__main__":
    # --- Octave-interval generator ---
    pink_noise = PinkNoiseVoss(10, 11205)
    wave = thinkdsp.Wave(pink_noise)
    spectrum = wave.make_spectrum()
    spectrum.plot_power()
    decorate(xlabel='Frequency (Hz)', ylabel='Power', **loglog)
    plt.title("Pink noise (octave-interval updates)")
    plt.tight_layout()
    plt.savefig("images/pink_noise_octaves_run.png", dpi=160)
    plt.close()

    # --- Stochastic generator (geometric updates) ---
    ys = voss(11205)
    wave = thinkdsp.Wave(ys)
    spectrum = wave.make_spectrum()
    spectrum.plot_power()
    decorate(xlabel='Frequency (Hz)', ylabel='Power', **loglog)
    plt.title("Pink noise (stochastic updates)")
    plt.tight_layout()
    plt.savefig("images/pink_noise_stochastic_run.png", dpi=160)
    plt.close()
