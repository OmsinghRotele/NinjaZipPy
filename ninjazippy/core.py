from pathlib import Path
import py7zr

def zip_to_7z(input_path: str, output_file: str, password: str = None):
    input_path = Path(input_path)
    output_file = Path(output_file)
    mode = 'w'
    # py7zr accepts password for encryption if provided
    with py7zr.SevenZipFile(str(output_file), mode, password=password) as archive:
        if input_path.is_dir():
            # writeall preserves directory tree under arcname
            archive.writeall(str(input_path), arcname=input_path.name)
        elif input_path.is_file():
            # write single file
            archive.write(str(input_path), arcname=input_path.name)
        else:
            raise FileNotFoundError(f"{input_path} not found")

def unzip_7z(archive_file: str, output_dir: str, password: str = None):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    with py7zr.SevenZipFile(archive_file, mode='r', password=password) as archive:
        archive.extractall(path=str(output_dir))

def list_contents(archive_file: str):
    with py7zr.SevenZipFile(archive_file, mode='r') as archive:
        return archive.getnames()  # list of file paths inside archive
