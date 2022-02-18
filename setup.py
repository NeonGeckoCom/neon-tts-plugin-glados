#!/usr/bin/env python3
from os import path, getenv
from setuptools import setup

PLUGIN_ENTRY_POINT = 'neon-tts-plugin-glados = ' \
                     'neon_tts_plugin_glados:GladosTTSPlugin'


def get_requirements(requirements_filename: str):
    requirements_file = path.join(path.abspath(path.dirname(__file__)), "requirements", requirements_filename)
    with open(requirements_file, 'r', encoding='utf-8') as r:
        requirements = r.readlines()
    requirements = [r.strip() for r in requirements if r.strip() and not r.strip().startswith("#")]

    for i in range(0, len(requirements)):
        r = requirements[i]
        if "@" in r:
            parts = [p.lower() if p.strip().startswith("git+http") else p for p in r.split('@')]
            r = "@".join(parts)
            if getenv("GITHUB_TOKEN"):
                if "github.com" in r:
                    r = r.replace("github.com", f"{getenv('GITHUB_TOKEN')}@github.com")
            requirements[i] = r
    return requirements


with open("README.md", "r") as f:
    long_description = f.read()

with open("./version.py", "r", encoding="utf-8") as v:
    for line in v.readlines():
        if line.startswith("__version__"):
            if '"' in line:
                version = line.split('"')[1]
            else:
                version = line.split("'")[1]

setup(
    name='neon-tts-plugin-glados',
    version=version,
    description='glados tts plugin for OpenVoiceOS',
    long_description=long_description,
    url='https://github.com/NeonGeckoCom/neon-tts-plugin-glados',
    author='Neongecko',
    author_email='developers@neon.ai',
    license='Apache-2.0',
    packages=['neon_tts_plugin_glados',
              'neon_tts_plugin_glados.utils'],
    install_requires=get_requirements("requirements.txt"),
    extras_require={
        "docker": get_requirements("docker.txt")
    },
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
