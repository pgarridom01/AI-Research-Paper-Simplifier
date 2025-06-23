import fitz  # PyMuPDF

def extract_text_sections(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    full_text = "\n".join([page.get_text() for page in doc])
    sections = {
        "Abstract": "",
        "Introduction": "",
        "Methodology": "",
        "Results": "",
        "Conclusion": ""
    }

    current_section = None
    for line in full_text.split("\n"):
        line_lower = line.lower()
        if "abstract" in line_lower:
            current_section = "Abstract"
        elif "introduction" in line_lower:
            current_section = "Introduction"
        elif "methodology" in line_lower or "methods" in line_lower:
            current_section = "Methodology"
        elif "results" in line_lower:
            current_section = "Results"
        elif "conclusion" in line_lower:
            current_section = "Conclusion"

        if current_section:
            sections[current_section] += line + "\n"

    return sections
