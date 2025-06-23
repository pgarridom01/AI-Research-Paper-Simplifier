import streamlit as st
from paper_parser import extract_text_sections
from simplify_utils import (
    simplify_abstract,
    extract_glossary,
    generate_flowchart,
    suggest_use_cases,
    answer_question,
)
from langchain_helper import llm
from translator import translate_text

st.set_page_config(page_title="📄 AI Research Paper Simplifier", layout="wide")
st.title("📄🤖AI Research Paper Simplifier")

uploaded_file = st.file_uploader("Upload a research paper (PDF)", type=["pdf"])
language = st.selectbox("🌐 Output Language", ["English", "Hindi", "French"])

qa_query = st.text_input("❓ Ask a custom question about the paper")

translated = ""
report_parts = []
sections = {}

if uploaded_file:
    with st.spinner("🔍 Extracting paper sections..."):
        sections = extract_text_sections(uploaded_file)

    full_text = "\n".join(sections.values())

    if st.button("🧠 Simplify Paper"):
        simplified = simplify_abstract(full_text)
        translated = translate_text(simplified, language)
        st.subheader("🧠 Simplified Paper")
        st.markdown(translated)
        report_parts.append(f"🧠 Simplified Paper:\n\n{translated}\n")

    if st.button("📘 Generate Glossary"):
        glossary_input = sections.get("Introduction", "") + sections.get("Methodology", "")
        glossary = extract_glossary(glossary_input)
        translated = translate_text(glossary, language)
        st.subheader("📘 Glossary of Terms")
        st.markdown(translated)
        report_parts.append(f"📘 Glossary:\n\n{translated}\n")

    if st.button("🧭 Generate Flowchart"):
        flowchart_input = sections.get("Methodology", "")
        flowchart_md = generate_flowchart(flowchart_input)
        st.subheader("🧭 Flowchart (Markdown)")
        st.markdown("```mermaid\n" + flowchart_md + "\n```")
        report_parts.append(f"🧭 Flowchart:\n\n```mermaid\n{flowchart_md}\n```\n")

    if st.button("🎯 Use Case Generator"):
        usecase_input = sections.get("Conclusion", "")
        usecases = suggest_use_cases(usecase_input)
        translated = translate_text(usecases, language)
        st.subheader("🎯 Possible Use Cases")
        st.markdown(translated)
        report_parts.append(f"🎯 Use Cases:\n\n{translated}\n")

    # Q&A block (show immediately after question input)
    if qa_query.strip():
        with st.spinner("💬 Generating answer..."):
            answer = answer_question(sections, qa_query)
            translated = translate_text(answer, language)
            st.subheader("💬 Answer to your question")
            st.markdown(translated)
            report_parts.append(f"❓Q: {qa_query}\n\n💡A: {translated}\n")

    if report_parts:
        full_report = "\n\n".join(report_parts)
        st.download_button("📥 Download Simplified Report", full_report, file_name="simplified_report.txt")
