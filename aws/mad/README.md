# Master Acceptance Database Example Application

`sudo mount --bind /mnt/c /c`

`docker-compose up -d`

`docker-compose run -e PGPASSWORD=mad_password database psql --host=database --dbname=mad_database -U mad_user -f /scripts/mad.sql`

`docker-compose run database bash`

`sudo apt install libpq-dev`

`python -m pip install --system psycopg2 -t ./lib`

`docker-compose down -v`


sudo apt-get install postgresql postgresql-contrib
sudo apt-get install libpq-dev # this is required as psycopg2 uses pg_config
sudo apt-get install python-dev

ln -s /mnt/c/Users/Ockle1P/dev/git_repos/ockleford/upskilling/aws/mad/app/ ~/.python




