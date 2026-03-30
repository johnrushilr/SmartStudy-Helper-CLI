import re

def make_summary(text):

    if text.strip() == "":
        return "No content to summarize."

    sentences = re.split(r'[.!?]', text)
    words = text.lower().split()

    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    scores = {}

    for s in sentences:
        for w in s.lower().split():
            if w in freq:
                scores[s] = scores.get(s, 0) + freq[w]

    sorted_sents = sorted(scores, key=scores.get, reverse=True)

    return ". ".join(sorted_sents[:2])


def create_questions(text):

    if text.strip() == "":
        return []

    sentences = re.split(r'[.!?]', text)
    questions = []

    for s in sentences:
        words = s.strip().split()
        if len(words) > 5:
            q = "Explain: " + " ".join(words[:5]) + "..."
            questions.append(q)

    return questions[:3]