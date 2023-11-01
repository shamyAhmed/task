with open("../assets/dataset-interview.csv", mode="r") as reader, open("../assets/dataset-limited.csv", mode="w") as writer:
    index = 1
    for line in reader:
        writer.write(line)
        index += 1
        if index == 200:
            break
        
    
    