# Step By step to install Autolab Documentation in Ubuntu 20.04

[Autolab Documentation on Ubuntu 18.04](https://docs.autolabproject.com/installation/ubuntu/)

### Step To Follow: 

1. Upgrade system packages and installing prerequisites
```
sudo apt-get update
```
```
sudo apt-get update
```
```
sudo apt install git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev
```
```
sudo apt-get install libmysqlclient-dev
```
```
sudo apt-get install vim
```
2. Cloning Autolab repo from Github to ~/Autolab
```
cd ~/
```
```
git clone https://github.com/autolab/Autolab.git
```
3. Setting up rbenv and ruby-build plugin
```
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | sudo bash
```
```
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
```
```
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
```
```
sudo apt install rbenv
```
```
source ~/.bashrc
```
```
git clone https://github.com/rbenv/ruby-build.git
```
```
PREFIX=/usr/local sudo ./ruby-build/install.sh
```
```
cd Autolab
```
4. Installing Ruby with ruby-build, choose your own version
```
rbenv install `cat .ruby-version`
```
```
rbenv global `cat .ruby-version`
```
```
sudo apt-get install sqlite3 libsqlite3-dev
```
5. Working with Gems
```
echo "gem: --no-document" > ~/.gemrc
```
```
gem install bundler
```
6. Installing Rails
```
gem install rails -v 6.1.4.1
```
```
rbenv rehash
```
```
bundle install
```
7. Initializing Autolab Configs
```
cp config/database.yml.template config/database.yml
```
```
cp config/school.yml.template config/school.yml
```
```
cp config/autogradeConfig.rb.template config/autogradeConfig.rb
```
8. Create a .env file to store Autolab configuration constants
```
cp .env.template .env
```
9. Initialize application secrets
```
./bin/initialize_secrets.sh
```
10. Initializing Autolab Database
```
bundle exec rails db:create
```
```
bundle exec rails db:reset
```
```
bundle exec rails db:migrate
```
```
./bin/initialize_user.sh -d
```
11. If you are just testing Autolab, you can populate the database with sample course & students
```
bundle exec rails autolab:populate
```
12. Run Autolab!
```
bundle exec rails s -p 3000 --binding=0.0.0.0
```
13. kill the server
```
ps -aux | grep redis-server/rails-server
```
```
kill -9 <server no>
```



















    



