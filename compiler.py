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
