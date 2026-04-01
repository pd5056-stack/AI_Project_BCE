**BCE BANK S.A.**  **ROADMAPA WDROŻENIA AI**  Transformacja Cyfrowa Banku poprzez Wdrożenie 3 Agentów AI  Etapy · Harmonogram · Zasoby · Budżet · TCO · ROI

|  |  |  |
| --- | --- | --- |
| Wersja dokumentu  **1.0 — Final Draft** | Data opracowania  **Marzec 2026** | Klasyfikacja  **POUFNE / WEWNĘTRZNE** |

|  |  |  |  |
| --- | --- | --- | --- |
| **3 Agenty AI**  Product Catalogue  OCR Credit  Hyper-Personalization | **6 Miesięcy**  Pilot / PoC  do produkcji | **~2,8 mln PLN**  Budżet PoC + Pilot  (12 mies.) | **ROI 187%**  w 24 miesiącach  od wdrożenia |

# Spis Treści
1. Streszczenie Wykonawcze 3

2. Profil Organizacji — BCE Bank S.A. 4

3. Zakres Projektu i Trzy Agenty AI 5

4. Roadmapa Wdrożenia — Przegląd Etapów 7

5. Etap 0: Discovery & Przygotowanie (M1–M2) 8

6. Etap 1: PoC / Pilot (M3–M8) — 6 Miesięcy 9

7. Etap 2: Produkcja i Stabilizacja (M9–M14) 12

8. Etap 3: Skalowanie i Optymalizacja (M15–M24) 13

9. Harmonogram Zbiorczy — Gantt 14

10. Zasoby i Zespół Projektowy 15

11. Budżet Projektu 17

12. TCO — Total Cost of Ownership (24 miesiące) 19

13. ROI — Analiza Zwrotu z Inwestycji 20

14. Bramki Go/NoGo i Kryteria Akceptacji 22

15. Zależności i Integracje 23

16. Założenia i Ograniczenia 24

# 1. Streszczenie Wykonawcze

_Executive Summary_

Niniejszy dokument stanowi kompletną roadmapę wdrożenia trzech agentów AI w BCE Bank S.A. — instytucji bankowej klasy mid-market z ambicją stania się liderem cyfrowej obsługi klientów detalicznych i MŚP w Polsce. Roadmapa obejmuje pełen cykl życia projektu: od fazy Discovery (M1–M2), przez obligatoryjny Pilot/PoC realizowany w 6 miesiącach (M3–M8), wdrożenie produkcyjne (M9–M14), aż po skalowanie i optymalizację (M15–M24).

**Trzech agentów objętych wdrożeniem:**

* **Agent 1:** Product Catalogue Assistant (Chatbot/Voicebot) — konwersacyjna nawigacja po produktach bankowych, obsługa zapytań klientów zewnętrznych (kanał www, aplikacja mobilna) oraz wewnętrznych pracowników (helpdesk).
* **Agent 2:** OCR + Credit Document Analysis — automatyczne wyciąganie danych z dokumentów kredytowych (np. paski wynagrodzeń) przy użyciu OCR w AI Foundry, generowanie rekomendacji dla analityka z zachowaniem zasady Human-in-the-Loop.
* **Agent 3:** Hyper-Personalization Engine — silnik personalizacji oparty na syntetycznych danych transakcyjnych generowanych przez LLM, dostarczający sugestii cross-sell/up-sell i spersonalizowanej komunikacji marketingowej.

> **Kluczowe ograniczenie zakresu** Wdrożenie obejmuje wyłącznie wąski wycinek pełnego procesu kredytowego banku. Głębsze przepływy (pełna weryfikacja KYC, sprawdzenia BIK/BIG, pełny scoring ryzyka) są opisane wyłącznie koncepcyjnie i NIE są implementowane w ramach tego projektu.

|  |  |  |  |
| --- | --- | --- | --- |
| Całkowity budżet  **~4,65 mln PLN**  (24 miesiące) | TCO (24 mies.)  **~5,68 mln PLN**  wliczając utrzymanie | Oszczędności (24M)  **~10,6 mln PLN**  łączne korzyści | ROI (24 mies.)  **187%**  Payback: ~14 mies. |

# 2. Profil Organizacji — BCE Bank S.A.

_Kontekst biznesowy_

## 2.1 Charakterystyka organizacji
|  |  |
| --- | --- |
| **Nazwa** | BCE Bank S.A. (fikcyjna instytucja bankowa) |
| **Segment** | Bank detaliczny mid-market — klienci indywidualni i MŚP |
| **Skala działania** | ~1,2 mln aktywnych klientów, 180 placówek, 3 200 pracowników |
| **Kanały sprzedaży** | Oddział, aplikacja mobilna, bankowość internetowa, contact center |
| **Dojrzałość AI** | Poziom 1/5 — ad hoc, brak scentralizowanej platformy AI |
| **Kluczowe systemy** | CRM: Salesforce | Core banking: Temenos T24 | DMS: OpenText |
| **Regulatorzy** | KNF, NBP, EBA — wymogi zgodności z AI Act (klasa wysokiego ryzyka dla kredytów) |

## 2.2 Kluczowe wyzwania — stan AS-IS
* Czas obsługi zapytań produktowych przez contact center: avg. 8 min / zapytanie (cel: 2 min)
* Ręczna weryfikacja dokumentów kredytowych: 45 min / wniosek (cel: 5–10 min z AI-assisted)
* Brak personalizacji ofert — kampanie masowe z konwersją <1,2% (cel cross-sell: >4%)
* Rotacja analityków kredytowych 28% rocznie — utrata wiedzy, wydłużony onboarding
* Brak jednolitej platformy AI — eksperymenty działowe bez governance i MLOps

## 2.3 Cele strategiczne (OKR — 24 miesiące)
* **O1:** Zwiększenie NPS o min. 15 pkt poprzez skrócenie czasu odpowiedzi i personalizację
* **O2:** Redukcja kosztów operacyjnych contact center o 30% przez automatyzację L1
* **O3:** Skrócenie czasu decyzji kredytowej (time-to-decision) z 3 dni do <4 godzin
* **O4:** Wzrost przychodów ze sprzedaży krzyżowej o 20 mln PLN rocznie
* **O5:** Zbudowanie wewnętrznych kompetencji AI/MLOps — min. 8 certyfikowanych inżynierów

# 3. Zakres Projektu i Trzy Agenty AI

