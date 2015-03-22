Developing AVA via Vagrant & Ansible
====================================

To help you get started with AVA development we've provided a Vagrant
configuration to create a VirtualBox virtual machine running AVA. The
required project dependencies are installed via an Ansible playbook.

Less setup time == more hacking time!


Installation
------------

 1. Install Vagrant from <https://www.vagrantup.com/downloads.html>.

 2. Install Ansible from source or a package via <http://docs.ansible.com/intro_installation.html#installing-the-control-machine>.

 3. (Optional) Install Virtual Box from source or a package via <https://www.virtualbox.org/wiki/Downloads>

 4. Clone the AVA repository with [TODO: Change this when merged]:

        git clone  https://github.com/SafeStack/ava.git

 5. Change to the Vagrant directory:

        cd ava/vagrant/

 6. Create the VM to run AVA (this will take many minutes):

        vagrant up

    Eventually, when asked, you'll need to supply a password.

 7. Connect to the running VM:

        vagrant ssh

 8. Change to the AVA directory (this is synced between the VM & your
    local machine):

        cd ava.github.com/ava/

 9. Create an initial administrator/superuser account [TODO: Automate this]:

        python manage.py createsuperuser

 10. Start AVA [TODO: Automate this?]:

        celery -A apps.ava_core worker -l info -B &

        python manage.py runserver 0.0.0.0:8000

    Note: The 0.0.0.0 ensures the VirtualBox port forwarding works.

 11. Visit this URL on your local machine (not in the VM):

        http://127.0.0.1:8000/

 12. You're running AVA!


Latest tested versions: Vagrant 1.7.2 & Ansible 1.8.2
