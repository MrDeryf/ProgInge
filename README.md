#  Генератор Оправданий (Excuse Generator)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-В%20разработке-orange)]()

> **Генератор Оправданий** — это веб-приложение, которое генерирует правдоподобные и абсурдные оправдания для любых ситуаций на основе множества факторов: текущей даты, дня недели, фазы луны, погоды и случайных переменных.

##  Возможности
-  Учёт текущей погоды через внешние API.
-  Интеграция с лунным календарём для повышения "абсурдности".
-  Настраиваемый уровень правдоподобности (от "Опоздал на 5 минут" до "Меня похитили инопланетяне").
-  Простой и адаптивный фронтенд.
-  RESTful API для генерации оправданий.

##  Стек технологий
| Компонент | Технология |
| :--- | :--- |
| **Backend** | Python, FastAPI |
| **Frontend** | HTML, CSS, Vanilla JS (или React) |
| **База данных** | SQLite / PostgreSQL |
| **Деплой** | Docker, GitHub Actions |

##  Архитектура (упрощённая)
```mermaid
graph TD
    A[Клиент / Браузер] -->|HTTP POST| B(FastAPI Backend)
    B -->|Запрос| C[(База шаблонов)]
    B -->|Запрос| D[API Погоды]
    B -->|Запрос| E[API Фазы Луны]
    B -->|Логика генерации| F{Генератор}
    F -->|JSON ответ| A
```
