from functools import lru_cache
from typing import List

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


@lru_cache(maxsize=1)
def get_section_embeddings(sections: tuple[str, ...]):
    return model.encode(sections)


def semantic_retrieve(
    query: str,
    knowledge_base: str,
    top_k: int = 2,
    threshold: float | None = 0.5,
) -> List[str]:
    sections = tuple(knowledge_base.split("\n\n"))

    query_embedding = model.encode([query])
    section_embeddings = get_section_embeddings(sections)

    similarities = cosine_similarity(
        query_embedding,
        section_embeddings,
    )[0]

    ranked_indices = similarities.argsort()[::-1]

    relevant_sections = [
        sections[index]
        for index in ranked_indices[:top_k]
        if threshold is None or similarities[index] >= threshold
    ]

    return relevant_sections
