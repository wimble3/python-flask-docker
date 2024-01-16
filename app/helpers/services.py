from PIL.Image import Image  # noqa: F401

from qrcode import make

from PIL.Image import Image  # noqa: F401


class FileService:
    """Service for working with files."""
    @staticmethod
    def save_pillow_image(pillow_image, path_to_save):
        """
        Saves Pillow file
        Args:
            pillow_image (Image): image from Pillow
            path_to_save (str): filepath of new file

        Returns:
            None:
        """
        pillow_image.save(path_to_save)


class QRCodeService:
    """Service for coding and decoding QR codes."""
    @staticmethod
    def generate_qrcode(text):
        """
        Generates QR code by text.
        Args:
            text (str): text to coding

        Returns:
            Image: pillow image contains QR code
        """
        return make(text)

    @staticmethod
    def decode_qrcode(qrcode):
        """
        Decodes QR code.
        Args:
            qrcode (Image): pillow image contains QR code

        Returns:
            str: decoded text
        """


class RedisService:
    """Service for working with redis."""

