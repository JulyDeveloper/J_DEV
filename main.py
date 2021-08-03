import sys
import cv2
import pyaudio
import numpy as np
from time import sleep
from threading import Thread


class Video_page(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.cap = cv2.VideoCapture(0)
        self.check = bool
        self.record_check = bool
        self.record_str = str
        self.check_str = str

    def check_video(self):
        self.check_str = input("do you want open webcam? : Y/N ")

        if self.check_str == "Y":
            self.check = True
        elif self.check_str == "N":
            self.check = False
        else:
            print("wrong answer")
            exit(1)

    def video_record(self):

        if not record_check:
            self.record_str = input("do you want record webcam? : Y/N ")

            if self.record_str == "Y":
                self.record_check = True
            elif self.record_str == "N":
                self.record_check = False
            else:
                print("wrong answer")
                exit(1)
        else:
            self.record_str = input("do you want record end? : Y/N ")

            if self.record_str == "Y":
                self.record_check = True
            elif self.record_str == "N":
                self.record_check = False
            else:
                print("wrong answer")
                exit(1)

    def video_close(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def run(self):
        self.check_video()

        if not self.check:
            print("do not open")
        else:
            if self.cap.isOpened() != 1:
                print("Can't open the camera cap(0)")
                self.cap = cv2.VideoCapture(1)

            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

            while cv2.waitKey(33) < 0:
                ret, frame = self.cap.read()
                cv2.imshow("VideoFrame", frame)
                self.video_record()

            self.video_close()


'''
class Audio_control:

    def __init__(self):
        self.p = pyaudio.PyAudio()
'''


# Audio recording parameters
RATE = 44100
CHUNK = 2 ** 10
FORMAT = pyaudio.paInt16


def main():
    th = Video_page()
    th.start()
    while True:
        print("video test")
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True,
                        frames_per_buffer=CHUNK, input_device_index=2)

        while True:
            data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
            print(int(np.average(np.abs(data))))

        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == "__main__":
    main()
