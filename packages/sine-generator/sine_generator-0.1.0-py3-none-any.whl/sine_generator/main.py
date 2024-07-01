#main.py

import numpy as np

def sine_generate(amplitude, frequency, sampling_rate, duration):
    """
    Generates a sinusoidal waveform with a DC offset to ensure only positive amplitudes.

    Parameters:
    - amplitude: Amplitude of the sine wave
    - frequency: Frequency of the sine wave in Hz
    - sampling_rate: Sampling rate in Hz
    - duration: Duration of the waveform in seconds

    Returns:
    - t: Time array
    - sine_wave_with_offset: Sine wave with DC offset
    """
    # Time array
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

    # Sine wave
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)

    # DC offset to make all values positive
    dc_offset = amplitude

    # Sine wave with DC offset
    sine_wave_with_offset = sine_wave + dc_offset

    return t, sine_wave_with_offset
