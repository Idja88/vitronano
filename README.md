# VitroCAD Plugin for Nanocad

## Описание

Данный скрипт автоматизирует инструкцию по установке плагина для САПР NanoCAD

1. Скопировать файлы vitro.ini, vitro.cfg, vitro.dll, vitroacadplugin_ru-ru.cuix в папку с установленным NanoCAD
2. Подправить в файле vitro.ini путь к модулю VitroNanoCadPlugIn*.nrx в зависимости от установленной версии NanoCAD
3. В папке с установленным NanoCAD найти файл nCad.ini и дописать в конец файла строку
#include "vitro.ini"
4. В папке с установленным NanoCAD найти файл nApp.cfg и дописать в конец файла строку
#include ".\vitro.cfg"
Если файла nApp.cfg нет его можно создать либо скопировать готовый из папки Reg в папку с установленным NanoCAD

## Требования

1. Python 3.8.1 так как это последняя версия поддерживающая Win7.
