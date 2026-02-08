# 🤖 Reeborg's Maze Escape (Day 05)

A Python solution for guiding Reeborg the robot through a complex maze in the Reeborg's World environment. This project focuses on developing a robust algorithm using `while` loops and conditional statements to navigate a dynamic maze, where Reeborg's starting position and orientation can vary.

---

### ❓ What does this project do?
This project provides a Python script designed to solve various maze challenges within the Reeborg's World simulator. The core functionality includes:
*   **Intelligent Navigation**: Reeborg follows a predefined logic to find its way through walls and obstacles.
*   **Dynamic Adaptation**: The algorithm is capable of handling different starting positions and orientations of Reeborg within the maze.
*   **Goal-Oriented Movement**: Reeborg continuously moves towards the checkered flag (goal) using a combination of movement and turning functions.
*   **Complex Logic**: Utilizes nested `while` loops and `if-elif-else` statements to react to Reeborg's surroundings (walls, clear paths, facing direction).

---

### Technologies Used
*   **Python**: The core programming language used for writing Reeborg's logic.
*   **Reeborg's World Simulator**: The online platform (like `https://reeborg.ca/`) providing the maze environment and built-in robot functions.

---

### 📘 Learning Outcomes
In this project, I practiced:
*   **Algorithmic Thinking**: Designing a step-by-step solution for a complex navigation problem.
*   **`while` Loops**: Mastering the use of `while` loops for continuous actions until a condition is met (`not at_goal()`).
*   **Conditional Logic (`if-elif-else`)**: Implementing advanced decision-making based on multiple environmental factors (e.g., `front_is_clear()`, `wall_on_right()`, `is_facing_north()`).
*   **Problem Solving in Dynamic Environments**: Creating code that works regardless of the initial state of the robot.
*   **Decomposition**: Breaking down a large problem (maze escape) into smaller, manageable logical blocks.
*   **Debugging and Refinement**: Iteratively testing and improving the robot's logic to handle edge cases.

---

### How to Run
This project is designed to be run within the [Reeborg's World](https://reeborg.ca/reeborg.html) online simulator.

1.  **Go to Reeborg's World:**
    Open your web browser and navigate to `https://reeborg.ca/`.
2.  **Select the World:**
    Load the maze world. You can usually find it in a dropdown menu.
3.  **Paste the Python Code:**
    In the "Python Code" tab (usually on the right side), clear any existing code and paste my code.
4.  **Run the Simulation:**
    Click the "Run" (▶️) button in the Reeborg's World interface to see the robot navigate the maze according to your code.
