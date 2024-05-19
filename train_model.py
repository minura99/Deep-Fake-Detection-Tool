import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define directories
data_directory = 'D:/Desktop/ISP_Project/Testfolder/train'
save_model_dir = 'D:/Desktop/ISP_Project/Pre-trained model'

# Parameters
input_shape = (64, 64, 3)  
batch_size = 16            
epochs = 10                 

# Data preprocessing
train_datagen = ImageDataGenerator(
    rescale=1./255,       
)

# Data generators
train_generator = train_datagen.flow_from_directory(
    data_directory,
    target_size=input_shape[:2],
    batch_size=batch_size,
    class_mode='binary')  

# Model architecture
model = Sequential([
    Conv2D(16, (3, 3), activation='relu', input_shape=input_shape),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')  
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Model Summary (optional)
model.summary()

# Training the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=epochs)

# Save the trained model
model_save_path = os.path.join(save_model_dir, 'model01.h5')
model.save(model_save_path)
print(f"Model saved to {model_save_path}")
