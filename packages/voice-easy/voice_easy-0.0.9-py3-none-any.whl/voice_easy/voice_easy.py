import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr

class Voice(object):

    def __init__(self, mike=1, fs=44100) -> None:
        self._fs = fs
        self.r = sr.Recognizer() # 음성 인식 객체 생성
        sd.default.samplerate = fs # 샘플링 속도
        # sd.default.channels = mike # 확인한 마이크 번호 등록
        
    def record(self, sec=2, language="ko-KR"):
        try:
            with sr.Microphone() as source:
                print("명령을 말하세요")
                audio_data = self.r.record(source, duration=sec)
                text = self.r.recognize_google(audio_data, language=language)
                print("명령을 받았습니다")
                return text
        except sr.UnknownValueError:
            print("음성을 인식하지 못했습니다. 다시 시도해주세요.")
            return None
        except sr.RequestError as e:
            print(f"음성 인식 서비스에 접근할 수 없습니다: {e}")
            return None
        except Exception as e:
            print(f"오류가 발생했습니다: {e}")
            return None

        '''
        myAudio = sd.rec(int(sec * self._fs), dtype='int32') # 음성 받기
        print("명령을 말하세요")
        sd.wait() # 음성을 받을 동안 대기
        print("명령을 받았습니다")
        write('tempWave.wav', self._fs, myAudio) # 음성 파일 저장
        ## 음성을 텍스트로 변환
        with sr.AudioFile('tempWave.wav') as source: # 음성 파일 읽어오기
            audio = self.r.record(source) # 음성 파일을 읽어 소리 데이터 변환
            text = self.r.recognize_google(audio, language=language) # 음성 인식(한글)
            return text
        return "받은 명령을 텍스트로 변환하지 못하였습니다"
        '''