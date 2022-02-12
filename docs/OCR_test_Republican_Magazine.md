# OCR test for Republican Magazines
---

Due to many reasons, producing full-text data is not easy for historical documents. Here is a first attempt of this, with several ready-to-use open-source OCR projects.

## Tested tools
From GitHub, I choose the two Chinese OCR repos with most followers, namely ChineseOCR_lite and PaddleOCR, which are widely applied to OCR in daily-life and natural scenes; and KindaiOCR project focuses on modern Japanese magazines. All of them are based on neural network. In this test, I use the models they have already trained.

Here are some default qualities of 3 tools:
Tools | ChineseOCR_lite | PaddleOCR | KindaiOCR
language| c++ | python | python
speed | very fast | fast | slow
reading direction | both | both | vertical
recognition of language | 简体中文 | multiple languages | Japanese


## Difficulty in processing Republican magazines
Unlike contemporary magazines, Republican ones have the following features:   

- reading direction mostly top-bottom and right-to-left;  
- no standardized punctuation system;  
- characters written in variant glyphs;  
- sometimes printed unclearly.

## Run Tests
As to the testing sample, I choose one page from the local magazine "Fan hou zhong" (飯後鐘) in the 1920s China. It has only texts without images and its reading direction is vertical. The punctuation system is the white and black circles besides characters (see picture).

<img src="./docs/OCRTest/sample.png" align="middle">

To see how the circles affect the OCR process, I manually clear them and save this pic as a sample2:

<img src="./docs/OCRTest/sample2.png" align="middle">

In the first round, let's have a look at the result of detecting text areas:

**ChineseOCR_lite** can not detect at all and is ruled out of this round. Since its default model is for Simplified Chinese, it is not very suprising.

**Paddle** wrongly reads the direction of texts, see picture:
<img src="./docs/OCRTest/PaddleOCR-result.jpg" align="middle">

**KindaiOCR** detects most of the texts but is obviously disrupted by the circles:
<img src="./docs/OCRTest/KindaiOCR-res_or.jpg" align="middle">

Given the fact that all three can not detect the text area well, it is meangless to compare the correct rate.

In the round 2, sample2 without circles will be tested.

**ChineseOCR_lite** does very well in detecting the text lines, but the titles on the top and right side are ignored:
<img src="./docs/OCRTest/ChineseOCR-result.jpg" align="middle">

**Paddle** can only ditect app. 80% of texts, which still needs much improvement:
<img src="./docs/OCRTest/PaddleOCR-result2.jpg" align="middle">

**KindaiOCR** this time perfectly detects all the texts:
<img src="./docs/OCRTest/KindaiOCR-res2.jpg" align="middle">

However, ChineseOCR_lite does not hold a model for tranditional Chinese yet, people who need this have to train it by themselves. PaddleOCR is still struggling with the detection performance. KindaiOCR's detection is good, but the recognition model is only for Japanese, not very suitable for Chinese. Still, we need to prepare the training.

In conclusion, the OCR performance for Republican materials is still poor. To improve it, my next step will focus on solving two major problems:
1. consider how to deal with the circles besides characters
2. prepare a better model for Republican magazines character recognition
