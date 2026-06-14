# Football Data Report

В проекте два Docker-контейнера:

1. `generator` - генерирует CSV-файл с данными о футболистах
2. `reporter` - читает CSV-файл и создаёт HTML-отчёт

Все основные действия выполняются через bash-скрипт `run.sh`

## Запуск

Перед использованием команд нужно дать файлу `run.sh` право на выполнение:

```bash
chmod +x run.sh
```

Далее соберите Docker-образ генератора:

```bash
./run.sh build_generator
```

После этого запустите генератор:

```bash
./run.sh run_generator
```


Затем собираем Docker-образ для создания отчёта:

```bash
./run.sh build_reporter
```

После этого запустите создание отчёта:

```bash
./run.sh run_reporter
```

Итоговые файлы после запуска:

```text
data/
├── data.csv
└── report.html
```

## Основные команды run.sh

### Локальное создание данных

```bash
./run.sh create_local_data
```

Команда запускает `generate.py` без Docker и создаёт CSV-файл в папке `local_data/`

### Просмотр структуры проекта

```bash
./run.sh structure
```

Команда выводит структуру файлов проекта

### Очистка данных

```bash
./run.sh clear_data
```

Папки `data/` и `local_data/` остаются

### Вход внутрь контейнера generator/reporter

```bash
./run.sh inside_generator
```

```bash
./run.sh inside_reporter
```

Команда открывает терминал внутри контейнера generator/reporter
Внутри контейнера можно проверить файлы командой:

```bash
ls /data
```

Для выхода нужно написать:

```bash
exit
```