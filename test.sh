#!/bin/sh
wget -O - ria.ru 2> /dev/null | pup 'a.cell-main-photo__link attr{href}' | head -n 1
