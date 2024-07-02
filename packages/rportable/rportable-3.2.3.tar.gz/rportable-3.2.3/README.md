# R Portable Launcher

## Binaries
This is a binary packaged.  i386 and x64 binaries are available as optional dependencies.
One of the two options is required for a working installation:

```
pip install rportable[i386]
```

```
pip install rportable[x64]
```

Both should not be necessary, but R Portable ships with both.

## R Portable base

R Portable v3.2.3 packaged for installation via with pip (Python's package manager).  

This library is intended for internal use only by sdna_plus, 
(in particular to allow moving this code outside that project, to 
be used as an optional dependency).  But let James know if you 
have other uses for Python wheels of R Portable, or want more 
launcher scripts.

The wheel contains the R Portable code (version 3.2.3) bundled with sDNA,
but all the R Portable installers are available 
from: https://sourceforge.net/projects/rportable/files/.

The Wheel includes a `.bat` file that is copied to the `Scripts` dir of the Python
environment `rportable` is installed in (`rportable_launcher_scripts\Rscript.bat`). 
This means, from that environment, `Rscript` will launch the included Rscript.exe 
(version 3.2.3) from the command line, just as if it was appended to the `%PATH%`.

## Operating system
Windows only.  I don't know of a Linux equivalent of the Portable Apps Framework 
R Portable uses.  Nor what other third party repacked versions of R are available.

## License
GPL2

## Building and installing from 'source'
Requires [pdm](https://pdm-project.org/en/latest/)
