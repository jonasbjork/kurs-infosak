# 06 - Personlig integritet och etik

## Laboration: DPIA

Laborationen finns i [DPIA-laboration.md](DPIA-laboration.md) och mallen ni skall fylla i heter [DPIA-mall.md](DPIA-mall.md).

## Laboration: Granska en verklig integritetspolicy

[laboration.md](laboration.md) handlar om att du skall granska en verklig integritetspolicy.

## Python: pseudonymisering och anonymisering

> Detta är en bonus, programmet är snabbt ihopknappat för att visa hur lagring av persondata kan se ut.

Filen [pseudonymisering.py](pseudonymisering.py) visar hur svårt det är att anonymisera persondata som personnummer på ett bra sätt.

Programmet är skrivet i Python och består av två funktioner:

```python
def dalig_pseudonymisering(pnr: str) -> str:
    return hashlib.sha256(pnr.encode()).hexdigest()

NYCKEL = secrets.token_bytes(32)
def battre_pseudonymisering(pnr: str) -> str:
    return hmac.new(NYCKEL, pnr.encode(), hashlib.sha256).hexdigest()
```

Funktionen `dalig_pseudonymisering()` tar emot personnumret och skapar samma hash varje gång. Skickar du in `121212-1212` får du tillbaka `92a763a0ab7ef9acbf84540e7fdeaa83345716fe23fe8df3c934c576ccc642c9`. När du skickar in `121212-1212` en gång till får du tillbaka samma hash. Varje gång.

Funktionen `battre_pseudonymisering()` använder en nyckel också, vilket gör att det blir svårare att gissa vilket personnummer det är - eftersom vi behöver ha korrekt nyckel också.

För att testa programmet behöver du ha Python installerat, sedan kör du det med:

```sh
python3 pseudonymisering.py
```

Läs koden, så ser du lite frågor i slutet också.

