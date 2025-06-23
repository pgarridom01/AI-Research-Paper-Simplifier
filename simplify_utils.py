from langchain_helper import llm

# Safe token limit (approx) — adjust as needed
MAX_CHARS = 3000

def simplify_abstract(text):
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]

    prompt = f"Simplify this research paper text for a non-expert:\n\n{text}\n\nUse easy terms and break complex sentences."
    return llm.invoke(prompt).content.strip()


def extract_glossary(text):
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]

    prompt = f"Extract 5-10 key technical terms from this research paper and explain them in simple terms:\n\n{text}"
    return llm.invoke(prompt).content.strip()


def generate_flowchart(text):
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]

    prompt = f"""
    You are a research assistant. Convert the following research methodology into a step-by-step Mermaid.js compatible flowchart.

    Only output Mermaid markdown like:
    ```mermaid
    graph TD
    Step1 --> Step2
    Step2 --> Step3
    ```

    Research Methodology:
    \"\"\"
    {text}
    \"\"\"
    """
    return llm.invoke(prompt).content.strip()


def suggest_use_cases(text):
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]

    prompt = f"Suggest 3 practical use cases of the following research paper content:\n\n{text}"
    return llm.invoke(prompt).content.strip()


def answer_question(sections, query):
    context = "\n".join(sections.values())
    if len(context) > MAX_CHARS:
        context = context[:MAX_CHARS]

    prompt = f"You are a research assistant. Answer the following based on this paper:\n\nQuestion: {query}\n\nPaper:\n{context}"
    return llm.invoke(prompt).content.strip()
