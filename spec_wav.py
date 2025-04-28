import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np
import torch
from glob import glob
from pathlib import Path

def plot_spectrogram(samples, sr, nfft=512,hop_frac=4,name='plot',dir=''):
    title = {'mix':'Mixture','spk1':'Speaker 1','spk2':'Speaker 2'}
    samples = samples.squeeze()
    if not torch.is_tensor(samples):
        samples = torch.tensor(samples)
    samples = samples/max(abs(samples))
    samples_stft = torch.stft(
        samples,
        n_fft=nfft,
        hop_length=nfft // hop_frac,
        win_length=nfft,
        window=torch.hamming_window(nfft),
        center=True,
        pad_mode='reflect',
        normalized=False,
        onesided=True,
        return_complex=True)

    spec = torch.abs(samples_stft)
    fig,ax0 = plt.subplots(figsize=(12, 5))

    # Spectrogram
    time_extent = np.linspace(0, samples.shape[0] / sr, spec.shape[-1])
    freq_extent = np.linspace(0, sr / 2, spec.shape[0])  
    img = ax0.imshow(
        20 * torch.log10(spec + 1e-9),  # Avoid log(0) issues
        origin='lower',                
        aspect='auto',
        extent=[time_extent[0], time_extent[-1], freq_extent[0], freq_extent[-1]],
        vmin=-60,
        vmax=45,
        cmap='magma'
    )
    ax0.set_ylabel('Frequency [Hz]')
    ax0.set_yticks(np.arange(0, sr / 2, sr / 16))
    ax0.set_yticklabels((np.arange(0, sr / 2, sr / 16)).astype(np.int16))
    ax0.set_xlabel('Time [s]')
    
    if 'mix' in name:
        t = title['mix']
    elif 'y_hat_1' in name:
        t = title['spk1']
    elif 'y_hat_2' in name:
        t = title['spk2']
    else:
        t=''
    ax0.set_title(t,fontsize=20)

    plt.tight_layout()
    d = Path(str(dir).replace('audio','images'))
    plt.savefig(d/f'{name}.png')

def plot_dir_path(p):
    for dir_path in p.glob('*'):
        print(dir_path)
        names = dir_path.glob('*.wav')
        for name in names:
            print(name.name)
            shift=0
            wav,fs = sf.read(name)
            plot_spectrogram(wav[int(shift*fs):,0],fs,name=name.name.split('.wa')[0],dir=dir_path)
            