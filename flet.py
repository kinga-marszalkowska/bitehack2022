import socket
import simpleaudio as sa
# from main import piano

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 6666))
sock.listen()
connection, addr = sock.accept()


while True:
    data = connection.recv(1)
    d = str(data).split("\'")
    print(d[1])
    if d[1] == "1":
        w = sa.WaveObject.from_wave_file("flute-short.wav")
        p = w.play()
    elif d[1] == "2":
        a = sa.WaveObject.from_wave_file("flute-medium.wav")
        b = a.play()
    elif d[1] == "3":
        c = sa.WaveObject.from_wave_file("flute-long.wav")
        d = c.play()

