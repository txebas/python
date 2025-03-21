import winreg
from datetime import datetime

def list_installed_programs():
    # Abrir la clave del registro donde se almacenan los programas instalados
    uninstall_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

    # Iterar sobre las subclaves para obtener la información de cada programa
    for i in range(0, winreg.QueryInfoKey(uninstall_key)[0]):
        try:
            subkey_name = winreg.EnumKey(uninstall_key, i)
            subkey = winreg.OpenKey(uninstall_key, subkey_name)
            
            # Obtener el nombre del programa
            try:
                program_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
            except FileNotFoundError:
                program_name = "Unknown"

            # Obtener la fecha de instalación
            try:
                install_date = winreg.QueryValueEx(subkey, "InstallDate")[0]
                install_date = datetime.strptime(install_date, "%Y%m%d").strftime("%Y-%m-%d")
            except FileNotFoundError:
                install_date = "Unknown"

            # Imprimir la información del programa
            print(f"Programa: {program_name}, Fecha de instalación: {install_date}")

        except OSError:
            continue

    winreg.CloseKey(uninstall_key)

if __name__ == "__main__":
    list_installed_programs()