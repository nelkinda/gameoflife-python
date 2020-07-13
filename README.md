# Game of Life

This is an example implementation of Conway's Game of Life in **Python**.
The primary focus of the implementation is cleanliness, not performance.
It serves as a lose guideline for Nelkinda Coderetreat facilitators.

## Disclaimer
This Python implementation is a new translation from Kotlin and has not yet undergone thorough review.

## Rules of Conway's Game of Life
> The universe of the _Game of Life_ is an infinite, two-dimensional orthogonal grid of square cells.
> Each cell is in one of two possible states:
> * Alive aka populated
> * Dead aka unpopulated
> 
> Every cell interacts with its eight neighbors.
> The neighbors are the cells that are horizontally, vertically, or diagonally adjacent.
> At each step in time, the following transitions occur:
> 1. Underpopulation: Any live cell with fewer than 2 live neighbors dies.
> 1. Survival: Any live cell with 2 or 3 live neighbors survives on to the next generation.
> 1. Overpopulation Any live cell with more than 3 live neighbors dies.
> 1. Reproduction (birth): Any dead cell with exactly 3 live neighbors becomes a live cell.

— [Conway's Game of Life - Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Activities (aka Constraints)
This implementation of Game of Life follows the following activities and constraints:
* Behavior Driven Development.
* Test-Driven Development.
* Immutable objects only (not enforced).
  Only pure functions.
* No variable reassignments (except for the Parser).
* Short functions only.
  Most functions are expression functions.
  Exception: The Parser is big.
* Domain-Specific Language:
  The symbol names are taken from the problem domain.
  A point, for example, is constructed with `P(x, y)` instead of `Point(x, y)`.
  That makes the code shorter and easier to read.
* Functional Core, Imperative Shell:
  The code is purely functional.
  The imperative shell is so far out that it's in the test only.
  The Parser implementation is imperative, but its interface and observable behavior are functional.

## References
- [Coderetreat](https://www.coderetreat.org/)
- [Conway's Game of Life - Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Questions/Contact
* [E-Mail: events@nelkinda.com](mailto:events@nelkinda.com)
* [Nelkinda Website](https://nelkinda.com/)
* [Nelkinda Events](https://nelkinda.com/events/)
* [Twitter (Nelkinda)](https://twitter.com/nelkinda)
* [Twitter (Christian Hujer)](https://twitter.com/christianhujer)
* [Facebook](https://www.facebook.com/nelkinda/)
* [LinkedIn](https://www.linkedin.com/company/nelkinda/)
