.. tip::
   
   This document can also be viewed using ``so help howto``.

Using the SO CLI :octicon:`plug`
================
This is a tutorial about how to use the SO CLI.

:octicon:`rocket` Installing
----------------------------
It's easy to install ``so``. However, the way to install it depends on your OS.

.. tab:: Linux/macOS/BSD
   
   Assuming that you have `Python
   <https://python.org>`_ (3.6 or newer required due to F-strings), including PyInstaller and everything in
   `the SO CLI requirements.txt
   <https://github.com/Tyler887/so/blob/main/requirements.txt>`_, you can install ``so``
   by using this command (works for and executes BASH):

   .. code-block:: shell

      bash -c "$(curl -fsSL https://raw.githubusercontent.com/Tyler887/so/main/install.sh)"

   This command may install Python if it is missing.
   
   If you are unable to execute this command, copy and paste the installation script
   from `Stack Apps
   <https://stackapps.com/questions/9375/placeholder-stackoverflow-cli>`_.

.. tab:: Windows
   
   To install ``so``, launch PowerShell (recommended Windows PowerShell 5.1 or
   PowerShell 7) and run:
   
   .. code-block:: powershell
      
      Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://github.com/Tyler887/so/raw/main/install.ps1')

.. tab:: Other (unsupported)
   
   .. warning::
     Make sure `compatibility for Python on your OS is available
     <https://pythondev.readthedocs.io/platforms.html>`_. ``so`` will not work otherwise.
     
     Support is not available for non-major platforms. Please do not report issues.
   
   To compile, use PyInstaller:
   
   .. tab:: Unix-like
   
     .. code-block:: bash
        
        pip3 install pyinstaller
        python -m PyInstaller --console --noupx --name so ./StackOverflowCommandLine.py
   
   .. tab:: ReactOS (NT-like)
     
     .. code-block:: powershell
        
        py -m pip install pyinstaller
        py -m PyInstaller --console --noupx --name so .\StackOverflowCommandLine.py

:octicon:`play` Using it
--------
.. admonition:: Todo
   
   Run ``so login``.

``so`` or ``so help`` will list commands.

``so feed <type>`` allows you to view the RSS feed of questions/answers. It
is useful to check this out everyday so you can answer questions that still
do not                      have                     an             answer.

For more info, refer to the rest of the docs.
