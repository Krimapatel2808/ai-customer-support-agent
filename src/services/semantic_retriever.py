from typing import List

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_retrieve(
    query: str,
    knowledge_base: str,
    top_k: int = 2,
) -> List[str]:
    sections = knowledge_base.split("\n\n")

    query_embedding = model.encode([query])
    section_embeddings = model.encode(sections)

    similarities = cosine_similarity(
        query_embedding,
        section_embeddings,
    )[0]

    ranked_indices = similarities.argsort()[::-1]

    return [
        sections[index]
        for index in ranked_indices[:top_k]
    ]