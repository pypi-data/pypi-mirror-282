# Access rclone from a pyfilesystem interface
I needed this.

__version__ = 0.1.2

#### Status
_(Under development, initializing repo)_ 

## About

This wraps `rclone-python` in a `pyfilesystem` interface. If you don't need a `pyfilesystem` interface you don't need `fs_rclone`. So if that's the case you should use `rclone-python` or `rclone` directly.

## Dependencies

#### Automatically installed: rclone-python

This handy tool controls `rclone` from python. 

[pypi.org/project/rclone-python/](https://pypi.org/project/rclone-python/)

[github.com/Johannes11833/rclone_python](https://github.com/Johannes11833/rclone_python)

#### Manually installed: rclone v1.67.0

This dep _is_ rclone. Control a wide variety of cloud storage with this puppy.

[github.com/rclone/rclone](https://github.com/rclone/rclone)
[Install rclone on your own.](https://rclone.org/install/)

__version_used_by_this_project__ = _rclone-v1.67.0-linux-amd64_

#### Automatically installed: pyfilesystem 2.4.12

The Mac-Daddy of all file system abstractions -- besides rclone -- and besides FUSE. But _absolutely_ one of the number ones.

Installed automagically with fs-rclone if'n y'all don't already have it.

## Changelog

0.1.2 Update README

0.1.0 Add dependencies to `pyproject.toml`. Add `SoftBOM` (software bill of materials). Delete test code.

0.0.1 fix bug in example::add_one

0.0.0 configure package files

