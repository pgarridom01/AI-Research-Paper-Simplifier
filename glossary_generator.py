from langchain_helper import llm
import re


def extract_keywords(text, num_keywords=10):
    # Simple regex-based keyword extraction (can be improved later)
    words = re.findall(r'\b[A-Za-z]{6,}\b', text)
    freq = {}
    for word in words:
        word_lower = word.lower()
        freq[word_lower] = freq.get(word_lower, 0) + 1

    # Sort by frequency and return top N unique keywords
    sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    unique_keywords = []
    for word, _ in sorted_keywords:
        if word not in unique_keywords:
            unique_keywords.append(word)
        if len(unique_keywords) >= num_keywords:
            break
    return unique_keywords


def generate_glossary(text, num_terms=10, language="English"):
    keywords = extract_keywords(text, num_terms)
    keyword_list = ", ".join(keywords)

    prompt = f"""
    You're an AI tutor. Simplify and explain each of the following technical terms for a student:

    Terms: {keyword_list}

    Format:
    Term: Definition (in {language})

    Keep the explanations very easy to understand.
    """
    response = llm.invoke(prompt)
    return response.content.strip()
