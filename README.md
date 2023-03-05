# Cross-Lingual Cross-Temporal Summarization Using Deep Learning

This work investigate the use of Transformer-based models for cross-lingual cross-temporal summarization (CLCT) and the influence of intermediate task finetuning on the results.


## Datasets 
Two main cross-lingual cross-temporal datasets are created as part of this work: a German dataset consisting of historical fairy tales and associated modern English summaries, and an English dataset consisting of historical short stories, fairy tales, and plays, including their associated modern German summaries. In addition, we create additional datasets using the collected texts: two cross-temporal summarization datasets (German and English) and one historical translation dataset containing historical German and the corresponding historical English translation. Texts are mainly retrieved from online text collections and archives such as DTA (Deutsches Textarchiv) and Wikisource. The summaries are retrieved from Wikipedia.

The datasets can ne found [here](https://drive.google.com/drive/folders/1MUaYjUfiThMX8H7HDJfpujikwmdku-7m?usp=sharing). 

## Models 
We experiment with following models: 
- [LED](https://huggingface.co/allenai/led-large-16384) using allenai/led-large-16384 with a maximum length of 8,192 
- mLED with a maximum length of 4,096
- [BigBird](https://huggingface.co/pszemraj/bigbird-pegasus-large-K-booksum) 
- [LongT5](https://huggingface.co/pszemraj/long-t5-tglobal-base-16384-book-summary) 

## mLED Creation 
We create a multilingual Longformer Encoder Decoder (mLED) using the published script from the [Longformer repository](https://github.com/allenai/longformer) and the [mBART-50](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt) model. 

The creation script can be found [here](https://github.com/jihedouni/CLCT/tree/master/models).

## Model finetuning
We follow different finetuning strategies: 
* Finetuning using only cross-lingual cross-temporal datasets 
* Intermediate task finetuning using monolingual and cross-lingual datasets

Model outputs can be found [here](https://drive.google.com/drive/folders/138bl4ELZU-Krp-nsChzDpY2vTsyJSWLf?usp=sharing). 


## Evaluation 

We use following metrics for the evaluation: 
* [ROUGE](https://pypi.org/project/rouge-score/): We calculate ROUGE-1, which computes the unigram overlap between the generated and reference summaries, and ROUGE-L, which computes the longest common subsequence between the two summaries.
* [BERTScore](https://github.com/Tiiiger/bert_score): We use the default models: "roberta-large" for English summaries and "bert-base-multilingual-cased"14 for German summaries. In addition, we use IDF-Weighting as recommended.
* [MoverScore](https://github.com/AIPHES/emnlp19-moverscore): We use "roberta-large" for the English summaries
and "xlm-roberta-large" for the German summaries.
* [BARTScore](https://github.com/neulab/BARTScore): We use "facebook/bart-large-cnn" for English summaries and "facebook/mbart-large-50-many-to-manymmt" for German summaries.
* [MENLI](https://github.com/cyr19/MENLI): We combine the NLI score with the BERTScore using an NLI-weight of 0.3. For NLI, we use entailment (e) as the formula for the score calculation. For the direction, we use the average between using the reference text as a hypothesis and using the generated text as a hypothesis.
* [SUPERT](https://github.com/Yale-LILY/SummEval/tree/master/evaluation/summ_eval): We use the cross-lingual model "xlm-r-bert-base-nli-stsb-mean-tokens" for the sentence Transformer.

We perfom a human evaluation (as used by [Fabbri et al. (2020)](https://arxiv.org/abs/2007.12626)). The results of the human evaluation can be found [here](https://drive.google.com/drive/folders/1MWvEuXcX9GTBPGgvjHcBRZu3ZnbMUC8Q?usp=sharing). 



Contact person: Jihed Ouni (jihed.ouni@stud.tu-darmstadt.de)
