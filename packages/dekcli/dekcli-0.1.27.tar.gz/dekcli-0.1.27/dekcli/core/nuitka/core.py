import os
import sys
from dektools.file import remove_path
from dektools.shell import shell_wrapper, shell_exitcode
from dekvenv.active import dir_name_venv, activate_venv
from dekmedia.image.svg import trans_image

builder = "python -m nuitka"
name_for_entry = 'main'
path_for_res = 'res'
name_of_icon = name_for_entry


def build_target(path):
    path_last = os.getcwd()
    os.chdir(path)
    activate_venv(os.path.join(path, dir_name_venv))
    if shell_exitcode(builder):
        raise ChildProcessError(f"Nuitka is not found in target virtualenv.")
    for fn in ['build', 'dist']:
        remove_path(os.path.join(path, f"{name_for_entry}.{fn}"))
    command = [
        builder,
        f"{name_for_entry}.py",
        "--standalone",
        "--disable-console",
    ]
    if os.path.isdir(os.path.join(path, path_for_res)):
        command.append(f"--include-package-data={path_for_res}")
    icon_svg = f"{name_of_icon}.svg"
    if sys.platform == "darwin":
        icon_src = f"{name_of_icon}.icns"
        if os.path.isfile(icon_svg):
            trans_image(icon_svg, icon_src, [(256, 256)])
        if os.path.isfile(icon_src):
            command.append(f"--macos-app-icon={icon_src}")
    elif sys.platform == 'win32':
        icon_src = f"{name_of_icon}.ico"
        if os.path.isfile(icon_svg):
            trans_image(icon_svg, icon_src, [(256, 256)])
        if os.path.isfile(icon_src):
            command.append(f"--windows-icon-from-ico={icon_src}")
    shell_wrapper(" ".join(command))
    os.chdir(path_last)
