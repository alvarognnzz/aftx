import sys

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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[ERROR] Please provide a file path as an argument.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    compiled_array = compile_array(file_path)
    compiled_text = compile_text(compiled_array)
    print(compiled_text)