from markdown_block import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # read the markdown file and store contents in a variable
    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    markdown_file.close()
    # read the template file and store contents in a variable
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    # convert markdown to html
    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    # grab the title
    title = extract_title(markdown)
    # replace the title and content in the template
    # with the html and title generated
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
     # Now replace URLs with the basepath
    final_html = final_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    # write new full html page to the destination path
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    dest_file = open(dest_path, "w")
    dest_file.write(final_html)
    dest_file.close()
    print(f"Page generated at {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # process each item in the content directory
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        print(f"Generating page from {src_path} to {dest_path} using {template_path}")
        # check if it's a file
        if os.path.isfile(src_path) and src_path.endswith(".md"):
            # Convert .md to .html in the destination path
            html_dest_path = dest_path.replace(".md", ".html")
            generate_page(src_path, template_path, html_dest_path, basepath)
        elif not os.path.isfile(src_path):
            # If it's a directory, create it and call recursively
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(src_path, template_path, dest_path, basepath)