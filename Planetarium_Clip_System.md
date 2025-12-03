<h2 align="center">Schulplanetarium Fulldome Titelsystem</h2>


![Image description](images/Banner_SP_Broschuere_20251129_193322.png)

<br>

<p align="center"><b>Organisationshandbuch und Clip-Übersicht</b></p>
<p align="center"><em> Implementierung von P.Holz</em></p>


<br>

---

# Inhaltsverzeichnis

1. [Zielsetzung](#ziele)
2. [Dateinamen-Schema](#schema)
3. [Clip-Katalog: FullDome-Filme](#katalog-fulldome)
4. [Clip-Katalog: Kurzclips](#katalog-kurzclips)
5. [Clip-Katalog: Kurzfilme](#katalog-kurzfilme)
6. [ISS-Filme und Kombinationen](#iss-kombinationen)
7. [Digitale Architektur](#digitale-architektur)
8. [Fazit und nächste Schritte](#fazit)

---
\newpage
<a id="ziele"></a>
# Ziel - mehr Ordnung im Fulldome Ordner

Das Schulplanetarium verfügt über eine umfangreiche Sammlung von hochwertigen Planetariums-Clips und Filmen. Leider erlaubt der ShiraPlayer lediglich einen Ordner als Ressource für alle Dateien. Um diesen effizient nutzen zu können, ist eine systematische Verwaltung erforderlich.

### Hauptziele des Systems:

- **Schnelle Auffindbarkeit:** VorführerInnen können innerhalb von Sekunden den passenden Clip für ihre Vorstellung finden
- **Konsistente Qualität:** Klare Klassifizierung nach Altersgruppe und Thema
- **Professionelle Struktur:** Einheitliches Dateinamenschema und Metadaten
- **Team-Kommunikation:** Alle haben Zugriff auf aktuelle Informationen und persönliche Notizen
- **Archivverwaltung:** Über den Katalog können ungenutzte Clips nach gemeinsamer Abstimmung archiviert werden

### Nutzen für das Team:

Der zentrale Katalog mit konsistenten Metadaten (Dauer, Zielgruppe, Tags, persönliche Notizen) ermöglicht:
- Optimale Programmplanung für verschiedene Altersgruppen
- Schnelle Reaktion auf kurzfristige Anfragen während der Vorstellung
- Wissenstransfer zwischen Team-Mitgliedern
- Identifikation von Lücken im Content-Portfolio

---

# Dateinamen-Schema

## Aufbau des Systems

Das Dateinamenschema folgt einem konsistenten Pattern, das ermöglicht, alle Informationen bereits aus dem Dateinamen abzulesen:

### Pattern

`[ALTERSGRUPPE]_[CONTENT-TYP]_[TITEL]_[DAUER]`

### Erklärung der Komponenten

| Komponente | Kürzel | Bedeutung | Beispiele |
|------------|--------|-----------|----------|
| **Altersgruppe** | 2 Buchstaben | Zielgruppe | `gs` (Grundschule), `ms` (Mittelstufe), `os` (Oberstufe), `vs` (Vorschule), `exo` (Spezial), `iss` (ISS) |
| **Content-Typ** | 4–6 Buchstaben | Art des Contents | `mov` (Fulldome-Film), `clip` (Clip), `short` (Kurzfilm 5–15 min), `skript` (Shira-Player Skript) |
| **Titel** | frei | Beschreibender Name | `magic_globe`, `solar_system`, `star_birth_death` |
| **Dauer** | Zahl + Einheit | Länge des Videos | `2_min`, `20_min`, `45_min` |

### Beispiele

```
gs_mov_Magic_Globe_29_min.mp4
├─ gs = Grundschule
├─ mov = FullDome Film
├─ Magic_Globe = Filmtitel
└─ 29_min = Dauer

os_clip_gdm_solar_system_milky_way_6_20_min.mp4
├─ os = Oberstufe
├─ clip = Clip
├─ gdm_solar_system_milky_way = Titel
└─ 6_20_min = Dauer

iss_short_tim_peake_ohne_sprache_10_min.mp4
├─ iss = ISS (Special Category)
├─ short = Kurzfilm (5–15 min)
├─ tim_peake_ohne_sprache = Titel
└─ 10_min = Dauer
```

---
\newpage
<a id="schema"></a>
# Dateinamenschema-Tabelle

| Altersgruppe | Kürzel | Typen | Beispiel |
|-------------|--------|-------|---------|
| Vorschule | `vs_` | `mov`, `clip` | `vs_mov_Der_Mond_45_min` |
| Grundschule | `gs_` | `mov`, `clip`, `short`, `skript` | `gs_mov_Cpt_Schnuppes_Weltraumreise_26_min` |
| Unterstufe | *integriert in gs/ms* | `clip`, `short` | `gs_clip_two_pieces_glass_jupyter_1_30_min` |
| Mittelstufe | `ms_` | `mov`, `clip`, `short` | `ms_mov_A_hot_and_energetic_universe_30_min` |
| Oberstufe | `os_` | `mov`, `clip`, `short` | `os_mov_Ferne_Welten_fremdes_Leben_54_min` |
| ISS-Programme | `iss_` | `clip`, `short` | `iss_short_tim_peake_ohne_sprache_10_min` |
| Spezial (Exoplaneten) | `exo_` | `clip`, `short` | `exo_clip_rubin_exoplanet_transit_2_min` |
| Jena-Filme | `x_` | `mov`| `x_Jena_Explore_28_min` |
| Ungenutzt | `z_` | `mov` | `z_mov_space_opera_41_min` |

---

# Kategorie-Übersicht

## Strukturierung der Inhalte

Die gesammte Sammlung ist sowohl in Altersgruppen eingeteilt (siehe oben) als auch in vier Hauptkategorien von Filmtypen eingeteilt (plus Skripte), um eine schnelle Übersicht und Navigation zu ermöglichen. Diese werden auf der nächsten Seite vorgestellt.

**Die Grundlage aller Clips und Shorts besteht den Fulldome-Filmen welche durch den OpenShot Movie Editor geschnitten werden und anschließend im ShiraPlayer Encoder codiert wurden.**

Teils gibt es verschiedene Längen von einem Film, weil in der Praxis oft die Zeit knapp ist und es dann hilfreich ist - eine verkürzte Version zeigen zu können.

\newpage
### 1. FullDome-Filme *mov* (>15 Minuten)

Diese sind die Highlight-Features des Planetariums. Sie werden für längere Vorstellungen oder dedizierte thematische Shows genutzt.  <br>


**Eigenschaften:**
- Längere Produktionen (meist 20–50 Minuten)
- Professionelle Animation und Visualisierung
- Ideal für Schulklassen, Familienvorstellungen oder spezielle Events
- Hoher immersiver Wert

**Umfang:** 24 Filme

---

### 2. Kurze Sequenzen *clips* (<5 Minuten)

Kurze, präzise Inhalte für spezifische Themen. Diese werden häufig als Einstiege oder zur Wiederholung verwendet.

**Eigenschaften:**
- Fokussiert auf ein Thema
- Teils mit Bemerkung *intro* oder *outro* um die Show zu beginnen/beenden
- Ideal zum Kombinieren in thematischen Programmen
- Sollte meist verbal eingeleitet/begleitet werden ("Wir schauen uns mal einen Ausschnitt an..")

**Umfang:** 20 Clips

---

### 3. Kurzfilme *short* (5–15 Minuten)

Die Mittelpunkt-Kategorie – lange genug für tiefere Erklärungen, kurz genug für flexible Programmgestaltung. Beispielsweise lässt sich FETU (30min) super in 3 shorts aufteilen.

**Eigenschaften:**
- Kompakte, eigenständige Inhalte
- Ideal als Hauptprogramm oder Programm-Baustein
- Vermitteln komplexere Konzepte
- Zeit für narrative oder erklärende Elemente

**Umfang:** 17 Kurzfilme

---

### 4. ISS-Programme (Altersübergreifend)

Spezielle Inhalte zur Internationalen Raumstation – vom Raketenstart bis zur Erdumrundung. Funktioniert für praktisch alle Altersgruppen - da hier selbst mitgesprochen wird.

**Eigenschaften:**
- Gute Immersion über Raketenstarts oder Blicke auf die ISS bzw auf die Erde
- Möglichkeit über eigenes Narrativ auch das Thema auf Ökosysteme - Klimawandel / Nachhaltigkeit zu richten
- Haupt-Baustein ist die Tim Peake-Dokumentation
- Kombinierbar mit verschiedenen Längen (je nach Zeit in der Vorstellung)
- Bieten für mich den besten Abschluss einer Vorstellung (durch den Zoom raus und wieder rein)

**Umfang:** 11 ISS-Videos

<br>

---

## Zielgruppen

| Gruppe | Kürzel | Alter | Fokus |
|--------|--------|-------|-------|
| Vorschule | `vs_` | 3–6 Jahre | Märchen, Spaß, visuelle Erfahrung |
| Grundschule | `gs_` | 6–12 Jahre | Sonnensystem, Tag/Nacht, Grundlagen |
| Unterstufe | (in gs/ms) | 10–14 Jahre | Erste wissenschaftliche Vertiefung der Grundlagen |
| Mittelstufe | `ms_` | 12–15 Jahre | Sterne mit Zahlen, Astronomie, Physik & Chemie |
| Oberstufe | `os_` | 15–18+ Jahre | Astrophysik, Forschung, Dunkle Materie|
| ISS | `iss_` | Alle Altersgruppen | Raumfahrt, aktuelle Raumstation |

---
<a id="katalog-fulldome"></a>
# Clip-Katalog: FullDome-Filme

## Alle verfügbaren Filme (>15 min)


| # | Titel | Dauer | Altersgruppe | Kat. | Thema | Notizen |
|---|-------|-------|-------------|-----------|-------|---------|
| 1 | 321 Liftoff | 36 min | Grundschule | Fulldome | Raumfahrt, Raketen | Etwas dramatisch am Ende, insgesamt gut für GS |
| 2 | Captain Franken-Schnuppe ohne Sonne | 20 min | Grundschule | Fulldome | Sonnensystem | Unglücklich geschnitten (Sonne fehlt) |
| 3 | Captain Schnuppes Weltraumreise | 26 min | Grundschule | Fulldome | Sonnensystem | Kürzere Version, einige Dialoge gekürzt |
| 4 | Captain Schnuppes Weltraumreise | 34 min | Grundschule | Fulldome | Sonnensystem | Perfekt für 1.–2. Klasse |
| 5 | Magic Globe | 29 min | Grundschule | Fulldome | Erde, Jahreszeiten | Grundlagen erklären, Kurzversion |
| 6 | Magic Globe | 39 min | Grundschule | Fulldome | Erde, Jahreszeiten | Erweiterte Version |
| 7 | Polaris (Deutsch) | 29 min | Grundschule | Fulldome | Jahreszeiten, Erdachse | Super für GS und Unterstufe |
| 8 | Polaris (Englisch) | 29 min | Grundschule | Fulldome | Jahreszeiten, Erdachse | Englische Version, auch auf Japanisch verfügbar |
| 9 | Two Small Pieces Of Glass | 23 min | Grundschule | Fulldome | Teleskope, Astronomie | Storytelling zur Geschichte der Teleskope |
| 10 | A Hot and Energetic Universe | 30 min | Mittelstufe | Fulldome | Hochenergie-Astrophysik | Viele gute Animationen |
| 11 | Back to the Moon | 25 min | Mittelstufe | Fulldome | Mond, Raumfahrt | Erste Hälfte besser, danach Google-Focus |
| 12 | Dawn of the Space Age | 30 min | Mittelstufe | Fulldome | Raumfahrt, Geschichte | Kurze Version |
| 13 | Dawn of the Space Age | 41 min | Mittelstufe | Fulldome | Raumfahrt, Geschichte | Lange Version |
| 14 | From the Earth to the Universe | 32 min | Mittelstufe | Fulldome | Sonnensystem, Galaxien | Empfohlen ab 5. Klasse |
| 15 | Out There | 30 min | Mittelstufe | Fulldome | Exoplaneten, Astrobiologie | Für 5. Klasse etwas schwierig |
| 16 | Ferne Welten, Fremdes Leben | 54 min | Oberstufe | Fulldome | Exoplaneten, Leben | Für Klasse 10+ |
| 17 | Geheimnis Dunkle Materie | 39 min | Oberstufe | Fulldome | Dunkle Materie, Kosmologie | Schöne Anfangssequenz |
| 18 | Phantom of the Universe | 28 min | Oberstufe | Fulldome | Dunkle Materie, Teilchenphysik | Fortgeschrittenes Thema |
| 19 | The Sun (German) | 25 min | Oberstufe | Fulldome | Sonne, Kernfusion | Erklärt Aufbau und Aktivität der Sonne |
| 20 | Space Opera | 41 min | Unsortiert | Fulldome | Musik, Weltraum | Wird sehr selten gezeigt |
| 21 | Seeing | 26 min | Mittelstufe | Fulldome | Sehen, Auge | Zeiss-Sponsoring |
| 22 | KIRA Movie | 24 min | Unsortiert | Fulldome | Spielfilm, Umwelt | Wird sehr selten gezeigt |
| 23 | Jena: Der Notenbaum | 49 min | Vorschule | Fulldome | Musik | Nur bei Sternevent-Events |
| 24 | Regenbogenfisch mit Sternen | 44 min | Vorschule | Fulldome | Geschichte, Sterne | lang und ohne viel Astronomie |
---
\newpage
<a id="katalog-kurzclips"></a>
# Clip-Katalog: Kurzclips (<5 Min)

## Kurze, prägnante Inhalte für flexible Programmgestaltung

### Grundschule

| Titel | Dauer | Thema | Notizen |
|-------|-------|-------|---------|
| Blue | 2:10 | Wasser, Intro | Besonders für jüngere Kinder geeignet |
| Magic Globe: Tag und Nacht | 2:07 | Erde, Rotation | Kurzer thematischer Ausschnitt |
| Magic Globe: Jahreszeiten | 2:25 | Jahreszeiten, Erde | Zeigt Amazonas und Nordpol |
| Petty Tyrant | 1:49 | Perspektivwechsel, Intro | Fliege-Perspektive vorbereitet auf Planetarium |
| Polaris: Jahreszeiten | 0:34 | Jahreszeiten, Erde | Sehr kurz – muss verbal eingeleitet werden |
| Two Pieces Glass: Jupiter | 1:33 | Jupiter, Galilei | Erklärt Bedeutung der Astronomie |
| Day Earth (kurz) | 0:26 | Tag-Nacht-Zyklus | Verkürzte Variante |
| Day Earth (lang) | 2:34 | Tag-Nacht-Zyklus | Komplette Variante – kann m. M. nach ins Archiv |
| Skripte: | Selbst eingesprochen | altersunabhängig |
| Solar System (Skript) | 3:05 | Sonnensystem | Sonne mit Planeten und Bahnen |
| Seasons Skripte | 2 - 3 | Jahreszeiten, Sternzeichen | versch. Versionen je nach Zeit |

\newpage

### Mittelstufe

| Titel | Dauer | Thema | Notizen |
|-------|-------|-------|---------|
| Ahead: Star Birth & Death | 3:07 | Sterne, Schwarze Löcher | Kann mit oder ohne Ton gezeigt werden |
| Ahead: Star Birth & Death (erweitert) | 4:47 | Sterne, Neutronensterne | Zusätzlich Neutronensterne |
| Back to Moon *intro* | 4:59 | Mond, Ressourcen | Schöne Animation, 70 Jahre Mond-Erforschung |
| Raumschwindel | 3:18 | Kunstfilm, Weltraum | Achtung: Kann Schwindel auslösen! |
| Star Sizes | 0:53 | Sterngrößen | STUMM schalten! Vergleich von Sternen |
| The Sun: Intro | 1:19 | Sonne, Sterne | Kurze Einführung |
| Skripte: | Selbst eingesprochen | altersunabhängig |
| Solar System (Skript) | 3:05 | Sonnensystem | Sonne mit Planeten und Bahnen |
| Seasons Skripte | 2 - 3 | Jahreszeiten, Sternzeichen | versch. Versionen je nach Zeit |


### Oberstufe 

| Titel | Dauer | Thema | Notizen |
|-------|-------|-------|---------|
| Intro: Listen | 2:31 | Musik, Schall, Wellen | Visualisierung von Frequenzen |
| Intro: Neptun | 2:20 | Neptun, Wissenschaftliche Methode | Entdeckungsgeschichte mit Mathematik |

---
\newpage
<a id="katalog-kurzfilme"></a>
# Clip-Katalog: Kurzfilme (5–15 Min)

### Grundschule

| Titel | Dauer | Thema | Notizen |
|-------|-------|-------|---------|
| FETU: Solar System | 6:42 | Sonnensystem | Merkur bis Kuipergürtel |
| Collage: Launch, Orbit, Peake | 11:11 | ISS, Raumfahrt | Immersive Erfahrung des Raketenstarts |
| Jena: Mond & Märchen Phasen | 3:09 | Mond, Phasen | Nur bei Sternevent-Events |

### Mittelstufe

| Titel | Dauer | Thema | Notizen |
|-------|-------|-------|---------|
| FETU Part 1 | 9:19 | Astronomie-Geschichte | Antike bis Neuzeit |
| FETU Part 2 | 10:18 | Sonnensystem | Planeten, Monde, Asteroiden |
| FETU Part 3 | 10:01 | Universum | Galaxien, Schwarze Löcher – wird selten gezeigt |
| Apollo 11 (ohne Gelaber) | 12:45 | Mondlandung, Raumfahrt | Eigenvertonung möglich |
| Apollo 11 | 12:45 | Mondlandung, Raumfahrt | Mit Originalton |
| AIDA: Asteroid Deflection | 7:42 | Asteroiden, Planetare Verteidigung | ESA/DART Mission, 2022 erfolgreich |

### Oberstufe 

| Titel | Dauer | Thema | Notizen |
|-------|-------|-------|---------|
| GDM: Solar System & Milky Way | 6:17 | Sonnensystem, Galaxie | Zeigt Einbettung in Milchstraße |
| The Sun: Part One | 7:17 | Sonne, Kernfusion | Schönes Intro |
| The Sun: Properties | 4:48 | Kernfusion, Sonnenaktivität | Anspruchsvollere Erklärungen |
| The Sun: Part Three | 8:12 | Sonnenaktivität, Magnetfeld | Polarlichter und Sonnenstürme |

## Besondere Themen - Exoplaneten

| Titel | Dauer | Thema | Notizen |
|-------|-------|-------|---------|
| Out There | 11:10 | Exoplaneten, Leben im All | Part aus „Out There" |
| Ferne Welten | 20:07 | Exoplaneten, Erforschung | Aus „Ferne Welten" Film |
| Exoplanet Transit (Rubin) | 2:23 | Exoplaneten, Transitmethode | Teil von Fabiennes Exoplaneten-Programm |

<br>

### ISS

| Titel | Dauer | Thema | Notizen |
|-------|-------|-------|---------|
| ISS: Orbit BlueDot | 1:30 | ISS, Erde | Beschreibung nachzutragen |
| ISS: Sojus Launch | 1:16 | Raketenstart, Raumfahrt | Gut für Immersion vor ISS-Film |
| ISS: Sojus Orbit | 1:58 | ISS, Raumfahrt | Langwierig, kann ins Archiv |
| ISS: Anflug | 1:24 | ISS, Anflug | Nie gezeigt – kann ins Archiv |
| ISS: Anfang | 5:46 | Leben auf ISS | Ohne Sonnensystem |
| ISS: Solar System Outro | 3:20 | Erde, Sonnensystem | Wenn nur 3 min Zeit bleibt |
| ISS: Ohne Sprache | 9:23 | ISS + Sonnensystem | der **Klassiker** |
| ISS: mit Sprache | 9:23 | ISS + Sonnensystem | Org. Version auf Englisch |
| ISS: Collage  | 11:11 | Launch, Orbit, Peake | Die ultimative ISS-Experience |

---

\newpage
<a id="iss-kombinationen"></a>
# ISS-Filme und Kombinationen

## Spezielle Inhalte zur Internationalen Raumstation

Die ISS-Videos sind perfekt für die Vermittlung von Raumfahrt und der aktuellen Arbeit auf der Internationalen Raumstation. Sie funktionieren für praktisch alle Altersgruppen mit unterschiedlichem Fokus.

### Kurzclips (Einstiege)

- **Sojus Launch (1:16):** Raketenstart von Kasachstan – ideal für Immersion
- **Sojus Orbit (1:58):** Flugbahn zur ISS – optionale Vorbereitungssequenz
- **Solar System Outro (3:20):** Wenn nur 3 Minuten Zeit bleiben

### Kurzfilme (Hauptprogramm)

- **Tim Peake: Anfang (5:46):** Fokus auf ISS und Erde
- **Tim Peake: Ohne Sprache (9:23):** Der Klassiker – mit Eigenvertonung möglich
- **Tim Peake: Mit Sprache Englisch (9:23):** Original-Dokumentation
- **Collage: Launch, Orbit, Peake (11:11):** Die ultimative ISS-Experience

### Kombinationsmöglichkeiten

**Für Grundschule:**
Sojus Launch (1:16) + Tim Peake Anfang (5:46) + Eigenvertonung
Collage: Launch, Orbit, Peake (11:11) + Eigenvertonung 

**Für Mittelstufe :**
Tim Peake ohne Sprache (9:23) + Eigenvertonung
Solar System Outro (3:20) - Wenn man das Sonnensystem noch nicht besproch hat

**Für Oberstufe/Erwachsene :**
Einführung in das Thema (flatmedia)  + Tim Peake mit Sprache Englisch (9:23) + diskutieren
Collage: Launch, Orbit, Peake (11:11) - mit wissenschaftlichen Erklärungen und Zahlen (Stichwort Fluchtgeschwindigkeit)

---

\newpage

<a id="digitale-architektur"></a>
# Digitale Architektur

## Datenspeicherung und Master-Daten

Die komplette JSON-Datei mit allen Metadaten ist zentral gespeichert und enthält:

- Alle Video-IDs und Dateipfade
- Dauer und Zielgruppen
- Thematische Tags
- Persönliche Notizen des Teams
- Längen-Kategorisierung

### Zugriff auf die Master-Datei

**Speicherort:**  Freigegebener Ordner ShiraPlayer `planetarium_clips_12_2025.json`

**Inhalt pro Clip:**
- ID, Dateipfad, Länge (Sekunden + Formatierung)
- Kategorie (FullDome, Clip, Short, Skript)
- Titel, Altersgruppe, Längen-Kategorie
- Ausführliche Beschreibung
- Zielgruppe(n)
- Tags (thematisch kategorisiert)
- Persönliche Team-Notizen

### Beispiel JSON-Eintrag

```json
{
  "id": "os_mov_Ferne_Welten_fremdes_Leben_54_min",
  "filename": "os_mov_Ferne_Welten_fremdes_Leben_54_min.mp4",
  "duration_seconds": 3180.03,
  "human_duration": "53:00",
  "category": "fulldome_film",
  "title": "Ferne Welten fremdes Leben",
  "educational_level": "Oberstufe",
  "description": "Film über die Suche nach Exoplaneten und außerirdischem Leben...",
  "target_group": "Oberstufe, Erwachsene",
  "tags": ["Ausserirdisches Leben", "Exoplaneten", "Habitabilität"],
  "notes": "Personal notes..."
}
```

---

<a id="fazit"></a>
# Fazit und nächste Schritte

Das neue Clip-System schafft **Klarheit, Effizienz und Professionalität** in der Verwaltung des Planetariums-Contents. Mit konsistenten Dateinamen, standardisierten Metadaten und dieser umfassenden Übersicht kann das Team schnell die perfekten Inhalte für jede Vorstellung finden.

### Nächste mögliche Schritte

1. **JSON-Datei als zentrale Datenbasis etablieren**
   - Zentrale Speicherung für alle VorführerInnen zugänglich
   - Regelmäßige Backups sofern neue Filme oder Clips dazu kommen
   - grafische Oberfläche um nach Tags zu suchen
   - vll. Implementierung in "Mitarbeiterbereich" in der Webseite

2. **Neues Kapitel "Schnellreferenz" **
   - Kurzübersicht mit Beispielhaftem nutzen von Fulldome und Flatmedia Inhalten
   - Verbindung dieser PDF mit den Beispielhaften Vorführungs-Skripts zu einem umfassenden Handbuch

3. **Team-Training für Dateinamenschema**
   - Schulung neuer VorführerInnen - sofern das System in Gießen gut funktioniert
   - Best Practices für Ergänzungen und Aktualisierungen

4. **Regelmäßige Aktualisierung der Notizen**
   - Team-Feedback sammeln
   - Notizen sammeln und entsprechend aktualisieren
   - Saisonale Anpassungen dokumentieren

5. **Archivierung selten genutzter Inhalte**
   - Jährliche Überprüfung -> Inaktive Clips ins Archiv verschieben
   - Speicherplatz optimieren

Link zum OneDrive Ordner mit JSON und Clip Dateien (PW  = *schulplanetarium*):
<a href="https://1drv.ms/f/c/78c27a82208a75e9/Eul1iiCCesIggHiDRQEAAAABOYOSHCKT7bsMcRuosGB9Sw?e=QqjNPS"> ShiraPlayer Ordner</a>
Vorerst nur Lese Berechtigung. Bei Fragen gerne an:
<a href="mailto:philipp@schulplanetarium.de">philipp@schulplanetarium.de</a>
