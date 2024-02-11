import re
import qrcode
import os
import shutil


class QRCode:
    def __init__(self, *, version, size, border, folder_path):
        self.path = folder_path
        self.qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=size,
            border=border
        )

    def create_qr(self):
        """Create the QRcode content with some simple content and input verification"""

        while True:
            user_choice: str = input('Input your text or your Link >> ')

            try:
                if user_choice in invalid_type:
                    raise ValueError

                else:
                    # checks if the user input is a link or text or does have 'https' at the start
                    check_input: list = re.split("[ .:/]", user_choice)

                    # QR Code properties such as colors and fit
                    self.qr.make(fit=True)
                    img = self.qr.make_image(fill_color="Black", back_color="White")

                    if check_input[0] == 'https':
                        self.qr.add_data(user_choice)
                        self.create_qr_image(img)

                    # if link
                    elif any(domain in domains for domain in check_input):
                        self.qr.add_data(f'https://{user_choice}')
                        self.create_qr_image(img)

                    # if text
                    else:
                        self.qr.add_data(user_choice)
                        self.create_qr_image(img)

            except ValueError:
                print(f"Please Input a Valid Input\n")
                continue

    def create_qr_image(self, img):
        """
        A function that will create the qrcode png image
        :param img: QRcode properties
        """

        name: str = input('Input your desire file name for your QRCODE >> ')
        file_name: str = f'{name}.png'
        original_path = os.path.abspath(file_name)

        if name in invalid_type:
            print("Please Input a Valid File Name!\n")
            self.create_qr_image(img)

        else:
            # save the image, move the image and print message that the files has been successfully created!
            img.save(file_name)
            shutil.move(original_path, self.path)
            print(f"Your File ({file_name}) has been successfully generated!")
            exit()


def main():
    """Main method"""
    print('Welcome to QRcode Generator!')
    myQR = QRCode(version=2, size=10, border=4, folder_path="C:\\Users\\PC\\Pictures\\myQR")
    myQR.create_qr()


if __name__ == '__main__':
    domains: tuple = ("www", "com", "net", "org", "info", "biz", "ph")
    invalid_type: tuple = (" ", "")
    main()