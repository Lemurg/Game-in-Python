# Космические падальщики

Космическая игра, в которой игрок управляет кораблём, уворачивается от астероидов и стреляет по ним, чтобы набрать очки.

---

## 📌 Описание игры
Игрок управляет космическим кораблём, который может двигаться влево и вправо. Цель игры — уничтожать астероиды, появляющиеся сверху экрана, и избегать столкновений с ними. За каждый уничтоженный астероид игрок получает очки. Игра заканчивается, если корабль сталкивается с астероидом, и у игрока заканчиваются жизни.

---

## 🎮 Управление
- **A** — движение влево  
- **D** — движение вправо  
- **Пробел** — выстрел  
- **P** — пауза  
- **R** — рестарт после проигрыша  
- **ESC** — выход в главное меню  

---

## 🚀 Особенности
- **Динамическая сложность**: скорость астероидов увеличивается с ростом счёта.  
- **Система жизней**: у игрока есть 3 жизни.  
- **Рекорды**: игра сохраняет лучший результат.  
- **Главное меню**: кнопки для начала игры и выхода.  
- **Звуковые эффекты**: фоновая музыка и звуки выстрелов, столкновений и взрывов.  

---

## 📂 Структура проекта
- **asteroid.py** — логика астероидов.  
- **bullet.py** — логика пуль.  
- **button.py** — создание кнопок для меню.  
- **config.py** — настройки игры (цвета, изображения, звуки).  
- **controls.py** — обработка событий и игровой логики.  
- **initiate.py** — инициализация и запуск игры.  
- **main.py** — главный файл для запуска приложения.  
- **scoreboard.py** — отображение счёта и жизней.  
- **ship.py** — логика корабля игрока.  
- **stats.py** — статистика игры (счёт, жизни, рекорды).  

---

## 🛠 Установка и запуск
1. Убедитесь, что у вас установлен Python (версия 3.7 или выше).  
2. Установите библиотеку Pygame:  
   ```bash
   pip install pygame
