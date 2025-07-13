from textnode import TextNode
import os, shutil
from markdown_to_htmlnode import markdown_to_html_node
from pathlib import Path
def main():
    copy_content_from_static_to_public(
        '/Users/rohitbhatia/Static-Site-Generator/static',
        '/Users/rohitbhatia/Static-Site-Generator/public'
    )
    generate_pages_recursive("content", "template.html", "public")

def copy_content_from_static_to_public(source_path, destination_path):
    source_path = os.path.abspath(source_path)
    destination_path = os.path.abspath(destination_path)

    if not os.path.exists(source_path):
        raise ValueError("Invalid source_path")
    if not os.path.exists(destination_path):
        raise ValueError("Invalid destination path")

    shutil.rmtree(destination_path)
    os.makedirs(destination_path, exist_ok=True)

    def copy_recursive(src, dst):
        for item in os.listdir(src):
            src_item = os.path.join(src, item)
            dst_item = os.path.join(dst, item)
            if os.path.isdir(src_item):
                os.makedirs(dst_item, exist_ok=True)
                copy_recursive(src_item, dst_item)
            else:
                shutil.copy2(src_item, dst_item)

    copy_recursive(source_path, destination_path)

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path,dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

if __name__ == "__main__":
    main()
