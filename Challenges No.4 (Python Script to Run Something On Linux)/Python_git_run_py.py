# Python program to explain os.system() method
	
# importing os module
import os

# Command to execute
# Using WSL OS command
# Create and change the current directory to the repo you just create
repo_name = input("Please key in the Git Repository Name: ")
os.mkdir(f"{repo_name}")
os.chdir(f"{repo_name}")

# Init the repository
os.system(f"git init")

# Create and add a file this the newly create repo
create_file = input("Please input your file name and extension: ")
os.system(f"touch {create_file}")

# git add all the file 
os.system(f"git add .")

# commit the file 
message = input("Please key in the message you will like to display: ")
os.system(f"git commit -m '{message}'")

# review and read a history of everything that happens to a repository
os.system(f"git log")

# getting confirmation to git push
push_confirm = input("Proceed with git push? [y/n] : ")

# confirm to git push 
while True:
    if push_confirm == "y":
        repo_url = input("Provide your Git Repo URL: ")
        os.system("git branch -M main")
        os.system(f"git remote add origin {repo_url}")
        os.system("git push -u origin main")
        break
    if push_confirm == "n":
        print("Project not pushed to github")
        break
       
