import os
import glob
import io
import logging
import torch, torchaudio

import numpy as np
from timeit import default_timer as timer

from faster_whisper import WhisperModel

from listen import I18N, MODEL_PATH
from listen.Whisper import utils

cuda_device = os.environ.get("ASR_GPU_ID", "0")
device = torch.device(f"cuda:{cuda_device}" if torch.cuda.is_available() else "cpu")

def load_model(models_id_or_path):
    '''
    Load the pre-trained model into the memory
    @param models: Path or name of the Whisper.
    @Retval
    Returns a list [Model, Model Load Time]
    '''
    model_path = os.path.join(MODEL_PATH, models_id_or_path)
    if not os.path.exists(model_path):
        logging.error(f"Model path {model_path} does not exist.")
        
        if models_id_or_path != "distil-large-v3":
            utils.download_ctranslate2_snapshot(models_id_or_path, model_path)
    
    if models_id_or_path == 'distil-whisper/distil-large-v3':
        models_id_or_path = 'distil-large-v3'
    else:
        models_id_or_path = os.path.join(model_path, "ctranslate2")
    
    logging.info(f"Loading {models_id_or_path}")
    model_load_start = timer()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    compute_type = "float16" if torch.cuda.is_available() else "float32"
    model = WhisperModel(models_id_or_path, device=device, compute_type=compute_type)
    model_load_end = timer() - model_load_start
    logging.debug("Loaded model in %0.3fs." % (model_load_end))

    return [model, model_load_end]


def resolve_models(dirName):
    '''
    Resolve directory path for the models and fetch each of them.
    @param dirName: Path to the directory containing pre-trained models
    @Retval:
    Returns the model dirName
    '''
    return dirName

class Transcriber:

    sample_rate = 16_000

    def __init__(self, models_id_or_path):
        self.model, _  = load_model(models_id_or_path)
    
    # def punctuate(self, sentence: str):
    #     return self.punct_model.restore_punctuation(sentence).capitalize()

    def _transcribe(self, audio_bin, beam_diameter=5):
        segments, _ = self.model.transcribe(audio_bin, beam_size=beam_diameter, language=I18N)
        return " ".join([seg.text for seg in segments])
        

    def transcribe(self, audio_bin, fs):
        '''
        Run Inference on input audio
        @param audio: Input audio for running inference on
        @param fs: Sample rate of the input audio file
        @Retval:
        Returns a list [Inference, Inference Time]
        '''
        inference_time = 0.0
        audio_length = len(audio_bin) * (1 / fs)

        # Run STT
        logging.debug('Running inference...')
        inference_start = timer()
        output = self._transcribe(audio_bin)
        inference_end = timer() - inference_start
        inference_time += inference_end
        logging.debug('Inference took %0.3fs for %0.3fs audio file.' % (inference_end, audio_length))
        # if output:
        #     logging.debug('Punctuating sentence...')
        #     inference_start = timer()
        #     output = self.punctuate(output)
        #     inference_end = timer() - inference_start
        #     inference_time += inference_end
        #     logging.debug('Punctuation took %0.3fs for %0.3fs audio file.' % (inference_end, audio_length))
        logging.debug(f'Inference: {output}')
        
        return [output, inference_time]

    def run(self, audio_bin: bytes, sample_rate: int):
        '''
        Takes audio_bin as input and returns the transcription
        @param audio_bin: Input audio for running inference on
        @Retval:
        Returns the transcription

        Audio is expected to be in the format of a 16-bit signed integer, i.e. 2 bytes per sample.
        '''
        audio_data = np.frombuffer(audio_bin, np.int16).astype(np.float32)
        # audio_data = torch.tensor(audio_data, dtype=torch.float32)
        return self.transcribe(audio_data, sample_rate)

class Response:  
    def __init__(self, text, time):
        self.text = text
        self.time = time

class Error:
    def __init__(self, message):
        self.message = message
