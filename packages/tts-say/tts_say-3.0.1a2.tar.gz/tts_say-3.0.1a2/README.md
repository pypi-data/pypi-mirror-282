# Say: echo but with TTS

Say uses coqui-TTS to create convincing voices for TTS application.

Flexible as you like it.

## Installation

```zsh
pip install tts-say
# Or from source
pip install git+https://gitlab.com/waser-technologies/technologies/say.git
```

## Usage

From super simple...

```zsh
❯ say Hello World
Hello World
```

...to choosing your own vocoder.

```zsh
❯ say --help
usage: say [-h] [-n] [-e] [-E] [-v] [-L LANG] [--out_path OUT_PATH] [--list_models [LIST_MODELS]] [--model_name MODEL_NAME] [--vocoder_name VOCODER_NAME] [--config_path CONFIG_PATH] [--model_path MODEL_PATH] [--vocoder_path VOCODER_PATH] [--vocoder_config_path VOCODER_CONFIG_PATH] [--speaker_idx SPEAKER_IDX]
           [--speaker_wav SPEAKER_WAV [SPEAKER_WAV ...]] [--speakers_file_path SPEAKERS_FILE_PATH] [--use_cuda USE_CUDA] [--debug DEBUG]
           [text ...]

Same as echo but with Text-To-Speech.

positional arguments:
  text                  Text to be said.

options:
  -h, --help            show this help message and exit
  -n, --n               do not output the trailing newline
  -e, --e               enable interpretation of backslash escapes
  -E, --E               disable interpretation of backslash escapes (default)
  -v, --version         output version information and exit
  -L LANG, --lang LANG  Language to be spoken (default: $LANG)
  --out_path OUT_PATH   Output wav file path.
  --list_models [LIST_MODELS]
                        list available pre-trained tts and vocoder models.
  --model_name MODEL_NAME
                        Name of one of the pre-trained tts models in format <language>/<dataset>/<model_name>
  --vocoder_name VOCODER_NAME
                        name of one of the released vocoder models.
  --config_path CONFIG_PATH
                        Path to model config file.
  --model_path MODEL_PATH
                        Path to model file.
  --vocoder_path VOCODER_PATH
                        Path to vocoder model file. If it is not defined, model uses GL as vocoder. Please make sure that you installed vocoder library before (WaveRNN).
  --vocoder_config_path VOCODER_CONFIG_PATH
                        Path to vocoder model config file.
  --speaker_idx SPEAKER_IDX
                        Target speaker ID for a multi-speaker TTS model.
  --speaker_wav SPEAKER_WAV [SPEAKER_WAV ...]
                        wav file(s) to condition a multi-speaker TTS model with a Speaker Encoder. You can give multiple file paths. The d_vectors is computed as their average.
  --speakers_file_path SPEAKERS_FILE_PATH
                        JSON file for multi-speaker model.
  --use_cuda USE_CUDA   true to use CUDA.
  --debug DEBUG         true to enable debug mode.
```

`say` gives you the power.

### Start the server

First you need to load the models in memory.

To do so, start the TTS server using `say` without any `text` argument.

```
say [--list_models [LIST_MODELS]] [--model_name MODEL_NAME] [--vocoder_name VOCODER_NAME] [--config_path CONFIG_PATH] [--model_path MODEL_PATH] [--vocoder_path VOCODER_PATH] [--vocoder_config_path VOCODER_CONFIG_PATH] [--speakers_file_path SPEAKERS_FILE_PATH] [--use_cuda USE_CUDA] [--debug DEBUG]
No attribute `text`.
say --help
For more information.
Starting server now.
Please wait.
...
```

Or enable its service.

```
cp ./speak.service.example /usr/lib/systemd/user/speak.service
systemctl --user enable --now speak.service
```

#### Get authorization to speak

You need to authorize the system to speak first. Change the service configuration as follows.

```toml
# ~/.assistant/tts.toml
...
[tts]
is_allowed = true
...
```

Then [start the server](#start-the-server) and use `say` with some `text` argument to [say something](#use-the-client).

### Use the client

Before you use the client, make sure :
  1. the system has a valid [authorization to speak](#get-authorization-to-speak), 
  2. the server has correctly loaded the models,
  3. if the server has loaded `YourTTS` (by default); you need to [create a `style_wav` file of your default speaker](#setup-your-own-voice-yourtts-only).


```zsh
say [-n] [-e] [-E] [-v] [-L LANG] [--out_path OUT_PATH] [text ...]

❯ say --version
Say, version two dot, zero dot, three.
Say: version 2.0.3
Copyright (c) 2022, Danny Waser
TTS version 0.6.2
...

❯ say Hello, this is a test
Hello, this is a test
```

### Save the audio

To save the resulted speech, use the argument `--out_path`.

```zsh
❯ say "Bonjour." --out_path "say_output.wav"
Bonjour.
❯ soxi say_output.wav

Input File     : 'say_output.wav'
Channels       : 1
Sample Rate    : 16000
Precision      : 16-bit
Duration       : 00:00:01.17 = 18726 samples ~ 87.7781 CDDA sectors
File Size      : 37.5k
Bit Rate       : 256k
Sample Encoding: 16-bit Signed Integer PCM
```

## Setup your own voice (YourTTS only)

By default, the server uses YourTTS to produce speech.

Therefor, before saying anything, you need to add a wav file to `~/.assistant/data/${lang}/TTS/styles/default.wav`.

Where `$lang` is your target language (_i.e_ _`en`_, _`fr`_, _etc._).

This wav file must contain between 5 and 15 seconds of speech.

Make sure it matches with your `tts.toml` configuration.

You can also use the flag `--speaker_wav` manually.

```zsh
say "Hello." --speaker_wav "~/.assistant/data/en/TTS/styles/default.wav"
```

### _Don't want to hunt down a voice?_

Checkout my [collection of high quality TTS voices](https://gitlab.com/waser-technologies/data/tts/en/voices) generated using TTS VTCK/VITS models. 

### Audio samples
<audio src="https://gitlab.com/waser-technologies/data/tts/en/voices/-/raw/master/female/default.wav?inline=false" controls preload></audio>
![](img/default_female.wav)

<audio src="https://gitlab.com/waser-technologies/data/tts/en/voices/-/raw/master/male/default.wav?inline=false" controls preload></audio>
![](img/default_male.wav)

<audio src="https://gitlab.com/waser-technologies/data/tts/en/voices/-/raw/master/female/default_2.wav?inline=false" controls preload></audio>
![](img/default_female_2.wav)

## Yes yes but echo is for text right ?

Yes but you should be able to `alias` `echo` to `say` inside your favorite shell.

Because when you think about it, asking your computer to `say something` is like asking it to `echo something`.

Both cases output `something`.

Where echo repeat what it got in stdin, say as an injonction is used to ask someone to repeat what comes after.

Like so :
```
❯ Assistant, say Hello.
[Assistant] Hello.
```