let pyodide;

async function loadPyodideAndPackages() {
  pyodide = await loadPyodide();
  const response = await fetch("solver.py");
  const code = await response.text();
  await pyodide.runPythonAsync(code);
}

loadPyodideAndPackages();

async function solveSudoku() {
  const gridText = document.getElementById("input-grid").value;
  const output = await pyodide.runPythonAsync(`
grid = '''${gridText}'''
solve_and_format(grid)
`);
  document.getElementById("output").textContent = output;
}