from pathlib import Path
import os


class project_dir:

    CURRENT_DIR = Path(__file__).resolve()



    BASE_DIR = CURRENT_DIR.parent.parent.absolute()

    DATA_DIR = BASE_DIR/'data'

    RAW_DATA_DIR = DATA_DIR/'raw'

    PROCESSED_DATA_DIR = DATA_DIR/'processed'

