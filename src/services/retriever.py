from typing import List


def retrieve(query: str, knowledge_base: str, top_k: int = 2) -> List[str]:
    sections = knowledge_base.split("\n\n")

    query_words = set(query.lower().split())

    scored_sections = []

    for section in sections:
        section_words = set(section.lower().split())
        score = len(query_words & section_words)

        if score > 0:
            scored_sections.append((score, section))

    scored_sections.sort(reverse=True, key=lambda item: item[0])

    return [section for _, section in scored_sections[:top_k]]