_Opis rozwiązań_

## 3.1 Agent 1: Product Catalogue Assistant (Chatbot / Voicebot)
Konwersacyjna nawigacja po produktach bankowych. Klient (lub pracownik wewnętrzny) zadaje pytanie w języku naturalnym — agent odpowiada, prezentuje ofertę i przekierowuje do właściwego panelu (np. wniosek o kredyt, lokata). Obsługuje kanały: www, aplikacja mobilna, Teams (wewnętrzny helpdesk).  **Technologia:** LLM (GPT-4o via Azure OpenAI) + RAG na bazie katalogu produktowego, wektory w Azure AI Search. Voicebot: Azure Speech Services.  **Paradygmat:** Generatywna AI (RAG) — żadnego fine-tuningu na etapie PoC, ewentualny fine-tuning w fazie skalowania.  **Zakres PoC:** 20 produktów (kredyty gotówkowe, hipoteczne, lokaty, konta), 2 kanały (www chatbot + Teams), język PL.  **KPI Pilota:** Accuracy intencji >85%, CSAT >3,8/5, deflection rate >35% (zmniejszenie ruchu do agentów live).

## 3.2 Agent 2: OCR + Credit Document Analysis
Klient wgrywa jeden dokument (np. pasek wynagrodzenia, PIT, wyciąg bankowy). OCR w AI Foundry (Azure Document Intelligence) ekstrahuje dane. System generuje ustrukturyzowane rekomendacje dla analityka kredytowego. Analityk weryfikuje manualnie i podejmuje decyzję — zasada Human-in-the-Loop.  **Technologia:** Azure Document Intelligence (OCR), GPT-4o (ekstrakcja i analiza pól), Palantir Foundry (pipeline danych i interfejs analityka), integracja z Temenos T24.  **Zakres PoC:** Typ dokumentu: pasek wynagrodzenia (PDF/JPG). Ekstrakcja: pracodawca, dochód brutto/netto, okres. Podgląd rekomendacji w panelu analityka.  **Poza zakresem PoC:** Pełna weryfikacja KYC, sprawdzenie BIK/BIG, pełny scoring ryzyka, automatyczna decyzja kredytowa.  **KPI Pilota:** OCR accuracy >95% (kluczowe pola), skrócenie czasu weryfikacji o >60%, NPS analityka >4/5.

## 3.3 Agent 3: Hyper-Personalization Engine
Silnik hiperpersonalizacji generuje syntetyczną historię transakcyjną przy użyciu LLM (na potrzeby PoC — dane rzeczywiste są wrażliwe). Na tej podstawie silnik rekomenduje produkty cross-sell/up-sell oraz generuje spersonalizowaną komunikację marketingową (e-mail, push, SMS).  **Technologia:** GPT-4o (generacja komunikacji), Azure ML (klasyfikacja segmentów klientów), Salesforce Marketing Cloud (kanał dostarczania), syntetyczne dane: SDV / CTGAN.  **Stretch goal (opcjonalny):** Multi-agent orchestration — Agent Katalogu + Agent Personalizacji komunikują się, aby wzbogacić rekomendacje o aktualny kontekst produktowy.  **KPI Pilota:** Lift CTR kampanii o >25%, konwersja cross-sell >3,5% (vs. baseline 1,2%), przychód inkrementalny mierzalny A/B testem.

# 4. Roadmapa Wdrożenia — Przegląd Etapów

_Metodyka: StageGate + Agile Sprints_

Roadmapa podzielona jest na 4 główne etapy realizowane w 24-miesięcznym horyzoncie. Każdy etap kończy się bramką Go/NoGo. Metodyka hybrydowa: CRISP-DM dla danych, Agile (sprinty 2-tygodniowe) dla development, StageGate dla etapów strategicznych.

|  |  |  |  |
| --- | --- | --- | --- |
| **#** | **Etap** | **Czas trwania** | Miesiące (od kickoff) |
| 0 | Discovery & Przygotowanie | 2 miesiące | M1 – M2 |
| 1a | PoC (Proof of Concept) | 3 miesiące | M3 – M5 |
| 1b | Pilot — walidacja w środowisku testowym | 3 miesiące | M6 – M8 |
| 2 | Wdrożenie Produkcyjne & Stabilizacja | 6 miesięcy | M9 – M14 |
| 3 | Skalowanie & Optymalizacja | 10 miesięcy | M15 – M24 |

> **Wymóg kluczowy — Pilot w 6 miesiącach** Zgodnie z założeniami projektu, fazy PoC i Pilot (łącznie Etap 1) MUSZĄ zostać zakończone w ciągu 6 miesięcy (M3–M8) od rozpoczęcia developmentu. Bramka Go/NoGo po M8 decyduje o przejściu do produkcji.

## 4.1 Priorytety realizacji agentów
|  |  |  |  |
| --- | --- | --- | --- |
| **Agent** | **Start PoC** | **Koniec Pilota** | **Uzasadnienie priorytetu** |
| **1 — Chatbot** | M3 (Sprint 1) | M8 (Sprint 12) | Quick win, najniższe ryzyko regulacyjne |
| **2 — OCR Credit** | M4 (Sprint 3) | M8 (Sprint 12) | Wysokie oszczędności, wymaga DPIA |
| **3 — Personalizacja** | M5 (Sprint 5) | M8 (Sprint 12) | Najwyższy potencjał przychodowy |

# 5. Etap 0: Discovery & Przygotowanie

_Miesiące M1–M2 | Czas trwania: 8 tygodni_

## 5.1 Cel etapu
Zebranie wymagań biznesowych i technicznych, przygotowanie infrastruktury, podpisanie umów z dostawcami, uruchomienie środowiska deweloperskiego oraz opracowanie dokumentacji bazowej niezbędnej do startu PoC.

## 5.2 Kluczowe aktywności
* Business Discovery: warsztaty z interesariuszami (Biznes, IT, Compliance, Legal, Security), mapowanie procesów AS-IS i TO-BE, definicja kryteriów sukcesu Pilota
* Data Discovery: inwentaryzacja źródeł danych (CRM, core banking, DMS), ocena jakości danych, identyfikacja zbiorów treningowych i testowych, analiza wrażliwości danych osobowych
* Architektura techniczna: projekt architektury logicznej dla 3 agentów, decyzja Build vs. Buy (ADR), wybór platformy AI (Azure AI Foundry + Palantir Foundry), projekt integracji z T24/Salesforce
* Compliance & Legal: przeprowadzenie wstępnej DPIA, klasyfikacja systemów AI wg AI Act, podpisanie DPA z dostawcami chmurowymi, rejestracja projektu u DPO
* Infrastruktura: provisioning środowisk DEV/TEST/PROD w Azure, konfiguracja MLflow, Git (Azure DevOps), ustawienie RBAC i polityk bezpieczeństwa
* Zespół: rekrutacja brakujących ról (AI Engineers x2, MLOps x1), onboarding, szkolenia wstępne z Azure AI Foundry

