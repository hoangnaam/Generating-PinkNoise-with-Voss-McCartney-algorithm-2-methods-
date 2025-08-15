# Pink Noise Generating by Voss–McCartney

Two implementations of pink noise (or so-called 1/f noise) built by using the Voss–McCartney algorithm:

1. **Octave-interval updates** (each random source updates every power-of-two sample).  
2. **Stochastic updates** (update indices chosen with a geometric distribution).

The octave-interval version was designed and implemented from scratch for this project, inspired by the algorithm’s description in literature.
Both implementations are included in src/pink_voss.py for side-by-side comparison of their spectra and slopes.

## Quick start

```bash
pip install numpy pandas thinkdsp matplotlib
python src/pink_voss.py
```

This will generate example spectra in `images/` for both approaches.

## Results (examples)

The plots show the power spectrum on log–log axes; in both cases, the slope approaches −1 (characteristic of pink noise), with differences in texture due to update scheduling.

## Files

```
pink-noise-voss/
├─ src/
│  └─ pink_voss.py        # both functions  unchanged bodies
├─ images/
│  ├─ pink_noise_octaves_power_spectrum.png
│  ├─ pink_noise_stochastic_power_spectrum.png
└─ README.md
```

## References

- Voss, R. F., & Clarke, J. (1978). **"1/f noise" in music and speech**. *Nature*.  
- McCartney, J. (1999). *SuperCollider* and discussions of 1/f noise generation.  
- Lyons, R. G. (2016). **The Voss–McCartney Algorithm for 1/f Noise** (DSPRelated).  
- Downey, A. (2014). **Think DSP** – pink noise, power spectra, and slope estimation.

> The stochastic implementation mirrors the approach described in the DSPRelated article, while the octave-interval version updates sources deterministically at powers of two.
