# rocketdata-task
# Collecting data about user (or project) repositories in Github

## Project Installation

<p>Clone the project directory from github git clone https://github.com/greatlaki/rocketdata-task.git. In the project directory set virtual environment <strong>python -m venv .venv</strong>
Activate the virtual environment <strong>source .venv/bin/activate</strong></p>

<p> Set dependencies </p> <strong>
  pip install -r requirements.txt</strong>

## Start spider 

<p><strong>cd rep_scraper -> cd rep_scraper</strong>
   <strong> scrapy crawl github  </strong> 
  </p>
  
### Data base is SQLite
<p> The data is saved in a file - github.db</p>
<p>If you don't need to program anything, you can use a GUI like sqlitebrowser or anything like that to view the database contents.</p>
<ol>
  <li>Website: http://sqlitebrowser.org/</li>
  <li>Project: https://github.com/sqlitebrowser/sqlitebrowser</li>
</ol> 
