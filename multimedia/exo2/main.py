import pygame
import numpy as np
import wave


def generate_sine_wave(frequency, duration, phase, amplitude, sample_rate=44100):
    x = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    samples = amplitude * np.sin(2 * np.pi * frequency * x + phase)
    return samples.astype(np.int16)


def save_wav(filename, samples, sample_rate=44100):
    with wave.open(filename, 'wb') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        f.writeframes(samples.tobytes())


def play_wav(filename):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.quit()


if __name__ == "__main__":
    samples = generate_sine_wave(frequency=200, duration=1, phase=np.pi/2, amplitude=1)
    save_wav("sine.wav", samples)
    play_wav("sine.wav")
