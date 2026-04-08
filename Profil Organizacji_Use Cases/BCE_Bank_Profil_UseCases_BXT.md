**BCE BANK S.A.**

Profil Organizacji | Use Cases AI (BXT Framework)

Transformacja Cyfrowa — Wdrożenie 3 Agentów AI

|  |  |  |
| --- | --- | --- |
| Wersja  **1.0 — Final Draft** | Data  **Marzec 2026** | Klasyfikacja  **POUFNE** |

<!-- TOC START -->
## Spis Treści
- [1. PROFIL ORGANIZACJI — BCE Bank S.A.](#sec-1-profil-organizacji-bce-bank-sa)
  - [1.1 Charakterystyka organizacji](#sec-11-charakterystyka-organizacji)
  - [1.2 Kluczowe wyzwania — stan AS-IS](#sec-12-kluczowe-wyzwania-stan-as-is)
  - [1.3 Dlaczego BCE Bank wdraża AI — uzasadnienie transformacji](#sec-13-dlaczego-bce-bank-wdraza-ai-uzasadnienie-transformacji)
  - [1.4 Cele strategiczne (OKR — horyzont 24 miesięcy)](#sec-14-cele-strategiczne-okr-horyzont-24-miesiecy)
- [2. METODOLOGIA BXT — PRE-WORKSHOP ASSESSMENT](#sec-2-metodologia-bxt-pre-workshop-assessment)
- [3. USE CASE #01 — Product Catalogue Assistant (Chatbot / Voicebot)](#sec-3-use-case-01-product-catalogue-assistant-chatbot-voicebot)
  - [3.1 Opis Use Case](#sec-31-opis-use-case)
  - [3.2 Problem do rozwiązania](#sec-32-problem-do-rozwiazania)
  - [3.3 Ocena BXT — Business Viability (Żywotność Biznesowa)](#sec-33-ocena-bxt-business-viability-zywotnosc-biznesowa)
  - [3.4 Ocena BXT — Experience Value (Desirability — Pożądalność)](#sec-34-ocena-bxt-experience-value-desirability-pozadalnosc)
  - [3.5 Ocena BXT — Technical Feasibility (Wykonalność Techniczna)](#sec-35-ocena-bxt-technical-feasibility-wykonalnosc-techniczna)
  - [3.6 Ocena priorytetyzacji BXT (Macierz Impact × Fit)](#sec-36-ocena-priorytetyzacji-bxt-macierz-impact-fit)
- [4. USE CASE #02 — OCR + Credit Document Analysis Assistant](#sec-4-use-case-02-ocr-credit-document-analysis-assistant)
  - [4.1 Opis Use Case](#sec-41-opis-use-case)
  - [4.2 Problem do rozwiązania](#sec-42-problem-do-rozwiazania)
  - [4.3 Ocena BXT — Business Viability (Żywotność Biznesowa)](#sec-43-ocena-bxt-business-viability-zywotnosc-biznesowa)
  - [4.4 Ocena BXT — Experience Value (Desirability — Pożądalność)](#sec-44-ocena-bxt-experience-value-desirability-pozadalnosc)
  - [4.5 Ocena BXT — Technical Feasibility (Wykonalność Techniczna)](#sec-45-ocena-bxt-technical-feasibility-wykonalnosc-techniczna)
  - [4.6 Ocena priorytetyzacji BXT (Macierz Impact × Fit)](#sec-46-ocena-priorytetyzacji-bxt-macierz-impact-fit)
- [5. USE CASE #03 — Hyper-Personalization Engine](#sec-5-use-case-03-hyper-personalization-engine)
  - [5.1 Opis Use Case](#sec-51-opis-use-case)
  - [5.2 Problem do rozwiązania](#sec-52-problem-do-rozwiazania)
  - [5.3 Ocena BXT — Business Viability (Żywotność Biznesowa)](#sec-53-ocena-bxt-business-viability-zywotnosc-biznesowa)
  - [5.4 Ocena BXT — Experience Value (Desirability — Pożądalność)](#sec-54-ocena-bxt-experience-value-desirability-pozadalnosc)
  - [5.5 Ocena BXT — Technical Feasibility (Wykonalność Techniczna)](#sec-55-ocena-bxt-technical-feasibility-wykonalnosc-techniczna)
  - [5.6 Ocena priorytetyzacji BXT (Macierz Impact × Fit)](#sec-56-ocena-priorytetyzacji-bxt-macierz-impact-fit)
- [6. ZESTAWIENIE BXT — PRIORYTETYZACJA WSZYSTKICH USE CASES](#sec-6-zestawienie-bxt-priorytetyzacja-wszystkich-use-cases)
  - [6.1 Macierz BXT — ocena porównawcza](#sec-61-macierz-bxt-ocena-porownawcza)
  - [6.2 Kolejność realizacji i uzasadnienie](#sec-62-kolejnosc-realizacji-i-uzasadnienie)
  - [6.3 Luki zidentyfikowane w oryginalnych Use Cases — uzupełnienia](#sec-63-luki-zidentyfikowane-w-oryginalnych-use-cases-uzupenienia)
<!-- TOC END -->

<a id="sec-1-profil-organizacji-bce-bank-sa"></a>
# 1. PROFIL ORGANIZACJI — BCE Bank S.A.
<a id="sec-11-charakterystyka-organizacji"></a>
## 1.1 Charakterystyka organizacji
BCE Bank S.A. (Bank Best Company Ever) jest fikcyjną, lecz modelową instytucją finansową klasy mid-market, działającą na polskim rynku bankowym. Obsługuje szerokie spektrum klientów — od osób fizycznych, przez mikroprzedsiębiorców, aż po małe i średnie przedsiębiorstwa (MŚP). Bank realizuje ambitną strategię stania się liderem cyfrowej obsługi klientów w Polsce, co wyróżnia go na tle konkurencji skupionej nadal na tradycyjnych modelach dystrybucji.

|  |  |
| --- | --- |
| **Nazwa pełna** | BCE Bank S.A. (Bank Best Company Ever) |
| **Segment** | Bank detaliczny mid-market — klienci indywidualni i MŚP |
| **Skala działania** | ~1,2 mln aktywnych klientów ; 180 placówek ; 3 200 pracowników |
| **Kanały sprzedaży** | Oddział, aplikacja mobilna, bankowość internetowa, contact center |
| **Dojrzałość AI** | Poziom 1/5 — ad hoc, brak scentralizowanej platformy AI |
| **CRM** | Salesforce |
| **Core banking** | Temenos T24 |
| **DMS** | OpenText |
| **Regulatorzy** | KNF, NBP, EBA — wymogi AI Act (klasa wysokiego ryzyka dla kredytów) |
| **Misja AI** | Stać się liderem cyfrowej transformacji w segmencie mid-market w Polsce do 2028 r. |

<a id="sec-12-kluczowe-wyzwania-stan-as-is"></a>
## 1.2 Kluczowe wyzwania — stan AS-IS
Bank zmaga się z szeregiem problemów operacyjnych i strategicznych, które hamują jego wzrost i obniżają satysfakcję klientów. Poniżej przedstawiamy mapę głównych bolączek organizacji.

| **Obszar problemowy** | **Stan obecny (AS-IS)** | **Cel (TO-BE)** |
| --- | --- | --- |
| Obsługa zapytań klientów | Śr. czas: 8 min/zapytanie ; Duże obciążenie CC ; Niska automatyzacja L1 | Śr. czas: 2 min ; Deflection rate >35% |
| Analiza kredytowa | 45 min/wniosek ; 60–70% czasu analityka to data entry ; Wysokie ryzyko błędu | 5–10 min z AI ; Analityk skupiony na ocenie merytorycznej |
| Personalizacja ofert | Kampanie masowe ; Konwersja cross-sell <1,2% ; Zero mikrosegmentacji | Konwersja cross-sell >3,5% ; Hiperpersonalizacja w czasie rzeczywistym |
| Retencja talentów | Rotacja analityków 28% rocznie ; Utrata wiedzy ; Długi onboarding | Wsparcie AI → mniejsze wypalenie → lepsza retencja |
| Decyzja kredytowa | Czas decyzji: 3 dni ; Klienci odchodzą do konkurencji | Time-to-decision: <4 godziny |
| Platforma AI | Brak centralnej platformy ; Eksperymenty działowe bez governance | Zjednoczona platforma Azure AI Foundry + MLOps |

<a id="sec-13-dlaczego-bce-bank-wdraza-ai-uzasadnienie-transformacji"></a>
## 1.3 Dlaczego BCE Bank wdraża AI — uzasadnienie transformacji
Decyzja o podjęciu transformacji cyfrowej z wykorzystaniem sztucznej inteligencji wynika z konwergencji kilku czynników strategicznych i presji rynkowych:

### Presja konkurencyjna
* Neobanki i fintechy (np. Revolut, mBank, Alior) oferują klientom natychmiastową, spersonalizowaną obsługę 24/7 — BCE Bank traci klientów MŚP na ich rzecz.
* Sektor bankowy w Polsce notuje wzrost penetracji AI o 340% rok do roku (dane EBA 2025) — brak transformacji oznacza wypadnięcie z rynku.
* Klienci detaliczni oczekują odpowiedzi w ciągu sekund — model oparty na call center kosztuje 12× więcej niż obsługa chatbotem.

### Presja kosztowa
* Koszty operacyjne contact center rosną o 8% rocznie przy braku wzrostu NPS — model jest nieefektywny.
* Rotacja analityków kredytowych na poziomie 28% generuje ~2,4 mln PLN rocznie kosztów rekrutacji i onboardingu.
* Koszt błędnej decyzji kredytowej wynikającej z ręcznego data entry wynosi średnio 18 000 PLN na incydent (write-off + koszty windykacji).

### Szansa wzrostowa
* Cross-sell rate w BCE Bank wynosi 1,2% vs. 4,8% u liderów rynkowych — luka do zamknięcia dzięki hiperpersonalizacji.
* Każda godzina szybszej decyzji kredytowej przekłada się na ~3% wyższy wskaźnik akceptacji wniosków przez klientów.
* Syntetyczne dane klientów umożliwiają trenowanie modeli AI bez ryzyka naruszenia RODO — to kluczowy przewagowy asset w erze AI Act.

### Wymogi regulacyjne jako katalizator
* AI Act (UE 2024/1689) wchodzi w życie stopniowo do 2027 r. — BCE Bank, wdrażając AI teraz, buduje compliance jako przewagę, nie obciążenie.
* EBA Guidelines on AI (EBA/GL/2025/01) wymagają formalnego systemu zarządzania modelami AI. Projekt buduje te fundamenty.
* KNF oczekuje od banków transparentności algorytmów decyzyjnych (obowiązek explainability) — wbudowanie Human-in-the-Loop w Agent 2 jest bezpośrednią odpowiedzią.

### Wizja strategiczna — 3 agenty AI jako rdzeń transformacji
Wybór trzech konkretnych agentów AI nie jest przypadkowy — reprezentują one trzy wymiary wartości bankowej:

| **Agent AI** | **Wymiar wartości** | **Główny beneficjent** | **Horyzont zwrotu** |
| --- | --- | --- | --- |
| Agent 1: Product Catalogue Assistant | Doświadczenie klienta (CX) | Klienci zewnętrzni + CC | ~6 miesięcy |
| Agent 2: OCR Credit Analysis | Efektywność operacyjna | Analitycy kredytowi | ~9 miesięcy |
| Agent 3: Hyper-Personalization | Wzrost przychodów | Marketing / Klienci | ~12 miesięcy |

<a id="sec-14-cele-strategiczne-okr-horyzont-24-miesiecy"></a>
## 1.4 Cele strategiczne (OKR — horyzont 24 miesięcy)
| **#** | **Cel (Objective)** | **Kluczowe wyniki (Key Results)** |
| --- | --- | --- |
| O1 | Zwiększenie NPS o min. 15 pkt poprzez szybszą, spersonalizowaną obsługę | NPS: z 28 → >43 pkt w M24 |
| O2 | Redukcja kosztów operacyjnych contact center o 30% | Deflection rate chatbota >35%; AHT <2,5 min |
| O3 | Skrócenie time-to-decision kredytowego z 3 dni do <4 godzin | OCR accuracy >95%; weryfikacja <18 min |
| O4 | Wzrost przychodów ze sprzedaży krzyżowej o 20 mln PLN rocznie | Cross-sell conversion >3,5%; CTR kampanii +25% |
| O5 | Zbudowanie wewnętrznych kompetencji AI/MLOps | Min. 8 certyfikowanych inżynierów AI; platforma MLOps live |

<a id="sec-2-metodologia-bxt-pre-workshop-assessment"></a>
# 2. METODOLOGIA BXT — PRE-WORKSHOP ASSESSMENT
Każdy z trzech Use Cases BCE Bank został oceniony zgodnie z metodyką BXT (Business, eXperience, Technology) — frameworkiem stosowanym przez Microsoft do oceny potencjału konceptów AI. Framework mierzy trzy wymiary:

| **Wymiar** | **Pytanie kluczowe** | **Co oceniamy** |
| --- | --- | --- |
| BUSINESS (Viability) | Czy to jest opłacalne? | Czy istnieje wyraźny strumień przychodów lub oszczędności? Czy organizacja jest gotowa płacić za rozwiązanie? |
| EXPERIENCE (Desirability) | Czy użytkownicy tego chcą? | Czy wartość proposycja jest wystarczająco atrakcyjna? Czy użytkownicy wybiorą to rozwiązanie nad alternatywami? |
| TECHNOLOGY (Feasibility) | Czy możemy to zbudować? | Czy technologia jest dostępna i dojrzała? Jakie są ryzyka implementacyjne i zabezpieczenia? |

Sukces produktu AI = przecięcie wszystkich trzech wymiarów BXT. Poniżej prezentujemy pełne oceny BXT dla każdego z trzech agentów BCE Bank, wzbogacone o elementy zidentyfikowane w oryginalnych Use Cases (UC-01, UC-02, UC-03) i uzupełnione o brakujące komponenty.

<a id="sec-3-use-case-01-product-catalogue-assistant-chatbot-voicebot"></a>
# 3. USE CASE #01 — Product Catalogue Assistant (Chatbot / Voicebot)
|  |  |
| --- | --- |
| **Nazwa Use Case** | Product Catalogue Assistant — Agent Głosowy & Chatbot |
| **Numer UC** | UC-01 |
| **Departament** | Contact Center / Digital Banking / Sprzedaż Detaliczna |
| **Kierowanie** | External Facing (klienci zewnętrzni) + Internal Facing (helpdesk pracowniczy via Teams) |
| **Główny interesariusz** | Dyrektor Bankowości Detalicznej / Dyrektor Contact Center |
| **Persona użytkownika** | Sławek (klient) & Tomek (pracownik banku) — szukają szybkiej informacji o produktach |

<a id="sec-31-opis-use-case"></a>
## 3.1 Opis Use Case
System konwersacyjnej nawigacji po produktach bankowych opartej na GenAI. Klient lub pracownik banku zadaje pytanie w języku naturalnym (głosowo lub tekstowo), a agent odpowiada, wyjaśnia warunki produktów oraz przekierowuje do właściwego panelu akcji (np. formularz wniosku o kredyt, kalkulator lokat). Agent obsługuje kanały: www chatbot, aplikacja mobilna, infolinia (voicebot IVR) oraz Teams (wewnętrzny helpdesk).

<a id="sec-32-problem-do-rozwiazania"></a>
## 3.2 Problem do rozwiązania
* Obecny czas obsługi zapytań produktowych przez contact center wynosi średnio 8 minut/zapytanie — cel to 2 minuty.
* Katalog produktów bankowych jest skomplikowany — klienci nie potrafią sami znaleźć właściwego produktu, co generuje ruch do CC.
* Konsultanci CC spędzają 60% czasu na odpowiadaniu na te same, powtarzające się pytania (FAQ) zamiast na obsłudze złożonych przypadków.
* Brak 24/7 obsługi w kanałach cyfrowych — klienci pytają w nocy, dostają odpowiedź dopiero rano.
* Wysoki koszt obsługi: 1 zapytanie przez agenta CC kosztuje ~18 PLN vs. ~0,08 PLN przez chatbota AI.

<a id="sec-33-ocena-bxt-business-viability-zywotnosc-biznesowa"></a>
## 3.3 Ocena BXT — Business Viability (Żywotność Biznesowa)
| **Kryterium biznesowe** | **Ocena i uzasadnienie** |
| --- | --- |
| **Jak Use Case generuje wartość biznesową?** | Redukcja kosztu obsługi L1 (deflection 40%) = oszczędność ~3,2 mln PLN/24M. Wzrost NPS o min. 8 pkt → poprawa retencji klientów. |
| **Zgodność ze strategią organizacji?** | Bezpośrednio realizuje OKR O1 (NPS +15 pkt) i O2 (redukcja kosztów CC o 30%). Quick win — najniższe ryzyko regulacyjne ze wszystkich 3 agentów. |
| **Kto jest właścicielem OKR?** | Dyrektor Contact Center (operacyjny) + Dyrektor Sprzedaży Detalicznej (wzrost). Sponsor: CEO/CDO. |
| **Cele biznesowe (Business Objectives)** | 1. Zwiększenie przepustowości CC bez wzrostu zatrudnienia 2. Skrócenie AHT z 8 do 2,5 min 3. Dostępność 24/7 we wszystkich kanałach cyfrowych |
| **Kluczowe wyniki (Key Results)** | - Deflection rate: >35% w M8, >50% w M24 - CSAT chatbota: >3,8/5 - Koszt obsługi L1: redukcja o 45% - Czas do pierwszej odpowiedzi: <3 sekundy |
| **Horyzont wdrożenia Change Mgmt** | 4–6 miesięcy dla MVP/Pilota. Szkolenia CC: 120 osób. Zmiana procesów: redirect flow, nowe KPI dla CC. |

| **Ocena skali biznesowej** | **Skala (1–5)** | **Wynik** |
| --- | --- | --- |
| **Wpływ biznesowy (Business Impact)** | **●●●●●** | **5 / 5** |
| **Dopasowanie wykonawcze (Executional Fit)** | **●●●●○** | **4 / 5** |
| **Pilność (Urgency)** | **●●●●●** | **5 / 5** |

<a id="sec-34-ocena-bxt-experience-value-desirability-pozadalnosc"></a>
## 3.4 Ocena BXT — Experience Value (Desirability — Pożądalność)
| **Kryterium doświadczenia** | **Ocena i uzasadnienie** |
| --- | --- |
| **Wartość proposycja dla użytkownika** | Klient otrzymuje natychmiastową, precyzyjną odpowiedź w języku naturalnym — bez czekania w kolejce, bez przekopywania się przez dokumenty PDF z tabelami produktowymi. |
| **Kim jest główny użytkownik (Primary User)?** | Sławek (klient detaliczny, 32 lata, zapracowany, preferuje mobilne) + Tomek (pracownik placówki, potrzebuje szybkiej informacji o produktach na spotkaniu z klientem) |
| **Kto jest pilotem (Who is the pilot)?** | Pilotaż: wybrana grupa klientów beta (500 osób, opt-in) + 15 pracowników contact center w fazie PoC. |
| **Co sprawia, że użytkownicy to wybiorą?** | Szybkość (odpowiedź w 3s vs. 8 min w CC), dostępność 24/7, personalizacja kontekstu rozmowy, brak frustracji z nieaktualnymi odpowiedziami (RAG = zawsze aktualne dane produktowe). |
| **Ryzyko adopcji** | Część klientów preferuje kontakt ludzki — chatbot musi bezproblemowo eskalować do agenta CC. Kluczowy element UX: 'one click to human'. |

| **Ocena desirability** | **Skala (1–5)** | **Wynik** |
| --- | --- | --- |
| **Pożądalność użytkownika (User Desirability)** | **●●●●○** | **4 / 5** |
| **Wartość proposycja vs. alternatywa (NBT)** | **●●●●●** | **5 / 5** |
| **Gotowość do adopcji (Adoption Readiness)** | **●●●●○** | **4 / 5** |

<a id="sec-35-ocena-bxt-technical-feasibility-wykonalnosc-techniczna"></a>
## 3.5 Ocena BXT — Technical Feasibility (Wykonalność Techniczna)
| **Kryterium techniczne** | **Ocena i uzasadnienie** |
| --- | --- |
| **Fit AI/LLM** | Rozwiązanie idealne dla GPT-4o via Azure OpenAI + RAG (Azure AI Search). Model nie halucynuje, bo opiera się wyłącznie na dostarczonym katalogu produktów — nie korzysta z 'wiedzy ogólnej'. |
| **Dostępna infrastruktura?** | Wymaga: Azure OpenAI (GPT-4o), Azure AI Search (wektoryzacja katalogu), Azure Bot Service (framework), Azure Speech Services (voicebot PL). Środowisko chmurowe w UE (data residency). |
| **Czy są wystarczające zabezpieczenia?** | - Model działa w zamkniętym środowisku chmurowym banku — dane nie wychodzą na zewnątrz - Automatyczne maskowanie PII (PESEL, nr konta) przed wysłaniem do modelu - Pełne szyfrowanie in-transit i at-rest - Content filters: blokada wulgaryzmów, prompt injection protection - RAG eliminuje ryzyko halucynacji finansowych |
| **Ryzyka wdrożeniowe i operacyjne** | - Halucynacje: ryzyko podania błędnego oprocentowania → mitigacja: RAG + source grounding - Bezpieczeństwo przy interakcji głosowej: PESEL/IBAN w strumieniu audio → maskowanie pre-processing - Integracja SDK iOS/Android: wymaga zaangażowania dev mobile (nie AI team) - Accuracy intencji na specjalistycznym słownictwie finansowym PL: wymaga starannego dataset Q&A |
| **Scope PoC vs. Pilot** | PoC: 20 produktów, chatbot tekstowy, kanał www + Teams, zbiór 200 Q&A. Pilot: voicebot PL (Azure Speech), integracja app mobilna, 500 klientów beta. Produkcja: pełny katalog 40+ produktów, integracja IVR, język EN. |
| **Horyzont czasowy** | 4–6 miesięcy do MVP/Pilota. PoC tekstowy: 1–3 miesiące. |

| **Ocena techniczna** | **Skala (1–5)** | **Wynik** |
| --- | --- | --- |
| **Wykonalność techniczna (Technical Feasibility)** | **●●●●○** | **4 / 5** |
| **Dojrzałość technologii (Tech Maturity)** | **●●●●●** | **5 / 5** |
| **Dostępność zabezpieczeń (Safeguards Availability)** | **●●●●○** | **4 / 5** |

<a id="sec-36-ocena-priorytetyzacji-bxt-macierz-impact-fit"></a>
## 3.6 Ocena priorytetyzacji BXT (Macierz Impact × Fit)
UC-01 plasuje się w kwadrancie 'Wysoki wpływ strategiczny / Wysokie dopasowanie wykonawcze' — rekomendacja: INVEST / Quick Win. Jest to typowy projekt Test & Learn: zweryfikować bariery bezpieczeństwa w PoC (1–3 mies.), a następnie szybki Pilot (kolejne 3 mies.). Niska bariera technologiczna i brak wymogów regulacyjnych klasy wysokiego ryzyka (AI Act) czyni z niego naturalny 'quick win' portfela AI.

| **Wymiar** | **Podsumowanie oceny BXT** |
| --- | --- |
| BUSINESS | ★★★★★ Wysoki wpływ — quick win, bezpośrednia oszczędność kosztów i wzrost NPS |
| EXPERIENCE | ★★★★☆ Wysoka pożądalność — klienci oczekują szybkości, GenAI > IVR legacy |
| TECHNOLOGY | ★★★★☆ Dojrzała technologia — Azure RAG stack sprawdzony, ryzyko śr.-niskie |
| REKOMENDACJA | START PoC natychmiast → Pilot M3–M8 → Produkcja M9 |

<a id="sec-4-use-case-02-ocr-credit-document-analysis-assistant"></a>
# 4. USE CASE #02 — OCR + Credit Document Analysis Assistant
|  |  |
| --- | --- |
| **Nazwa Use Case** | Inteligentna Analiza Dokumentów Kredytowych — GenAI Credit Analysis Assistant |
| **Numer UC** | UC-02 |
| **Departament** | Departament Ryzyka Kredytowego / Obsługa Klienta Indywidualnego i MŚP |
| **Kierowanie** | Internal Facing — narzędzie dla analityków kredytowych banku |
| **Główny interesariusz** | Dyrektor Departamentu Ryzyka Kredytowego (Jolanta Kaczyńska) |
| **Persona użytkownika** | Marcin — starszy analityk kredytowy MŚP, przeciążony data entry, frustacja niskim poziomem pracy merytorycznej |

<a id="sec-41-opis-use-case"></a>
## 4.1 Opis Use Case
System wykorzystujący multimodalne GenAI (GPT-4o + Azure Document Intelligence) do automatycznej ekstrakcji danych z dokumentów finansowych klientów (paski wynagrodzeń, PIT, wyciągi bankowe, umowy o pracę — etapowo). System generuje wstępną notatkę analityczną (Credit Memo) dla analityka ryzyka. Analityk weryfikuje manualnie każdą pozycję i podejmuje ostateczną decyzję — zasada Human-in-the-Loop jest nienaruszalna.

<a id="sec-42-problem-do-rozwiazania"></a>
## 4.2 Problem do rozwiązania
* Analitycy kredytowi spędzają 60–70% czasu na ręcznym przepisywaniu danych z aplikacji kredytowych do systemów — to praca 'data entry', nie analityczna.
* Czas oczekiwania klienta na decyzję: 3 dni → klienci biznesowi BCE odchodzą do konkurencji, która decyduje w 24h.
* Ręczne wprowadzanie danych sprzyja błędom → błędna ocena zdolności kredytowej → potencjalne straty (~18 000 PLN/incydent).
* Wysoka rotacja analityków (28%/rok) — nowi pracownicy uczą się bardzo długo, co jest 'wąskim gardłem' produktywności.
* Skanowane dokumenty o niskiej jakości (zdjęcia telefonem) są trudne do ręcznej weryfikacji, co spowalnia proces.

<a id="sec-43-ocena-bxt-business-viability-zywotnosc-biznesowa"></a>
## 4.3 Ocena BXT — Business Viability (Żywotność Biznesowa)
| **Kryterium biznesowe** | **Ocena i uzasadnienie** |
| --- | --- |
| **Jak Use Case generuje wartość biznesową?** | Znacznie szybsza decyzja kredytowa (z 3 dni → tego samego dnia) → wzrost konwersji wniosków o ~8% → bezpośredni wzrost przychodów. Redukcja cost-to-serve na 1 wniosek o ~60%. |
| **Zgodność ze strategią organizacji?** | Bezpośrednio realizuje OKR O3 (time-to-decision <4h). Wzrost efektywności operacyjnej (Operational Excellence) — priorytet strategiczny zarządu. |
| **Kto jest właścicielem OKR?** | Dyrektor Dep. Ryzyka Kredytowego — Jolanta Kaczyńska. Sponsor: CFO + CRO (Chief Risk Officer). |
| **Cele biznesowe (Business Objectives)** | 1. Zwiększenie efektywności analityków (więcej wniosków bez nowych etatów) 2. Redukcja cost-to-serve na 1 wniosek kredytowy 3. Skrócenie time-to-decision z 3 dni do <4 godzin |
| **Kluczowe wyniki (Key Results)** | - Czas weryfikacji wniosku: z 45 min → <18 min w M8, <8 min w M24 - OCR accuracy kluczowych pól: >95% - Wzrost liczby wniosków na analityka: +60% bez wzrostu FTE - Zero fałszywych akceptacji kredytów (kryterium bramki Go/NoGo) - NPS analityka: >4,0/5 |
| **Horyzont wdrożenia Change Mgmt** | 4–6 miesięcy (MVP: jeden typ dokumentu — pasek wynagrodzeń). Szkolenia: 50 analityków kredytowych. Zmiana procesu: nowy workflow 'AI suggest → human verify → system update'. |

| **Ocena skali biznesowej** | **Skala (1–5)** | **Wynik** |
| --- | --- | --- |
| **Wpływ biznesowy (Business Impact)** | **●●●●●** | **5 / 5** |
| **Dopasowanie wykonawcze (Executional Fit)** | **●●●●○** | **4 / 5** |
| **Priorytet regulacyjny (Compliance Priority)** | **●●●●●** | **5 / 5** |

<a id="sec-44-ocena-bxt-experience-value-desirability-pozadalnosc"></a>
## 4.4 Ocena BXT — Experience Value (Desirability — Pożądalność)
| **Kryterium doświadczenia** | **Ocena i uzasadnienie** |
| --- | --- |
| **Wartość proposycja dla użytkownika** | AI działa jak 'junior analyst' — przygotowuje brudnopis analizy (ekstrakcja danych, wstępna ocena, Credit Memo), a doświadczony analityk zajmuje się wyłącznie oceną merytoryczną i decyzją. Uwolnienie od 'nudnej pracy data entry'. |
| **Kim jest główny użytkownik (Primary User)?** | Marcin — Senior Credit Analyst MŚP, 8 lat doświadczenia, przeciążony pracą administracyjną. Chce skupiać się na skomplikowanych przypadkach, nie na przepisywaniu danych ze skanów. |
| **Kto jest pilotem (Who is the pilot)?** | 5 analityków kredytowych w środowisku staging M6–M7, obsługa 200 rzeczywistych wniosków w trybie wspomaganym (AI suggest, human decide). |
| **Desirability — dlaczego analitycy to zaadoptują?** | Analitycy są mocno przeciążeni pracą administracyjną. Narzędzie, które automatycznie 'czyta' skany i wypełnia dane w systemie, jest przez nich bardzo pożądane — pod warunkiem, że nie sprawi, że poczują się zagrożeni utratą pracy (change management kluczowy!). |
| **Ryzyko nieadopcji / oporu** | Główne ryzyko: analitycy obawiają się, że AI 'zastąpi' ich lub że błędy AI będą przypisywane im. Mitygacja: wyraźna komunikacja Human-in-the-Loop, AI jako narzędzie NIE decyduje, NPS analityków mierzony jako KPI. |

| **Ocena desirability** | **Skala (1–5)** | **Wynik** |
| --- | --- | --- |
| **Pożądalność użytkownika (User Desirability)** | **●●●●●** | **5 / 5** |
| **Wartość proposycja vs. status quo** | **●●●●●** | **5 / 5** |
| **Ryzyko change management (niższy = lepszy)** | **●●●○○** | **3 / 5** |

<a id="sec-45-ocena-bxt-technical-feasibility-wykonalnosc-techniczna"></a>
## 4.5 Ocena BXT — Technical Feasibility (Wykonalność Techniczna)
| **Kryterium techniczne** | **Ocena i uzasadnienie** |
| --- | --- |
| **Fit AI/LLM** | Idealne dla Multimodal LLM (GPT-4o) — model potrafi 'widzieć' dokumenty (OCR vision) i rozumieć kontekst finansowy. Azure Document Intelligence v3.1 jako dedykowany OCR engine z pre-built modelem dla dokumentów finansowych. |
| **Dostępna infrastruktura?** | Wymaga: Azure Document Intelligence (OCR), GPT-4o (analiza i generacja Credit Memo), Palantir Foundry (pipeline danych, interfejs analityka), integracja z Temenos T24 (read-only w PoC). |
| **Czy są wystarczające zabezpieczenia?** | - Human-in-the-Loop: AI NIE podejmuje decyzji kredytowej — jedynie rekomenduje - Każda liczba wyciągnięta przez AI z dokumentu ma 'klikalne' odniesienie do oryginału (source grounding) — analityk może zweryfikować - Przetwarzanie dokumentów wyłącznie w zamkniętym środowisku chmurowym UE - DPIA wymagana i realizowana w M2 - Explainability: AI Act art. 13 — przejrzystość systemu wysokiego ryzyka |
| **Ryzyka wdrożeniowe i operacyjne** | - Jakość skanów: ryzyko błędów OCR przy słabych dokumentach (zdjęcia telefonem) → próg odrzucenia, augmentation - Formaty niestandardowe: różne layouty pasków od różnych pracodawców → rozszerzanie modelu - Integracja z Core Banking (T24): krytyczna ścieżka — wymaga formalnego change request IT (bufor +3 tygodnie) - Regulatorzy (AI Act): system wysokiego ryzyka → wymogi art. 9, 13, 14, 17 |
| **Scope PoC vs. Pilot** | PoC: pasek wynagrodzeń (PDF/JPG), 3 pola (pracodawca, dochód brutto/netto, okres), pipeline end-to-end na 30 dokumentach. Pilot: 200 wniosków, 5 analityków, pełny Credit Memo. Produkcja: PIT, wyciąg bankowy, umowa o pracę, integracja BIK (koncepcyjnie). |
| **Horyzont czasowy** | 3–6 miesięcy dla MVP wspierającego 1 typ dokumentu (pasek wynagrodzeń). Quick Win jeśli zaczniemy od prostego 'asystenta czytającego PDFy' bez pełnej integracji T24 na start. |

| **Ocena techniczna** | **Skala (1–5)** | **Wynik** |
| --- | --- | --- |
| **Wykonalność techniczna (Technical Feasibility)** | **●●●●○** | **4 / 5** |
| **Dojrzałość technologii OCR + GenAI** | **●●●●●** | **5 / 5** |
| **Kompleksowość integracji (niższy = łatwiej)** | **●●●○○** | **3 / 5** |

<a id="sec-46-ocena-priorytetyzacji-bxt-macierz-impact-fit"></a>
## 4.6 Ocena priorytetyzacji BXT (Macierz Impact × Fit)
UC-02 plasuje się jako 'Invest Long Term' lub 'Quick Win' (jeśli zaczniemy od prostego asystenta czytającego PDFy bez pełnej integracji na start). Strategiczny wpływ biznesowy: poziom 5 — kluczowe dla efektywności banku. Poziom 4 pod kątem dopasowania wykonawczego — łatwiejsze wdrożenie niż voicebot ze względu na Internal Facing (mniejsze ryzyko wizerunkowe).

| **Wymiar** | **Podsumowanie oceny BXT** |
| --- | --- |
| BUSINESS | ★★★★★ Najwyższy wpływ — bezpośrednie oszczędności + wzrost przychodów przez szybszą decyzję |
| EXPERIENCE | ★★★★★ Analitycy desperacko potrzebują tego narzędzia — uwolnienie od data entry |
| TECHNOLOGY | ★★★★☆ Dojrzała technologia OCR+LLM, wyzwanie to integracja T24 + wymogi AI Act |
| REKOMENDACJA | Quick Win (prosty PDF reader) → następnie Invest Long Term (pełna integracja T24 + multi-doc) |

<a id="sec-5-use-case-03-hyper-personalization-engine"></a>
# 5. USE CASE #03 — Hyper-Personalization Engine
|  |  |
| --- | --- |
| **Nazwa Use Case** | Hiperpersonalizacja Ofert Marketingowych — Hyper-Personalization Engine |
| **Numer UC** | UC-03 |
| **Departament** | Dział Marketingu / CRM / Digital Banking |
| **Kierowanie** | External Facing — kampanie do klientów; Internal Facing — narzędzie dla działu marketingu |
| **Główny interesariusz** | Dyrektor Marketingu — CMO (Krzysztof Bark) |
| **Persona użytkownika** | Magda — Specjalista działu marketingu, tworzy kampanie dla milionów klientów, nie ma czasu na ręczną segmentację |

<a id="sec-51-opis-use-case"></a>
## 5.1 Opis Use Case
Silnik hiperpersonalizacji generujący unikalne treści komunikacyjne (e-mail, push, SMS) dla każdego klienta na podstawie analizy historii transakcyjnej i momentów życiowych. W fazie PoC — syntetyczna historia transakcyjna generowana przez LLM (dane rzeczywiste są wrażliwe RODO). Na tej podstawie silnik identyfikuje okazje cross-sell/up-sell i generuje spersonalizowaną komunikację marketingową. Opcjonalny stretch goal: multi-agent interaction z Agent 1 (Chatbot) dla głębszego kontekstu produktowego.

<a id="sec-52-problem-do-rozwiazania"></a>
## 5.2 Problem do rozwiązania
* Klienci otrzymują generyczne wiadomości ('Mamy dla Ciebie kredyt') — ignorują je (Open Rate <8%, CTR 1,8%).
* Tworzenie spersonalizowanych treści dla 1,2 mln klientów jest niemożliwe dla ludzi — brak skalowalności.
* Cross-sell conversion wynosi 1,2% vs. 4,8% u liderów rynku — potencjalna utrata 20+ mln PLN przychodów rocznie.
* Segmentacja jest statyczna i prosta (wiek + saldo) — brak mikrosegmentacji opartej na zachowaniach i momentach życiowych.
* Wysoki koszt kampanii masowych przy niskim ROI — dyrektor marketingu nie potrafi uzasadnić budżetu akcjonariuszom.

<a id="sec-53-ocena-bxt-business-viability-zywotnosc-biznesowa"></a>
## 5.3 Ocena BXT — Business Viability (Żywotność Biznesowa)
| **Kryterium biznesowe** | **Ocena i uzasadnienie** |
| --- | --- |
| **Jak Use Case generuje wartość biznesową?** | Cross-sell uplift: +2,8% konwersja vs. 1,2% baseline × 500 000 aktywnych klientów × marża ~200 PLN = ~2,8 mln PLN/rok. Redukcja churnu o 0,5% × LTV 480 PLN = ~2,88 mln PLN/24M. |
| **Zgodność ze strategią organizacji?** | Bezpośrednio realizuje OKR O4 (wzrost przychodów ze sprzedaży krzyżowej +20 mln PLN rocznie) i O1 (NPS +15 pkt — klient czuje, że bank go rozumie). |
| **Kto jest właścicielem OKR?** | CMO (Krzysztof Bark) — właściciel przychodów z cross-sell. Sponsor: CEO/CCO (Chief Commercial Officer). |
| **Cele biznesowe (Business Objectives)** | 1. Wzrost konwersji kampanii marketingowych (CR) 2. Redukcja kosztów kampanii przy zachowaniu ROI 3. Automatyzacja segmentacji i mikrosegmentacji (segmenty dynamiczne) 4. Redukcja churnu przez relevantną komunikację |
| **Kluczowe wyniki (Key Results)** | - Lift CTR e-mail: z 1,8% → >2,2% (+22%) w M8 Pilota - Cross-sell conversion: z 1,2% → >3,0% w grupie testowej - Przychód inkrementalny mierzalny A/B testem: >500 000 PLN w Pilocie - Churn reduction: -0,5% bazy klientów w 24M - Koszt na konwersję (CPAcq): redukcja o 30% |
| **Horyzont wdrożenia Change Mgmt** | 4–6 miesięcy (pilotaż na 1000 klientów, kampania e-mail). Wymaga: akceptacja CMO, DPO (DPIA dla danych transakcyjnych), integracja Salesforce MC. |

| **Ocena skali biznesowej** | **Skala (1–5)** | **Wynik** |
| --- | --- | --- |
| **Wpływ biznesowy (Business Impact)** | **●●●●●** | **5 / 5** |
| **Dopasowanie do strategii wzrostu** | **●●●●●** | **5 / 5** |
| **Dopasowanie wykonawcze (Executional Fit)** | **●●●●○** | **4 / 5** |

<a id="sec-54-ocena-bxt-experience-value-desirability-pozadalnosc"></a>
## 5.4 Ocena BXT — Experience Value (Desirability — Pożądalność)
| **Kryterium doświadczenia** | **Ocena i uzasadnienie** |
| --- | --- |
| **Wartość proposycja dla użytkownika (klient)** | Klient czuje, że bank go rozumie, a nie spamuje — 'bank wie, że mam małe dziecko i oferuje mi kartę cashback na stację paliw, nie kredyt hipoteczny'. Większe zaangażowanie w aplikacji mobilnej, lojalność. |
| **Wartość proposycja dla Magdy (marketer)** | Magda zamiast ręcznie tworzyć segmenty i treści dla 20 grup klientów, otrzymuje narzędzie generujące tysiące wariantów komunikacji automatycznie. Skupia się na strategii, nie operacjach. |
| **Kim jest główny użytkownik (Primary User)?** | Dwie persony: (1) Magda — specjalista marketingu, beneficjent produktywności. (2) Klient banku — beneficjent relevantnej oferty. |
| **Kto jest pilotem (Who is the pilot)?** | Pracownik działu marketingu (Magda) + wybrana grupa 1000 klientów beta (e-mail opt-in) w fazie Pilota M7–M8. |
| **Ryzyko doświadczenia użytkownika** | - Klienci mogą postrzegać hiperpersonalizację jako 'creepy' (zbyt dokładna wiedza banku) → konieczny control nad preferencjami komunikacji - RODO: zgoda na profilowanie — wymaga jasnego opt-in/opt-out mechanizmu - Ryzyko dyskryminacji: segmentacja AI może nieświadomie wykluczać pewne grupy (bias) → monitoring i fairness assessment |

| **Ocena desirability** | **Skala (1–5)** | **Wynik** |
| --- | --- | --- |
| **Pożądalność przez klientów banku** | **●●●●○** | **4 / 5** |
| **Pożądalność przez dział marketingu** | **●●●●●** | **5 / 5** |
| **Ryzyko percepcji prywatności (niższy = lepiej)** | **●●●○○** | **3 / 5** |

<a id="sec-55-ocena-bxt-technical-feasibility-wykonalnosc-techniczna"></a>
## 5.5 Ocena BXT — Technical Feasibility (Wykonalność Techniczna)
| **Kryterium techniczne** | **Ocena i uzasadnienie** |
| --- | --- |
| **Fit AI/LLM** | Rozwiązanie zakłada integrację GenAI (GPT-4o) z wewnętrznym CRM (Salesforce) oraz podejście RAG dla kontekstu produktowego. Azure ML do klasyfikacji segmentów. SDV/CTGAN do generacji syntetycznych danych transakcyjnych w PoC. |
| **Dostępna infrastruktura?** | Wymaga: GPT-4o (generacja komunikacji), Azure ML (segmentacja klientów), Salesforce Marketing Cloud (delivery kanału), SDV/CTGAN (syntetyczne dane do PoC), opcjonalnie Apache Kafka (real-time w skalowaniu). |
| **Czy są wystarczające zabezpieczenia?** | W praktyce bank MUSI dodać: - Lokalne lub VPC-hosted modele (prywatna chmura) dla danych transakcyjnych - Formalny proces aprobacyjny AI (review treści przed wysłaniem) - DPIA (ocena skutków dla ochrony danych osobowych) - AI Risk Assessment (bias, dyskryminacja) - Monitoring generowanych treści (content moderation) - Privacy guardrails: opt-in/opt-out dla profilowania - Syntetyczne dane w PoC = obejście problemów RODO |
| **Ryzyka wdrożeniowe i operacyjne** | - Ryzyka danych (Data Risks): profilowanie transakcji wrażliwe RODO - Integracja z CRM (Salesforce): wymaga konfiguracji API + testy deliverability - Stabilność i dostępność modelu (SLA) - Bias i dyskryminacja modeli: segmentacja może nieświadomie dyskryminować - Halucynacje modelu: AI może generować nieprawdziwe informacje o produktach → guardrails - Zależność od zewnętrznego dostawcy: zmiany API/cennika mogą przerwać usługę |
| **Scope PoC vs. Pilot vs. Skalowanie** | PoC: 10 000 syntetycznych profili, 3 segmenty, ocena jakości przez ekspertów marketingowych. Pilot: 1000 klientów beta, kampania e-mail, A/B test vs. standardowy. Skalowanie: real-time (Kafka), multi-agent (Agent 1 + Agent 3), push + SMS. |
| **Stretch goal — Multi-Agent Orchestration** | Agent 1 (Chatbot) + Agent 3 (Personalizacja) komunikują się: klient pytający o kredyt hipoteczny otrzymuje odpowiedź opartą jednocześnie na katalogu produktowym i spersonalizowanej analizie jego historii transakcyjnej. Termin: M18–M20 opcjonalnie. |

| **Ocena techniczna** | **Skala (1–5)** | **Wynik** |
| --- | --- | --- |
| **Wykonalność techniczna (Technical Feasibility)** | **●●●●○** | **4 / 5** |
| **Dojrzałość technologii GenAI + CRM** | **●●●●○** | **4 / 5** |
| **Kompleksowość compliance RODO/AI Act (niższy = łatwiej)** | **●●●●○** | **4 / 5** |

<a id="sec-56-ocena-priorytetyzacji-bxt-macierz-impact-fit"></a>
## 5.6 Ocena priorytetyzacji BXT (Macierz Impact × Fit)
UC-03 plasuje się w kwadrancie 'Wysoki wpływ strategiczny / Średnio-wysokie dopasowanie wykonawcze'. Najwyższy potencjał przychodowy ze wszystkich trzech agentów, ale też najwyższe wymagania compliance (RODO + AI Act). Rekomendacja: start PoC na danych syntetycznych (eliminuje ryzyko RODO), fast-follow po UC-01.

| **Wymiar** | **Podsumowanie oceny BXT** |
| --- | --- |
| BUSINESS | ★★★★★ Najwyższy potencjał przychodowy — cross-sell uplift + redukcja churnu = >5 mln PLN/24M |
| EXPERIENCE | ★★★★☆ Klienci pożądają relevantnych ofert; marketingowcy — automatyzacji segmentacji |
| TECHNOLOGY | ★★★★☆ Technologia dostępna; wyzwanie = RODO compliance i dane transakcyjne → syntetyczne dane as mitigation |
| REKOMENDACJA | Start PoC M5 (syntetyczne dane) → Pilot M7–M8 → Produkcja M9 → Real-time M18 + Multi-Agent stretch |

<a id="sec-6-zestawienie-bxt-priorytetyzacja-wszystkich-use-cases"></a>
# 6. ZESTAWIENIE BXT — PRIORYTETYZACJA WSZYSTKICH USE CASES
<a id="sec-61-macierz-bxt-ocena-porownawcza"></a>
## 6.1 Macierz BXT — ocena porównawcza
| **Use Case** | **BUSINESS (1–5)** | **EXPERIENCE (1–5)** | **TECHNOLOGY (1–5)** | **Rekomendacja** |
| --- | --- | --- | --- | --- |
| UC-01: Product Catalogue Chatbot/Voicebot | 5 | 4 | 4 | Quick Win → INVEST |
| UC-02: OCR Credit Analysis | 5 | 5 | 4 | Quick Win + Invest LT |
| UC-03: Hyper-Personalization Engine | 5 | 4 | 4 | Test & Learn → INVEST |

<a id="sec-62-kolejnosc-realizacji-i-uzasadnienie"></a>
## 6.2 Kolejność realizacji i uzasadnienie
| **#** | **Agent** | **Start PoC** | **Uzasadnienie priorytetu** |
| --- | --- | --- | --- |
| 1 | UC-01 — Chatbot | M3 (Sprint 1) | Quick win, najniższe ryzyko regulacyjne, najszybszy czas do wartości, external-facing = widoczny efekt |
| 2 | UC-02 — OCR Credit | M4 (Sprint 3) | Wysokie oszczędności kosztowe, analitycy gotowi do UAT, wymaga DPIA — startujemy po DPIA z M2 |
| 3 | UC-03 — Personalizacja | M5 (Sprint 5) | Najwyższy potencjał przychodowy, ale wymaga syntetycznych danych i akceptacji DPO — startuje po UC-01 i UC-02 |

<a id="sec-63-luki-zidentyfikowane-w-oryginalnych-use-cases-uzupenienia"></a>
## 6.3 Luki zidentyfikowane w oryginalnych Use Cases — uzupełnienia
Porównując oryginalne prezentacje UC-01, UC-02, UC-03 z wymaganiami szablonu BXT pre-workshop assessment, zidentyfikowano następujące braki, które zostały uzupełnione w niniejszym dokumencie:

| **UC** | **Brakujący element** | **Status w oryginale** | **Uzupełnienie w tym dokumencie** |
| --- | --- | --- | --- |
| UC-01 | Szczegółowe KPI Pilota z baseline | Brak numerycznych baseline'ów | Dodano: AHT 8min, deflection 0%, koszt CC |
| UC-01 | Pełny opis zmiany procesowej (Change Mgmt) | Brak | Dodano: 120 osób CC, redirect flow, nowe KPI |
| UC-02 | Persona użytkownika (Primary User) | Zbiorowa 'Zespół Analityków' | Dodano: Marcin — konkretna persona z potrzebami |
| UC-02 | Wymogi AI Act (high-risk system) | Tylko ogólna wzmianka | Dodano: art. 9, 13, 14, 17 + explainability + DPIA |
| UC-03 | Ryzyko bias i dyskryminacji | Wzmianka bez mitygacji | Dodano: fairness assessment, monitoring, guardrails |
| UC-03 | Mechanizm opt-in/opt-out RODO | Brak | Dodano: zgoda profilowanie, privacy guardrails |
| Wszystkie | Macierz zależności między UC | Brak | Dodano: kolejność startów, stretch goal multi-agent |
| Wszystkie | Profil organizacji BCE Bank | Szczątkowy | Pełny profil: historia, metryki, wyzwania, OKR |

**BCE BANK S.A. — Profil Organizacji & BXT Use Cases AI**

Dokument opracowany zgodnie z metodyką BXT (Microsoft) i standardami AI Act UE | Wersja 1.0 | Marzec 2026 | POUFNE — wyłącznie do użytku wewnętrznego
