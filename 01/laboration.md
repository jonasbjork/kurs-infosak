# Laboration 1 - Hotmodellering av AcmeShop AB

Arbeta två och två i 45 minuter. Laborationen avslutas med en gemensam redovisning.

Syftet med laborationen är att du ska träna på:
- Att identifiera tillgångar.
- Att se möjliga hot mot dessa.
- Att göra en enkel riskbedömning (låg/medel/hög).
- Att koppla riskerna till C, I eller A i CIA-triaden.

AcmeShop AB säljer kläder online:
- De har en webbshop i molnet.
- Kunddatabas med 200 000 kunder.
- Betalningar via extern betalningsleverantör.
- De har 15 anställda, varav tre jobbar med IT.
- Kontoret ligger i Stockholm.

## Lista de fem viktigaste tillgångarna

Exempel på typer av tillgångar (ni skall själva välja och formulera):
- Information (kunddata, orderdata, produktdata)
- System (webbshopen, e-postsystem, ekonomi- och lönesystem)
- Tjänster (att kunder kan beställa och betala)
- Fysiska tillgångar (kontor, datorer)
- Varumärke och rykte

Skriv en numrerad lista (1 till 5) med de tillgångar ni bedömer som viktigast för AcmeShop.

## Identifiera tre hot per tillgång

För varje tillgång:
1. Tänk: *Vad skulle kunna gå riktigt fel här?*
2. Formulera tre konkreta hot.

Exempel (som ni kan inspireras av):
- Kunddatabas:
	- Angripare stjäl hela kundregistret.
	- En anställd kopierar data och tar med den till en konkurrent.
	- Databasen raderas av misstag och backup fungerar inte.
- Webbshop:
	- Tjänsten ligger nere under Black Friday.
	- Webbplatsen blir utsatt för defacing (startsidans innehåll byts ut).
	- Angripare injicerar skadlig kod på sidan.

### Bedöm risk - låg/medel/hög

För varje hot:
- Diskutera hur sannolikt ni tror att det är.
- Diskutera hur stora konsekvenserna skulle bli för AcmeShop om det inträffar.
- Sätt en övergripande bedömning: Låg, Medel eller Hög.

> Det är bättre att motivera varför ni bedömer risken som medel än att gissa exakt.

Ni kan till exempel utgå från:
- **Låg**: Ovanligt och/eller små konsekvenser.
- **Medel**: Inte jättevanligt men kan hända, och/eller tydliga konsekvenser.
- **Hög**: Troligt eller mycket allvarliga konsekvenser om det händer.

## Koppla varje risk till C, I eller A

För varje hot:
- Fundera på vilken del av CIA-triaden som framförallt påverkas:
	- Konfidentialitet (C) - handlar det om att hemlig information läcker eller läses av fel person?
	- Riktighet (I) - handlar det om att information ändras eller blir felaktig?
	- Tillgänglighet (A) - handlar det om att något inte går att använda eller ligger nere?
- Skriv C, I eller A (eller flera om ni kan motivera det)

Exempel:
- Kunddatabas stjäls - Konfidentialitet (C).
- Webbshop nere under kampanj - Tillgänglighet (A).
- Orderbelopp ändras i systemet - Riktighet (I).

## Redovisning

1. Varje par väljer en tillgång och en risk att presentera.
2. Ni berättar om:
- Tillgången
- Hotet
- Er risknivå (låg/medel/hög) och motiveringen till varför
- Vilken del av CIA-triaden som påverkas mest

