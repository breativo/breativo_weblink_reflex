@echo off

echo Activando el entorno virtual...
call venv\Scripts\activate.bat

echo Actualizando pip...
python -m pip install --upgrade pip

echo Instalando las dependencias del proyecto...
pip install -r requirements.txt

echo Inicializando Reflex...
python -m reflex init

echo Exportando la aplicación frontend...
python -m reflex export --frontend-only

echo Eliminando la carpeta 'public'...
rmdir /s /q public

echo Descomprimiendo el archivo 'frontend.zip' en la carpeta 'public'...
powershell Expand-Archive -Path frontend.zip -DestinationPath public

echo Eliminando el archivo 'frontend.zip'...
del /f frontend.zip

echo Desactivando el entorno virtual...
deactivate

echo Script finalizado.
