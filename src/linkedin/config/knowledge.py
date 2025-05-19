import os
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource


def get_knowledge_sources():
    """
    Reads all text files from the ./knowledge directory and creates StringKnowledgeSources.
    Returns a Knowledge object containing all sources.
    """
    # Create knowledge sources list
    knowledge_sources = []

    knowledge_dir = "./knowledge"

    # Read all text files from the knowledge directory
    text_files = [f for f in os.listdir(knowledge_dir) if f.endswith(".txt")]
    # Load each text file's content as a knowledge source
    file_paths = []
    for file_name in text_files:
        print(f"Added {file_name} as knowledge source")
        file_paths.append(file_name)
    text_sources = TextFileKnowledgeSource(file_paths=file_paths)
    knowledge_sources.append(text_sources)

    pdf_files = [f for f in os.listdir(knowledge_dir) if f.endswith(".pdf")]

    # Load each pdf file's content as a knowledge source
    file_paths = []
    for file_name in pdf_files:
        print(f"Added {file_name} as knowledge source")
        file_paths.append(file_name)

    pdf_sources = PDFKnowledgeSource(file_paths=file_paths)
    knowledge_sources.append(pdf_sources)
    # Create a Knowledge object with all sources
    return knowledge_sources
