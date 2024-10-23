from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout, Rescaling
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.densenet import DenseNet121
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.callbacks import CSVLogger
import pathlib
import os
import pickle
import matplotlib.pyplot as plt
import pandas as pd


def training(model):
    weight_dir = './weights'
    if not os.path.exists(weight_dir):
        os.makedirs(weight_dir)

    log_dir = './trains'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    data_path = pathlib.Path('./dataset')

    train_ds = image_dataset_from_directory(os.path.join(data_path, 'train'), seed=42, image_size=(224, 224), batch_size=16)
    test_ds = image_dataset_from_directory(os.path.join(data_path, 'test'), seed=42, image_size=(224, 224), batch_size=16)

    if model == 'DenseNet121':
        base_model = DenseNet121(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    elif model == 'ResNet50':
        base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    elif model == 'VGG16':
        base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    cnn = Sequential()
    cnn.add(Rescaling(1.0 / 255.0))
    cnn.add(base_model)
    cnn.add(Flatten())
    cnn.add(Dense(1024, activation='relu'))
    cnn.add(Dropout(0.75))
    cnn.add(Dense(units=120, activation='softmax'))

    cnn.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(learning_rate=0.0001), metrics=['accuracy'])

    csv_logger = CSVLogger(os.path.join(log_dir, f'{model}_log.txt'), append=True)

    hist = cnn.fit(train_ds, epochs=50, validation_data=test_ds, verbose=2, callbacks=[csv_logger])

    cnn.save(os.path.join(weight_dir, f'{model}.h5'))

    f = open(os.path.join(log_dir, 'apple_disease_types.txt', 'wb'))
    pickle.dump(train_ds.class_names, f)
    f.close()


def drawing_training(model):
    graph_dir = './graph'
    if not os.path.exists(graph_dir):
        os.makedirs(graph_dir)

    data = pd.read_csv(f'./trains/{model}_log.txt')

    # 에포크
    epochs = data['epoch']

    # 정확도
    train_accuracy = data['accuracy']
    val_accuracy = data['val_accuracy']

    # 손실
    train_loss = data['loss']
    val_loss = data['val_loss']

    # 정확도 그래프
    plt.figure(figsize=(14, 6))
    plt.suptitle(f'{model}')

    plt.subplot(1, 2, 1)
    plt.plot(epochs, train_accuracy, label='Train Accuracy')
    plt.plot(epochs, val_accuracy, label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Accuracy vs. Epoch')
    plt.legend()

    # 손실 그래프
    plt.subplot(1, 2, 2)
    plt.plot(epochs, train_loss, label='Train Loss')
    plt.plot(epochs, val_loss, label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss vs. Epoch')
    plt.legend()

    plt.tight_layout(rect=[0,0,1,0.96])
    plt.savefig(os.path.join(graph_dir, f'{model}_result.png'))


def main():
    models = ['DenseNet121', 'ResNet50', 'VGG16']

    for model in models:
        # 1. MODEL TRAINING
        training(model)

        # 2. DRAWING GRAPH
        drawing_training(model)


if __name__ == '__main__':
    main()
