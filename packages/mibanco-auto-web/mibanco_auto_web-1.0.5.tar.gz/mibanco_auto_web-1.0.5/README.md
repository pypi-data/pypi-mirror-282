# mibanco_auto_web

mibanco_auto_web es una biblioteca de pruebas funcionales simple que utiliza Python, Selenium y Chrome driver.

## Pre-requisitos

Antes de instalar mibanco_auto_web, asegúrate de tener instalado lo siguiente:

- Python 3.12.2

## Instalación

Puedes instalar mibanco_auto_web usando pip:

```bash
pip install mibanco_auto_web
```

Si necesitas una versión específica de mibanco_auto_web, puedes especificarla así:

```bash
pip install mibanco_auto_web==version
```
## Uso

Una vez instalado, puedes usar mibanco_auto_web con varios argumentos:

| Argumento   | Descripción                                           |
|-------------|-------------------------------------------------------|
| --version   | Imprime la versión de mibanco_auto_web.                       |
| --setup     | Copia el directorio de la aplicación e instala las dependencias. |
| --run-tests | Ejecuta las pruebas.                                  |
| --report-html    | Genera un informe en html.                                    |
| --report-word      | Genera un informe en formato word. |
| --reset      | Elimina directorios innecesarios.  |
| --open-app   | Abre la interfaz de ejecución de pruebas.  |
| --open-logs   | Abre archivo excel con los logs de ejecución. |
| --modify-data   | Abre archivo excel con la data de pruebas. |
| --help  -h    | Muestra la ayuda y explica cómo usar los argumentos.  |

Por ejemplo, para imprimir la versión de mibanco_auto_web, puedes usar:

```bash
mibanco_auto_web --version
```
Para configurar tu aplicación, puedes usar:

```bash
mibanco_auto_web --setup
```
Esto copiará el directorio de la aplicación e instalará las dependencias necesarias.

Para ejecutar las pruebas, debes ubicarte dentro de la carpeta framework_web y ejecutar el siguiente comando:

```bash
mibanco_auto_web --run-tests
```
Para generar un informe en allure html, debes ubicarte dentro de la carpeta framework_web y usar este comando:

```bash
mibanco_auto_web --report-html
```
Para generar un informe en formato word, debes ubicarte dentro de la carpeta framework_web y usar este comando:

```bash
mibanco_auto_web --report-word
```

Para abrir la interfaz de ejecución de pruebas, debes ubicarte dentro de la carpeta framework_web y usar este comando:

```bash
mibanco_auto_web --open-app
```

Para abrir archivo excel con los logs de ejecución, debes ubicarte dentro de la carpeta framework_web y usar este comando:

```bash
mibanco_auto_web --open-logs
```

Para abrir archivo excel con la data de pruebas, debes ubicarte dentro de la carpeta framework_web y usar este comando:

```bash
mibanco_auto_web --modify-data
```

Si desea eliminar carpetas de ejecuciones anteriores, escriba el siguiente comando:

```bash
mibanco_auto_web --reset
```

Para obtener ayuda y saber cómo usar los argumentos, puedes usar:

```bash
mibanco_auto_web --help
```