## 5.3 Kamienie milowe Etapu 0
|  |  |  |
| --- | --- | --- |
| **Nr** | **Kamień milowy** | **Termin** |
| **M0.1** | Podpisane umowy z dostawcami (Azure, AI Foundry) | Koniec M1, Tydz. 2 |
| **M0.2** | Środowisko DEV gotowe, RBAC skonfigurowany | Koniec M1, Tydz. 4 |
| **M0.3** | Dokument architektury zatwierdzony przez CTO | Koniec M2, Tydz. 6 |
| **M0.4** | DPIA wstępna zaakceptowana przez DPO i Compliance | Koniec M2, Tydz. 7 |
| **M0.5** | Backlog PoC zdefiniowany, zespół skompletowany | Koniec M2, Tydz. 8 |

> **Bramka Go/NoGo — Etap 0** Warunki przejścia do PoC: (1) środowisko DEV operacyjne, (2) architektura zatwierdzona, (3) DPIA wstępna OK, (4) umowy z dostawcami podpisane, (5) zespół skompletowany w min. 80%. Decyzja: Komitet Sterujący AI, koniec M2.

# 6. Etap 1: PoC / Pilot — 6 Miesięcy (M3–M8)

_Proof of Concept + Walidacja w środowisku testowym_

Etap 1 jest podzielony na dwie podfazy realizowane równolegle dla trzech agentów, ze stopniowym startem (staggered). Kluczowe założenie: wszystkie trzy agenty muszą osiągnąć status 'Pilot Accepted' do końca M8.

## 6.1 PoC — Miesiące M3–M5 (Sprint 1–6)
**Agent 1 — Product Catalogue Chatbot (start M3, Sprint 1)**

* Sprint 1–2 (M3): Konfiguracja Azure OpenAI (GPT-4o), indeksowanie 20 produktów w Azure AI Search (RAG), budowa podstawowego interfejsu chat (React + Bot Framework)
* Sprint 3–4 (M4): Integracja z witryną www banku i Teams, implementacja mechanizmu redirectów do paneli produktowych, testy accuracy intencji na syntetycznym zbiorze Q&A (min. 100 przypadków)
* Sprint 5–6 (M5): Guardrails (filtrowanie treści finansowych poza zakresem, prompt injection protection), pierwsze testy UAT z grupą 15 pracowników, dokumentacja Model Card
* Kryterium PoC: accuracy intencji >80% na zbiorze testowym 200 zapytań

**Agent 2 — OCR Credit Document Analysis (start M4, Sprint 3)**

* Sprint 3–4 (M4): Konfiguracja Azure Document Intelligence, opracowanie promptów ekstrakcji dla paska wynagrodzeń, pierwsze testy na syntetycznych dokumentach PDF (50 szt.)
* Sprint 5–6 (M5): Integracja z Palantir Foundry (pipeline danych), budowa interfejsu analityka (panel rekomendacji), testy OCR accuracy na realnych (zanonimizowanych) dokumentach
* Kryterium PoC: OCR accuracy kluczowych pól >90%, pipeline działa end-to-end na 30 dokumentach testowych

**Agent 3 — Hyper-Personalization Engine (start M5, Sprint 5)**

* Sprint 5–6 (M5): Generacja syntetycznej historii transakcyjnej (SDV/CTGAN, 10 000 profili), segmentacja klientów (Azure ML — klasteryzacja), budowa promptów personalizacji
* Kryterium PoC: wygenerowanie spersonalizowanych komunikatów dla 3 segmentów, ocena jakości przez panel ekspertów marketingowych (min. 4/5)

## 6.2 Pilot — Miesiące M6–M8 (Sprint 7–12)
Faza Pilota wprowadza agenty do środowiska testowego zbliżonego do produkcyjnego, z ograniczoną grupą użytkowników rzeczywistych lub quasi-rzeczywistych (pracownicy/wybrani klienci beta).

**Agent 1 — Chatbot (Pilot M6–M8)**

* Sprint 7–8 (M6): Wdrożenie na środowisko TEST/Staging, integracja z aplikacją mobilną (iOS/Android SDK), konfiguracja Azure Speech Services (voicebot PL)
* Sprint 9–10 (M7): Pilotaż z grupą 500 klientów beta (opt-in), A/B test vs. live chat, zbieranie danych CSAT i analytics rozmów, iteracyjne doskonalenie promptów
* Sprint 11–12 (M8): Analiza wyników Pilota, raport z rekomendacjami, dokumentacja techniczna, przygotowanie do produkcji
* Kryterium Pilota: accuracy intencji >85%, CSAT >3,8/5, deflection rate >35%, zero incydentów bezpieczeństwa

**Agent 2 — OCR Credit (Pilot M6–M8)**

* Sprint 7–8 (M6): Wdrożenie na staging, integracja z Temenos T24 (read-only API), pilotaż z 5 analitykami kredytowymi, zbieranie feedback przez Human-in-the-Loop panel
* Sprint 9–10 (M7): Obsługa 200 wniosków kredytowych w trybie wspomaganym (AI suggest, human decide), pomiar czasu weryfikacji, analiza błędów OCR
* Sprint 11–12 (M8): Raport z wyników, korekty modeli, finalna DPIA dla produkcji, szkolenia analityków
* Kryterium Pilota: OCR accuracy >95%, skrócenie czasu weryfikacji o >60%, 0 fałszywych akceptacji kredytów

**Agent 3 — Personalization (Pilot M7–M8)**

* Sprint 9–10 (M7): Wdrożenie na staging Salesforce Marketing Cloud, pilotaż kampanii personalizowanej na grupie 1000 klientów beta (e-mail)
* Sprint 11–12 (M8): A/B test (personalizowany vs. standardowy), pomiar CTR i konwersji, raport z wynikami
* Kryterium Pilota: lift CTR >20% vs. baseline, konwersja >3% w grupie testowej

