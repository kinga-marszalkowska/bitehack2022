import time

# import sounddevice as sd
# from scipy.io.wavfile import write
# from pydub import AudioSegment
# import simpleaudio as sa
#
# fs = 44100  # Sample rate
# seconds = 3  # Duration of recording
#
# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# sd.wait()  # Wait until recording is finished
# write('output.wav', fs, myrecording)  # Save as WAV file
#
#
# time.sleep(2)
# wave_object = sa.WaveObject.from_wave_file("output.wav")
# play_object = wave_object.play()