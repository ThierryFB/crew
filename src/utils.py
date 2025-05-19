import os


def save_markdown_to_file(content, filepath):
    """Save markdown content to a file, creating directories if needed."""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
