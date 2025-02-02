# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack import *


class Shumlib(MakefilePackage):
    """A set of libraries which are used by the UK Met Office's Unified Model,
    that may be of use to external tools or applications where
    identical functionality is desired"""

    homepage = "https://github.com/metomi/shumlib"
    # git = "https://github.com/metomi/shumlib.git"
    git = "https://github.com/climbfuji/shumlib.git"
    url = "https://github.com/metomi/shumlib/archive/refs/tags/2021.10.1.zip"

    maintainers = ['matthewrmshin', 'climbfuji']

    version('macos_clang_linux_intel_port', commit='84770606669463a54b51f9b8ed65a1d31f105fe9')
    version('macos_clang_port', commit='e5e5c9f23ce2656aacd75a884c26b01a5380752e')
    # version('2021.10.1', commit='545874fba961deadf4b2758926be7c26f4c8dcb9')
    # version('2021.07.1', commit='a4ea525ad3bf04684ef39b0241991a350e2b7241')
    # version('2021.03.1', commit='58f599ce9cfb4bd47197125548a44039695fa7f1')
    # version('2020.11.1', commit='58f599ce9cfb4bd47197125548a44039695fa7f1')

    def edit(self, spec, prefix):
        env['LIBDIR_OUT'] = os.path.join(self.build_directory, 'spack-build')
        # env['LIBDIR_ROOT'] = self.build_directory

    def build(self, spec, prefix):
        if spec.satisfies('%clang') or spec.satisfies('%apple-clang'):
            os.system('make -f make/vm-x86-gfortran-clang.mk')
        elif spec.satisfies('%gcc'):
            os.system('make -f make/vm-x86-gfortran-gcc.mk')
        elif spec.satisfies('%intel'):
            os.system('make -f make/vm-x86-ifort-icc.mk')
        else:
            raise InstallError('No shumlib make config for this compiler')

    def install(self, spec, prefix):
        install_tree(os.path.join(os.getenv('LIBDIR_OUT'), 'include'), prefix.include)
        install_tree(os.path.join(os.getenv('LIBDIR_OUT'), 'lib'), prefix.lib)
