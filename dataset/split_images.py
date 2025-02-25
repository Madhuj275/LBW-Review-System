import os
import random
import shutil

# Paths
train_folder = "C:\\Users\\madhu\\Documents\\lbw\\LBW-Review-System\\dataset\\images\\train"
val_folder = "C:\\Users\\madhu\\Documents\\lbw\\LBW-Review-System\\dataset\\images\\val"
# os.makedirs(val_folder, exist_ok=True)

# Sabhi images ki list
images = os.listdir(train_folder)
total_images = len(images)
print(f"Total images: {total_images}")

# 20% images ka count
val_count = int(total_images * 0.2)
print(f"Validation images: {val_count}")

# Randomly 20% images select karein
val_images = random.sample(images, val_count)

# Selected images ko val folder mein move karein
for image in val_images:
    src = os.path.join(train_folder, image)
    dst = os.path.join(val_folder, image)
    shutil.move(src, dst)
    print(f"Moved: {image}")

print("Images successfully split into train and val folders.")