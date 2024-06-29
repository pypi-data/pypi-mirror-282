import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr

class Voice(object):

    def __init__(self, mike=1, fs=44100) -> None:
        self._mike = mike
        self._fs = fs
        r = sr.Recognizer() # 음성 인식 객체 생성
        sd.default.samplerate = _fs # 샘플링 속도
        sd.default.channels = _mike # 확인한 마이크 번호 등록
        
    def record(self, sec=2, language="ko-KR"):
        myAudio = sd.rec(int(sec * _fs), dtype='int32') # 음성 받기
        print("명령을 말하세요")
        sd.wait() # 음성을 받을 동안 대기
        print("명령을 받았습니다")
        write('tempWave.wav', _fs, myAudio) # 음성 파일 저장
        ## 음성을 텍스트로 변환
        with sr.AudioFile('tempWave.wav') as source: # 음성 파일 읽어오기
            audio = r.record(source) # 음성 파일을 읽어 소리 데이터 변환
            text = r.recognize_google(audio, language=language) # 음성 인식(한글)
            return text
        return "받은 명령을 텍스트로 변환하지 못하였습니다"