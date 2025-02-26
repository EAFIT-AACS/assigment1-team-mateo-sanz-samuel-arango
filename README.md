# DFA Minimization

## Authors
- **Mateo Sanz Medina**
- **Samuel Arango Echeveri**

## Description
This program reads a Deterministic Finite Automaton (DFA) from an input file and applies the **state minimization algorithm** to find and merge equivalent states. The result is a set of equivalent state pairs, reducing the DFA's complexity.

## File Structure
- **`archivo.txt`** → Input file containing DFA definitions.
- **`main.py`** → Python script that implements DFA minimization.

---

## How the Code Works
### 1. **`obtener_grupo(particiones, estado)`**
This function determines which subset of states (partition) a given state belongs to.
- **Parameters**:
  - `particiones` (list of lists): Current state partitions.
  - `estado` (int): The state whose group is to be determined.
- **Returns**:
  - The index of the partition containing the given state, or `-1` if not found.

### 2. **`minimizardfa(estados, alfabeto, estados_finales, transiciones)`**
Implements the DFA minimization algorithm using state partitioning.
- **Parameters**:
  - `estados` (list of int): Set of DFA states.
  - `alfabeto` (list of str): Alphabet symbols.
  - `estados_finales` (set of int): Final states.
  - `transiciones` (list of lists): Transition table.
- **Process**:
  1. Initial partitioning:
     - Final states are grouped together.
     - Non-final states are grouped together.
  2. Iteratively refines partitions:
     - Splits states into smaller groups based on their transition behavior.
  3. If no further partitioning occurs, outputs equivalent states.
- **Returns**:
  - A formatted string listing equivalent state pairs, or "No hay estados equivalentes" if no states can be merged.

### 3. **`leer_entrada(archivo)`**
Reads the input file and extracts DFA specifications.
- **Parameters**:
  - `archivo` (str): The file name to read from.
- **Process**:
  1. Reads the number of test cases.
  2. Parses each DFA:
     - Reads number of states.
     - Reads the alphabet.
     - Reads the final states.
     - Reads transition table, ensuring each state has correct transitions.
- **Returns**:
  - Number of test cases and a list of parsed DFA configurations.

### 4. **`automata()`**
Main function that executes the minimization process.
- **Process**:
  1. Reads the DFA from `archivo.txt`.
  2. Calls `minimizardfa()` for each test case.
  3. Prints the minimized state pairs or an error message if an issue occurs.

---

## Input File Format (`archivo.txt`)
Each DFA is represented in the following format:
```
1                # Number of test cases
6                # Number of states
0 1              # Alphabet symbols
1 3              # Final states
0 1              # State 0 transitions
2 3              # State 1 transitions
4 5              # State 2 transitions
5 0              # State 3 transitions
3 1              # State 4 transitions
2 4              # State 5 transitions
```
Each line corresponds to:
1. **Number of test cases**.
2. **Number of states**.
3. **Alphabet symbols**.
4. **Final states**.
5. **Transition table** (one row per state).

---

## Example Execution
### **Input (`archivo.txt`)**
```
1
3
a b
2
0 1
1 2
2 0
```
### **Expected Output**
```
Caso 1: (0,2)
```
This means states 0 and 2 are equivalent.

---

## Error Handling
- **"Error en estado X: número incorrecto de transiciones."**
  - The number of transitions in state `X` does not match the alphabet size.
- **"Error al procesar el archivo: {error}"**
  - General error handling when reading the input file.

---

## How to Run the Program
1. Ensure `archivo.txt` follows the correct format.
2. Run the script:
   ```bash
   python main.py
   ```
3. Check the console for minimized state pairs.

---

## Improvements and Notes
- This algorithm assumes states are numbered from `0` to `n-1`.
- Assumes a well-formed input file, with appropriate spacing.
- Future improvements could include:
  - Reading input dynamically instead of from a file.
  - Supporting NFA minimization.
  - Providing a visualization of minimized DFAs.

