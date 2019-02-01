### PoleStarShip ###
This application will create API to track position of ship
### Step To Run Server with data
#### Step 1
      git clone https://github.com/vinayinfo/PoleStarShip.git
      cd PoleStarShip
#### Step 2
      sudo docker-compose build
#### Step 3
      sudo docker-compose run web python3 manage.py migrate

#### Step 4
      sudo docker-compose up
#### Step 5
      http://localhost:8000
### To Run Test Case
      sudo docker-compose run web python3 manage.py test

#### API details
To get all ship 
      http://localhost:8000/api/ships/
     
To get all ship 
      http://localhost:8000/api/positions/imo_id/
