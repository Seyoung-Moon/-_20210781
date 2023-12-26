import os
import numpy as np

def load_data(folder):
    data = []
    labels = []
    for filename in os.listdir(folder):
        # 파일명에서 라벨 추출
        label = int(filename.split('_')[0])
        filepath = os.path.join(folder, filename)
        with open(filepath, 'r') as file:
            # 파일 내용을 읽어서 숫자 배열로 변환하여 데이터에 추가
            content = file.read().replace('\n', '')
            data.append([int(digit) for digit in content])
            labels.append(label)
     # NumPy 배열로 변환하여 반환
    return np.array(data), np.array(labels)

def calc_distance(point1, point2):
    # 두 점 간의 유클리드 거리 계산
    return np.sqrt(np.sum((point1 - point2) ** 2))

def k_nn_predict(train_data, train_labels, test_point, k):
    distances = [calc_distance(train_point, test_point) for train_point in train_data]
    # 거리가 가장 짧은 k개의 이웃 인덱스를 찾음
    nearest_indices = np.argsort(distances)[:k]
    nearest_labels = train_labels[nearest_indices]
     # 이웃들의 라벨 중 가장 많이 등장한 라벨을 예측 결과로 반환
    unique_labels, counts = np.unique(nearest_labels, return_counts=True)
    return unique_labels[np.argmax(counts)]

def k_nn_error_rate(train_data, train_labels, test_data, test_labels, k):
    # 모든 테스트 데이터에 대한 예측을 수행
    predictions = [k_nn_predict(train_data, train_labels, test_point, k) for test_point in test_data]
    # 예측 결과와 실제 라벨을 비교하여 에러율 계산
    error_rate = 1 - np.mean(predictions == test_labels)
    return error_rate

def main():
    # 훈련 데이터 및 라벨 로드
    train_data, train_labels = load_data("trainingDigits")

    # 테스트 데이터 및 라벨 로드
    test_data, test_labels = load_data("testDigits")

    # k를 1부터 20까지 변화시켜가며 에러율 출력
    for k in range(1, 21):
        # 현재 k 값에 대한 에러율 계산 및 출력
        error_rate = k_nn_error_rate(train_data, train_labels, test_data, test_labels, k)
        print(int(error_rate * 100))

if __name__ == "__main__":
    main()

