# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Yafyaml(CMakePackage):
    """Yet another Fortran (implementation of) YAML
    The rationale for this one is simply to be compatible with the
    containers in gFTL.  It is not intended to be a complete YAML
    parser, just the subset needed by my own projects."""

    homepage = "https://github.com/Goddard-Fortran-Ecosystem/yaFyaml"
    url      = "https://github.com/Goddard-Fortran-Ecosystem/yaFyaml/archive/refs/tags/v0.5.1.tar.gz"

    maintainers = ['kgerheiser', 'edwardhartnett', 'Hang-Lei-NOAA']

    version('1.0.2', sha256='1d08d093d0f4331e4019306a3b6cb0b230aed18998692b57931555d6805f3d94')
    version('0.5.1', sha256='7019460314e388b2d556db75d5eb734237a18494f79b921613addb96b7b7ce2f')
    version('0.5.0', sha256='8ac5d41b1020e9311ac87f50dbd61b9f3e3188f3599ce463ad59650208fdb8ad')

    depends_on('gftl-shared')
