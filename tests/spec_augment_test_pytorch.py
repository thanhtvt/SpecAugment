# Copyright 2019 RnD at Spoon Radio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""SpecAugment test"""

import os
import sys
import argparse
import librosa
import numpy as np
from torch import from_numpy

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from SpecAugment import spec_augment_pytorch

parser = argparse.ArgumentParser(description='Spec Augment')
parser.add_argument('--audio-path', default='../data/61-70968-0002.wav', help='The audio file.')
parser.add_argument('--time-warp-para', default=80, help='time warp parameter W')
parser.add_argument('--frequency-mask-para', default=100, help='frequency mask parameter F')
parser.add_argument('--time-mask-para', default=27, help='time mask parameter T')
parser.add_argument('--masking-line-number', default=1, help='masking line number')

args = parser.parse_args()
audio_path = args.audio_path
time_warping_para = args.time_warp_para
time_masking_para = args.frequency_mask_para
frequency_masking_para = args.time_mask_para
masking_line_number = args.masking_line_number

if __name__ == "__main__":
    # Step 0 : cd to right dir, load audio file, extract mel spectrogram
    if os.getcwd() != os.path.dirname(os.path.abspath(__file__)):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
    audio, sampling_rate = librosa.load(audio_path)
    mel_spectrogram = librosa.feature.melspectrogram(y=audio,
                                                     sr=sampling_rate,
                                                     n_mels=256,
                                                     hop_length=128,
                                                     fmax=8000)

    # reshape spectrogram shape to [batch_size, time, frequency]
    shape = mel_spectrogram.shape
    mel_spectrogram = np.reshape(mel_spectrogram, (-1, shape[0], shape[1]))
    mel_spectrogram = from_numpy(mel_spectrogram)

    # Show Raw mel-spectrogram
    spec_augment_pytorch.visualization_spectrogram(mel_spectrogram=mel_spectrogram,
                                                   title="Raw Mel Spectrogram")

    # Calculate SpecAugment pytorch
    warped_masked_spectrogram = spec_augment_pytorch.spec_augment(mel_spectrogram=mel_spectrogram)

    # Show time warped & masked spectrogram
    spec_augment_pytorch.visualization_spectrogram(mel_spectrogram=warped_masked_spectrogram,
                                                   title="pytorch Warped & Masked Mel Spectrogram")
