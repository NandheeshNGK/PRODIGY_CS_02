#PRODIGY_CS_02
#TASK 2

from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Ensure key has the same shape as img_array
    key = np.resize(key, img_array.shape)

    # Encrypt each pixel using XOR with the key
    encrypted_array = np.bitwise_xor(img_array, key)
    
    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save("Your_encrypted_image.png")
    print("Image has been encrypted successfully.")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Convert the encrypted image to a NumPy array
    encrypted_array = np.array(encrypted_img)

    # Ensure key has the same shape as encrypted_array
    key = np.resize(key, encrypted_array.shape)

    # Decrypt each pixel using XOR with the key
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    
    # Convert the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_img.save("Your_decrypted_image.png")
    print("Image has been decrypted successfully.")

def main():
    print("Image Encryption and Decryption using Pixel Manipulation")

    # Get the path to the original image from the user
    image_path = input("Enter the path to the image file: ").strip()  # Remove any leading/trailing spaces

    # Input validation for the key value
    while True:
        try:
            # Get the key value from the user
            key_value = int(input("Enter the key value for encryption/decryption (0-255): "))
            if 0 <= key_value <= 255:
                key = np.array([key_value], dtype=np.uint8)
                break
            else:
                print("Key value must be between 0 and 255. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer between 0 and 255.")

    # Encrypt the image
    encrypt_image(image_path, key)
    
    # Decrypt the image
    decrypt_image("Your_encrypted_image.png", key)

if __name__ == "__main__":
    main()
