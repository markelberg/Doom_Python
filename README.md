# Doom_Python (in progress)
(Recommended tutorials: https://lodev.org/cgtutor/raycasting.html, https://www.youtube.com/watch?v=4gqPv7A_YRY)

<br>

### Initial Setup
Currently, I implemented the initial setup: the map, the player and the logics of player-wall collision and movement using basic trigonometry to update the player's coordinates.
Knowing the angle of the player's direction and the speed of his movement, we can update the coordinates of the player (dx, dy). 

![movement_croquis](https://i.imgur.com/dxXTI9x.png)
<br>
![preview](https://i.imgur.com/ymliYA2.gif)

<br>

### Raycasting logic (player's FOV)
I implemented the raycasting logic so the FOV-rays also check when a collision occurs and optimize the mathematical parts of the code using Numpy and Math libraries.

For each ray in the FOV we need to get its intersection point with the wall. Knowing the map functions as a grid, we're going to search for vertical and horizontal intersections in each "square" of the grid to check if it has collided against a wall. We calculate separately the horizontals and verticals intersections of the grid-map using trigonometry.

![ray_croquis](https://i.imgur.com/tmiVQv5.png)
![preview2](https://i.imgur.com/EXjnEFt.gif)
