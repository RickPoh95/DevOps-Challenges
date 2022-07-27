## Ansible-Challenges No.1 

## Create a simple ansible Playbook 

* The purpose of this challenges is to create a simple ansible playbook to do the following tasks

### Below is the task that execute using this ansible playbook:

1. Create a directory (Practice) with the Linux permission (rwxrwxr--)
2. Create a directory (Report) with the Linux permission (rwxrwxr--)
3. Create a file (modification_1.py) in directory (Report)
4. Move file (modification_1.py) in directory (Report) to  directory (Practice) and rename to file (mount.txt)
5. Copy file (mount.txt) from directory (Practice) to directory (Report)
6. List all the files including hidden files in directory (Report) and register --> 'check_Report_directory'
7. Print the content in 'check_Report_directory'

Further Reading:
 
* [ansible.builtin.file module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html) 
* [ansible.builtin.shell module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/shell_module.html)
* [ansible.builtin.copy module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html)
* [ansible.builtin.command module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/command_module.html)
* [ansible.builtin.debug module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/debug_module.html)

