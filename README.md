# team-staff
This repo demonstrates how to configure your team repository for the project.
Your team repo should be a sibling to the class-repo (i.e. in the same directory).
Note the naming and directory location specified in the path to search for files (in solver.py)

Your Directory Structure should look like this:
ParentDirectory
	class-repo
		projectClasses
	team-repo
		solver.py
		algorithms	# place your algorithm implementation in this folder
			bfs.py
			Astar.py
		problems	# place your problem implementation in this folder
			simpleProblem.py
			slidingPuzzle.py


The demonstration simpleProblem uses the same simple puzzle used for demonstration in the BFS assignment.
BFS has been re-implemented using the classes provided in class-repo.
The problem has been re-implemented as well, by inheriting from the generic classes provided in class-repo.