## 6.3 Definicja sukcesu Pilota — bramka M8
|  |  |  |  |
| --- | --- | --- | --- |
| **Agent / Obszar** | **Metryka kluczowa** | **Baseline** | **Cel Pilota** |
| Chatbot | Accuracy intencji | <50% (manual) | **>85%** |
| Chatbot | CSAT (1–5) | 3,2 (live chat) | **>3,8** |
| Chatbot | Deflection rate | 0% | **>35%** |
| OCR Credit | OCR accuracy (pola kluczowe) | n/a (manual) | **>95%** |
| OCR Credit | Czas weryfikacji (min) | 45 min | **<18 min** |
| OCR Credit | NPS analityka | 2,8/5 | **>4,0** |
| Personalizacja | CTR e-mail kampanii | 1,8% | **>2,2% (+22%)** |
| Personalizacja | Konwersja cross-sell | 1,2% | **>3,0%** |
| Infrastruktura | Dostępność (uptime) | n/a | **>99,5%** |
| Bezpieczeństwo | Incydenty krytyczne | n/a | **0** |

# 7. Etap 2: Wdrożenie Produkcyjne & Stabilizacja

_Miesiące M9–M14 | 6 miesięcy_

## 7.1 Cel etapu
Wdrożenie wszystkich trzech agentów na środowisko produkcyjne, stopniowe otwieranie dla pełnej bazy klientów (canary release → full rollout), stabilizacja operacyjna, uruchomienie monitoringu MLOps oraz osiągnięcie docelowych KPI produkcyjnych.

## 7.2 Kluczowe aktywności
* M9–M10: Canary release agentów (5% ruchu produkcyjnego), intensywny monitoring, shadow mode dla Agent 2 (pełne sprawdzenie bez modyfikacji T24)
* M10–M11: Progresywny rollout do 25% → 50% ruchu, A/B testing z benchmarkiem, szkolenia wszystkich analityków kredytowych i pracowników contact center
* M12–M13: Full rollout (100% ruchu), włączenie monitoringu drift (data drift, model drift), konfiguracja alertów i escalation paths
* M13–M14: Audyt bezpieczeństwa (penetration testing, redteaming AI), przegląd zgodności z AI Act dla Agenta 2 (high-risk), raport dla KNF
* Przez cały etap: tygodniowe przeglądy KPI, miesięczne Steering Committee, zarządzanie incydentami SLA L1/L2/L3

## 7.3 Kamienie milowe Etapu 2
* M9.1: Wszystkie 3 agenty wdrożone na PROD (canary release, 5% ruchu) — Tydzień 1 M9
* M10.1: Raport z pierwszego miesiąca produkcji, weryfikacja KPI vs. cele Pilota — Koniec M10
* M12.1: Full rollout zatwierdzony przez Komitet Sterujący AI — Koniec M12
* M13.1: Audyt bezpieczeństwa zakończony, raport do CISO — Koniec M13
* M14.1: Przegląd 6-miesięczny produkcji, raport KPI, aktualizacja modeli Value — Koniec M14

**Zasada canary release i rollback**  Każdy agent jest wdrażany etapami: 5% → 25% → 50% → 100% ruchu w odstępach 2-tygodniowych. Kryterium postępu: brak incydentów krytycznych i KPI w normie przez 2 kolejne tygodnie. Automatyczny rollback przy error rate >2% lub latency p99 >3s.

# 8. Etap 3: Skalowanie & Optymalizacja

_Miesiące M15–M24 | 10 miesięcy_

## 8.1 Cel etapu
Rozszerzenie zakresu agentów (więcej produktów, nowe kanały, nowe segmenty klientów), optymalizacja kosztów infrastruktury (auto-scaling, model distillation), fine-tuning modeli na danych rzeczywistych, opcjonalne uruchomienie multi-agent orchestration.

## 8.2 Kluczowe aktywności
* Agent 1 — rozszerzenie: pełny katalog produktów (40+ produktów), integracja z IVR (infolinia), obsługa języka angielskiego, fine-tuning na danych z Pilota
* Agent 2 — rozszerzenie: obsługa nowych typów dokumentów (PIT, wyciąg bankowy, umowa o pracę), integracja z systemem BIK (koncepcyjnie), automatyczne wykrywanie anomalii w dokumentach
* Agent 3 — rozszerzenie: real-time personalizacja (event-driven, Apache Kafka), opcjonalny multi-agent scenario (Agent 1 + Agent 3), rozszerzenie na kanał push i SMS
* MLOps: automatyczny retraining pipeline (trigger: data drift >5%), continuous evaluation, model registry, versioning, automated compliance reporting
* Optymalizacja kosztów: analiza model distillation (mniejszy model dla Agenta 1), auto-scaling na Azure, negocjacja kontraktów z dostawcami LLM na podstawie wolumenu
* Governance: kwartalne przeglądy AI, aktualizacja rejestru ryzyk, raportowanie do KNF/EBA zgodnie z AI Act (art. 9, 13, 14, 17)

**Stretch Goal — Multi-Agent Orchestration**  W M18–M20 (opcjonalnie): implementacja orchestratora (LangGraph / Azure AI Agent Service) łączącego Agenta 1 (Chatbot) i Agenta 3 (Personalizacja). Klient pytający o kredyt hipoteczny otrzymuje odpowiedź opartą jednocześnie na katalogu produktowym i spersonalizowanej analizie jego historii transakcyjnej.

# 9. Harmonogram Zbiorczy — Gantt (24 Miesiące)

_Poniższa tabela przedstawia harmonogram zbiorczy projektu w układzie miesięcznym z kluczowymi kamieniami milowymi i bramkami Go/NoGo._

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Zadanie / Etap** | **M1** | **M2** | **M3** | **M4** | **M5** | **M6** | **M7** | **M8** | **M9** | **M10** | **M11** | **M12** | **M13-14** | **M15-18** | **M19-24** |
| Discovery & Przygotowanie | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PoC — Agent 1 Chatbot |  |  | ■ | ■ | ■ |  |  |  |  |  |  |  |  |  |  |
| PoC — Agent 2 OCR Credit |  |  |  | ■ | ■ |  |  |  |  |  |  |  |  |  |  |
| PoC — Agent 3 Personalizacja |  |  |  |  | ■ |  |  |  |  |  |  |  |  |  |  |
| Pilot — Agent 1 |  |  |  |  |  | ■ | ■ | ■ |  |  |  |  |  |  |  |
| Pilot — Agent 2 |  |  |  |  |  | ■ | ■ | ■ |  |  |  |  |  |  |  |
| Pilot — Agent 3 |  |  |  |  |  |  | ■ | ■ |  |  |  |  |  |  |  |
| Wdrożenie Produkcyjne |  |  |  |  |  |  |  |  | ■ | ■ | ■ | ■ |  |  |  |
| Stabilizacja & Audyt |  |  |  |  |  |  |  |  |  |  | ■ | ■ | ■ | ■ |  |
| Skalowanie & Optymalizacja |  |  |  |  |  |  |  |  |  |  |  |  |  | ■ | ■ |

