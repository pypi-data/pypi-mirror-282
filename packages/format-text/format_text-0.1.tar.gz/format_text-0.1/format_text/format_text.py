import re

def format_for_notes(input_text):
    # Remove leading numbering or bullet points
    formatted_text = re.sub(r'^[0-9]*[.)]*\s*', '', input_text, flags=re.MULTILINE)
    
    # Convert and remove specific Markdown syntax
    formatted_text = re.sub(r'###*\s', '\n\n', formatted_text)  # Removes any number of '#' followed by space
    formatted_text = re.sub(r'\*\*', '', formatted_text)
    
    # Add a blank line between distinct groups (headings and paragraphs)
    formatted_text = re.sub(r'(\n\n.+?)\n(- )', r'\1\n\n\2', formatted_text, flags=re.DOTALL)
    
    return formatted_text
