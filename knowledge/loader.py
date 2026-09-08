def load_md(path):
    with open(path,"r",encoding="utf-8") as f:
        md = f.read()
        return md