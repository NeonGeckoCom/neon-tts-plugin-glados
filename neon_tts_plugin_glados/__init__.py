# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from os.path import join, isfile
import os
import requests
import torch
from ovos_plugin_manager.templates.tts import TTS, TTSValidator
from neon_tts_plugin_glados.utils import prepare_text
from ovos_utils.xdg_utils import xdg_data_home
from scipy.io.wavfile import write


class GladosTTSPlugin(TTS):
    """Interface to Glados TTS."""

    def __init__(self, lang="en-us", config=None):
        super(GladosTTSPlugin, self).__init__(lang, config, GladosTTSValidator(self), 'wav')
        model = self.config.get("model", "https://github.com/R2D2FISH/glados-tts/raw/main/models/glados.pt")
        vocoder = self.config.get("vocoder", "https://github.com/R2D2FISH/glados-tts/raw/main/models/vocoder-cpu-lq.pt")
        device = self.config.get("device", "cpu")
        if model.startswith("http"):
            model = self.download_model(model)
        if vocoder.startswith("http"):
            vocoder = self.download_model(vocoder)
        self.glados = torch.jit.load(model)
        self.vocoder = torch.jit.load(vocoder)

        self.glados.cpu()
        self.vocoder.to(device)

    @staticmethod
    def download_model(url):
        base_folder = join(xdg_data_home(), 'glados_tts')
        os.makedirs(base_folder, exist_ok=True)
        path = join(base_folder, url.split("/")[-1])
        if not isfile(path):
            data = requests.get(url).content
            with open(path, "wb") as f:
                f.write(data)
        return path

    def synth(self, utterance, wav_file):
        x = prepare_text(utterance).to('cpu')
        with torch.no_grad():
            tts_output = self.glados.generate_jit(x)
            mel = tts_output['mel_post'].cpu()
            audio = self.vocoder(mel)
            audio = audio.squeeze()
            audio = audio * 32768.0
            audio = audio.cpu().numpy().astype('int16')
            write(wav_file, 22050, audio)
        return wav_file

    def get_tts(self, sentence, wav_file, lang=None):
        """Generate WAV and phonemes.

        Arguments:
            sentence (str): sentence to generate audio for
            wav_file (str): output file

        Returns:
            tuple ((str) file location, (str) generated phonemes)
        """
        return self.synth(sentence, wav_file), None


class GladosTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(GladosTTSValidator, self).__init__(tts)

    def validate_voice(self):
        pass

    def validate_connection(self):
        pass

    def get_tts_class(self):
        return GladosTTSPlugin

    @staticmethod
    def get_lang_list():
        return []
