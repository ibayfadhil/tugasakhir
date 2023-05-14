#file = open("latihan\data.txt",mode="r")

#print(file.read())

import base64, os
file = 'latihan\CV_Habibie Rizqi.pdf'
with open(file, 'rb') as f:
    content = f.read()
    print(content)

enkripsi = content # Data biner dalam format byte string
with open('file.pdf', 'wb') as file:
    file.write(enkripsi)


# Konversi PDF ke biner
#with open('latihan\CV_Habibie Rizqi.pdf', 'rb') as file:
#    binary_data = file.read()

# Konversi biner ke PDF
#with open('file_new.pdf', 'wb') as file:
#    file.write(binary_data)


#binary_data = b'content' # Data biner dalam format byte string
#with open('file.pdf', 'wb') as file:
   # file.write(binary_data)



#binary_data = file.read()
#char = ''.join(content) 
#binary_content = base64.b64encode(content)

#encode_content = base64.b64encode(content)
#encode_content_str = encode_content.decode('utf-8')


#decoded_content = base64.b64decode(encode_content_str)

#with open('new_image.jpg', 'web') as f:
#    f.write(decoded_content)
