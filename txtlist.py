import os

file_path = "onehand10k_training"  # Path
path_list = os.listdir(file_path)

path_name = []

for i in path_list:
    path_name.append(i.split(".")[0])

# path_name.sort()

for file_name in path_name:
    with open("onehand10k_training.txt", "a") as file:
        file.write("onehand10k_training/"+file_name + ".jpg" + " " +"onehand10k_training_blur/"+ file_name + ".jpg" + "\n")
        print(file_name)
