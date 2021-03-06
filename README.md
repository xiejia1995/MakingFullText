# MakingFullText


This project aims at helping humanities scholars to produce and share our own full-text data.

---

## A usual workflow for producing full-text data from contemporary materials:

1. Prepare a scan of your documents (in any form, PDF, PNG, etc.)

2. Process the images of the documents into a clearly visible form.

3. Choose proper [OCR tools](#ot) to detect and recognize texts, and save them into txt format.

4. Based on the txt data, we can do a [distant reading](#dr) by means of computer.

## Republican materials
The workflow for Republican materials is on the way. A test of OCR tools recognizing Republican sample can be seen [here](./docs/OCR_test_Republican_Magazine.md).

<a name="ot"></a>
## OCR tools
For academic use, we should avoid relying too much on commercial ones, but to choose open-source tools. Currently, the prevalent Chinese OCR projects are [ChineseOCR_Lite](https://github.com/DayBreak-u/chineseocr_lite), [ChineseOCR](https://github.com/chineseocr/chineseocr), and [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR).

ChineseOCR is written in C++, while PaddleOCR is python. PaddleOCR supports recognizing multiple languages.

An excellent OCR tool for periodicals should do well in two functions:
1. Detecting the text area
2. Recognizing the Chinese characters

<a name="dr"></a>
## Distant reading

#### Definition
>Distant Reading ist ein Ansatz aus den digitalen Literaturwissenschaften, bei dem computationelle Verfahren auf häufig große Mengen an Textdaten angewandt werden, ohne dass die Texte selber gelesen werden. [(fortext.net)](https://fortext.net/ueber-fortext/glossar/distant-reading#:~:text=Distant%20Reading%20ist%20ein%20Ansatz,die%20Texte%20selber%20gelesen%20werden.&text=Als%20Gegenbegriff%20zu%20Close%20Reading,Franco%20Moretti%20(2000)%20gepr%C3%A4gt.)
>>>
     
     
<a name="wf"></a>   
#### An example of Word frequency

Let's start with a simplest word frequency test!

This is an example of how we check the words appear most times in Nongjianübaishitong (农家女百事通) 1997 (page 1- 120).

To prepare, we should install a [python](https://www.python.org/) 3.x (e.g. 3.8), and run
```shell
pip install jieba wordcloud
```
to install the dependent modules for running our scripts.

In the word_frequency folder, there are   

"[NJN1997.txt](https://github.com/xiejia1995/MakingFullText/blob/main/word_frequency/NJN1997.txt)" which is the full text of NJNBST 1997;  and

"[excludes.txt](https://github.com/xiejia1995/MakingFullText/blob/main/word_frequency/excludes.txt)" which contains the words that won't be counted, such as "一个", or "因为".  


run the [RunWordFreq_NJN1997.py](https://github.com/xiejia1995/MakingFullText/blob/main/word_frequency/RunWordFreq_NJN1997.py)

in seconds, we get this:  
```shell  
自己          256
孩子          198
生活          178
农村          142
妇女          117
丈夫           99
公斤           89
母亲           88
现在           82
技术           82
希望           81
父母           80
农民           80
老师           75
问题           71
工作           69
...
```  

Since the word "孩子" appears more than 190 times, we can guess that it is indeed an important topic. 


Thanks to the wordcloud, we can visualise this result and generate the image below for use in our presentations.

<img src="./word_frequency/wordcloudNJN1997_Sample.jpg" align="middle" width = "500"/>



   

## Files in this repo
#### data
the full-text data in txt format, recommended path is " \[NAME\]/year/(volume)/page.txt" e.g. Nongjianv_Baishitong/1997/1.txt

#### docs
documents of this project

#### easy_tools
some practical python scripts.

#### py_paddleocr
python scripts on using PaddleOCR

#### word_frequency
a simple python script to see the word frequency of texts, to apply it, see [here](#wf)
