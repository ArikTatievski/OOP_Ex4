Authors:
Arik Tatievski, 208997056 Roi Meshulam, 315635649

What is this project?
This project displays a simple pokemon game. You have pokemon collectors(Agents) and pokemons on weighed edges. We must catch as many pokemons as we can.

The main "code" in here is the complexity of finding the shortestPath to a pokemon with as low runing time as we can.

The way we made our project:

We have made a few classes these next lines will explain them.

Agent/Pokemon - are 2 low-key classes that will simply make our code cleaner and more readable.

Node/Edge- are 2 low-key classes that know how to do the most basic functions.(Creating nodes/edges/getting their location values etc..)

DiGraph - this class is represting a graph = (V=group of vertexes,E=group of edges) and all the functions we can do on a graph(adding and removing edges/nodes, getting Iterators of the graph edges/nodes and more)

GraphAlgo - this class allows us to make alogrithems on graphs such as tsp(getting cities),calculating shortest path(through dijkstra algorithm), checking if a graph is connected(BFS on same vertes on a graph&the graph's opposite),Using matplotlib to show a graphic visual of the graph and more.

client - this is a class we will NOT touch, it allows us to speak with the server and draw information from it(new pokemons, agent's curret location and more).

myalgo - this is our main class that "combines" all the classes together, the class runs as a loop as long as the game runs (we get it from the client) and each time it allocates each agent a pokemon to catch while drawing the new "state of the game"

How did we test our project?
In every step and every function we made we did all the tests on the extreme conditions of the graph to make sure that our graph can handle all possible situations. In addition there are 2 testing classes

Reasults:
WE NEED TO ADD REASULTS HERE AFTER WE FINISHHHH

How to use our project:
In order to use our project you will have to run the server (simply open the src folder and run in cmd 'java -jar Ex4_Server_v0.0.jar level' instand of level u can write 0-15 for different levvels)

After runing the server please run 'myalgo.py' and enjoy the game :)

Hope you find good usuage of this project!