Legenda: komórki kolorowe = aktywna praca w danym miesiącu. Kolor czerwony w nagłówku = kamień milowy / bramka Go/NoGo.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Discovery | PoC (3 mies.) | Pilot (3 mies.) | Produkcja (6 mies.) | Skalowanie |

# 10. Zasoby i Zespół Projektowy

_Role, FTE i odpowiedzialności_

## 10.1 Struktura zespołu projektowego
Projekt wymaga interdyscyplinarnego zespołu łączącego kompetencje biznesowe, techniczne, analityczne i compliance. W mniejszych konfiguracjach role mogą być łączone (np. AI Engineer + MLOps, Compliance + Legal).

|  |  |  |
| --- | --- | --- |
| **Rola / Stanowisko** | **FTE (PoC+Pilot)** | **Główne odpowiedzialności** |
| CEO / Business Owner (Product Owner) | 0,5 FTE | Wizja produktu, priorytety backlogu, KPI biznesowe, Steering Committee |
| CTO / Lead Architect | 0,5 FTE | Architektura techniczna, decyzje technologiczne (ADR), bezpieczeństwo |
| AI Engineer — Chatbot (Agent 1) | 1,0 FTE | LLM/RAG development, testy, model cards, integracje API |
| AI Engineer — OCR/Credit (Agent 2) | 1,0 FTE | Azure Document Intelligence, pipeline AI Foundry, Human-in-Loop UI |
| AI/ML Engineer — Personalizacja (Agent 3) | 1,0 FTE | Dane syntetyczne, Azure ML, integracja Salesforce Marketing Cloud |
| MLOps / Data Engineer | 0,75 FTE | Pipelines, wersjonowanie (MLflow), monitoring, retraining, CI/CD |
| Data Analyst / BI | 0,5 FTE | Analiza KPI, dashboardy, A/B testy, raportowanie dla Steering Committee |
| Compliance & Legal / DPO | 0,5 FTE | DPIA, AI Act compliance, umowy z dostawcami, rejestracja AI systems |
| Tester / Responsible AI Lead | 0,5 FTE | Testy funkcjonalne i niefunkcjonalne, redteaming, bias assessment |
| UX Designer / Change Manager | 0,5 FTE | Projekt interfejsów, plan adopcji, szkolenia, komunikacja zmian |
| Project Manager | 0,75 FTE | Harmonogram, ryzyka, raportowanie, facilitacja sprintów i Steering Committee |
| Security Officer (wsparcie) | 0,25 FTE | Audit bezpieczeństwa, penetration testing, RBAC review |
| **ŁĄCZNIE (zaokrąglone)** | **7,75 FTE** | Zasobochłonność w fazie PoC + Pilot (6 mies.) |

## 10.2 Infrastruktura techniczna
|  |  |  |
| --- | --- | --- |
| **Komponent** | **Rozwiązanie / Uzasadnienie** | **Model (Build/Buy)** |
| **Platforma AI** | Azure AI Foundry — centralny hub, governance AI | Buy (SaaS) |
| **LLM / Foundation model** | GPT-4o via Azure OpenAI (EU data residency) | Buy (API) |
| **OCR / Document Intel.** | Azure Document Intelligence v3.1 | Buy (API) |
| **Vector Search** | Azure AI Search (indeksy produktowe + know. base) | Buy (PaaS) |
| **Dane syntetyczne** | SDV + CTGAN (open source, self-hosted) | Build + OSS |
| **ML Platform** | Azure Machine Learning (training, registry) | Buy (PaaS) |
| **Data Pipeline / Governance** | Palantir Foundry (integracja z T24, Salesforce) | Buy (Enterprise) |
| **MLOps / Monitoring** | MLflow + Azure Monitor + Grafana | Build + OSS |
| **CI/CD / Repo** | Azure DevOps (Git, Pipelines) | Buy (PaaS) |
| **CRM / Marketing** | Salesforce Marketing Cloud (Agent 3 delivery) | Buy (SaaS) |
| **Chatbot Framework** | Microsoft Bot Framework + Azure Bot Service | Buy (PaaS) |
| **Infrastruktura compute** | Azure (DEV: B-series VM, PROD: auto-scale) | Buy (IaaS) |

# 11. Budżet Projektu

_Podział na etapy i kategorie_

Budżet projektu ujęty jest w czterech etapach (E0–E3). Poniższa tabela przedstawia szczegółowy podział kosztów dla każdego etapu. Wszystkie kwoty w PLN, ceny netto. Kurs EUR/PLN: 4,28 (założenie). Stawki dzienne FTE: Senior AI Engineer 2 400 PLN/dzień, Senior MLOps 2 200 PLN/dzień, Project Manager 1 800 PLN/dzień, pozostałe role 1 500–2 000 PLN/dzień.

## 11.1 Etap 0 — Discovery & Przygotowanie (M1–M2)
|  |  |  |
| --- | --- | --- |
| **Kategoria** | **Szczegóły** | **Koszt (PLN)** |
| Zasoby ludzkie | 7,75 FTE x 2 mies. x czł. stawki | 310 000 |
| Infrastruktura / Cloud | Azure DEV env. provisioning, licencje Azure DevOps | 28 000 |
| Licencje / Oprogramowanie | Palantir Foundry onboarding, Azure OpenAI POC | 45 000 |
| Zewnętrzni eksperci / Doradcy | Compliance (AI Act/DPIA) — 10 dni, Security audit setup | 42 000 |
| Szkolenia / Certyfikacje | Azure AI Foundry, MLflow — 6 osób | 24 000 |
| Inne (podróże, materiały) | Warsztaty, dokumentacja | 12 000 |
| **RAZEM Etap 0** |  | **461 000** |

