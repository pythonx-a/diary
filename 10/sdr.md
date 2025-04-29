# Specifications for the Mini Project on Software Defined Radio (SDR)

## Project Description

The goal of this project is to explore RF signal acquisition and transmission using three software-defined radio devices:

- [RTL-SDR](https://www.rtl-sdr.com/rtl-sdr-quick-start-guide/)
- [LimeSDR Mini](https://limemicro.com/boards/limesdr-mini/)
- [HackRF One](https://greatscottgadgets.com/hackrf/one/)

All the development is done using direct programming of Python scripts (no graphical interfaces) and lightweight, widely supported Python libraries.

---

## Achievable (Mandatory) Objectives

- Installation, configuration, and functional testing of the three SDR devices.
- Capture a simple RF signal (e.g., FM) using all three SDR devices.
- Visualize the real-time spectrum (FFT) of the captured signals.
- Generate and transmit simple signals:
  - Pure carrier (unmodulated)
  - Simple sine wave
- Compare the capabilities of the three devices.
- Document the process in a project journal and a simple report (e.g., wiki).

---

## Features

- Automatic detection and initialization of the selected SDR device (RTL-SDR, LimeSDR Mini, HackRF One).
- RF signal acquisition and FFT-based spectrum visualization.
- Transmission of simple signals generated in Python (carrier or sine wave).
- Simple command-line interface to select the device and operation (reception/transmission).
- Well-documented, modular, and easy-to-use scripts.

---

## Technologies Used

- **Hardware**:
  - [RTL-SDR](https://www.rtl-sdr.com/rtl-sdr-quick-start-guide/)
  - [LimeSDR Mini](https://limemicro.com/boards/limesdr-mini/)
  - [HackRF One](https://greatscottgadgets.com/hackrf/one/)

- **System**:
  - Ubuntu 24.04
  - Python 3.10+

- **Python Libraries**:
  - [`numpy`](https://numpy.org/), [`scipy`](https://scipy.org/): signal processing, IQ sample generation.
  - [`matplotlib`](https://matplotlib.org/): spectrum visualization.
  - [`pyrtlsdr`](https://pyrtlsdr.readthedocs.io/): control for RTL-SDR.
  - [`SoapySDR`](https://github.com/pothosware/SoapySDR/wiki): control for LimeSDR Mini.
  - [`python-hackrf`](https://pypi.org/project/python-hackrf/): control for HackRF One.
  - [`click`](https://click.palletsprojects.com/): implement the command-line interface.
  - *(optional)* [`pyliquid-dsp`](https://github.com/michelp/pyliquid-dsp): Python bindings for [`liquid-dsp`](https://github.com/jgaeddert/liquid-dsp), for simple digital modulations (if time allows).
  - *(optional)* [`pyfftw`](https://github.com/pyFFTW/pyFFTW): faster FFT computations than `numpy.fft`.
  - *(optional)* [`sounddevice`](https://python-sounddevice.readthedocs.io/en/0.4.6/): real-time audio transmission or reception.
  - *(optional)* [`scikit-dsp-comm`](https://scikit-dsp-comm.readthedocs.io/en/latest/): communication and DSP algorithms for educational SDR projects.

---

## Team Members

- Sara Grassi

---

## Task Distribution

- **Week 1**: Installation and configuration of the three SDR devices.
- **Week 2**: Signal reception with each device; acquisition and spectrum visualization.
- **Week 3**: Implementation of basic signal transmission (pure carrier, sine wave).
- **Week 4**: Reception and visualization of transmitted signals.
- **Week 5**: Comparison, improvements, code finalization.
- **Week 6**: Writing of the final report, preparation of the demonstration and the final presentation.

---

## Possible Extensions (if time allows)

- Transmission of a frequency-modulated (FM) tone.
- Transmission of a simple audio file (FM modulation).
- Implementation of basic digital modulations (BPSK, QPSK...) using `pyliquid-dsp`:
  - Transmit/receive a short text file containing a message (e.g., "Hello from SDR!").
- Attempt a more complex digital modulation, such as 16-QAM.

---

## Advanced Future Work (out of project scope)

- Full "FM radio" demonstrator:
  - Capture an audio signal from a microphone or file.
  - Modulate it into RF and transmit it.
  - Receive it and demodulate it.
  - Play the received audio.
- Passive spectrum sniffing:
  - Scanning and analyzing existing RF signals (e.g., Bluetooth, Wi-Fi, 4G/5G) without decoding or active transmission.
- Exploration of spectrum intelligence techniques:
  - Manual or semi-automatic analysis of received signals to infer modulation types (BPSK, QPSK, QAM...).
  - Classical machine learning with [`scikit-learn`](https://scikit-learn.org/stable/), e.g., clustering IQ samples, training classifiers to recognize modulation patterns automatically.
  - Deep learning using [`Keras`](https://keras.io/), [`TensorFlow`](https://www.tensorflow.org/), and [`PyTorch`](https://pytorch.org/) to build neural network classifiers for modulation recognition.

---
