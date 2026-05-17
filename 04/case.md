# Case: NordicShop AB, Organisationsbeskrivning

## Om NordicShop AB

NordicShop AB är ett svenskt e-handelsföretag grundat 2016 med huvudkontor i Göteborg. Företaget säljer hemelektronik och smart hemteknik till konsumenter i Sverige, Norge och Finland via sin webshop `nordicshop.se`. 

- **Anställda:** 65 personer (45 på kontoret, 20 i lager i Borås)
- **Omsättning:** ca 280 MSEK/år
- **Kundregister:** ca 180 000 registrerade kunder
- **Betalningar:** Klarna, Swish, kortbetalning via Stripe
- **IT-plattform:** Webshop byggd på Shopify och egen integrationsplattform i AWS
- **Interna system:** Microsoft 365, Fortnox (ekonomi), eget lagersystem i AWS

Företaget har börjat ta emot B2B-kunder (företagsorder) och en av deras största potentiella kunder, en nordisk bank, kräver ISO 27001-certifiering för att skriva avtal. VD har därför initierat ett certifieringsprojekt och anlitat er som konsulter för att göra en gap-analys som utgångspunkt.

## IT-organisation och rutiner (resultat av era intervjuer)

### Personal och ansvar

- **IT-chef:** Markus (började för 4 månader sedan). Rapporterar till CFO.
- **Systemadministratör:** Erik, senior. Har varit på NordicShop sedan starten.
- **Utvecklare:** 3 personer, jobbar mot integrationsplattformen.
- **Ingen dedikerad säkerhetsroll.** Markus "har hand om säkerheten" vid sidan av sitt ordinarie jobb som IT-chef.
- **Ingen DPO** - "vi har pratat med en jurist en gång"

### Dokumentation

- Det finns en "IT-policy" från 2019 på två sidor. Markus har inte hunnit läsa den.
- Ingen informationssäkerhetspolicy.
- Ingen klassificering av information.
- Det finns en tillgångsförteckning i Excel, senast uppdaterad 2022. Erik underhåller den "när han kommer ihåg".
- Ingen formell riskanalys har gjorts.

### Åtkomst och identitet

- Alla anställda har Microsoft 365-konto. MFA är påslaget sedan 2023 för alla utom tre personer (inklusive en av utvecklarna) som "klagade så mycket".
- Admin-åtkomst till AWS delas mellan IT-chef, systemadministratör och två utvecklare via ett gemensamt konto.
- När en anställd slutar skickar HR ett mejl till IT "inom någon vecka". Ibland glöms det.
- Ingen har gjort en formell åtkomstgenomgång de senaste 18 månaderna.

### Backup och kontinuitet

- AWS-miljön backas upp dagligen till en separat AWS-region.
- Fortnox backas upp av leverantören (antar man).
- Återställning från backup har aldrig testats. Erik säger att "det borde funka".
- Ingen kontinuitetsplan eller katastrofplan finns dokumenterad.

### Säkerhetsåtgärder

- Brandvägg i AWS, standardkonfiguration från deras konsult som var inne år 2020.
- Antivirus (Microsoft Defender) är installerat på alla Windows-datorer.
- Patchning av servrar sker "när det passar", ungefär kvartalsvis.
- Arbetsstationer patchas automatiskt via Microsoft Intune.
- Inga regelbundna sårbarhetsskanningar.
- Ett penetrationstest gjordes 2021 — rapporten finns men de flesta fynd är inte åtgärdade.

### Incidenthantering

- Ingen formell incidenthanteringsplan.
- "Om något händer ringer vi Markus."
- En incident 2023 där 500 kunduppgifter läckte via en felkonfigurerad S3-bucket hanterades - men ingen analys dokumenterades efteråt.

### Leverantörer

- Viktiga leverantörer: Shopify, AWS, Stripe, Klarna, Fortnox, en städfirma med nyckelkort till kontoret.
- Inga leverantörsriskbedömningar har gjorts.
- Avtal finns med de flesta, men ingen har läst säkerhetsbilagorna.

### Utbildning

- En GDPR-webbkurs 2022 som alla skulle gå igenom. Cirka 60% slutförde den.
- Ingen återkommande utbildning i informationssäkerhet.
- Ingen phishing-övning har gjorts.

### Fysisk säkerhet

- Kontoret har kodlås och nyckelkort. Besökare skriver in sig i en pärm i receptionen.
- Serverrum finns inte — allt är i molnet.
- Lagret i Borås har kameror och larm.
