# NinjaZipPy

NinjaZipPy is a Python command-line utility for compressing and extracting files/folders using the 7-Zip format via the bit7z library.  
This project was migrated from the original C++ bit7z repository as part of an internship task using LLM assistance.

## Features
- Zip files or folders into `.7z` archives.
- Unzip `.7z` archives into folders.
- Simple and clean CLI interface.

## Installation
1. Clone the repository:
git clone https://github.com/OmsinghRotele/NinjaZipPy.git

2. **Navigate to the project folder**  
cd NinjaZipPy

3. **Create a virtual environment** 
python -m venv venv

4. **Activate the virtual environment**  
- Windows (cmd): `venv\Scripts\activate.bat`  
- Windows (PowerShell): `venv\Scripts\Activate.ps1`  
- Unix/Linux: `source venv/bin/activate`

5. **Install the package**  
pip install -e .


## Usage

After setup, NinjaZipPy can be used directly from the terminal via the CLI command `ninjazippy`.

- **Zip a folder or files**  
ninjazippy zip <source_folder> <destination_archive.7z>
Example:
ninjazippy zip D:\NinjaZipPy\abc D:\NinjaZipPy\abc.7z

- **Unzip an archive**  
ninjazippy unzip <archive.7z> <destination_folder>
Example:
ninjazippy unzip D:\NinjaZipPy\abc.7z D:\NinjaZipPy\abc_unzipped


## Notes
- The CLI command is lowercase (`ninjazippy`).  
- Tests from the original C++ repository were not migrated, per the task instructions.  
- This project demonstrates Python CLI packaging, file I/O, and working with 7-Zip archives.
