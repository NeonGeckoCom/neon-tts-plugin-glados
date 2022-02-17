#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'neon-tts-plugin-glados = ' \
                     'neon_tts_plugin_glados:GladosTTSPlugin'
setup(
    name='neon-tts-plugin-glados',
    version='0.0.1',
    description='glados tts plugin for OpenVoiceOS',
    url='https://github.com/NeonGeckoCom/neon-tts-plugin-glados',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['neon_tts_plugin_glados',
              'neon_tts_plugin_glados.utils'],
    install_requires=["ovos-plugin-manager>=0.0.4a2",
                      "ovos-utils~=0.0.14a7",
                      "phonemizer~=3.0",
                      "torch~=1.10"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft plugin tts OVOS OpenVoiceOS',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT}
)
