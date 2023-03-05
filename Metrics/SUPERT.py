import os
import sys
import csv
import re
import torch
import pandas as pd
import numpy as np
import nltk

device = "cuda:0" if torch.cuda.is_available() else "cpu"
csv.field_size_limit(sys.maxsize)

print("device:", device)

os.environ["TOKENIZERS_PARALLELISM"] = "false"

import os
from collections import Counter
from nltk.tokenize import sent_tokenize
import gin
from summ_eval import sentence_transformers
from summ_eval.sentence_transformers import SentenceTransformer
from summ_eval.metric import Metric
from summ_eval.supert_utils import parse_documents, get_all_token_vecs, build_pseudo_ref, get_sbert_score, get_token_vecs
 
from summ_eval import sentence_transformers

class SupertMetric(Metric):
    def __init__(self, ref_metric='top15', sim_metric='f1'):
        self.bert_model = SentenceTransformer("https://huggingface.co/sentence-transformers/xlm-r-bert-base-nli-stsb-mean-tokens") #"bert-base-nli-stsb-mean-tokens", 
        self.ref_metric = ref_metric
        self.sim_metric = sim_metric

    def evaluate_example(self, summary, input_text):
        # if input is not a sent-tokenized list
        if not isinstance(input_text, list):
            input_text_sents = sent_tokenize(input_text)
        else:
            input_text_sents = input_text
        docs = [("DOC0", input_text_sents)]
        sent_info_dic, _, sents_weights = parse_documents(docs, None, self.ref_metric)

        all_token_vecs, all_tokens = get_all_token_vecs(self.bert_model, sent_info_dic)
        ref_vecs, _ = build_pseudo_ref(sent_info_dic, sents_weights, all_tokens, all_token_vecs)

        summ_vecs = []
        summ_tokens = []
        vv, tt = get_token_vecs(self.bert_model, sent_tokenize(summary))
        summ_vecs.append(vv)
        summ_tokens.append(tt)
        scores = get_sbert_score(ref_vecs, summ_vecs, self.sim_metric)[0]
        return {"supert": scores}

    def evaluate_batch(self, summaries, input_texts, aggregate=True):
        corpus_score_dict = Counter()
        results = []
        for summ, input_text in zip(summaries, input_texts):
            results.append(self.evaluate_example(summ, input_text))
        if aggregate:
            [corpus_score_dict.update(x) for x in results]
            for key in corpus_score_dict.keys():
                corpus_score_dict[key] /= float(len(input_texts))
            return corpus_score_dict
        else:
            return results

    @property
    def supports_multi_ref(self):
        return False






