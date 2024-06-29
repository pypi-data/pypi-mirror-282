import os
from dektools.file import remove_path
from dektools.shell import shell_wrapper, shell_exitcode
from dekvenv.active import dir_name_venv, activate_venv

builder = "python -m nuitka"
name_for_entry = 'main'
path_for_res = 'res'


def build_target(path):
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
    shell_wrapper(" ".join(command), chdir=path)
