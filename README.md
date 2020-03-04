# PWJS - Article Analizer

## 1. Idea

 - Stworzenie aplikacji internetowej, która pozwoli na szybkie zbieranie artykułów z kilku kategorii - (biznes, nauka.).
 - Stworzenie BOTa do aplikacji Messenger, który wraz z aktualizacją API wysyła wiadomość do użytkownika o najnowszym artykule
 - Stworzenie spersonalizowanego widoku dla użytkownika - możliwość wyboru źródeł/wyszukiwania po frazie.
  
## 2. Development Plan

Za pomocą Frameworka DJANGO, oraz darmowego planu developerskiego w API [News Api](https://newsapi.org/) stworzenie strony, gdzie będą dostępne widoki:

* Biznes
* Rozrywka
* Zdrowie
* Nauka
* Sport
* Technologia

Następnie napisanie widoku, który pozwala na definiowanie własnego, spersonalizowanego widoku, na którym możemy wyświetlać swoje ulubione źródła, lub szukać czegoś po dowolnej frazie. 
*Przykład: szukanie po frazie "bitcoin" zwróci ostatnie artykuły ze wszystkich źródeł, które zawierają tagi bitcoin w swojej treści/tytule/opisie*

## 3. Technologie

**BACKEND**: Django, RestfulAPI, Python. Możliwe, że SQLite3, jeżeli będzie potrzebna komunikacja z bazą danych.

**FRONTEND**: Raw JavaScript, opcjonalnie JQuery - zależnie od tego, jak wiele dynamicznych rzeczy będzie do stworzenia. HTML, CSS, Bootstrap, może preprocessor Sass, jeżeli będzie dużo kodu CSS. 


## 4. TODO Lista

 - [ ] Wymyślenie nazwy aplikacji
 - [x] Stworzenie pustej aplikacji w DJANGO
 - [x] Stworzenie repozytorium dla projektu
 - [x] Zdefiniowanie wszystkich statycznych widoków
 - [x] Zdefiniowanie wszystkich statycznych URL
 - [x] Zdefiniowanie wszystkich zapytań API dla powyższych, statycznych danych aplikacji.
 - [ ] Stworzenie BOTa do Messengera
 - [ ] Zalinkowanie Bootstrapa do strony
 - [ ] Stworzenie block contentu, do którego dodawane będą kolejne widoki
 - [ ] Stworzenie Layoutu strony
 - [ ] Stworzenie Designu strony
 - [ ] Stworzenie speronalizowanej strony

