import os

__version__ = "4.0.0b1"

try:
    I18N, L10N = (x for x in os.environ.get('LANG', "en_EN.UTF-8").split(".")[0].split("_"))
except ValueError as e:
    I18N, L10N = ("en", "EN")

USERNAME = os.environ.get("USER", 'root')
HOME = f"/home/{USERNAME}" if USERNAME != "root" else "/root"
ASSISTANT_PATH = f"{HOME}/.assistant" if USERNAME != "root" else "/usr/share/assistant"
CONFIG_PATH = f"{ASSISTANT_PATH}/stt.toml"
MODEL_PATH = f"{ASSISTANT_PATH}/models/{I18N}/ASR/"