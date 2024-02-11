import time
import re
import qrcode


# function for qrcode properties
def qr_properties(qr):
    qr.make()
    qr.make(fit=True)
    image = qr.make_image(fill_color="Black", back_color="White")

    return image


# function to create the qrcode png image
def create_qr_image(img) -> str:

    while True:
        file_name: str = input('Input your desire file name for your QRCODE >> ')

        try:
            if file_name in invalid_type:
                raise ValueError

        except ValueError:
            print("Please Input a Valid File Name!\n")
            continue

        else:
            file: str = img.save(f'{file_name}.png')

            # print message that the files has been successfully created!
            print(f"Your File ({file_name}.png) has been successfully generated!")
            time.sleep(2)  # wait 2 seconds to exit the system

            return file


# function to create the qrcode contents based on condition met
def create_qrcode(qr) -> str:

    while True:

        user_choice: str = input('Input your text or your Link >> ').strip().lower()

        # catch exception if the user tries to create an empty or space value
        try:
            if user_choice in invalid_type:
                raise ValueError

        except ValueError:
            print("Please Input a Valid choices or inputs\n")
            continue

        else:
            # checks if the user input is a link or text or does have 'https' at the start
            check_input: list = re.split("[ .:/]", user_choice)

            # if the link has "https" at the start
            if check_input[0] == 'https':
                qr.add_data(user_choice)
                img = qr_properties(qr)

                return create_qr_image(img)

            # if link
            elif any(domain in domains for domain in check_input):
                qr.add_data(f'https://{user_choice}')
                img = qr_properties(qr)

                return create_qr_image(img)

            # if text
            else:
                qr.add_data(user_choice)
                img = qr_properties(qr)

                return create_qr_image(img)


# main function
def main():
    print("Welcome to My Project QRcode generator!")

    # Initialize the properties of the qrcode
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    create_qrcode(qr)    # create_qr_image(image)


if __name__ == '__main__':
    domains: tuple = ("www", "com", "net", "org", "info", "biz", "ph")
    invalid_type: tuple = (" ", "")
    main()