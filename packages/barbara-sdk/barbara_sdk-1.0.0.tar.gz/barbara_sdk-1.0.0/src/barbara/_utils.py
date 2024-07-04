import os
import hashlib
import base64
import shutil

def calculate_next_version(previous_version):
    """
    Calculate the next version number based on the previous version.
    If no previous version is provided, it defaults to "1.0.0".
    
    Parameters:
    previous_version (str): The previous version number in the format 'major.minor.patch'.
    
    Returns:
    str: The next version number.
    """
    # Check if a previous version was provided
    if previous_version:
        # Split the previous version string into major, minor, and patch components
        major_minor_patch = previous_version.split('.')
        # Increment the patch version by 1
        major_minor_patch[2] = str(int(major_minor_patch[2]) + 1)
        # Combine the components back into a version string
        next_version = major_minor_patch[0] + '.' + major_minor_patch[1] + '.' + major_minor_patch[2]
    else:
        # Default to version "1.0.0" if no previous version is provided
        next_version = "1.0.0"
    # Return the next version number
    return next_version

def calculate_sha(file_path):
    """
    Calculate the SHA-256 hash of a file.
    
    Parameters:
    file_path (str): The path to the file to be hashed.
    
    Returns:
    str: The hexadecimal representation of the SHA-256 hash.
    """
    # Define the block size for reading the file in chunks
    block_size = 65536
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()
    # Open the file in binary read mode
    with open(file_path, 'rb') as f:
        # Read the file in chunks and update the hash object
        for byte_block in iter(lambda: f.read(block_size), b''):
            sha256.update(byte_block)
    # Return the hexadecimal representation of the hash
    return sha256.hexdigest()

def encode_to_base64(string):
    """
    Encode a string to Base64.
    
    Parameters:
    string (str): The input string to be encoded.
    
    Returns:
    str: The Base64 encoded string.
    """
    # Convert the string to bytes using ASCII encoding
    string_bytes = string.encode("ascii")
    # Encode the bytes to Base64
    base64_bytes = base64.b64encode(string_bytes)
    # Convert the Base64 bytes back to a string using ASCII encoding
    base64_string = base64_bytes.decode("ascii")
    # Return the Base64 encoded string
    return base64_string

def get_file_size(file_path):
    """
    Get the size of a file in bytes.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    int: The size of the file in bytes.
    """
    # Return the size of the file in bytes
    return os.path.getsize(file_path)

def zip_folder(folder_path):
    """
    Zip the contents of a folder.
    
    Parameters:
    folder_path (str): The path to the folder to be zipped.
    
    Returns:
    str: The path to the created zip file.
    """
    # Check if the folder path ends with a slash and remove it if it does
    if folder_path.endswith('/'):
        folder_path = os.path.dirname(folder_path)
    # Create a zip archive of the folder
    shutil.make_archive(folder_path, 'zip', folder_path)
    # Construct the path to the zip file
    zip_path = folder_path + '.zip'
    # Return the path to the zip file
    return zip_path