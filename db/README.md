 2007  sudo -u postgres createuser david
 2008  sudo service postgresql stop
 2009  sudo apt-get install python-psycopg2
 2010  sudo -u postgres createuser david
 2011  sudo service postgresql start
 2012  sudo -u postgres createdb testdb -O david
 2013  cd dev/scratch/
 2014  mkdir db
 2015  cd db
 2016  history 10 > README.md
