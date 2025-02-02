# Симуляция "Тигры и Косули"

## Описание проекта

Этот проект представляет собой 2D-консольную игру-симуляцию, в которой тигры охотятся на косуль, а косули ищут пропитание. Основная цель симуляции — продемонстрировать взаимодействие хищников и травоядных в рамках замкнутой экосистемы. 

Игра реализована в объектно-ориентированном стиле (ООП).

Особенность техничской реализации заключается в необходимом нажатии любой клавиши и отправки ее в консоль в случае полного заполнения мира.

---

## Функционал игры

1. **Объекты:**
   - **Тигры:**
     - Охотятся за косулями.
     - Погибают от голода, если долгое время не получают добычу.
   - **Косули:**
     - Ищут пропитание (например, траву или другие ресурсы).
     - Погибают от голода, если не находят пищу.

2. **Игровое поле:**
   - Представляет собой 2D-сетку (размер можно настроить).
   - Каждая клетка может быть:
     - Пустой.
     - Занятой тигром или косулей.
     - Содержать ресурс для питания косуль.
     - Занята статичным объектом

3. **Механики:**
   - **Голод:**
     - У каждого животного есть счётчик голода, который уменьшается со временем.
     - Если счётчик достигает нуля, животное получает урон, равный количеству оставшихся действий на момент наступления истощения.
   - **Движение:**
     - Животные могут перемещаться по игровому полю.
     - Косули перемещаются в поисках еды.
     - Тигры преследуют ближайших косуль.
   - **Охота:**
     - Тигры могут атаковать косуль, если находятся на соседней клетке.
   - **Питание:**
     - Косули восполняют голод, находя еду.
     - Тигры восполняют голод, поедая косуль.

---

## Технические детали

1. **Классы:**
   - `Creature` — базовый класс для всех животных.
   - `Predator` — класс для тигров, наследуется от `Animal`.
   - `Herbivore` — класс для косуль, наследуется от `Animal`.
   - `Manager` — класс, который управляет игровым полем, объектами и правилами симуляции.

2. **Алгоритмы:**
   - Поиск ближайшей цели для тигров.
   - Поиск еды для косуль.
   - Генерация нового ресурса на игровом поле (например, травы).
   - Обработка событий голода, охоты и передвижения.

3. **Настройки:**
   - Размер игрового поля.
   - Количество тигров и косуль.
   - Количество стартовых ресурсов.
   - Скорость игры (интервал между циклами симуляции).

---

## Как запустить

1. Клонируйте репозиторий.
2. Зайдите в корень проекта
3. Запустите симуляцию командой:
   ```bash
   python main.py
   ```
