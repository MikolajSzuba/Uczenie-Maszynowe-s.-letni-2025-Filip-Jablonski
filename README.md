
# ScriptGenerator – Kreator skryptów do filmów YouTube z wykorzystaniem AI

## 1. Struktura projektu
```
.
├── main.py                 # Główna aplikacja Kivy
├── api.py                  # Obsługa API Gemini (send_prompt, read_credentials)
├── credentials.txt         # Plik z kluczem API (pomijany w repo)
├── youtube_script.txt      # Zapisany skrypt z sesji
```

## 2. Użyte technologie
- **Python 3.11+**
- **Kivy** – GUI (interfejs użytkownika)
- **Google Generative AI (Gemini API)** – generacja treści przez LLM
- **Reular Expressions (re)** – formatowanie tekstu

## 3. Opis działania
Aplikacja umożliwia użytkownikowi wygenerowanie skryptu do filmu YouTube na podstawie parametrów:

- Temat filmu,
- Gatunek (np. edukacyjny, vlog, motywacyjny),
- Długość filmu,
- Styl wypowiedzi,
- Grupa docelowa,
- Opcjonalne wskazówki montażowe.

LLM generuje treść, która jest formatowana i może zostać zapisana do pliku. Komunikacja odbywa się przez darmowe API Gemini.

## 4. Bezpieczeństwo
- Klucz API przechowywany lokalnie w pliku `credentials.txt` (pomijany w `.gitignore`)
- Brak gromadzenia danych użytkowników
- Brak integracji z bazami zewnętrznymi – aplikacja działa lokalnie

## 5. Etyka w AI – zgodność z zasadami Microsoft

### Sprawiedliwość
Aplikacja została zaprojektowana tak, aby nie dyskryminować żadnej grupy użytkowników. Wybór grupy docelowej (np. młodzież, seniorzy) służy personalizacji treści, a nie ich wartościowaniu. Nie faworyzujemy żadnych ideologii, poglądów czy treści kontrowersyjnych.

### Niezawodność i Bezpieczeństwo
Generowana treść może zawierać błędy – użytkownik jest o tym informowany. Aplikacja nie powinna być wykorzystywana jako jedyne źródło wiedzy ani jako narzędzie do przygotowywania treści o charakterze medycznym, prawnym czy finansowym. Wszelkie treści powinny być **weryfikowane przed publikacją**.

### Prywatność i Bezpieczeństwo
Aplikacja nie zapisuje żadnych danych użytkownika. Dane są przetwarzane lokalnie (w aplikacji), a do API wysyłany jest jedynie prompt. Klucz API przechowywany jest w lokalnym pliku `credentials.txt` i nie jest publicznie udostępniany. Nie są tworzone żadne logi ani historia zapytań.

### Inkluzywność
Interfejs aplikacji został zaprojektowany z myślą o dostępności i prostocie, tak aby mógł być używany przez osoby z różnym poziomem zaawansowania technologicznego. Nie wymaga konta ani rejestracji.

### Przejrzystość
Użytkownik jest świadomy, że treści są generowane przez model językowy (LLM), a nie przez człowieka. Komunikaty w aplikacji jasno informują o wykorzystaniu AI oraz jej ograniczeniach.

### Odpowiedzialność
Twórcy aplikacji nie ponoszą odpowiedzialności za skutki wykorzystania treści wygenerowanej przez model. W szczególności:
- Nie gwarantujemy zgodności treści z faktami.
- Nie odpowiadamy za potencjalne naruszenia praw autorskich.
- Użytkownik powinien **zweryfikować treść przed publikacją**, aby uniknąć szerzenia dezinformacji.

Aplikacja działa jako **asystent kreatywny**, nie jako autonomiczne źródło wiedzy.

## 6. Instrukcja obsługi aplikacji

### Wymagania systemowe:
- Python 3.10 lub nowszy
- Połączenie z internetem (do komunikacji z API Gemini)

### Wymagane biblioteki:
Aby uruchomić aplikację, należy wcześniej zainstalować poniższe biblioteki:

```bash
pip install kivy
pip install google-genai
```

### Jak uruchomić aplikacje?

Należy uruchomić terminal w folderzez programem i wpisać:

```bash
python YoutubeScriptGenerator.py
```

Następnie wpisać **API_key** we wskazanym polu **(wymagane)**

Należy wygenerować go na stronie https://aistudio.google.com/apikey 

Po wybraniu wybranych opcjii należy kliknąć **Generate Script**

### Rekomendacje dla użytkownika

- Traktuj wyniki AI jako **inspirację**, nie gotowy produkt.
- Przeglądaj i modyfikuj wygenerowane skrypty przed publikacją.
- Nie wykorzystuj AI do tworzenia treści szkodliwych, fałszywych lub nieetycznych.
- Zadbaj o oryginalność materiałów – AI nie gwarantuje unikalności treści.
