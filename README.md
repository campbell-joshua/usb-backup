# usb backup files


Purpose
------------
I built this program because my dad has files stored on a 128gb flashdrive at work,
and is required to back the files up to a base computer.
The computer will take several hours to back up the entire drive.
Time is wasted when the computer is copying identical files from the flashdrive to the C: drive.
This program is eliminates the duplication of identical files when backing up
the flashdrive to increase efficiency.

How it works
------------
Compares files on a flashdrive to a directory on the C: drive.
If files on the flashdrive are newer that the files on the C: drive, the files will be copied over.
If files exist on the flashdrive and not on C: drive the files will be copied over.
If the files exist on both drives and were modified at the same time, the file is skipped and is not copied.
This allows for large amounts of data to be scanned and backed up efficiently.

Installation
------------

Change this to what directory your flashdrive is on:

```python
flashdrive = 'D:\\'
```
Change this to what directory you are copying from your flash drive to
```python
C_drive = 'C:\\Users\\Josh\\Documents\\PyCharm'
```


Usage:

Run through the shell or a editor:

    $ python3 usb file backups.py

Tips and tricks
---------------
---

A link to the Contributors Guide: I don't know what this is?

**usb file backups**, Joshua Campbell Released under the [GNU GPLv3].<br>
Authored and maintained by Joshua Campbell

[GNU GPLv3]: http://www.gnu.org/licenses/gpl-3.0.txt