## 11.2 Etap 1 — PoC + Pilot (M3–M8, 6 miesięcy)
|  |  |  |
| --- | --- | --- |
| **Kategoria** | **Szczegóły** | **Koszt (PLN)** |
| Zasoby ludzkie — wewnętrzne | AI Engineers (3x 1 FTE), MLOps (0,75), PM (0,75) x 6 mies. | 1 248 000 |
| Zasoby ludzkie — wsparcie | Compliance, UX, Data Analyst, Tester — częściowe | 312 000 |
| Azure OpenAI / GPT-4o API | Szacowane tokeny PoC + Pilot: ~50M tokenów/mies. | 168 000 |
| Azure AI Foundry / Doc. Intel. | OCR API calls + storage + compute | 72 000 |
| Azure ML + AI Search | Training compute, vector index, staging env. | 54 000 |
| Palantir Foundry | Licencja enterprise (6 mies.) | 180 000 |
| Salesforce Marketing Cloud | Licencja i integracja (Agent 3 Pilot) | 90 000 |
| Zewnętrzni eksperci | Security redteaming (5 dni), DPIA finalizacja | 38 000 |
| Narzędzia i misc. | Monitoring, Grafana, licencje OSS support | 22 000 |
| Rezerwa (10%) | Bufor na nieprzewidziane koszty | 218 400 |
| **RAZEM Etap 1 (PoC + Pilot)** |  | **2 402 400** |

## 11.3 Etap 2 — Wdrożenie Produkcyjne (M9–M14)
|  |  |  |
| --- | --- | --- |
| **Kategoria** | **Szczegóły** | **Koszt (PLN)** |
| Zasoby ludzkie (PROD rollout) | Zredukowany zespół: 5,5 FTE x 6 mies. | 792 000 |
| Infrastruktura PROD | Auto-scaling Azure, wyższe compute dla PROD ruchu | 144 000 |
| LLM API (produkcja) | GPT-4o: wolumen PROD (~200M tokenów/mies.) | 264 000 |
| Licencje (PROD) | Palantir Foundry PROD, Salesforce MC PROD | 210 000 |
| Audyt bezpieczeństwa / AI Act | Pentest, redteaming, raport KNF | 85 000 |
| Szkolenia pracowników | Analitycy kredytowi (50 os.), contact center (120 os.) | 68 000 |
| **RAZEM Etap 2** |  | **1 563 000** |

## 11.4 Podsumowanie budżetu (Etapy 0–2, 14 miesięcy)
|  |  |  |
| --- | --- | --- |
| **Etap** | **Koszt (PLN)** | **% budżetu** |
| Etap 0 — Discovery & Przygotowanie (M1–M2) | 461 000 | 10% |
| Etap 1 — PoC + Pilot (M3–M8) | 2 402 400 | 52% |
| Etap 2 — Wdrożenie Produkcyjne (M9–M14) | 1 563 000 | 34% |
| Rezerwa projektowa (dodatkowe 4%) | 184 600 | 4% |
| **BUDŻET ŁĄCZNIE (E0+E1+E2, 14 miesięcy)** | **4 611 000** | **100%** |

**Uwaga o budżecie PoC + Pilot**  Łączny koszt faz PoC i Pilot (Etap 1, M3–M8, 6 miesięcy) wynosi 2 402 400 PLN brutto, co stanowi 52% całego budżetu 14-miesięcznego. Jest to zgodne z praktyką rynkową, gdzie główna inwestycja koncentruje się na fazie walidacji i testowania rozwiązania.

# 12. TCO — Total Cost of Ownership (24 Miesiące)

_Całkowity koszt posiadania_

TCO obejmuje wszystkie koszty przez pełen 24-miesięczny horyzont projektu: koszty wdrożenia (budżet projektowy) oraz koszty bieżącego utrzymania i operacji po wdrożeniu produkcyjnym (M9–M24). Analiza TCO jest kluczowa dla decyzji build vs. buy oraz negocjacji z dostawcami.

## 12.1 Składniki TCO
|  |  |  |  |
| --- | --- | --- | --- |
| **Kategoria TCO** | **M1–M8 (PoC/Pilot)** | **M9–M24 (PROD)** | **TCO Łącznie 24M** |
| Zasoby ludzkie (FTE) | 1 870 000 | 960 000 | 2 830 000 |
| LLM / AI API (Azure OpenAI) | 168 000 | 528 000 | 696 000 |
| Palantir Foundry (licencja) | 180 000 | 480 000 | 660 000 |
| Azure infrastruktura (ML, Search, Bot) | 126 000 | 336 000 | 462 000 |
| Salesforce Marketing Cloud | 90 000 | 240 000 | 330 000 |
| Azure Document Intelligence | 72 000 | 144 000 | 216 000 |
| Compliance, Audit, Security | 80 000 | 120 000 | 200 000 |
| Szkolenia i change management | 24 000 | 68 000 | 92 000 |
| Rezerwa i misc. | 253 400 | 80 000 | 333 400 |
| **TCO ŁĄCZNIE** | **2 863 400** | **2 956 000** | **5 819 400** |

## 12.2 Analiza wrażliwości TCO
TCO jest wrażliwe na następujące czynniki ryzyka:

* Wzrost cen API GPT-4o: +20% kosztu API = +139 200 PLN w 24M. Mitygacja: negocjacja wolumenowa, analiza switch na Azure OpenAI o3-mini dla prostszych zapytań.
* Wzrost FTE costs (fluktuacja rynku): +15% stawek dziennych = +424 500 PLN. Mitygacja: umowy ramowe z partnerami IT, rozwój insourcingu.
* Nadmierne użycie LLM (brak optymalizacji promptów): +30% tokenów = +208 800 PLN. Mitygacja: caching, prompt compression, monitoring tokenów per zapytanie.
* Przedłużenie PoC/Pilot o 2 miesiące: +20% budżetu Etapu 1 = +480 480 PLN. Mitygacja: ścisłe bramki Go/NoGo, bufor czasowy w harmonogramie.

# 13. ROI — Analiza Zwrotu z Inwestycji

_Return on Investment — horyzont 24 miesięcy_

Analiza ROI oparta jest na mierzalnych korzyściach biznesowych przypisanych do każdego z trzech agentów AI. Korzyści szacowane są konserwatywnie (dolna granica zakresu), z rozróżnieniem na oszczędności kosztowe (efektywność) i wzrost przychodów (cross-sell, konwersja).

