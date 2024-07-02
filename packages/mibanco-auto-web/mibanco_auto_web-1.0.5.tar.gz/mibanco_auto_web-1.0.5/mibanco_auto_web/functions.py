import os
import shutil
import subprocess
from .variables import version, repository_options, app

url_repository = ""

def print_version():
    print(f'Version: {version}')

def execute_tests():
    print('Ejecutando pruebas...')
    subprocess.run('behave --no-skipped --no-capture', shell=True)

def open_report_html():
    current_path = os.getcwd()
    report_path = os.path.join(current_path, 'src','test','reports')
    if os.path.exists(report_path):
        os.startfile(report_path)
    else:       
        print("¡No se encontró ninguna carpeta de reportes!")

def open_report_word():
    current_path = os.getcwd()
    evidencias_path = os.path.join(current_path,'Evidencias')
    if os.path.exists(evidencias_path):
        os.startfile(evidencias_path)
    else:       
        print("¡Debe realizar una ejecución de pruebas para generar el reporte Word!")

def reset_files():
    folders = ["screenshots", "Evidencias"]
    current_dir = os.getcwd()

    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        try:
            shutil.rmtree(folder_path)
            print(f"La carpeta '{folder}' ha sido eliminada exitosamente.")
        except FileNotFoundError:
            print(f"La carpeta '{folder}' no existe.")

def clone_repository():
    print('¡Vamos a descargar el repositorio del framework web!') #replicar para mobile
    
    repository_type = select_repository_type()
    if repository_type == "Github":
        repository_name = select_repository_name()
        branch_name = select_brach_name()
        url_repository = f"https://github.com/aariverar/{repository_name}.git"
    elif repository_type == "Azure Repos":
        repository_name = select_repository_name()
        branch_name = select_brach_name()
        url_repository = f"https://mibanco-devops@dev.azure.com/mibanco-devops/DevOps/_git/{repository_name}"
    else: 
        url_repository = None

    if url_repository is not None:
        # Verificar si la rama existe en el repositorio remoto
        result = subprocess.run(f'git ls-remote --heads {url_repository} {branch_name}', shell=True, capture_output=True, text=True)
        if branch_name in result.stdout:
            if os.path.isdir(app):
                print(f'El directorio {app} ya existe. Actualizando...')
                subprocess.run(f'git pull', shell=True)
                subprocess.run(f'git -C {app} checkout {branch_name}', shell=True)
                subprocess.run(f'git -C {app} pull origin {branch_name}', shell=True)
            else:
                print('Clonando repositorio...')
                subprocess.run(f'git clone {url_repository} {app}', shell=True)
                print(f'Cambiando a la rama {branch_name}...')
                subprocess.run(f'git -C {app} checkout {branch_name}', shell=True)
        else:
            print(f"La rama {branch_name} no existe en el repositorio {url_repository}.")

def select_repository_type():
    print('Selecciona el repositorio que deseas clonar:')
    for index, key in enumerate(repository_options):
        print(f'{index + 1}. {key}')

    option = int(input('Opción: '))

    if option > len(repository_options):
        print('Opción inválida. Inténtalo de nuevo.')
        select_repository_type()

    repository_type = repository_options[option - 1]
    print(repository_type)
    return repository_type

def select_repository_name():
    repository_name = input("Escribe el nombre del repositorio:")
    return repository_name

def select_brach_name():
    branch_name = input('Escribe el nombre de la rama (La rama debe existir en el repositorio): ')
    return branch_name

def open_application():
    current_path = os.getcwd()
    report_path = os.path.join(current_path, 'src', 'test', 'app', 'app.py')
    subprocess.run(f'python {report_path}', shell=True)

def open_log_file():
    current_dir = os.getcwd()
    excel_path = os.path.join(current_dir, 'src', 'test', 'resources', 'log')
    os.startfile(excel_path)

def open_excel_data():
    current_path = os.getcwd()
    excel_file = os.path.join(current_path, 'src', 'test', 'resources', 'data', 'excel')
    os.startfile(excel_file)