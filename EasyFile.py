import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

file_type = {
    'Documentos': ['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', "csv", "xlsm"],
    'Imágenes': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', "webp"],
    'Videos': ['mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv', "ts"],
    'Música': ['mp3', 'wav', 'aac', 'flac', 'ogg'],
    'Programas': ['exe', 'msi', 'bat', 'sh', 'apk',"inf"],
    'Comprimidos': ['zip', 'rar', '7z', 'tar', 'gz'],
    'Ebooks': ['epub', 'mobi', 'azw'],
    'Fuentes': ['ttf', 'otf', 'woff', 'woff2'],
    'Scripts y códigos': ['py', 'js', 'html', 'css', 'java', 'c', 'cpp', 'rb', 'php', "ipynb"],
    'Otros': []
}

app_name="EasyFile~Sorter"

def find_folder(extension):
    for folder, extensions in file_type.items():
        if extension in extensions:
            return folder
    return 'Otros'

def organize_directory(folder_path):
    try:
        os.chdir(folder_path)
        for file in os.listdir():
            if os.path.isfile(file):
                extension = file.split('.')[-1].lower()
                folder = find_folder(extension)

                if not os.path.exists(folder):
                    os.makedirs(folder)
                dest_file = os.path.join(folder, file)

                if os.path.exists(dest_file):
                    base, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(dest_file):
                        new_file = f"{base}_{counter}{ext}"
                        dest_file = os.path.join(folder, new_file)
                        counter += 1
                shutil.move(file, dest_file)

        messagebox.showinfo(
            app_name, "¡Felicidades!\n\nLos archivos se organizaron correctamente.")

    except Exception as e:
        messagebox.showerror(app_name, f"Ocurrió un error: {e}")

def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

def check_continue():
    message = (
        "Bienvenido al organizador de archivos.\n\n"
        "Este programa organizará los archivos de la carpeta que seleccione según su tipo:\n\n"
        "- Documentos (pdf, doc, xls, etc.)\n"
        "- Imágenes (jpg, png, svg, etc.)\n"
        "- Videos (mp4, avi, mov, etc.)\n"
        "- Música (mp3, wav, flac, etc.)\n"
        "- Programas (exe, msi, sh, etc.)\n"
        "- Comprimidos (zip, rar, 7z, etc.)\n"
        "- Ebooks (epub, mobi, pdf, etc.)\n"
        "- Fuentes (ttf, otf, woff, etc.)\n"
        "- Scripts y Códigos (py, js, html, etc.)\n\n"
        "Los archivos se moverán automáticamente a las carpetas correspondientes.\n"
        "\n"
        "Para más información y actualizaciones, visite nuestro repositorio en GitHub: "
        "https://github.com/eliasvlc/file-sorter"
        "\n\n"
        "¿Desea continuar?"
        
    )

    return messagebox.askyesno(app_name+" [Sea7]", message)

def main():
    while True:
        if check_continue():
            folder_path = select_folder()
            if folder_path:
                if os.path.exists(folder_path) and os.listdir(folder_path):
                    if messagebox.askyesno(app_name, "Se procederá a organizar los archivos de la carpeta seleccionada \n \n¿Desea continuar?"):
                        organize_directory(folder_path)
                    else:
                        messagebox.showinfo(app_name, "Organización cancelada.")
                else:
                    messagebox.showerror(
                        app_name, "La carpeta seleccionada es inválida o está vacía.")
            else:
                messagebox.showinfo(app_name, "No se seleccionó ninguna carpeta.")
        else:
            break

if __name__ == "__main__":
    main()