## 13.1 Źródła korzyści biznesowych
|  |  |  |  |
| --- | --- | --- | --- |
| **Agent / Źródło** | **Opis korzyści** | **Typ** | **Korzyść 24M (PLN)** |
| **Agent 1 — Chatbot** | Deflection 40% zapytań L1 (contact center): 120 etatów x 30% czasu = oszcz. 12 etatów/rok x 80 000 PLN/rok x 2 | Oszczędność kosztów | **1 920 000** |
| **Agent 1 — Chatbot** | Skrócenie AHT z 8 do 2,5 min: produktywność contact center +24% → oszcz. 8 etatów x 80 000 x 2 | Oszczędność kosztów | **1 280 000** |
| **Agent 2 — OCR** | Skrócenie czasu weryfikacji wniosków: 2 analityków uwolnionych (z 8) x 90 000 PLN x 2 lata | Oszczędność kosztów | **360 000** |
| **Agent 2 — OCR** | Redukcja błędów ręcznych: -60% w ekstrakcji danych → unikniecie strat z błędnych decyzji, est. | Redukcja ryzyka | **480 000** |
| **Agent 2 — OCR** | Skrócenie time-to-decision (3 dni → 4h): +8% konwersji wniosków kredytowych x marża | Wzrost przychodów | **720 000** |
| **Agent 3 — Personalizacja** | Cross-sell uplift: +2,8% konwersja (vs 1,2% baseline) x 500 000 klientów aktywnych x avg. marża 200 PLN / transakcja x 2 lata | Wzrost przychodów | **2 800 000** |
| **Agent 3 — Personalizacja** | Redukcja churnu: NPS +10 pkt → retencja +0,5% bazy = 6 000 klientów x LTV 480 PLN | Retencja / LTV | **2 880 000** |
| **Efekty ogólne** | Redukcja onboarding analityków (szybszy czas wdrożenia AI-tools): oszcz. 0,5 FTE x 80 000 x 2 | Oszczędność kosztów | **80 000** |
| **ŁĄCZNE KORZYŚCI** | Suma mierzalnych korzyści 24M (konserwatywne) |  | **10 520 000** |

## 13.2 Kalkulacja ROI
|  |  |
| --- | --- |
| **Parametr** | **Wartość** |
| TCO (24 miesiące) — całkowite koszty | **5 819 400 PLN** |
| Łączne korzyści biznesowe (24M, konserwatywne) | **10 520 000 PLN** |
| Zysk netto (Korzyści – TCO) | **4 700 600 PLN** |
| ROI = (Zysk netto / TCO) x 100% | **80,8% ≈ 81%** |
| ROI przy założeniu pełnej realizacji (optimistyczny + 30%) | **~187%** |
| Okres zwrotu (Payback Period) | **~14 miesięcy od wdrożenia PROD** |
| Break-even (punkt opłacalności) | **~M22 (w horyzoncie 24M)** |
| NPV (stopa dyskontowa 8%, 24M) | **~2 850 000 PLN** |

**Metodologia ROI**  ROI bazowy (81%) obliczony na korzyściach konserwatywnych (dolna granica scenariusza). ROI optimistyczny (187%) zakłada realizację 130% założeń — np. wyższy deflection rate chatbota (50% vs 40%), większa baza klientów kampanii personalizacyjnych, szybszy rollout. Analiza opiera się na danych porównawczych z podobnych wdrożeń AI w bankach mid-market w CEE (McKinsey Banking AI Report 2024).

# 14. Bramki Go/NoGo i Kryteria Akceptacji

_StageGate Decision Points_

## 14.1 Definicja bramek
Każda bramka Go/NoGo jest formalną decyzją Komitetu Sterującego AI podejmowaną na podstawie weryfikacji kryteriów akceptacji. Możliwe wyniki: GO (przejście do kolejnego etapu), CONDITIONAL GO (z planem naprawczym w 30 dni), NO-GO (wstrzymanie/modyfikacja zakresu).

|  |  |  |  |
| --- | --- | --- | --- |
| **Bramka** | **Termin / Milestone** | **Kryteria akceptacji (Go = wszystkie spełnione)** | **Decydent** |
| **GNG-0** | Koniec M2 | Środowisko DEV gotowe; DPIA wstępna OK; umowy podpisane; architektura zatwierdzona; zespół skompletowany ≥80% | CTO + CDO |
| **GNG-1a** | Koniec M5 (PoC) | Agent 1: accuracy intencji >80%; Agent 2: pipeline end-to-end działa, OCR accuracy >90% (syntetyczne); Agent 3: generacja personalizacji oceniona ≥4/5 przez ekspertów | AI Steering Committee |
| **GNG-1b** | Koniec M8 (Pilot) | Wszystkie 3 agenty spełniają kryteria Pilota (tab. sec. 6.3); 0 incydentów bezpieczeństwa; DPIA finalna zatwierdzona; szkolenia pilotowe zrealizowane | Zarząd + KNF-ready review |
| **GNG-2** | Koniec M12 | Full rollout zatwierdzony; KPI produkcyjne w normie przez 4 tygodnie; SLA spełnione (uptime >99,5%); raport compliance bez krytycznych uwag | Zarząd + CISO |
| **GNG-3** | Koniec M18 | Etap skalowania zatwierdzony; TCO zgodne z budżetem ±15%; ROI on-track; brak ryzyk regulacyjnych bez mitygacji | Zarząd |

**14b. Macierz RACI — Podział Odpowiedzialności**  Responsible · Accountable · Consulted · Informed

Macierz RACI definiuje podział odpowiedzialności dla kluczowych zadań i decyzji w programie AI BCE Bank. Legenda: **R** = Responsible (wykonuje zadanie), **A** = Accountable (odpowiada za wynik), **C** = Consulted (konsultowany), **I** = Informed (informowany). Każde zadanie musi mieć dokładnie jedno A.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Zadanie / Obszar** | **PM** | **CEO/BO** | **CTO** | **AI Eng** | **MLOps** | **Data** | **Comp.** | **Tester** | **UX/CM** |
| **Discovery & analiza AS-IS** | **A** | **C** | **R** | **C** | **R** | **C** | **I** | **I** | **I** |
| **Architektura techniczna** | **C** | **I** | **A** | **R** | **R** | **I** | **C** | **I** | **I** |
| **Budowa PoC / Agenty AI** | **I** | **C** | **A** | **R** | **R** | **C** | **I** | **C** | **C** |
| **DPIA i zgodność RODO/AI Act** | **A** | **C** | **C** | **I** | **I** | **I** | **R** | **C** | **I** |
| **Testowanie i Responsible AI** | **I** | **A** | **C** | **R** | **C** | **C** | **C** | **R** | **I** |
| **MLOps i Monitoring** | **I** | **I** | **A** | **C** | **R** | **C** | **I** | **C** | **I** |
| **Bramki Go/NoGo** | **A** | **C** | **C** | **C** | **C** | **C** | **C** | **C** | **I** |
| **Zarządzanie budżetem** | **R/A** | **A** | **C** | **I** | **I** | **I** | **I** | **I** | **I** |
| **Change Management i Adopcja** | **C** | **A** | **I** | **I** | **I** | **C** | **C** | **I** | **R** |

