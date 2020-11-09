# Project-2: Escaping 2020 on Earth 
## Overview 
* After experiencing the whirlwind that has been the year 2020, our team has decided to search for an alternative home. Through the examination of planets, species, and climates, as well as an analysis of spacecraft and vehicles, we will determine the best place to relocate.
### Data Source
* We used the Star Wars API which can be found <a href="https://swapi.dev/">HERE</a>.
### Built With
This project was built using the following frameworks/libraries/databases:
* Python
* Pandas
* Flask
* SQLite 
* JavaScript
* D3.js
## How It Works
* Data from the API was loaded into SQLite using Pandas. 
* Our flask app then connected to the database and converted the data into a JSON object. 
* Finally, JavaScript accesses this object through D3 in order to render our visuals.
## Results
* Our team recommends the planet Cato Neimoidia, the starship CR90 Corvette, the vehicle TIE/LN Starfighter, and the species Zabrak.

## Visualizations

-Planets

![planets](Images/planets.png)

In this page we used d3 to create a scatter graph that had changing axis. We also used d3 to create a table to show the planet name, gravity, climate, and terrain. Orbital, rotational, population, and diameter buttons were created so that when they were clicked, a bar graph would display the data of the button clicked.

We recommended, that to escape earth, Cata Neimoidia would be a good planet to move to because it had a low population, not too long of days or years, and a decent climate/terrain.

-Spaceships

![spaceships](Images/spaceships.png)

We also used d3 in this page to create a table and a scatter graph with changing axis. Buttons were also created similar to the planets page so that the data was shown in a different way. 

We recommended that to get to our new planet, that CR90 Corvette would be the best spaceship to travel on. We chose this spaceship because it wasn't too high in cost of credits, and it could hold a lot of passengers.

-Species

![species](Images/species.png)

On this page, d3 was used to create a table that displayed information for soecies' name, classification, language, average height, and average lifespan. 

We thought that the Zabrak species would be the best species to travel with and too keep us safe from other aggressive species we might run into.

-Vehicles

![vehicles](Images/vehicles.png)

On this page, d3 was used to create a scatter graph with changing axis. Number of passengers and cost in credits was compared to crew and max atmospheric speed. 

We recomend that the TIE/LN Starfighter was the best vehicle to travel around on once we are on our new planet. We thought that this would be the best vehicle because of its speed
