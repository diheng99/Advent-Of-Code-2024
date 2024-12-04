data = []

with open("Day4.txt", "r") as file:
    for line in file:
        data.append(line.strip())

def find_xmas(inputData):
    
    # insert transpose
    lines = inputData[:]
    lines.extend(["".join(row[i] for row in inputData) for i in range(len(data[0]))])
    
    def find_diagonal(array):
        col, row = len(array[0]), len(array)

        diagonal_dict = {}
        anti_diagonal_dict = {}

        for rows in range(row):
            for cols in range(col):
                diagonal_key = rows - cols
                if diagonal_key not in diagonal_dict:
                    diagonal_dict[diagonal_key] = []
                diagonal_dict[diagonal_key].append(array[rows][cols])

                diagonal_key = rows + cols
                if diagonal_key not in anti_diagonal_dict:
                    anti_diagonal_dict[diagonal_key] = []
                anti_diagonal_dict[diagonal_key].append(array[rows][cols])
        
        return diagonal_dict, anti_diagonal_dict
       
    diagonals, anti_diagonals = find_diagonal(inputData)
    
    lines.extend("".join(i) for i in diagonals.values())
    lines.extend("".join(i) for i in anti_diagonals.values())

    count = sum(line.count("XMAS") + line.count("SAMX") for line in lines)

    return count

result = find_xmas(data)
print(result)

def find_mas(array):
    row, col = len(array), len(array[0])

    _set = {"M", "S"}

    count = 0
    for r in range(1, row -1):
        for c in range(1, col-1):
            if array[r][c] == "A":
                if {array[r+1][c+1], array[r-1][c-1]} == _set and {array[r-1][c+1], array[r+1][c-1]} == _set:
                    count += 1
                
    return count

result = find_mas(data)
print(result)