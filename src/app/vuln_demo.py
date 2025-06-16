# src/app/vuln_demo.py
def dangerous(user_input: str):
    # ❗ Uso de eval: Bandit lo reporta como High severity (B307)
    eval("print(" + user_input + ")")
