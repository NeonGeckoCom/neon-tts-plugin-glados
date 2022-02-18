## Description

OVOS TTS plugin for [GladosTTS](https://github.com/R2D2FISH/glados-tts)

The initial, regular Tacotron model was trained first on LJSpeech, and then on a heavily modified version of the Ellen McClain dataset (all non-Portal 2 voice lines removed, punctuation added). 
The Forward Tacotron model was only trained on about 600 voice lines. 
The HiFiGAN model was generated through transfer learning from the sample. 
All models have been optimized and quantized.

## Install

`pip install neon-tts-plugin-glados`

## Configuration

```json
  "tts": {
    "module": "neon-tts-plugin-glados"
    }
```

## Docker

build it
```bash
docker build . -t gladostts
```

run it
```bash
docker run -p 8080:9666 gladostts
```

use it `http://localhost:8080/synthesize/hello`
