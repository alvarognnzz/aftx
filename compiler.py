import sys
import os
import pdfkit


def compile_array(file):
    text = []
    f = open(file, "r")

    for line in f:
        if line.startswith("# "):
            text.append('<h1>{}</h1>'.format(line[2:].rstrip()))
        
        elif line.startswith("## "):
            text.append('<h2>{}</h2>'.format(line[3:].rstrip()))

        elif line.strip() != '':
            text.append('<p>{}</p>'.format(line.rstrip()))

    return text

def compile_text(array):
    return '\n'.join(array)

def exit_error(code):
    if code == 1:
        print("[ERROR] Please provide a file path as an argument.")
        sys.exit(1)

    elif code == 2:
        print("[ERROR] File type must be '.aftx'.")
        sys.exit(1)

    elif code == 3:
        print("[ERROR] File not found.")
        sys.exit(1)

    elif code == 4:
        print("[ERROR] Could not create PDF. Make sure you've installed wkhtmltopdf")
        sys.exit(1)

    else:
        print("[ERROR] Unknown exception")


def html_to_pdf(html_string, output_pdf):
    try:
        pdfkit.from_string(html_string, output_pdf, options={"enable-local-file-access": ""})
    except Exception as e:
        exit_error(4)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit_error(1)
    
    file_path = sys.argv[1]
    if not file_path.endswith(".aftx"):
        exit_error(2)

    if not os.path.exists(file_path):
        exit_error(3)
    
    compiled_array = compile_array(file_path)
    compiled_text = compile_text(compiled_array)

    with open("template.txt") as f:
        template = f.read()

    html_to_pdf(template.format(compiled_text), 'output.pdf')