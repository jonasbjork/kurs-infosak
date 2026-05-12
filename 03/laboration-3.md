# Laboration: GRC-verktyg

> Den här laborationen kräver att du har Docker installerat på din dator.

GRC står för Governance, Risk and Compliance, på svenska ofta översatt till Styrning, Riskhantering och Regelefterlevnad. Ett GRC-verktyg är en mjukvaruplattform som hjälper organisationer att samla ihop, strukturera och automatisera arbetet med just dessa tre områden. Istället för att sprida ut policys, riskbedömningar, kontrollåtgärder och compliance-dokument i olika Excel-filer, Word-dokument och e-posttrådar, får allt en gemensam plats där informationen blir sökbar, spårbar och lätt att följa upp.

I ett GRC-verktyg kan man bland annat identifiera och värdera risker, koppla dem till lämpliga säkerhetskontroller, hantera policys och riktlinjer, följa upp åtgärdsplaner samt hantera revisioner och attestflöden. Verktyget underlättar också rapportering till ledning, revisorer och externa parter. Många GRC-plattformar har dessutom stöd för olika ramverk och standarder som ISO 27001, GDPR, NIST, SOC2 och NIS2.

Moderna organisationer möter idag allt fler krav från kunder, leverantörer, myndigheter och försäkringsbolag. Manuella metoder blir snabbt oöverskådliga och svåra att hålla uppdaterade. Ett bra GRC-verktyg ger därför bättre överblick, minskar risken för misstag, sparar tid och skapar de förutsättningar som behövs för ett systematiskt och kontinuerligt förbättringsarbete.

I den här laborationen kommer du att testa två populära open source GRC-verktyg: [Eramba](https://www.eramba.org) och [SimpleRisk](https://www.simplerisk.com). Båda kan köras enkelt via Docker, vilket gör det smidigt att installera och prova dem lokalt på din dator.

## Eramba

> Vill du bara se hur Eramba ser ut kan du kika på deras [demo](https://demo.cloud.eramba.org/).

```sh
git clone https://github.com/eramba/docker.git eramba-docker
cd eramba-docker
```

Du kan ändra lösenord för databasen i filen `.env` :

```txt
DB_PASSWORD=Your_DB_user_P@ssw0rd
MYSQL_ROOT_PASSWORD=Your_MysQl_ROOt_P@ssw0rd
```

Starta Eramba med:

```sh
docker compose -f docker-compose.simple-install.yml down
docker compose -f docker-compose.simple-install.yml up -d
```

Sedan öppnar du https://localhost:8443/ i din webbläsare. Det tar ett tag innan du kan nå sidan, så ha lite tålamod.

Väl inne ser du till att konfigurera Eramba. Du kommer få en kod till din e-postadress (som du registerar) så använd en riktig e-postadress.

Installationsbeskrivning finns [här](https://www.eramba.org/learning/courses/12/episodes/274).

## SimpleRisk

> Vill du bara se applikationen kan du kika på deras [demo](https://www.simplerisk.com/demo). Välj **Demo Option #3** så kommer du rakt in i applikationen.

Docker-applikationen fungerar bara på intel x86, inte på nya Mac (med Mx processor).

```sh
docker run -d -p 8080:80 --name simplerisk simplerisk/simplerisk
```

När den startat upp använder du din webbläsare och anger http://localhost:8080/ för att komma till applikationen.

