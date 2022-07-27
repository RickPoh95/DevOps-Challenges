## Ansible-Challenges No.4 -  Get data from API and Analyse it

## Create a Ansible Playbook to automate the following process 

  1. Grab data from data.gov.sg (CSV zipped file)
  2. Unzip the file
  3. Using python pandas Find the row with IT grads 
  4. Print the number

## There is two way to complete this challenges:
* Ansible with Python
* Ansible 

### Below is the task that execute using this ansible playbook:
> Ansible with Python
>>Ansible Part
1. Download the University and Polytechnic statistic file that study IT from data.gov.sg api and keep it as a zip file
2. Unzip the University and Polytechnic data 
>>Python
1. Read University csv file
2. Filter out IT course and MF sex
3. Save to filtereduni.csv without the first column index
4. Sum total of Uni IT graduates
5. Write total to finaluni.csv
6. Repeat the step for Polytechnic csv file
7. Print the total number of graduate that save to GrandTotal

> Ansible 
1. Query IT university graduate data
2. Filter and Output content for uni graduates to it_uni_data.csv
3. Calculate total number of IT university graduates and print to file (it_uni_data.csv)
4. Repeat the same for IT polytechnic graduate data
5. Calculate total number of IT university graduates and print to file (it_poly_data.csv)
6. Calculate the total number of IT graduates from University and Polytechnic and record to finaldata.txt

### Command to execute before execute bryan-panda
* Remember to install this two items before run bryan-panda.yml
```
sudo apt install zip
```
```
python3 -m pip install pandas
```

Further Reading:
 
* [ansible.builtin.get_url module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/get_url_module.html)
* [ansible.builtin.unarchive module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/unarchive_module.html)
* [ansible.builtin.script module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/script_module.html)
* [Pandas Read CSV](https://www.w3schools.com/python/pandas/pandas_csv.asp)
* [ansible.builtin.uri module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html)
* [ansible.builtin.set_fact module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/set_fact_module.html)

