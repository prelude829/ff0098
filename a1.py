import os
import pandas as pd

# CSV 파일 경로
csv_path = 'pokemon.csv'

# 이미지와 라벨 저장 폴더
image_dir = 'yolov5/data/pokemon/images/train'
label_dir = 'yolov5/data/pokemon/labels/train'

# 폴더 생성
os.makedirs(image_dir, exist_ok=True)
os.makedirs(label_dir, exist_ok=True)

# CSV 파일 읽기
df = pd.read_csv(csv_path)

# 클래스 이름 -> ID 매핑
class_mapping = {name: idx for idx, name in enumerate(df['Type1'].unique())}

# 라벨 파일 생성
for _, row in df.iterrows():
    image_name = row['Name'] + '.png'  # 이미지 파일 이름
    class_id = class_mapping[row['Type1']]  # 클래스 ID
    x_center, y_center = row['x_center'], row['y_center']  # 중심 좌표
    width, height = row['width'], row['height']  # 바운딩 박스 크기

    # 라벨 파일 생성
    label_path = os.path.join(label_dir, image_name.replace('.png', '.txt'))
    with open(label_path, 'w') as f:
        f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")
