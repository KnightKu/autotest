#!/usr/bin/python
from common.check_version import check_python_version
check_python_version()

import os
from autotest_lib.client.common_lib import utils
from autotest_lib.client.bin import autotest_utils

version = 1

def setup(tarball, topdir):
    # FIXME - Waiting to be able to specify dependency.
    #self.job.setup_dep(['pgsql'])
    srcdir = os.path.join(topdir, 'src')
    if not os.path.exists(tarball):
        utils.get_file('http://pgfoundry.org/frs/download.php/1083/pgpool-II-1.0.1.tar.gz', tarball)
    autotest_utils.extract_tarball_to_dir(tarball, 'src')
    os.chdir(srcdir)
    # FIXEME - Waiting to be able to use self.autodir instead of
    # os.environ['AUTODIR']
    utils.system('./configure --prefix=%s/pgpool --with-pgsql=%s/deps/pgsql/pgsql' \
                    % (topdir, os.environ['AUTODIR']))
    utils.system('make -j %d' % count_cpus())
    utils.system('make install')

    os.chdir(topdir)

pwd = os.getcwd()
tarball = os.path.join(pwd, 'pgpool-II-1.0.1.tar.gz')
utils.update_version(pwd+'/src', False, version, setup, tarball, pwd)
