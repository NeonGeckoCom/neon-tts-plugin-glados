from ovos_tts_plugin_glados import GladosTTSPlugin

engine = GladosTTSPlugin()
engine.get_tts("hello world", wav_file="hello_world.wav")
