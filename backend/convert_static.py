from pathlib import Path
import re

fichier = Path("templates/rentaly/index.html")

html = fichier.read_text(encoding="utf-8")

# Images
html = re.sub(
    r'(?<=src=")images/(.*?)(?=")',
    r"{% static 'images/\1' %}",
    html
)

# Javascript
html = re.sub(
    r'(?<=src=")js/(.*?)(?=")',
    r"{% static 'js/\1' %}",
    html
)

# CSS
html = re.sub(
    r'(?<=href=")css/(.*?)(?=")',
    r"{% static 'css/\1' %}",
    html
)

# Fonts
html = re.sub(
    r'(?<=href=")fonts/(.*?)(?=")',
    r"{% static 'fonts/\1' %}",
    html
)

fichier.write_text(html, encoding="utf-8")

print("Conversion terminée.")