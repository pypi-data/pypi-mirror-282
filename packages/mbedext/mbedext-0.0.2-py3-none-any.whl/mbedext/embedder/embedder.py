from abc import ABC, abstractmethod


class Embedder:
    def __init__(self, model, text) -> None:
        self.model = model
        self.text = text

    @abstractmethod
    def embed(self, txt):
        raise NotImplementedError