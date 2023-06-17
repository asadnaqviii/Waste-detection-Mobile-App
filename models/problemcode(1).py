from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

label_map = {1:'waste'}
train_images_dir = 'train'
train_annotations_dir = 'train'
val_images_dir = 'valid'
val_annotations_dir = 'valid'
test_images_dir = 'test'
test_annotations_dir = 'test'


use_custom_dataset = True

dataset_is_split = True 

if use_custom_dataset:
  if dataset_is_split:
    train_data = object_detector.DataLoader.from_pascal_voc(
        'train','train', label_map=label_map)
    validation_data = object_detector.DataLoader.from_pascal_voc(
        val_images_dir, val_annotations_dir, label_map=label_map)
    test_data = object_detector.DataLoader.from_pascal_voc(
        test_images_dir, test_annotations_dir, label_map=label_map)
    

    
  print(f'train count: {len(train_data)}')
  print(f'validation count: {len(validation_data)}')
  print(f'test count: {len(test_data)}')