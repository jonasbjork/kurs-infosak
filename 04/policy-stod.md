# Principer för en informationssäkerhetspolicy

Det här dokumentet förklarar vanliga principer som bör finnas med i en informationssäkerhetspolicy. Använd det som uppslagsverk medan ni skriver er policy för NordicShop AB.

## Vad är en princip i det här sammanhanget?

En princip är en grundregel som styr hur organisationen tänker kring och hanterar informationssäkerhet. Principerna ska vara tillräckligt konkreta för att vägleda beslut i vardagen, men tillräckligt generella för att gälla hela organisationen. En bra princip går att svara ja eller nej på: *Följer vi den här principen i det vi gör just nu?*

Principerna i er policy ska fungera som ett *ramverk* — de talar om **vad** som gäller, medan rutiner och instruktioner (som är separata dokument) talar om **hur**.

## CIA-triaden - de tre grundpelarna

Dessa tre är obligatoriska i varje informationssäkerhetspolicy. De kommer från ISO 27000 och utgör själva definitionen av informationssäkerhet.

### Konfidentialitet (Confidentiality)

Information ska bara vara tillgänglig för dem som har rätt att ta del av den. Det innebär att organisationen aktivt begränsar åtkomst baserat på behov och roll, och att känslig information skyddas mot obehörig insyn, både tekniskt och organisatoriskt.

**Exempel:** Kundernas betaluppgifter hos NordicShop ska inte vara tillgängliga för lagerpersonal. En utvecklare behöver inte åtkomst till HR-avdelningens lönesystem.

### Integritet (Integrity)

Information ska vara korrekt, fullständig och skyddad mot obehörig eller oavsiktlig förändring. Det handlar inte bara om att data inte ska manipuleras av en angripare — det handlar lika mycket om att förhindra att någon råkar skriva över eller radera data av misstag.

**Exempel:** En order i lagersystemet ska inte kunna ändras utan att det loggas vem som ändrade, vad som ändrades och när det ändrades.

### Tillgänglighet (Availability)

Information och system ska vara tillgängliga när de behövs. Det innebär att organisationen planerar för driftstörningar, har backup-rutiner och vet hur lång tid det får ta att återställa verksamheten efter en incident.

**Exempel:** NordicShops webshop måste vara tillgänglig under Black Friday. Ett avbrott på en timme kan kosta hundratusentals kronor.

## Ytterligare principer att välja bland

Ni ska välja **minst fem** av principerna nedan (eller formulera egna). Välj de som passar NordicShops verksamhet och situation bäst.

### 1. Behov av att veta (Need to know)

Åtkomst till information ges bara till den som behöver den för att utföra sitt arbete. Principen kompletterar konfidentialitet med ett praktiskt beslutskriterium: frågan är inte "kan den här personen vara betrodd?" utan "behöver den här personen informationen just nu för att kunna utföra sitt arbete?"

**Koppling till ISO 27001:** Kontroll 5.10 (Acceptable use of information), 8.3 (Information access restriction).

### 2. Minsta möjliga behörighet (Least privilege)

Användare, system och processer ska ha så lite behörighet som möjligt för att utföra sin uppgift. Om en utvecklare bara behöver läsa en databas ska kontot inte ha skrivrättigheter. Om en administratör bara behöver hantera e-postkonton ska kontot inte vara domänadmin.

Den här principen minskar skadan vid en incident: om ett konto komprometteras kan angriparen bara göra det som kontot hade rätt att göra.

**Tänk på NordicShop:** Det delade admin-kontot i AWS bryter direkt mot den här principen.

### 3. Defense in depth

Organisationen förlitar sig inte på en enda skyddsåtgärd utan bygger flera lager av skydd. Om brandväggen missar ett intrång finns det loggning som upptäcker det. Om loggningen missar finns det segmenterat nätverk som begränsar skadan. Om segmenteringen missar finns det backup som möjliggör återställning.

Tanken är att varje enskilt lager kan misslyckas - men sannolikheten att *alla* lager misslyckas samtidigt är mycket lägre.

### 4. Informationsklassificering

