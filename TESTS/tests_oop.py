import subprocess
from pathlib import Path
import time

res = []
topics = ['Abstraction', 'Encapsulation', 'Inheritance', 'Polymorphism']

print("\033[44m" + f"TESTING YOUR FILES...PLEASE WAIT" + "\033[0m\n")

abstraction = subprocess.run(
    ["python", str(Path(__file__).resolve().parent) + "/../7.python_oop/1.abstraction.py"], 
    capture_output=True, 
    text=True
)

abstractiono = abstraction.stdout
abstractione = abstraction.stderr

if not abstractione:
    res.append("t") if abstractiono.strip() == """Connected securely to Stripe API using secret tokens...\nStripe successfully charged: $50\nReceipt generated for $50\nYou have 2050.0 remaining""".strip() else res.append("f")
else:
    res.append("e")

encapsulation = subprocess.run(
    ["python", str(Path(__file__).resolve().parent) + "/../7.python_oop/2.encapsulation.py"], 
    capture_output=True, 
    text=True
)

encapsulationo = encapsulation.stdout
encapsulatione = encapsulation.stderr

if not encapsulatione:
    res.append("t") if encapsulationo.strip() == """5000.0\n7500.0\n0\nPublic key: vjti@123\nVault viewed/modified 5 times...""".strip() else res.append("f")
else:
    res.append("e")

inheritance = subprocess.run(
    ["python", str(Path(__file__).resolve().parent) + "/../7.python_oop/3.inheritance.py"], 
    capture_output=True, 
    text=True
)
#Hello
inheritanceo = inheritance.stdout
inheritancee = inheritance.stderr

if not inheritancee:
    res.append("t") if inheritanceo.strip() == """Hybrid systems active -> Electric silent start -> Turbo boost engaged -> Engine starting""".strip() else res.append("f")
else:
    res.append("e")

polymorphism = subprocess.run(
    ["python", str(Path(__file__).resolve().parent) + "/../7.python_oop/4.polymorphism.py"], 
    capture_output=True, 
    text=True
)

polymorphismo = polymorphism.stdout
polymorphisme = polymorphism.stderr

if not polymorphisme:
    res.append("t") if polymorphismo.strip() == """$1,500.00\n€120.00""".strip() else res.append("f")
else:
    res.append("e")

for i, r in enumerate(res):
    if r == "t":
        print("\033[42m" + f"{i+1}.{topics[i].upper()} TEST SUCCESSFULLY PASSED :)" + "\033[0m")
    elif r == "f":
        print("\033[41m" + f"{i+1}.{topics[i].upper()} GAVE WRONG ANSWER :(" + "\033[0m")
    elif r == "e":
        print("\033[41m" + f"{i+1}.{topics[i].upper()} THREW ERROR :(" + "\033[0m")
    time.sleep(0.7)