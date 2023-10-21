# Knight’s Tour
The Knight's Tour, a actually a mathematical problem ([Hamiltonian Path](https://www.geeksforgeeks.org/hamiltonian-cycle/)) with origins dating back to the ninth century, involves a knight commencing its journey from any square on the board and then maneuvering through the remaining squares, all without revisiting any previously occupied square. 

![Knight’s Tour](assets/img/knights-tour.gif)

## Table of Contents
- [About](#about)
  - [Backtracking](#backtracking)
  - [Recursion](#recursion)
  - [Warnsdorff's Rule](#warnsdorffs-rule)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)
- [References](#references)

## About

This project presents an engaging exploration of the Knight's Tour problem across a range of chessboard sizes, including 5x5, 6x6, 7x7, 8x8 and 9x9. It serves as an implementation and visualization of the Knight's Tour problem, featuring a solving algorithm constructed through recursion and the application of Warnsdorff's heuristic rule.


### Backtracking

First, let's begin by visualizing and considering how to tackle the Knight's Tour problem. Let's assume we start at position D5. Now, let's examine the potential moves available from this starting point:

<img src="assets/img/example1.png" width="400">

Because the knight moves in an 'L' shape, involving 2 moves in one direction and 1 in another, we have a total of 8 potential moves at our disposal. Let's select one:

<img src="assets/img/example2.png" width="400">

Now, you can see that we have only 7 possible moves since we have already been to one of them (D5). It's important to keep in mind that making the wrong choices of movements can lead to getting stuck in the tour. Let's take a look at the example below:

<img src="assets/img/example3.png" width="400">

In the example above, the knight moved as follows: F4, G6, E5, F7, and H8. From position H8, the knight has two options: G6 and F7, but unfortunately, these have already been visited. In this case, we need to backtrack one (or more, depending on the situation) step and try different paths to avoid getting stuck. To solve this, the software was built using the backtracking technique. So for each dead end, the program goes back one move and tries a different one.

<img src="assets/img/backtracking.png" width="600">

### Recursion

Since we need to check many different possible paths and, therefore, call the solution function several times, the software uses recursion to solve this. Let's take a look at the structure of the solution function:

```python
def solution():
    if all squares are visited:
        print "Knight's Tour"
        return True
    else:
        possible_movements = possible_movements_function()

        if possible_movements == []:
            """If there are no possible movements, we return False. 
            This will remove this move from the solution vector, backtrack one movement,
            and try other alternative moves."""

        for move in possible_movements:
            """Add the move to the solution vector and recursively check if this move leads to a solution.

            If the move chosen in the above step doesn't lead to a solution, then remove this
            move from the solution vector and try other alternative moves.

            If none of the alternatives work, then return false. Returning false will remove
            the previously added item in recursion, and if false is returned by the initial
            call of recursion, then "no solution exists.""""

``` 

### Warnsdorff's Rule

You can imagine that this would take a while to compute since from each position, we have 8 (or fewer) possible next moves, and each one of these next moves produces more possible moves. As a result, you can notice that this leads to exponential growth in the number of possible paths, and as you explore different paths, the search space expands rapidly. Another cost factor for the computation is the number of possible solutions you can return, which makes the challenge not just finding one specific solution, but rather finding any valid solution. Therefore, we need a feature in our software that makes it faster, and that's Warnsdorff's Rule.

This simple rule was formulated by the German mathematician H.C. Warnsdorff in 1823, and it consists of the following principle:

> **Always move the knight to an adjacent, unvisited square with minimal degree.**

The primary objective of this rule is to move the knight to an unvisited square that has the fewest possible moves. However, because Warnsdorff’s rule is heuristic, it is not guaranteed to find a solution.



## Getting Started

First, let's clone and enter this repository on your local machine:

```bash
   git clone https://github.com/Adneycm/knights-tour.git
   cd knights-tour
```
To run this project on your local machine, you'll need to have Python installed. Once you have Python installed, you also need to install some Python libraries, namely numpy and Pygame. These libraries are already listed in the requirements file, so you can simply run the following command in your local project directory:

```bash
   pip install -r requirements.txt
```

If you prefer to install them manually, here are the specific versions:

```bash
numpy==1.26.0
pygame==2.5.2
```

## Usage

I've prepared a video teaching how to use it, and you can simply watch it by clicking on this link: [Youtube Video]()

To run the application, you can use the following command:
```bash
   python main.py
```
You can choose the starting position of the tour by clicking on any square of the chessboard. After the tour is finished, you can press 'C' to clear the chessboard and start a new tour. You can also select different chessboard sizes by pressing 5, 6, 7, 8, or 9.


## Acknowledgements

I'd like to provide some sources of inspiration and further study materials related to this project:

- [Knight's Tour - Numberphile](https://www.youtube.com/watch?v=ab_dY3dZFHM&t=96s)
- [Image Encryption Scheme Based on Knight’s Tour Problem](https://pdf.sciencedirectassets.com/280203/1-s2.0-S1877050915X00329/1-s2.0-S1877050915032457/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIF4GyojL%2Fs3KvJeLJ%2BmybZxBXbW%2Ff%2B9uKvvQgRvmm%2BgSAiEAkY%2B0Rc28DCgzZaSsg7Q63Dico84kxqZB3wg2m2kyIlcqvAUI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAFGgwwNTkwMDM1NDY4NjUiDHkk9HTwfvhH6OgmUyqQBSkOa9UMliuTNbpJJMFDo11J6thCxRr79nLEw7b01YGc6SxYqRR3ljhlGb979xGl8My5tsGlewI4%2F8TdCijqmPRPN8RzC3JHelaBROhD6JHZ2ajD93B0cMCUkhcRqa%2FMbTMjB%2F3L6eRqHC0iMs46jcRNdb1g%2Fkz40gO%2Fw4ikaeBpG0yC9TZAyAP%2F0ln1NtWZTAExfi2sbYPR0o9o1%2FInMouaK4bZYV6siwjN2GQIwkJlbTuAxTQM0bA3e47rw70VokQftr6t68lg5GJDAxN5VlvVlhunFAdlokLZkrVAXE7AjfQKlmn81AP6tlCe2MutP74r5MGgdsemAcGboqr280%2B5aDxwlLfMtYzYZoXJJsbVlCviFUfA6N9F7%2Fd3fbswe9CojhyUZkJXiVwl2KZhZHezXcpZJkcQTF5GINNm%2Fq%2FWBHxcP4JVR0I1pU4Q5MXjyyKkaZqWjWWyiox%2Ff%2Fj5FkuzMD6Mh3HoMxINdkWJSSuJ0jEGqgka%2FX6H7ZVBRQTpZedP%2BNno6N9RnVqYU3aRkCGuK5fF%2Ft7OZ97RQbmnLKDTotX3g7OZsyuZWoOax7y9Or5QrO8HX%2F%2BT0Nn2AQeolAqhRxSA%2Bb1KeXawOJ9POul987wTS7jHEsmxpcUMSfGvU8cJbPuHFLRwlg%2Fw4GyUR3WeM9zPwT%2Fw6knQZoRtIBhZaNPn3NBd0gBPySrtKNgAesqFmjYzMANo5w1qpeCeD0f7t18NzfMimsLT%2B5fyPA7V45fEVWxAmhahLLwlJF6EdzFb7lV5WjGm68QDoMColFjJP%2B%2FXqymuRwt1qDF4GO65hr6oxaDJW9LRlSSjBxxlXuN4FZCq9dv4z%2Bj4LNwn5ljOwfQkX8KSs81jjWzGNcUVMLT0yKkGOrEB2DzN8Dv7uQljS6aqslOBNZ7%2B6FC%2Be1XVBFXkrLdCbnbGySuU5WuZX6Ibd6U8v2v%2BVaHnyY%2BNmvGoQCeODboFqLLGflJaK18MqwrMjAsHAH8eZv%2FmSCDihbTFQT4drUfwdj8CSw1m0Yj7Yquq%2BRH%2BKBDaA%2Fcwjfv4WDqSmPTV%2B9Rij0cko7blaDqm3A4EAJik0faXI0EigVdhvBEhZ%2BZUlE%2B0dHlt%2Fbfs7RFZ6V1402r9&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231020T090959Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY3BOYPW4I%2F20231020%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a3390b981b25041d8a46d0ef42fb7e225a345fdd45f4e71b33b4f9d5c709f1b6&hash=1b4e10b08966fd0b49c709b05ee5e02915a525c1f4136b24f006376a25322a16&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1877050915032457&tid=spdf-8568cad1-5d58-450a-b19e-81d7ae777abc&sid=6710149f94c7644b9c783e39a3e4cb999167gxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=1e035a555c52505f555d03&rr=81902003fca6716c&cc=de)
- [How good is the Warnsdorff’s knight’s tour heuristic?](https://arxiv.org/pdf/0803.4321.pdf)

## References

- https://www.chess.com/analysis?tab=analysis
- https://support.sas.com/resources/papers/proceedings15/3060-2015.pdf
- https://www.geeksforgeeks.org/hamiltonian-cycle/