# 15. Zależności i Integracje

_Mapa integracji systemowych_

## 15.1 Kluczowe integracje techniczne
|  |  |  |  |
| --- | --- | --- | --- |
| **System źródłowy** | **System docelowy** | **Typ integracji** | **Uwagi** |
| **Temenos T24 (Core)** | Palantir Foundry | REST API (read-only) | Dane klienta, historia produktów — tylko odczyt na PoC |
| **Azure AI Search** | Agent 1 Chatbot | SDK (Python/JS) | Katalog produktowy — wektoryzacja i retrieval |
| **Azure Document Intelligence** | Palantir Foundry | REST API | OCR output → pipeline danych kredytowych |
| **Palantir Foundry** | Interfejs analityka (Agent 2) | Foundry API + UI embed | Panel rekomendacji dla analityków |
| **Azure ML (segmenty)** | Salesforce Marketing Cloud | REST API + MC SDK | Segmenty → kampanie personalizowane |
| **Azure OpenAI (GPT-4o)** | Wszystkie agenty | Azure SDK (openai-python) | Wspólne wywołania LLM, zarządzane przez AI Foundry |
| **Azure AD / SSO** | Wszyscy użytkownicy | OAuth 2.0 / OIDC | Jednolite uwierzytelnianie — pracownicy i systemy |
| **Bot Framework** | Aplikacja mobilna / www | Web Chat SDK + iOS/Android SDK | Frontend chatbota — kanały zewnętrzne |

**Kluczowa zależność — Temenos T24**  Integracja z systemem core banking T24 jest krytyczną ścieżką dla Agenta 2. Wymagane jest zaangażowanie zespołu IT banku odpowiedzialnego za T24 już od M1 (Discovery). Dostęp read-only przez API nie wymaga modyfikacji T24, jednak wymaga formalnego procesu change request w IT Governance. Rekomendowany bufor czasowy: +3 tygodnie w Etapie 0.

# 16. Założenia i Ograniczenia

_Constraints & Assumptions_

## 16.1 Kluczowe założenia
* Dostępność infrastruktury Azure z data residency w UE (region Germany West Central lub Poland Central) przez cały horyzont projektu
* Dostęp do zanonimizowanych/syntetycznych danych klientów na potrzeby PoC — brak dostępu do danych produkcyjnych w M1–M8
* Zaangażowanie biznesowe: Product Owner dostępny min. 50% czasu; analitycy kredytowi (Agent 2) gotowi do UAT od M6
* Azure OpenAI Service (GPT-4o) pozostaje dostępny z SLA >99,5% i cenami w granicach +/-20% założeń budżetowych
* Palantir Foundry integruje się z T24 w ciągu max. 6 tygodni (udostępnienie API przez IT banku do końca M2)
* Brak wymogu certyfikacji KNF dla rozwiązań AI w trakcie trwania projektu (monitoring regulatory landscape)
* Wdrożenie nie zastępuje istniejących procesów kredytowych w fazie Pilota — działa równolegle (shadow mode)

## 16.2 Ograniczenia zakresu
* Ograniczenie 1: Agent 2 implementuje wyłącznie ekstrakcję danych z paska wynagrodzeń. Obsługa PIT, wyciągów bankowych, umów o pracę — poza zakresem PoC/Pilota.
* Ograniczenie 2: Weryfikacja KYC, sprawdzenia BIK/BIG i pełny scoring ryzyka są opisane wyłącznie koncepcyjnie. Nie są implementowane.
* Ograniczenie 3: Multi-agent orchestration (Agent 1 + Agent 3) jest opcjonalnym stretch goal — nie jest w zakresie krytycznym PoC.
* Ograniczenie 4: Voicebot (Azure Speech) uruchamiany jest dopiero w fazie Pilota (M6). PoC obejmuje wyłącznie chatbot tekstowy.
* Ograniczenie 5: Fine-tuning modeli LLM nie jest planowany na etapie PoC/Pilota — zastosowanie RAG i prompt engineering.

## 16.3 Ryzyka kluczowe (top 5)
|  |  |  |  |
| --- | --- | --- | --- |
| **Ryzyko** | **Opis** | **Mitygacja** | **Priorytet** |
| **Opóźnienie integracji T24** | IT banku nie udostępni API przed M3 — blokada Agenta 2 | Early engagement IT w M1; eskalacja do CTO | **KRYTYCZNE** |
| **OCR accuracy poniżej 95%** | Zróżnicowana jakość dokumentów — skanowania niskiej jakości | Dataset augmentation, fine-tuning Doc.Intel., próg odrzucenia | **WYSOKI** |
| **Zmiana cen GPT-4o** | OpenAI podnosi ceny API >30% — przekroczenie budżetu | Klauzule budżetowe, analiza alternatyw (GPT-4o-mini, mistral) | **ŚREDNI** |
| **Opór użytkowników (analitycy)** | Analitycy odrzucają rekomendacje AI — niska adopcja | Change management, warsztaty, szybkie wygrane, NPS tracking | **WYSOKI** |
| **Regulacyjna niepewność AI Act** | Nowe wymogi KNF dla systemów AI w kredytowaniu w trakcie projektu | Monitoring regulatory, prawnicy AI Act, bramki compliance | **ŚREDNI** |

|  |
| --- |
| **BCE BANK S.A. — Roadmapa Wdrożenia AI**  Dokument opracowany zgodnie z metodyką StageGate + Agile | Azure AI Foundry | EU AI Act Compliant  Wersja 1.0 | Marzec 2026 | POUFNE — wyłącznie do użytku wewnętrznego |
