import re
import requests
import time
# Path to the CSS file
css_file_path = 'vendor/devicons/css/devicons.min.css'  # Replace with the path to your CSS file

# Function to read the CSS file and extract all font links
def extract_font_links(css_file_path):
    # Regular expression pattern for extracting font URLs
    font_url_pattern = re.compile(r'url\([\'"]?(../fonts/[^\'")]+)[\'"]?\)')


    # Read the CSS file
    with open(css_file_path, 'r', encoding='utf-8') as file:
        css_content = file.read()

    # Find all matches and return the list of links
    return font_url_pattern.findall(css_content)

font_links = extract_font_links(css_file_path)


def remove_after_question_mark(text):
    # Find the position of the "?" symbol
    question_mark_index = text.find('?')
    # If the "?" symbol is found, return the substring up to that point
    if question_mark_index != -1:
        return text[:question_mark_index]
    # If there is no "?" symbol, return the original text
    return text


def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


for link in font_links : 
    
    url = 'https://antoineauger.fr/vendor/devicons/'+link[2:]

    local_filename = 'vendor/devicons/fonts/'+remove_after_question_mark(link[9:])
    download_file(url, local_filename)
    time.sleep(0.5)

