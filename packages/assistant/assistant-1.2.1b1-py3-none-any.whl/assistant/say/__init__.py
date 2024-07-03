import sys
import json
import websockets
import asyncio
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pydub")

from assistant import I18N

try:
    from say.TTS import utils as tts_utils
    from say.TTS.as_client import tts, split_sentences, playback_engine
    # from num2words import num2words
except (ModuleNotFoundError, ImportError) as e:
    # print(e)
    # print("For Assistant to speak, you need to install the say module.")
    # print("Run the following command:\n```shell\npip install -r tts-say\n```")
    # sys.exit(1)
    raise e

TTS_CONFIG = tts_utils.get_config_or_default()
is_allowed_to_speak = tts_utils.is_allowed_to_speak(TTS_CONFIG)
if not is_allowed_to_speak:
    print("System has not user autorization to speak.")


class TTS:
    def __init__(self, host=None, port=None, language=None, speaker=None, style_wav=None):
        self.config = tts_utils.get_config_or_default()
        self.host = self.config.get("host", host)
        self.port = self.config.get("port", port)
        self.language = self.config.get("language", language)
        self.speaker = self.config.get("speaker", speaker)
        self.style_wav = self.config.get("style_wav", style_wav)
        # self.queue = asyncio.Queue(1)
        # self.wait = True
        self.tts = tts
        self.split_sentences = split_sentences
        self.playback_engine = playback_engine
        

    @property
    def is_allowed_to_speak(self):
        if self.config is None:
            self.config = tts_utils.get_config_or_default()
        return tts_utils.is_allowed_to_speak(self.config)

    # def split_sentences(self, text: str, split_char="|"):
    #     text = text.strip("\n")
    #     text = text.replace(",", f",{split_char}")
    #     text = text.replace(".", f".{split_char}")
    #     text = text.replace("!", f"!{split_char}")
    #     text = text.replace("?", f"?{split_char}")
    #     text = text.replace(":", f":{split_char}")
    #     text = text.replace(";", f";{split_char}")
    #     text = text.replace("\n", f"{split_char}")
    #     return text.split(split_char)
    
    
    
    def say(self, text: list[str] | str):
        if isinstance(text, str):
            text = text.split("\n")           
        if not self.is_allowed_to_speak:
            print('\n'.join(text))
            return
        
        for t in text:
            _t = split_sentences(t)
            for _text in _t:
                # tts_utils.echo(_text, no_newline=True)
                try:
                    asyncio.run(tts(_text, language="EN-NEWEST" if I18N.lower() == "en" else I18N.upper(), speaker="en-newest" if I18N.lower() == "en" else I18N.lower(), style_wav=f"{self.config['tts']['speaker_wav']}", save_output=False))
                except (ConnectionRefusedError, OSError):
                    pass # Server is not active or something
                except Exception as tts_e:
                    raise tts_e
            # tts_utils.echo("", no_newline=False)
            # asyncio.run(tts(text, language="fr-fr" if I18N == "fr" else I18N.lower(), voice_name="freeman", preset='fast', save_output=False))
            try:
                playback_engine.wait_done()
            except KeyboardInterrupt:
                playback_engine.stop()
                break
                
    async def asay(self, text: list[str]):
        if isinstance(text, str):
            text = text.split("\n")           
        if not self.is_allowed_to_speak:
            print('\n'.join(text))
            return
        
        for t in text:
            _t = split_sentences(t)
            for _text in _t:
                # tts_utils.echo(_text, no_newline=True, flush=True)
                try:
                    await tts(_text, language="EN-NEWEST" if I18N.lower() == "en" else I18N.upper(), speaker="en-newest" if I18N.lower() == "en" else I18N.lower(), style_wav=f"{self.config['tts']['speaker_wav']}", save_output=False)
                except (ConnectionRefusedError, OSError):
                    pass
                except Exception as tts_e:
                    raise tts_e
            # tts_utils.echo("\n", end="\n", no_newline=False, flush=True)
            while playback_engine.is_playing():
                try:
                    playback_engine.wait_done()
                except KeyboardInterrupt:
                    playback_engine.stop()
                    break
