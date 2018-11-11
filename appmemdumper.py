#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = "Alexandre D'Hondt"
__version__ = "2.0"
__copyright__ = "AGPLv3 (http://www.gnu.org/licenses/agpl.html)"
__doc__ = """
This tool automates the research of some artifacts for forensics purpose in
 memory dumps based upon Volatility for a series of common Windows applications.

It can also open multiple archive formats (it uses pyunpack). In case of an
 archive, the tool will extract all its files to a temporary directory and then
 try to open each file as a memory dump.
"""
__examples__ = ["memory.dmp", "my-dumps.tar.gz", "dump.raw -a 0,1 -f"]
__print__ = "Print documentation:\n- stdout: pydoc {0}\n- html  : pydoc -w {0}"


from core import *
from tinyscript import *


if __name__ == '__main__':
    appsl = '\n'.join("  [{}] {}{}".format(i, a, ["", "*"][globals()[a] \
                      .procnames is None]) for i, a in enumerate(DUMPERS))
    parser.add_argument("dump", help="memory dump file path")
    parser.add_argument("-a", dest="apps", default="*", type=CommaListOfInts,
                        help="comma-separated list of integers designating "
                             "applications to be parsed (default: *)\n Current"
                             "ly supported: \n{}\n (*: general-purpose dumper)"
                             .format(appsl))
    parser.add_argument("-d", "--dump-dir", dest="dump_dir", default="files",
                        help="dump directory (default: ./files/)")
    parser.add_argument("-f", "--force", dest="force", action="store_true",
                        help="force profile search, do not use cached profile"
                             " (default: false)")
    parser.add_argument("-p", "--plugins-dir", dest="plugins_dir",
                        help="path to custom plugins directory (default: none)")
    parser.add_argument("-t", "--temp-dir", dest="temp_dir", default=".temp",
                        help="temporary directory for decompressed images"
                             " (default: ./.temp/)")
    initialize(globals())
    validate(globals(),
        ('dump', "not os.path.isfile( ? )", "Dump file does not exist !"),
        ('dump_dir', "not os.path.isdir( ? )", "Dump dir does not exist !"),
        ('plugins_dir', "not os.path.isdir( ? ) or ? is None",
         "Bad input plugins directory ; setting ignored.", None),
        ('temp_dir', "not os.path.isdir( ? )", "Temp dir does not exist !"),
    )
    sys.argv = sys.argv[:1]  # remove arguments for avoiding passing them to the
                             #  Volatility API (e.g. -p will cause a clash with
                             #  the PID option of Volatility)
    for l in ['pyunpack', 'easyprocess', 'volatility.debug']:
        logging.getLogger(l).setLevel(51)
    # running the main stuff
    _, args.dump = decompress(args.dump, args.temp_dir)
    from_cache = not args.force
    for dump in args.dump:
        dump_dir = os.path.join(args.dump_dir, os.path.basename(dump))
        VolatilityMemDump(dump, args.apps, dump_dir, args.plugins_dir,
                          from_cache).dump()
        # if archive, assume that every other dump has the same profile as
        #  the first one in order to spare time
        from_cache = True
    # clean the extracted files' folder
    shutil.rmtree(args.temp_dir)
