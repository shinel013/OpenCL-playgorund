# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import print_function, unicode_literals

import os
import platform
import sys

SEARCH_PATHS = [
    'python/mach/mach',
#    'python/hce_build_sys/mach',
]

# Individual files providing mach commands.
MACH_MODULES = [
    'python/mach/mach/commands/commandinfo.py',
#    'python/hce_build_sys/hcf_build_sys/config.py',
#    'python/hce_build_sys/hcf_build_sys/mach_commands.py',
#    'python/hce_build_sys/hcf_build_sys/frontend/mach_commands.py',
#    'tools/mach_commands.py',
]

def bootstrap(topsrcdir, hce_dir=None):
    if hce_dir is None:
        hce_dir = topsrcdir

    # Ensure we are running Python 2.7+. We put this check here so we generate a
    # user-friendly error message rather than a cryptic stack trace on module
    # import.
    if sys.version_info[0] != 2 or sys.version_info[1] < 7:
        print('Python 2.7 or above (but not Python 3) is required to run mach.')
        print('You are running Python', platform.python_version())
        sys.exit(1)

    try:
        import main_module
    except ImportError:
        sys.path[0:0] = [os.path.join(hce_dir, path) for path in SEARCH_PATHS]
        import main_module

    mach = main_module.Mach(topsrcdir)
    for path in MACH_MODULES:
        mach.load_commands_from_file(os.path.join(hce_dir, path))
    return mach

