# 3.How many possible unique board states are there after the first move?
4.	#1. Draw an initial empty 3x3 board.
5.	board = ["-", "-", "-",
6.	         "-", "-", "-",
7.	         "-", "-", "-"]
8.	
9.	#2. List all possible first moves for Player X.
10.	possible_moves_for_X = [
11.	"""
12.	X, -, -,
13.	-, -, -,
14.	-, -, -
15.	""", 
16.	"""
17.	-, X, -,
18.	-, -, -,
19.	-, -, -
20.	""",
21.	"""
22.	-, -, X,
23.	-, -, -,
24.	-, -, -
25.	""",
26.	"""
27.	-, -, -,
28.	X, -, -,
29.	-, -, -
30.	""",
31.	"""
32.	-, -, -,
33.	-, X, -,
34.	-, -, -
35.	""",
36.	"""
37.	-, --, -,
38.	-, -, X,
39.	-, -, -
40.	""",
41.	"""
42.	-, , -,
43.	-, -, -,
44.	X, -, -
45.	""",
46.	"""
47.	-, -, -,
48.	-, -, -,
49.	-, X, -
50.	""",
51.	"""
52.	-, , -,
53.	-, -, -,
54.	-, -, X
55.	"""
56.	]
57.	
58.	#3. How many possible unique board states are there after the first move?
59.	After Player X makes the first move, one cell will have an X and the remaining 8 cells will be empty.
60.	Since there are 9 empty positions initially, and placing X in any one of them creates a unique state:
61.	 There are 9 possible unique board states after the first move.
