data = []

with open("Day4.txt", "r") as file:
    for line in file:
        data.append(line.strip())

def find_xmas(inputData):
    
    # insert transpose
    lines = data
    lines.extend(["".join(row[i] for row in inputData) for i in range(len(data[0]))])
        
            
    
    print(inputData)
find_xmas(data)