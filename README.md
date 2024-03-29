# VitroCAD Plugin for NanoCAD

## Описание

Данный скрипт автоматизирует инструкцию по установке плагина для САПР NanoCAD, так как NanoCAD не содержит средств для автоматизированного разворачивания плагинов внутри себя.

1. Скопировать файлы vitro.ini, vitro.cfg, vitro.dll, vitroacadplugin_ru-ru.cuix в папку с установленным NanoCAD
2. Подправить в файле vitro.ini путь к модулю VitroNanoCadPlugIn*.nrx в зависимости от установленной версии NanoCAD
3. В папке с установленным NanoCAD найти файл nCad.ini и дописать в конец файла строку
#include "vitro.ini"
4. В папке с установленным NanoCAD найти файл nApp.cfg и дописать в конец файла строку
#include ".\vitro.cfg"
Если файла nApp.cfg нет его можно создать либо скопировать готовый из папки Reg в папку с установленным NanoCAD

## Настройка

1. Создайте файл `config.json` в корневой папке проекта с следующей структурой:

```json
{
    "vitro_path": "/path/to/vitro",
    "nano_path": "/path/to/nanocad",
    "version_list": ["30", "29", "28", "27", "26", "25", "24", "23", "22", "21", "20", "11", "10", "8", "7"],
    "arch_list": ["x64", "x32"]
}

```
2. Замените значения в vitro_path, nano_path на соответствующие значения, если директория установки отличается от директории по умолчанию.

## Использование

```
py vitronano.py
```

### Использование с компиляцией в .exe-файл
Обычно на клиентских машинах не установлен интерпретатор Python, поэтому использование предполагается с компиляцией кода в исполняемый .exe-файл при помощи библиотеки [Nuitka](https://github.com/Nuitka/Nuitka) или [Pyinstaller](https://github.com/pyinstaller/pyinstaller).