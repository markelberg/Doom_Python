# Doom_Python (in progress)
(Recommended tutorials: https://lodev.org/cgtutor/raycasting.html, https://www.youtube.com/watch?v=4gqPv7A_YRY)

### Initial Setup
Currently, I implemented the initial setup: the map, the player and the logics of player-wall collision and movement using basic trigonometry to update the player's coordinates.
Knowing the angle of the player's direction and the speed of his movement, we can update the coordinates of the player (dx, dy). 

![movement_croquis](https://i.imgur.com/dxXTI9x.png)
<br>
![preview](https://i.imgur.com/ymliYA2.gif)

<br>

### Raycasting logic (player's FOV)
I implemented the raycasting logic and optimize it with numpy library so the FOV-rays also check when a collision occurs.

![preview2](https://i.imgur.com/EXjnEFt.gif)
