from typing import Optional

import torch
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

from ..utils import set_device
from ..embedder import STEmbedder, HFEmbedder


class Mbedder:
    def __init__(self, text: list[str], dev: Optional[str] = None) -> None:
        self.text = text
        self.embeddings = None
        self.labels = None
        self.dev = set_device(dev)

    def embed(self, model):
        if isinstance(model, SentenceTransformer):
            emb = STEmbedder(model, self.text)
        elif False:#isinstance(model, SentenceTransformer):
            return HFEmbedder
        else:
            raise NotImplementedError
        
        embeddings = self._batch_embed(emb)
        return embeddings
        

    def _batch_embed(self, embedder, batch_size=256):
        embeddings = []
        for i in tqdm(range(0, len(embedder.text), batch_size), leave=False):
            batch = embedder.text[i:i+batch_size]
            embeddings.append(embedder(batch))

        embeddings = torch.cat(embeddings, dim=0)
        
        if self.dev.type == "mps":
            torch.mps.empty_cache()
        if self.dev.type == "cuda":
            torch.cuda.empty_cache()
        return embeddings
