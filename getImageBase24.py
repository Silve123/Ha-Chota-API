import base64

def get_image_base24(image_file):
    # Open and read the image file in binary mode
    with open(image_file, 'rb') as image_file:
        # Read the binary data
        image_binary = image_file.read()

    # Encode the binary data as Base64
    base64_encoded = base64.b64encode(image_binary)

    # Convert the bytes to a string (UTF-8 encoding)
    base64_string = base64_encoded.decode('utf-8')

    # Print or use the Base64 string as needed
    return base64_string

def get_items():
    itemsList = []
    with open('items.txt') as items:
        for item in items.readlines():
            item = item.split(",")
            # Convert the 'on_special' value to an integer
            to_boolean = 1 if item[5].strip() == 'True' else 0
            item[5] = to_boolean  # Set the 'on_special' field as an integer
            item[-1] = to_boolean
            item[4] = get_image_base24('images/'+item[4].replace("'", "")[1:])
            holdingTuple = ()
            for singleItem in item:
                holdingTuple = holdingTuple + (singleItem,)
            itemsList.append(holdingTuple)
    return itemsList




if __name__ == "__main__":
    get_items()