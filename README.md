# initialize-virtualenv

Initialize virtualenv and install the required modules,
if the system doesn't have them yet.

The demo case runs as follows:

1. Try to import required modules
2. If not, try to detect the predefined virtualenv path.
3. If no virtualenv yet, trigger initialize-virtualenv to initialize a virtualenv,
   activate it, and install modules inside it.
4. Launch itself within the virtualenv

