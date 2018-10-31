#
# Sudoku puzzle solver by by Luigi Poderico (www.poderico.it).
#
import sys
from constraint import Problem


nb2 = 12
nb1 = 12
nb50 = 90
nb20 = 56
nb10 = 21

price = 10.50
total = 20
 
def solve():
    problem = Problem()
    problem.addVariable("X1", range(nb1))
    problem.addVariable("X2", range(nb2))
    problem.addVariable("X50", range(nb50))
    problem.addVariable("X20", range(nb20))
    problem.addVariable("X10", range(nb10))
    problem.addVariable("X", range(nb10))
    
    problem.addConstraint(lambda x1 , x2 , x50 , x10 , x20 :100 * ( total - price ) == x1 * 100 + x2 * 200 + x20 * 20 + x10 * 10 + x50 *50, ["X1","X2","X50","X20","X10"])
    problem.addConstraint(lambda x , x1 , x2 , x50 , x10 , x20 : x == x1 + x2 + x20 + x10 + x50, ["X","X1","X2","X50","X20","X10"])
    
    # Get the solutions.
    solutions = problem.getSolutions()
    minX = solutions[0]["X"]
    solution = solutions[0]
    
    for s in solutions :
        if s["X"] < minX:
            minX = s["X"]
            solution = s
        
    return [solution]


def main():
    solutions = solve()
    # Print the solutions
    print("Found %d solution(s)!" % len(solutions))
    print("X1 = %d" % solutions[0]["X1"])
    print("X2 = %d" % solutions[0]["X2"])
    print("X10 = %d" % solutions[0]["X10"])
    print("X20 = %d" % solutions[0]["X20"])
    print("X50 = %d" % solutions[0]["X50"])
    

if __name__ == "__main__":
    main()
