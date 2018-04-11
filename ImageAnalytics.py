from .FaceDetector import FaceDetector


class ImageAnalytics:
    def __init__(self):
        self.fd = FaceDetector()
    
    def get_face_score(self, img):
        """
        Gives image score 0 if it contains faces and 1 otherwise
        :param img: Image
        :return: 0 or 1
        """
        face = self.fd.is_with_faces(img)
        return int(not face)
