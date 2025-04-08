
# SubHunter V1.5
**Инструмент для поиска поддоменов и проверки их статуса в реальном времени**
| [GitHub](https://github.com/FreedomSec1337/SubHunter)
![screenshot](https://raw.githubusercontent.com/FreedomSec1337/SubHunter/main/eses.png) *(если доступно)*
---

## Обзор

**SubHunter** — мощный инструмент для разведки поддоменов, созданный для пассивного поиска через DNS и проверки статуса в реальном времени. Построен для red team-специалистов, исследователей безопасности и кибер-воинов, ценящих эффективность и чистый вывод.

---

## Возможности

- Пассивный сбор DNS через AlienVault OTX
- Сортировка и фильтрация поддоменов
- Проверка HTTP-статуса в реальном времени (200, 404, 429 и др.)
- Разрешение IP-адреса для каждого поддомена
- Сохранение результатов в файл

---

## Установка

Проверено с:
- **Python**: `3.8+`
- **Pip**: `20+`

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/FreedomSec1337/SubHunter
cd SubHunter
```

### 2. Установите зависимости:

```bash
pip install -r requirements.txt
```

Если `requirements.txt` отсутствует, установите вручную:

```bash
pip install -r xxx.mp4
```

---

## Использование

Базовая команда:

```bash
python3 SubHunter.py <домен>
```

### Пример:

```bash
python3 SubHunter.py ukraine.ua
```

После сканирования вас попросят сохранить результаты. Просто введите имя файла и наслаждайтесь славой.

---

## Поддержка

**Kirov Elite Group**  
_www.kirovgroup.org_

---

## Контакты

- Telegram: [@fsec1337](https://t.me/fsec1337)
- GitHub: [FreedomSec1337](https://github.com/FreedomSec1337)
