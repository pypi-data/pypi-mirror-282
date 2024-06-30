import os
import sys
from dektools.file import remove_path
from dektools.shell import shell_wrapper
from dekvenv.active import dir_name_venv, sys_paths_relative
from dekmedia.image.svg import trans_image
from .tmpl import ProjectGenerator

name_for_entry = 'main'
name_of_icon = name_for_entry


def build_target(path, data=None):
    path_last = os.getcwd()
    os.chdir(path)
    data = data or {}
    platlib = sys_paths_relative(os.path.join(path, dir_name_venv))['platlib']
    data_default = dict(
        entry=f"{name_for_entry}.py",
        name=name_for_entry,
        venv=repr(platlib) if os.path.isdir(platlib) else ''
    )
    ProjectGenerator(path, {**data_default, **data}).render()
    for fn in ['build', 'dist']:
        remove_path(os.path.join(path, fn))
    icon_svg = f"{name_of_icon}.svg"
    if sys.platform == "darwin":
        icon_src = f"{name_of_icon}.icns"
        if os.path.isfile(icon_svg):
            trans_image(icon_svg, icon_src, [(256, 256)])
    elif sys.platform == 'win32':
        icon_src = f"{name_of_icon}.ico"
        if os.path.isfile(icon_svg):
            trans_image(icon_svg, icon_src, [(256, 256)])
    shell_wrapper(f'pyinstaller .pyinstaller.spec')
    os.chdir(path_last)
