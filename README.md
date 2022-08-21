# Spider_task

## Branch Main   

### To run in local environment:

``docker-compose build``    
``docker-compose up``

### To stop containers in local :

``docker-compose down``

### Using Github Actions these containers are pushed to :

[Server Container](https://hub.docker.com/repository/docker/maaran/spider_web)   
[db Container](https://hub.docker.com/repository/docker/maaran/spider_db)   

## Branch Master

### This webiste is hosted on [heroku](https://www.heroku.com/)

#### Hosted on the website [here](https://spider987.herokuapp.com/)
#### Form details are [here](https://spider987.herokuapp.com/table)
#### View Responses [here](https://spider987.herokuapp.com/viewResponse)


### To run in local environment:

``docker build -t maaran/spider:dev .``  
``docker run -d --name spider -p 5000:5000 maaran/spider:dev``   

##### To stop containers in local :

``docker rm -f  spider``

