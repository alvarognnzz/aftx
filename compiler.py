import sys

def compile_array(file):
    text = []
    f = open(file, "r")

    for line in f:
        if line.startswith("# "):
            text.append("<h1>" + line[2:].rstrip() + "</h1>")
        
        elif line.startswith("## "):
            text.append("<h2>" + line[3:].rstrip() + "</h2>")

        elif line.strip() != '':
            text.append(line.rstrip())

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