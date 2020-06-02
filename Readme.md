# Sublime 3 Dlang Auto File Name

Sublime 3 Dlang Auto File Name plugin. 
Set new file name from "module name" | "class Name" | "interface Name" | "struct Name"

## Demo

![Demo](demo/dlang_auto_file_name_demo.gif)


## Algo
- Check for it is new unsaved file
- Get name
-- Grep for "\<module name\>"
-- Grep for "\<class Name\>"
-- Grep for "\<interface Name\>"
-- Grep for "\<struct Name\>"
- Set tab name. It will be file name.


## Installation

Install [DlangAutoFileName](https://packagecontrol.io/packages/DlangAutoFileName) from Package Control.
