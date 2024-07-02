import os
import re
# import json
import toml
import logging
import threading
import requests
# import torchaudio
from huggingface_hub import snapshot_download
from pathlib import Path
# from urllib import request
from time import sleep
# from typing import List, Optional, Dict

from listen import CONFIG_PATH, I18N

logging.basicConfig(level=logging.INFO)

# custom exception hook
def custom_hook(args):
    # report the failure
    logging.error(f'Thread failed: {args.exc_value}')

# set the exception hook
threading.excepthook = custom_hook

# def get_audio_info(audio_bin):
#     audio_info = torchaudio.info(audio_bin)
#     return audio_info

# def get_sample_rate(audio_bin):
#     audio_info = get_audio_info(audio_bin)
#     sample_rate = audio_info.sample_rate
#     return sample_rate

def get_config_or_default():
    # Check if conf exist

    if os.path.isfile(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as cfg:
            CONFIG = toml.loads(cfg.read())
    else:        
        CONFIG = {
            'service': {
                'host': '0.0.0.0',
                'port': '5063',
                'n_proc': 2
            },
            'stt': {
                'is_allowed': False
            }
        }
        if not os.path.isdir(os.path.dirname(CONFIG_PATH)):
            os.makedirs(os.path.dirname(CONFIG_PATH))
        with open(CONFIG_PATH, 'w') as f:
            f.write(toml.dumps(CONFIG))
    
    return CONFIG

def is_allowed_to_listen(conf=get_config_or_default()):
    _stt_conf = conf.get('stt', False)
    if _stt_conf:
        return _stt_conf.get('is_allowed', False)
    return False

def get_best_model(lang):
    if lang == 'en':
        return 'distil-whisper/distil-large-v3'
    elif lang == 'fr':
        return 'bofenghuang/whisper-large-v3-french'
    # feel free to add more languages
    else:
        return 'distil-whisper/distil-large-v3'

def get_loc_model_path(language=None):
    """
    Get localised model path.
    Returns the path or name to the Whisper model of the choosen language.
    [Default] language: System language
    """
    return os.environ.get('ASR_MODEL_ID') or get_best_model(language or I18N)

def download_ctranslate2_snapshot(model_id, model_path):
    return snapshot_download(repo_id=model_id, local_dir=model_path, allow_patterns='ctranslate2/*')

def get_available_cpu_count():
    """Number of available virtual or physical CPUs on this system, i.e.
    user/real as output by time(1) when called with an optimally scaling
    userspace-only program
    See this https://stackoverflow.com/a/1006301/13561390"""

    # cpuset
    # cpuset may restrict the number of *available* processors
    try:
        m = re.search(r"(?m)^Cpus_allowed:\s*(.*)$", open("/proc/self/status").read())
        if m:
            res = bin(int(m.group(1).replace(",", ""), 16)).count("1")
            if res > 0:
                return res
    except IOError:
        pass

    # Python 2.6+
    try:
        import multiprocessing

        return multiprocessing.cpu_count()
    except (ImportError, NotImplementedError):
        pass

    # https://github.com/giampaolo/psutil
    try:
        import psutil

        return psutil.cpu_count()  # psutil.NUM_CPUS on old versions
    except (ImportError, AttributeError):
        pass

    # POSIX
    try:
        res = int(os.sysconf("SC_NPROCESSORS_ONLN"))

        if res > 0:
            return res
    except (AttributeError, ValueError):
        pass

    # Windows
    try:
        res = int(os.environ["NUMBER_OF_PROCESSORS"])

        if res > 0:
            return res
    except (KeyError, ValueError):
        pass

    # jython
    try:
        from java.lang import Runtime

        runtime = Runtime.getRuntime()
        res = runtime.availableProcessors()
        if res > 0:
            return res
    except ImportError:
        pass

    # BSD
    try:
        sysctl = subprocess.Popen(["sysctl", "-n", "hw.ncpu"], stdout=subprocess.PIPE)
        scStdout = sysctl.communicate()[0]
        res = int(scStdout)

        if res > 0:
            return res
    except (OSError, ValueError):
        pass

    # Linux
    try:
        res = open("/proc/cpuinfo").read().count("processor\t:")

        if res > 0:
            return res
    except IOError:
        pass

    # Solaris
    try:
        pseudoDevices = os.listdir("/devices/pseudo/")
        res = 0
        for pd in pseudoDevices:
            if re.match(r"^cpuid@[0-9]+$", pd):
                res += 1

        if res > 0:
            return res
    except OSError:
        pass

    # Other UNIXes (heuristic)
    try:
        try:
            dmesg = open("/var/run/dmesg.boot").read()
        except IOError:
            dmesgProcess = subprocess.Popen(["dmesg"], stdout=subprocess.PIPE)
            dmesg = dmesgProcess.communicate()[0]

        res = 0
        while "\ncpu" + str(res) + ":" in dmesg:
            res += 1

        if res > 0:
            return res
    except OSError:
        pass

    raise Exception("Can not determine number of CPUs on this system")

