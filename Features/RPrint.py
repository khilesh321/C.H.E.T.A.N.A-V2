from rich import print

def rprint(text,color):
        print(" " * 100, end="\r", flush=True)
        print(f"[{color}]{text}[/{color}]",end="\r",flush=True)

