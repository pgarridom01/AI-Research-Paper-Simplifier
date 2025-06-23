from langchain_helper import llm

def translate_text(text, language):
    if language == "English":
        return text
    prompt = f"Translate the following text to {language}:\n\n{text}"
    return llm.invoke(prompt).content.strip()
