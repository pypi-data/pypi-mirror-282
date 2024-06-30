from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2

class TMEasy(object):

    def __init__(self, model_path='keras_model.h5', labels_file_path='labels.txt', model_type='h5') -> None:
        self._model_type = model_type.lower()
        self._labels_file_path = labels_file_path
        self._supported_types = ('keras', 'Keras', 'h5', 'h5py')

        np.set_printoptions(suppress=True)
        try:
            self._model = load_model(model_path, compile=False)
        except IOError as e:
            print('LoadingModelError: 티처블 머신 모델을 불러오는 중 오류가 발생하였습니다')
            raise IOError from e
        except:
            print("LoadingModelError: 티처블 머신 모델을 불러오는 중 오류가 발생하였습니다")
            raise FileNotFoundError
        try:
            self._labels_file = open(self._labels_file_path, "r").readlines()
        except IOError as e:
            print('LoadingLabelsError: labels.txt 파일을 불러오는 중 오류가 발생하였습니다')
            raise IOError from e
        except:
            print("LoadingLabelsError: labels.txt 파일을 불러오는 중 오류가 발생하였습니다")
            raise FileNotFoundError

        self._object_creation_status = self._model_type in self._supported_types
        if self._object_creation_status:
            print('모델 불러오기를 성공하였습니다.')
        else:
            raise 'NotSupportedType: 지원되지 않는 모델 유형입니다. "keras" 또는 "h5"를 사용하세요.'

    def classify_image(self, frame_path: str):
        try:
            frame = Image.open(frame_path)
            if frame.mode != "RGB":
                frame = frame.convert("RGB")
        except FileNotFoundError as e:
            print("ImageNotFound: 이미지를 찾을 수 없습니다")
            raise FileNotFoundError from e
        except TypeError as e:
            print(
                "ImageTypeError: 이미지를 RGB로 전환할 수 없습니다.")
        try:
            if self._object_creation_status:
                return self._get_image_classification(frame)
        except BaseException as e:
            print('분류 중 오류가 발생하였습니다.')
            raise e

    def _get_image_classification(self, image):
        data = self._form_image(image)
        prediction = self._model.predict(data, verbose=0)
        class_index = np.argmax(prediction)
        class_name = self._labels_file[class_index]
        class_confidence = prediction[0][class_index]

        return {
            "class_name": class_name[2:],
            "highest_class_name": class_name[2:],
            "highest_class_id": class_index,
            "class_index": class_index,
            "class_id": class_index,
            "predictions": prediction,
            "all_predictions": prediction,
            "class_confidence": class_confidence,
            "highest_class_confidence": class_confidence,
        }

    def _form_image(self, image):
        image_data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        crop_size = (224, 224)
        image = ImageOps.fit(image, crop_size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)

        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        image_data[0] = normalized_image_array
        return image_data

    def cap(self, capt):
        ret, img = capt.read()
        img = cv2.flip(img, 1)
        cv2.imwrite("temp.jpg", img)
        result = self.classify_image("temp.jpg")

        cv2.putText(img, result['class_name'][:-1], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        return img, result['class_name'][:-1]