import time
from rich import print

def print_time(text,color="#FF69B4",text2=""):
    print('C.H.E.T.A.N.A : ',end="")
    for i in text:
        print(f"[{color}]{i}[/{color}]",end="")
        time.sleep(0.05)
    print(f"{text2}\n\n")
if __name__ == "__main__":        
    print_time("Hello, sir how can I assist you?")
    # print_time("Hello, sir how can I assist you?")