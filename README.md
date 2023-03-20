# VitroCAD Plugin for NanoCAD

## Описание

Данный скрипт автоматизирует инструкцию по установке плагина для САПР NanoCAD

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
    "version_list": ["nCadVersion1", "nCadVersion2"],
    "arch_list": ["nCadArch1", "nCadArch2"]
}

```
2. Замените значения в vitro_path, nano_path на соответствующие значения, если директория установки отличается от директории по умолчанию.

## Использование

### Использование с компиляцией в .exe-файл
Обычно на клиентских машинах не установлен интерпретатор Python, поэтому вы можете скомпилировать код в .exe-файл с помощью библиотеки pyinstaller.
Установите pyinstaller с помощью команды:

```
pip install pyinstaller
```
Далее выполните следующую команду для компиляции кода в .exe-файл:

```
pyinstaller --onedir --add-data "config.json;." vitronano22.py
```
В результате компиляции в папке dist будет создана папка с названием вашего Python-файла. 
Внутри этой папки вы найдете исполняемый файл vitronano22.exe.

```
./dist/etl/vitronano22.exe
```
