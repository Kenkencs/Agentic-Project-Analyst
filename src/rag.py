from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")

chunks = [
    "Students complain that their daily study plans contain too many tasks.",
    "Users like receiving weekly learning reports.",
    "Some students want unfinished tasks to automatically move to another day.",
    "Notifications are too frequent and distracting.",
    "Students find it difficult to manage more than three subjects in one day.",
    "Users want workload to be automatically balanced across the week.",
]

chunk_embeddings = model.encode(chunks)


def retrieve(
    query: str,
    top_k: int = 3,
    threshold: float = 0.4,
) -> list[str]:

    query_embedding = model.encode(query)

    scores = cos_sim(
        query_embedding,
        chunk_embeddings,
    )[0]

    top_results = scores.argsort(descending=True)[:top_k]

    results = []

    for index in top_results:
        score = scores[index].item()

        if score >= threshold:
            results.append(chunks[index])

    return results