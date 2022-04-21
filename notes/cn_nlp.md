# Chinese NLP

## Chinese BERT

- [ChineseBERT: Chinese Pretraining Enhanced by Glyph and Pinyin Information](https://aclanthology.org/2021.acl-long.161) (Sun et al., ACL 2021)
- [ACL2021论文之ChineseBERT：融合字形与拼音信息的中文预训练模型](https://zhuanlan.zhihu.com/p/393617564)
- [Devlin, Jacob, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. "Bert: Pre-training of deep bidirectional transformers for language understanding." *arXiv preprint arXiv:1810.04805* (2018).](https://arxiv.org/abs/1810.04805)
- [Stanford CS224n Winter 2021 More about Transformers and Pretraining](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1214/slides/cs224n-2021-lecture10-pretraining.pdf)



1. Structure: 
   - position embedding
   - fusion embedding:
     - concatenate the three embedding vectors below, the fusion layers maps the 3D-dimensional vector to D-dimensional through a fully connected layer
     - 字符嵌入 char embedding
       - Similar to token embedding in original BERT
     - 字形嵌入 glyph embedding
       - use three types of Chinese fonts – Fang- Song, XingKai and LiShu, each of which is in- stantiated as a 24 × 24 image with floating point pixels ranging from 0 to 255
     - 拼音嵌入 pinyin embedding
       - use the opensourced pypinyin package to generate pinyin sequences for its constituent characters
       - Pinyin for a Chinese character is a sequence of Romanian characters, with one of four diacritics denoting tones
       - The length of the input pinyin se- quence is fixed at 8, with the remaining slots filled with a special letter “-” when the actual length of the pinyin sequence does not reach 8.
       - use CNN model with width 2 on the pinyin sequence, followed by max-pooling to derive the resulting pinyin embedding
2. 在训练过程中，采用packed input和single input交替训练，比例为9:1，其中single input为一个单句，packed input由总长度不超过512字符的多个单句拼接而成。并且90%的概率进行全字掩码，10%的概率进行字符掩码。词语或字符的mask概率为15%，80%的概率将mask的字符使用[MASK]替换，10%的概率将mask的字符使用随机字符替换，10%的概率将mask的字符保持不变。采用了动态掩码策略来避免数据的重复训练。
3. 原始BERT: Bidirectional Encoder
   - Limitations: encoder 结构不能用于language model，需要用pretrained decoder

​		

## Chinese Named Entity Recognition 中文命名实体识别

- [1 - Chinese NER Using Lattice LSTM (Zhang and Yang. ACL 2018)](https://arxiv.org/abs/1805.02023)
- [2 - An Encoding Strategy Based Word-Character LSTM for Chinese NER (Liu et al., ACL 2019)](https://aclanthology.org/N19-1247/)
- [3 - A Neural Multi-digraph Model for Chinese NER with Gazetteers (Ding et al., ACL 2019)](https://aclanthology.org/P19-1141/)
- [4 - Leverage Lexical Knowledge for Chinese Named Entity Recognition via Collaborative Graph Network (Sui et al., EMNLP 2019)](https://aclanthology.org/D19-1396/)

- [5 - A Lexicon-Based Graph Neural Network for Chinese NER (Gui et al. EMNLP 2019)](https://aclanthology.org/D19-1096/)

- [知乎 - 最新中文NER模型介绍](https://zhuanlan.zhihu.com/p/77788495)，包含1-3
- [知乎 - 词典信息在中文命名实体识别中的应用](https://zhuanlan.zhihu.com/p/136277575)，包含4-5