All information ska klassificeras efter sitt skyddsvärde och hanteras i enlighet med sin klassificering. Vanliga klasser är:

- **Öppen** - kan delas fritt (marknadsföringsmaterial, publika priser)
- **Intern** - inte hemlig men inte avsedd för allmänheten (mötesprotokoll)
- **Konfidentiell** - kan skada organisationen om den sprids (affärsplaner, kunddata)
- **Hemlig/strikt konfidentiell** — allvarlig skada om den sprids (löneuppgifter, känsliga personuppgifter)

Klassificeringen avgör vilka skyddsåtgärder som krävs: kryptering, åtkomstkontroll, lagringsregler med mera.

### 5. Ansvar och ägarskap (Accountability)

All information och alla system ska ha en utsedd ägare som ansvarar för klassificering, skydd och uppföljning. *Alla ansvarar* betyder i verkligheten att ingen ansvarar. Ägarskap ska vara personligt - inte kopplat till en avdelning eller en roll utan till en namngiven person.

### 6. Medvetenhet och utbildning (Awareness)

Informationssäkerhet är inte bara en teknisk fråga utan i hög grad en mänsklig fråga. Alla medarbetare ska ha den kunskap de behöver för att fatta säkra beslut i sin vardag. Det innebär regelbunden utbildning, inte bara ett engångstillfälle vid anställning.

**Tänk på NordicShop:** 40% av personalen genomförde aldrig GDPR-kursen 2022. Ingen phishing-övning har genomförts.

### 7. Incidentberedskap

Organisationen ska vara förberedd på att säkerhetsincidenter inträffar. Det innebär dokumenterade processer för att upptäcka, rapportera, hantera och lära sig av incidenter. "Ring Markus" är inte en incidenthanteringsplan.

### 8. Kontinuitet och återställning

Organisationen ska kunna fortsätta sin verksamhet även vid allvarliga störningar, och kunna återställa kritiska system inom definierade tidsramar. Det kräver att man vet vilka system som är kritiska, hur lång tid man klarar sig utan dem, och att man testar sina planer regelbundet.

### 9. Leverantörssäkerhet

Organisationens säkerhet är aldrig starkare än den svagaste leverantörens. Alla leverantörer som hanterar organisationens information eller har åtkomst till dess system ska riskbedömas, och avtal ska innehålla säkerhetskrav.

**Tänk på NordicShop:** Städfirman har nyckelkort till kontoret. Ingen leverantörsriskbedömning har gjorts.

### 10. Efterlevnad och regelefterlevnad (Compliance)

Organisationen ska följa tillämpliga lagar, förordningar, standarder och avtalskrav. Det gäller bland annat GDPR, PCI DSS (eftersom NordicShop hanterar kortbetalningar via Stripe) och eventuellt NIS2 beroende på sektorsklassificering. Efterlevnad ska inte vara en engångsaktivitet utan en löpande process.

### 11. Spårbarhet (Traceability)

Händelser i system och processer ska kunna spåras tillbaka till en specifik person, tidpunkt och handling. Det kräver loggning, tidsstämplar och individuella konton. Delade konton bryter mot den här principen direkt.

### 12. Säkerhet som en del av verksamheten

Informationssäkerhet ska inte vara ett separat "IT-projekt" utan en integrerad del av hela verksamheten. Säkerhetsfrågor ska beaktas vid alla beslut — inte bara tekniska utan även affärsmässiga, organisatoriska och personalrelaterade.

## Tips för er policy

- **Välj de principer som är mest relevanta för NordicShop.** Ni behöver inte ta med alla - det är bättre med åtta väl valda principer som ni kan motivera än tolv generella.
- **Skriv kort och tydligt.** Varje princip bör kunna formuleras i två, tre, meningar i policyn. Förklaringar och detaljer hör hemma i rutindokument, inte i policyn.
- **Tänk på läsaren.** Policyn ska kunna förstås av en nyanställd lagerarbetare i Borås, inte bara av IT-avdelningen.
- **Koppla till verkligheten.** De principer ni väljer ska adressera *verkliga problem*.

