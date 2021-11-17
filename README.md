# SpecAugment [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
This is a implementation of SpecAugment that speech data augmentation method which directly process the spectrogram with Tensorflow & Pytorch, introduced by Google Brain[1]. This is currently under the Apache 2.0, Please feel free to use for your project. Enjoy!  
  
**Note**: Since the original repository is not actively maintained and has lots of bugs, I have to edit some to make it work.

## How to use

First, you need to have python 3 installed along with [Tensorflow](https://www.tensorflow.org/install/) or [PyTorch](https://pytorch.org/get-started/locally/)

Next, you need to install some audio libraries work properly. To install the requirement packages, run the following command:

```bash
pip3 install -r requirements.txt
```

And then, run the specAugment.py program. It modifies the spectrogram by warping it in the time direction, masking blocks of consecutive frequency channels, and masking blocks of utterances in time.

## Example
Learn more examples about how to do specific tasks in SpecAugment at the test code.

```bash
git clone https://github.com/thanhtvt/SpecAugment.git
cd ./SpecAugment/tests
# Uncomment the following line to run with Tensorflow
# python3 spec_augment_test_TF.py
python3 spec_augment_test_pytorch.py
```
In test code, we using one of the [LibriSpeech dataset](http://www.openslr.org/12/).

<p align="center">
  <img src="https://github.com/shelling203/SpecAugment/blob/master/images/Figure_1.png" alt="Example result of base spectrogram" width=600>
  <img src="https://github.com/shelling203/SpecAugment/blob/master/images/Figure_2.png" alt="Example result of base spectrogram" width=600>
</p>


# Reference

1. https://arxiv.org/pdf/1904.08779.pdf
2. https://github.com/DemisEom/SpecAugment (Original repo)