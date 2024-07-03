from typing import Union, Optional

from .embedder import Embedder

class STEmbedder(Embedder):
    def __init__(self, model) -> None:
        super().__init__(model)

    def embed(self, txt: Union[list[str], str], batch_size: Optional[int] = 256):
        return self.model.encode(txt, batch_size=batch_size, convert_to_tensor=True)