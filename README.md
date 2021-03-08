# Lista 8 - Języki programowania wysokiego poziomu

**Python (8) - Pliki**

(1) Operacje na plikach są możliwe dzięki obiektom plikowym, np:
fo = open(’plik.txt’,’w’)
TU COŚ WPISUJEMY DO PLIKU
fo.close()
Podstawowe parametry przy otwieraniu pliku (są jeszcze inne opcje):
’w’ (write) plik jest stworzony i można w nim coś zapisywać (jeśli istnieje to
poprzednia zawartość zostanie wymazana)
’r’ (read) czytamy z istniejącego pliku bez modyfikacji
’a’ (append) do istniejącego pliku dopisujemy nowe dane
Do pliku (otworzonego z ’w’ lub ’a’) wpisujemy dane:
fo.write(’To zostanie do dane do pliku!\nTo będzie w nowej linijce\n’)
Stwórz plik o nazwie p.txt i wpisz do niego trzy dowolne linijki.
Sprawdź że plik powstał otwierając p.txt w edytorze (np. klikając na p.txt)
Zmodyfikuj wpisane linijki, uruchom program i sprawdź ponownie zawartość
p.txt.

(2) Otwórz plik p.txt (stworzony w (1)) do odczytu (opcja ’r’).
Przetestuj: s=fo.read(5); print(s); s=fo.read(3); print(s); s=fo.read(); print(s)
Gdy dojdziemy do końca pliku s przyjmuje wartość ” (pusty łańcuch).
Polecenie break powoduje wyjście z pętli while lub for. Stosując while 1:
(nieskończona pętla, bo 1 odpowiada prawdzie) napisz program odczytujący
i wyświetlający po 3 znaki z pliku p.txt. Trzeba użyć break gdy s jest równe
”.

(3) Otwórz plik p.txt do dodawania (opcja ’a’). Za pomocą dwukrotnego
input po wywołaniu programu użytkownik ma dodać 2 linijki do pliku. Przetestuj i sprawdź nową zawratość pliku p.txt. Jeśli linijki się sklejają należy
dodać na konću każdej linijki ’\n’ (skok do następnej linijki). Przetestuj.

(4) Napisz program który zlicza ilość literek ’a’ w pliku p.txt. Przetestuj
zmieniając w edytorze ilość ’a’ w tym pliku.

(5) Napisz program który sprawdza czy wprowadzone słowo za pomocą
input znajduje się w pliku i wyświetla linijkę pliku z tym słowem. Można użyć fo.readline() do pobierania całych linijek. Przydatne może też być
polecenie in dla łańcucha znaków.

(6) Napisz program który otwiera plik p.txt do odczytu i tworzy plik p2.txt
który ma być taki jak p.txt oprócz tego że spacje mają być zamienione na
gwiazdki (*). Przetestuj.

(7) (Dodatkowe) Takie jak 6 ale w pliku p2.txt małe litery z p.txt mają
być zamienione na duże litery. Przetestuj.
