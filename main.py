import time
import serial
import simpleaudio as sa

from pydub import AudioSegment
from pydub.playback import play

scream = AudioSegment.from_file("scream.wav")
mmm = AudioSegment.from_file("mmm.wav")


def piano():
    ser = serial.Serial(port = "COM6", baudrate=9600,
                        bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    val = ser.readline().rstrip().decode()
    while True:
        try:
            signal = val.split(":")
            print(signal)
            if signal[0] == "s1":
                if int(signal[1]) > 10_000:
                    w = sa.WaveObject.from_wave_file("drum1.wav")
                    p = w.play()
            elif signal[0] == "s2":
                if int(signal[1]) > 10_000:
                    a = sa.WaveObject.from_wave_file("drum2.wav")
                    b = a.play()
            elif signal[0] == "s3":
                if int(signal[1]) > 10_000:
                    c = sa.WaveObject.from_wave_file("drum3.wav")
                    xx = c.play()
            elif signal[0] == "s4":
                if int(signal[1]) >= 30_000:
                    wave_object = sa.WaveObject.from_wave_file("scream.wav")
                    play_object = wave_object.play()
                    print("aaaaa")
                    time.sleep(0.5)
                elif 10_000 <= int(signal[1]) < 30_000:
                    wave_object1 = sa.WaveObject.from_wave_file("mmm.wav")
                    play_object1 = wave_object1.play()
                    # play(mmm)

            # if int(val) >= 30_000:
            #     wave_object = sa.WaveObject.from_wave_file("scream.wav")
            #     play_object = wave_object.play()
            #     print("aaaaa")
            #     time.sleep(0.5)
            # elif 10_000 <= int(val) < 30_000:
            #     wave_object1 = sa.WaveObject.from_wave_file("mmm.wav")
            #     play_object1 = wave_object1.play()
            #     # play(mmm)
            #
            # elif int(val) <= 3_000:
            #     pass

        except ValueError:
            pass

piano()