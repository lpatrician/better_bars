### better_bars 🎶 <= 🎸 🤓 ###
Better bars is a tool for generating musical progressions (bars) that improve with user input.

The program should start by generating a random progression, playing it for the user, and taking a 1-10 rating as input. 

For every run after the first, the program should call a different function that analyzes past progressions' ratings and features in order to generate the next.

### To-do ###
1) Create Django skeleton for project
2) Choose db, configure within django project
3) Initialize with random progression creator, runtime file
4) Add user input to runtime
5) Add counter of # of runs, initialize at 1
6) Save progression + rating to database
7) Determine features of past progressions that are important to analyze
8) Create 'informed progression creator' (IPC) using features and ratings to generate better_bars
9) Integrate IPC into runtime => each run subsequent to the first should call this instead of the initial rpc
