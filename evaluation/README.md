## Evaluation 

### Evaluation metrics

We use following metrics for the evaluation: 
* [ROUGE](https://pypi.org/project/rouge-score/): We calculate ROUGE-1, which computes the unigram overlap between the generated and reference summaries, and ROUGE-L, which computes the longest common subsequence between the two summaries.
* [BERTScore](https://github.com/Tiiiger/bert_score): We use the default models: "[roberta-large](https://huggingface.co/roberta-large)" for English summaries and "[bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased)" for German summaries. In addition, we use IDF-Weighting as recommended.
* [MoverScore](https://github.com/AIPHES/emnlp19-moverscore): We use "[roberta-large](https://huggingface.co/roberta-large)" for the English summaries
and "xlm-roberta-large" for the German summaries.
* [BARTScore](https://github.com/neulab/BARTScore): We use "[facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)" for English summaries and "[facebook/mbart-large-50-many-to-manymmt](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt)" for German summaries.
* [MENLI](https://github.com/cyr19/MENLI): We combine the NLI score with the BERTScore using an NLI-weight of 0.3. For NLI, we use entailment (e) as the formula for the score calculation. For the direction, we use the average between using the reference text as a hypothesis and using the generated text as a hypothesis.
* [SUPERT](https://github.com/Yale-LILY/SummEval/tree/master/evaluation/summ_eval): We use the cross-lingual model "[xlm-r-bert-base-nli-stsb-mean-tokens](https://huggingface.co/sentence-transformers/xlm-r-bert-base-nli-stsb-mean-tokens)" for the sentence Transformer.

### Human evaluation

We perfom a human evaluation (as used by [Fabbri et al. (2020)](https://arxiv.org/abs/2007.12626)). The results of the human evaluation can be found [here](https://drive.google.com/drive/folders/1MWvEuXcX9GTBPGgvjHcBRZu3ZnbMUC8Q?usp=sharing). 
