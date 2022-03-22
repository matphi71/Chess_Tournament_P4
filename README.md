# Chess tournament management system ♙  

### ***This programm will handle the roll out of chess tournaments, according to the swiss tournament system.***


![python-3 9](https://user-images.githubusercontent.com/83288091/159372342-92c15c10-0cc3-452b-89f5-a45436ccea9f.svg)

___

## RUN from scratch

   - ### Loading:
   
   git clone

    https://github.com/matphi71/Chess_Tournament_P4.git

[link for git clone](https://github.com/matphi71/Chess_Tournament_P4.git)

   - ### Virtual Environment set up:
   
1. #### creation
```python -m venv env```

2. #### activation
```source env/bin/activate```
or for windows:
```env/Scripts/activate.bat```

3. #### requirements
```pip install -r requirements.txt```


## Command line
      Chess_Tournament_P4.py

## FEATURES

**This programm will be able to:**

   - **Generate players** 
     - We will assume players are already registered. If we mean to change the all set of players: 
     
        ***just remove the #***
   
   In controller_player:
 
 ``` python
 def add_players_to_database(self):
    # model_players.player_db.truncate()
    added_players = 0
    while added_players != NUMBER_OF_PLAYERS_TO_ADD:
        self.collecting_players_info().add_player_to_database()
        added_players += 1
    return
 ```
    
   and in controller_menu:
      
```python    
def run(self):
    # controller_player.ControllerPlayer().add_players_to_database()
    self.welcome_message()
    self.options_access()
  ```
   If we mean to add some players then just change the variable `NUMBER_OF_PLAYERS_TO_ADD` in the controller_player module and remove #
  as apply the previous step.

  - **Change a player's rank anytime**
  - **Generate a report** 
  
    - with possibility to see it all in one or by section like: 
   
          1. Alphabetical participant list
          2. Ranking participant list
          3. Tournament list
          4. Match list

## Generate a flake-8 repport

*The max line lenght is setup at 119*

Run flake8 passing the --format=html option and a --htmldir:

    $ flake8 --format=html --htmldir=flake-report


***

<p align="center">
<img src="https://user-images.githubusercontent.com/83288091/159367851-a7cc3cfa-5cef-470b-b44d-942130c07da0.svg"width="150px" />
</p>


<div align="center">
Author:

*Mathilde Philippe*

:slightly_smiling_face:












