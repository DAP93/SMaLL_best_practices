VNC Server
==========

Often there is a need to operate the workstation remotely but using various graphical user interfaces (GUIs). 
As an alternative to `XServer <hhttps://en.wikipedia.org/wiki/X.Org_Server>`_ or commercial remote control programs 
(e.g. TeamViewer, AnyDesk, etc.) 
`Virtual Network Computing (VNC) <https://en.wikipedia.org/wiki/Virtual_Network_Computing>`_ is a viable alternative 
that can often make life easier. 
This guide shows you how to install on an Ubuntu system (20.04) the server (which is the machine you want to control) 
and then use it with a client (RealVNC in this case) on any PC.


VNC Server Installation
^^^^^^^^^^^^^^^^^^^^^^^

Update everithing

.. code-block:: bash 

    $ sudo apt update && sudo apt upgrade

Install the client `vnc4server`

.. code-block:: bash 

    $ sudo apt install vnc4server

.. attention::
    Please make sure that you are using only vnc-server and no other VNC-server are installed as 
    this could give errors in future mostly that clipboard sharing between the host Ubuntu Server & vnc-client machine. 
    You can check it as follows: 
    
    .. code-block:: bash 

        $ dpkg -l | grep vnc


.. toctree::
   :maxdepth: 3
   :hidden: