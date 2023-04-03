# Requirements specification

## General overview

An application for creating, saving and inspecting 2D tilemaps (maps composed of square pieces, "tiles") for top-down 2D role-playing games.

## Core functionality

* Initialize a new, empty map file
* Select a tile (a 2D square of a fixed size) from a list of available tiles (loaded from a specific directory relative to the application's path)
* Add the selected tile to a specific location with integer coordinates within the map
* Replace old tiles
* Save the map file
* Open and start editing a map file by inputting a filename or otherwise selecting a file

## Additional functionality

* Copy-paste tiles and combinations (patterns) of tiles over large areas instead of single locations
* Add tiles of different (both smaller and larger) dimensions
* Add tiles to non-integer, sub-tile positions
* Change the directory from which to load the available tiles
* Instead of single tiles, select "templates" (combinations of tiles loaded as maps from a specific directory or a filename inputted) to be added into the map