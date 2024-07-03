from .embedder import Embedder


class HFEmbedder(Embedder):
    def __init__(self) -> None:
        super().__init__()

    def embed(self, txt):
        return super().embed(txt)