import logging
import platform
from pathlib import Path

logger = logging.getLogger(__name__)


def get_best_guess_of_blender_path():
    if platform.system() == "Windows":
        try:
            base_path = Path("C:\Program Files\Blender Foundation")
            blender_folder_path = [path for path in base_path.glob("Blender*")]
            blender_exe_path = blender_folder_path[0] / "blender.exe"
            logger.info(
                f"Windows machine detected - guessing that `blender` is installed at: {str(blender_exe_path)}"
            )

            if blender_exe_path.is_file():
                return str(blender_exe_path)
        except Exception as e:
            print(e)
            logger.warning(
                "Couldn't find Blender path automatically, need to select it manually"
            )

        return None

    else:
        logger.info(f"Non-Windows machine detected - TODO - This, lol")
        return None
