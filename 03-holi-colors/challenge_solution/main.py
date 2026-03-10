def find_missing_colors(grid):
  colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
  
  present = set()

  for row in grid:
      for cell in row:
        present.add(cell)

  missing = []
  for c in colors:
    if c not in present:
      missing.append(c)
  return missing

grid =[["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟥"],
  ["🟨", "🟩", "🟦", "🟪", "🟥", "🟧", "🟨"],
  ["🟦", "🟥", "🟧", "🟨", "🟩", "🟪", "🟦"],
  ["🟩", "🟦", "🟪", "🟥", "🟧", "🟨", "🟩"],
  ["🟧", "🟨", "🟩", "🟦", "🟪", "🟥", "🟧"],
  ["🟪", "🟧", "🟨", "🟩", "🟦", "🟥", "🟪"],
  ["🟥", "🟦", "🟩", "🟪", "🟨", "🟧", "🟦"]]

print(find_missing_colors(grid))