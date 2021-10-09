import os
import cv2

dir_path = os.path.dirname(os.path.realpath(__file__))
img_dir_path = dir_path + "/picked_faces/"
resized_dir_path = dir_path + "/resized_faces/"
if not os.path.isdir(resized_dir_path):
    os.mkdir(resized_dir_path)

img_width = 0
img_height = 0
faces = 0
for file in os.listdir(img_dir_path):
    filepath = img_dir_path + file
    if filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        faces += 1
        img = cv2.imread(filepath)
        img_height += img.shape[0]
        img_width += img.shape[1]

img_width //= faces
img_height //= faces
img_shape = (img_height, img_width)
print(img_shape)

for file in os.listdir(img_dir_path):
    filepath = img_dir_path + file
    if filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        img = cv2.imread(filepath)
        resized_img = cv2.resize(img, img_shape, interpolation=cv2.INTER_AREA)
        path = resized_dir_path + file
        cv2.imwrite(path, resized_img)
