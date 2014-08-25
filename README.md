# Hg19 Example

## Purpose

This project is an example of how you can analyze and visualize a DNA data set using python, django, postgresql and postBIS.


### Install requirements


If you are using a Debian based distribution:

```
sudo apt-get install python-dev python-setuptools git-core build-essential libdbd-pg-perl ssl-cert bedtools postgresql libpq-dev -y
```
### Install pip
```
sudo easy_install pip
```

### Install virtualenvwrapper with pip
```
sudo pip install virtualenvwrapper
```

Select a directory where you want to install all you python packages. Lets say ~/hg19/var/local/virtualenvs.

```
mkdir -p ~/hg19/var/local/virtualenvs
```

### Append the following lines to ~/.bashrc
```
export WORKON_HOME=~/hg19/var/local/virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

### Clone the project
Select your working directory. Lets say ~/hg19 and call it {hg19}

```cd {hg19}```

```git clone https://github.com/mexiCoders/hg19_example.git```


### Create a python virtual enviroment
```mkvirtualenv hg19```

```workon hg19```

### Install project requirements
```cd hg19```

```add2virtualenv .```

```workon hg19```

```pip install -r requirements.txt```


### Install postBIS


```svn co https://colab.mpi-bremen.de/postbis/svn/trunk postbis```

```make```

```make install```

Create the postgresql database

```createdb hg19 ```

```psql hg19```

In postgresql shell

```CREATE EXTENSION postbis;```


### Download/Load data


```workon hg19```

```cd scripts```

Warning: it takes a long time

```./download_and_load_chromosomes.sh ```

If you want to upload only a chromosome you can do this:

```./download_and_load_chromosomes.sh {chromosome}``` 
