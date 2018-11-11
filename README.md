[![Build Status](https://travis-ci.org/dhondta/AppmemDumper.svg?branch=master)](https://travis-ci.org/dhondta/AppmemDumper)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.804958.svg)](https://doi.org/10.5281/zenodo.804958)


## Table of Contents

   * [Introduction](#introduction)
   * [System Requirements](#system-requirements)
   * [Installation](#installation)
   * [Quick Start](#quick-start)
   * [Issues management](#issues-management)


## Introduction

This tool automates the research of some artifacts for forensics purpose in memory dumps based upon Volatility for a series of common Windows applications.

It can also open multiple archive formats. In case of an archive, the tool will extract all its files to a temporary directory and then try to open each file as a memory dump (except files named README or README.md).


## System Requirements

This framework was tested on an Ubuntu 16.04 with Python 2.7.


## Installation

1. Install system requirements

 ```session
 $ sudo apt-get install foremost
 ```

 > **Behind a proxy ?**
 > 
 > Do not forget to configure your Network system settings (or manually edit `/etc/apt/apt.conf`).
 
2. Install from Pip

 ```session
 $ pip install appmemdumper
 ```

 > **Behind a proxy ?**
 > 
 > Do not forget to add option `--proxy=http://[user]:[pwd]@[host]:[port]` to your pip command.


## Quick Start

1. Help

 ```session
 $ app-mem-dumper -h
usage: app-mem-dumper [-h] [-a APPS] [-d DUMP_DIR] [-f] [-p PLUGINS_DIR]
                      [-t TEMP_DIR] [-v]
                      dump

AppMemDumper v2.0.0
Author: Alexandre D'Hondt

This tool automates the research of some artifacts for forensics purpose in
 memory dumps based upon Volatility for a series of common Windows applications.

It can also open multiple archive formats (it uses pyunpack). In case of an
 archive, the tool will extract all its files to a temporary directory and then
 try to open each file as a memory dump.

positional arguments:
  dump                  memory dump file path

optional arguments:
  -h, --help            show this help message and exit
  -a APPS               comma-separated list of integers designating applications to be parsed (default: *)
                         Currently supported: 
                          [0] AdobeReader
                          [1] DumpInfo*
                          [2] Firefox
                          [3] FoxitReader
                          [4] InternetExplorer
                          [5] KeePass
                          [6] MSPaint
                          [7] MediaPlayerClassic
                          [8] Notepad
                          [9] OpenOffice
                          [10] PDFLite
                          [11] SumatraPDF
                          [12] TrueCrypt
                          [13] UserHashes*
                          [14] Wordpad
                         (*: general-purpose dumper)
  -d DUMP_DIR, --dump-dir DUMP_DIR
                        dump directory (default: ./files/)
  -f, --force           force profile search, do not use cached profile (default: false)
  -p PLUGINS_DIR, --plugins-dir PLUGINS_DIR
                        path to custom plugins directory (default: none)
  -t TEMP_DIR, --temp-dir TEMP_DIR
                        temporary directory for decompressed images (default: ./.temp/)
  -v                    debug verbose level (default: false)

Usage examples:
  python app-mem-dumper memory.dmp
  python app-mem-dumper my-dumps.tar.gz
  python app-mem-dumper dump.raw -a 0,1 -f
 
 ```
 
2. Example of output

 ```session
 $ app-mem-dumper memory.dump -v -p plugins
 [appmemdumper] XX:XX:XX [DEBUG] Attempting to decompress 'memory.dump'...
 [appmemdumper] XX:XX:XX [DEBUG] Not an archive, continuing...
 [appmemdumper] XX:XX:XX [DEBUG] Setting output directory to 'files/memory.dump'...
 [appmemdumper] XX:XX:XX [INFO] Opening dump file 'memory.dump'...
 [appmemdumper] XX:XX:XX [INFO] Getting profile...
 [appmemdumper] XX:XX:XX [INFO] Getting processes...
 [appmemdumper] XX:XX:XX [DEBUG] > Executing command 'pslist'...
 [appmemdumper] XX:XX:XX [DEBUG] Found       : mspaint.exe
 [appmemdumper] XX:XX:XX [DEBUG] Not handled : audiodg.exe, csrss.exe, dllhost.exe, [...]
 [appmemdumper] XX:XX:XX [DEBUG] Profile: Win7SP0x86
 [appmemdumper] XX:XX:XX [INFO] Processing dumper 'dumpinfo'...
 [appmemdumper] XX:XX:XX [INFO] Processing dumper 'mspaint'...
 [appmemdumper] XX:XX:XX [DEBUG] Dumping for PID XXXX
 [appmemdumper] XX:XX:XX [DEBUG] > Calling command 'memdump'...
 [appmemdumper] XX:XX:XX [DEBUG] >> volatility --plugins=/path/to/plugins --file=[...]
 [appmemdumper] XX:XX:XX [INFO] > /path/to/files/memory.dump/mspaint-2640-memdump.data
 [appmemdumper] XX:XX:XX [WARNING] 
 The following applies to collected objects of:
 - mspaint
 
 Raw data (.data files) requires manual handling ;
 Follow this procedure:
  1. Open the collected resources with Gimp
  2. Set the width and height to the expected screen resolution
  3. Set another color palette than 'RVB'
 Restart this procedure by setting other parameters for width|height|palette.

 ```


## Issues management

Please [open an Issue](https://github.com/dhondta/appmemdumper/issues/new) if you want to contribute or submit suggestions. 

The *labels* usage convention is as follows :
 - General question: *question*
 - Suggestion: *help wanted*
 - Bug/exception/problem: *bug*
 - Improvement/contribution: *enhancement* ; NB: please precise if you are motivated and able to contribute

If you want to build and submit new dumpers, please open a Pull Request.
