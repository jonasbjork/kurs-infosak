import hashlib
import hmac
import secrets

# DÅLIGT: ren hash av personnummer
def dalig_pseudonymisering(pnr: str) -> str:
    return hashlib.sha256(pnr.encode()).hexdigest()

# BÄTTRE: HMAC med hemlig nyckel
NYCKEL = secrets.token_bytes(32)  # lagras separat!
def battre_pseudonymisering(pnr: str) -> str:
    return hmac.new(NYCKEL, pnr.encode(), hashlib.sha256).hexdigest()

persnr = "121212-1212"
print(f"Mitt personnummer är {persnr}")
pseudo = dalig_pseudonymisering(persnr)
print(f"Dålig pseudonymisering ger:\n{pseudo}")
pseudo2 = dalig_pseudonymisering(persnr)
print(f"Om jag nu gissar {persnr} och kör genom dålig pseudo igen får jag\n{pseudo2}")
print("Alltså samma")
print("Så genom att gissa personnummer och använda samma algoritm kan jag")
print("återskapa det personnummer som är lagrat. Det tar bara lite tid.")
print("När min hash är samma som den lagrade hashen har jag hittat rätt.")
print("-----")
print("Vi har en NYCKEL och använder battre_pseudonymisering()")
battre = battre_pseudonymisering(persnr)
print(f"- Personnummer {persnr} ger oss {battre}")
save_me = NYCKEL
NYCKEL = secrets.token_bytes(32)
battre2 = battre_pseudonymisering(persnr)
print("Vi byter NYCKEL till en ny nyckel")
print("- Och sedan kör vi battre_pseudonymisering(persnr) igen")
print(f"- Nu är vår hash: {battre2}")
print("Så med en annan nyckel kommer vår hash se annorlunda ut")
print("Men om vi får tag rätt nyckel, och gissar rätt personnummer")
print("Kommer vi kunna ta reda på personnumret igen")
print("Vi byter NYCKEL till den gamla nyckeln")
NYCKEL = save_me
battre3 = battre_pseudonymisering(persnr)
print("- Och sedan kör vi battre_pseudonymisering(persnr) igen")
print(f"- Nu är vår hash: {battre3}")
print("- Alltså samma hash som tidigare, eftersom vi har samma nyckel.")

# Notera också att nyckeln ändras varje gång du kör skriptet
# så hash blir olika för varje gång det körs.

# Diskussionsfrågor:
# 1. Varför är den första metoden osäker för personnummer?
#    Ledtråd: hur många giltiga personnummer finns det?
#    Kan du bygga en regnbågstabell?
# 2. Är HMAC-versionen anonymisering eller pseudonymisering enligt GDPR?
# 3. Vad händer med skyddet om nyckeln läcker?

