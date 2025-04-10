from markdown_block import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split('\n')
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # read the markdown file and store contents in a variable
    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    # read the template file and store contents in a variable
    template_file = open(template_path, "r")
    template = template_file.read()
    # convert markdown to html
    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    # grab the title
    title = extract_title(markdown)
    # replace the title and content in the template
    # with the html and title generated
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    # write new full html page to the destination path
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    dest_file = open(dest_path, "w")
    dest_file.write(final_html)
    # close all files
    markdown_file.close()
    template_file.close()
    dest_file.close()
    print(f"Page generated at {dest_path}")