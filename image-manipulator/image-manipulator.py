import os, shutil
from PIL import Image, ImageFilter

for filename in os.listdir(): # Creating variables for every image in the directory
    if filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png'):
        file_contents = Image.open(filename)
        globals()[filename] = file_contents

print('Welcome to the Python Interactive Image Manipulation Tool.')
while True:
    print('Valid commands: Open, Open JPEG, Open JPG, Open PNG, Open All, Convert, Resize, Rotate, BW, Blur')
    choice = input("What would you like to do? ").upper()
    
    if choice == 'OPEN':
        target = input("Please specify the name of the image you would like to open: ")
        
        for filename in os.listdir():
            if filename.startswith(target):
                globals()[filename].show()
            
    elif choice == 'OPEN JPEG':
        
        for filename in os.listdir():
            if filename.endswith('.jpeg'):
                globals()[filename].show()
    
    elif choice == 'OPEN JPG':
        
        for filename in os.listdir():
            if filename.endswith('.jpg'):
                globals()[filename].show()
    
    elif choice == 'OPEN PNG':
        
        for filename in os.listdir():
            if filename.endswith('.png'):
                globals()[filename].show()
                
    elif choice == 'OPEN ALL':
        
        for filename in os.listdir():
            globals()[filename].show()
                    
    elif choice == 'CONVERT':
        print('Image Conversion Tool')
        print('This tool will convert an image to a specified format.')
        print('Valid image formats: png, jpg, jpeg')
        toFormat = input("Please specify the format you wish to convert the image to: ").lower()
        
        if toFormat == 'png' or toFormat == 'jpg' or toFormat == 'jpeg':
            target = input("Please specify the name of the image to convert: ")
            
            for filename in os.listdir():
                if filename.startswith(target):
                    file, extension = os.path.splitext(filename)
                    output = file + "." + toFormat
                    
                    if filename != output:
                        try:
                            if os.path.isdir(toFormat) == False:
                                os.mkdir(toFormat)
                                globals()[filename].save(output)
                                shutil.move(os.path.join(os.getcwd(), output), toFormat)
                                print("Converted successfully. You can view the file in " + os.path.join(os.getcwd(), output))
                            elif os.path.isdir(toFormat) == True:
                                globals()[filename].save(output)
                                shutil.move(os.path.join(os.getcwd(), output), toFormat)
                                print("Converted successfully. You can view the file in " + os.path.join(os.getcwd(), output))
                        except OSError:
                            print("Failed to convert", filename)    
                    else:
                        print("Failed to convert", filename, "as it is already in the requested format.")
        else:
            print("Invalid format specified. Valid options are: png, jpg, jpeg")
    
    elif choice == 'RESIZE':
        print('Image Resize Tool')
        print('This tool will create a thumbnail of the specified image in the specified size.')
        print('Valid size formats: 200, 400, 600')
        size = input("Please specify the size thumbnail you wish to create: ")
        target = input("Please specify the name of the image to resize: ")
        
        if size.isnumeric() == True:
            for filename in os.listdir():
                    if filename.startswith(target):
                        output = os.path.splitext(filename)[0] + ".thumbnail"
                        output = output.replace(".", "") + ".jpeg"
                        sizeFormat = (int(size), int(size))
                        
                        if filename != output:
                            try:
                                if os.path.isdir(size) == False:
                                    os.mkdir(size)
                                    with globals()[filename] as im:
                                        im.thumbnail(sizeFormat)
                                        im.save(output, "JPEG")
                                    shutil.move(os.path.join(os.getcwd(), output), size)
                                    print("Thumbnail created successfully. You can view the file in " + os.path.join(os.getcwd(), output))
                                elif os.path.isdir(size) == True:
                                    with globals()[filename] as im:
                                        im.thumbnail(sizeFormat)
                                        im.save(output, "JPEG")
                                    shutil.move(os.path.join(os.getcwd(), output), size)
                                    print("Thumbnail created successfully. You can view the file in " + os.path.join(os.getcwd(), output))
                            except OSError:
                                print("Failed to create thumbnail for", filename)    
                        else:
                            print("Failed to create thumbnail for", filename, "as a thumbnail already exists.")
        else:
            print("Invalid format specified. Valid options are: 200, 400, 600")

    elif choice == 'ROTATE':
        print('Image Rotation Tool')
        print('This tool will rotate an image by the specified amount of degrees.')
        print('Rotation degrees must be between 0-360.')
        deg = input("Please specify the amount of degrees you wish to rotate by: ")
        target = input("Please specify the name of the image to rotate: ")
        
        if deg.isnumeric() == True:
            if int(deg) <= 360 and int(deg) >= 0:
                for filename in os.listdir():
                    if filename.startswith(target):
                        if os.path.isdir('rotation') == False:
                            os.mkdir('rotation')
                            with globals()[filename] as im:
                                output = im.rotate(int(deg))
                                output.save(os.path.join(os.getcwd(), "rotation", filename), "JPEG")
                            print("Rotated successfully. You can view the file in " + os.path.join(os.getcwd(), "rotation", filename))
                        elif os.path.isdir('rotation') == True:
                            with globals()[filename] as im:
                                output = im.rotate(int(deg))
                                output.save(os.path.join(os.getcwd(), "rotation", filename), "JPEG")
                            print("Rotated successfully. You can view the file in " + os.path.join(os.getcwd(), "rotation", filename))
            else:
                print("Invalid degree rotation specified. Must be between 0-360.")    
        else:
            print("Invalid degree rotation specified. Must be a numeric value.")
            
    elif choice == 'BW':
        print('Image Black & White Filter')
        print('This tool will apply a Black & White filter onto the specified image.')
        target = input("Please specify the name of the image to apply the filter onto: ")
        
        for filename in os.listdir():
            if filename.startswith(target):
                if os.path.isdir('bw') == False:
                    os.mkdir('bw')
                    with globals()[filename] as im:
                        output = im.convert('L')
                        output.save(os.path.join(os.getcwd(), "bw", filename), "JPEG")
                    print("Filter applied successfully. You can view the file in " + os.path.join(os.getcwd(), "bw", filename))
                elif os.path.isdir('bw') == True:
                    with globals()[filename] as im:
                       output = im.convert('L')
                       output.save(os.path.join(os.getcwd(), "bw", filename), "JPEG")
                    print("Filter applied successfully. You can view the file in " + os.path.join(os.getcwd(), "bw", filename))
        
    elif choice == 'BLUR':
        print('Image Blur Tool')
        print('This tool will apply a blur on an image by a specified radius.')
        print('Valid blurs: Box, Gaussian')
        print('Blur radius must be between 0-100.')
        blur = input("Please specify the type of blur to apply to the image: ")
        rate = input("Please specify the radius of intensity to blur the image: ")
        target = input("Please specify the name of the image to blur: ")
        
        if rate.isnumeric() == True:
            if int(rate) <= 100 and int(rate) >= 0:
                for filename in os.listdir():
                    if filename.startswith(target):
                        if blur.upper() == 'BOX':
                            if os.path.isdir('blur') == False:
                                os.mkdir('blur')
                                with globals()[filename] as im:
                                    output = im.filter(ImageFilter.BoxBlur(int(rate)))
                                    output.save(os.path.join(os.getcwd(), "blur", filename), "JPEG")
                                print("Box Blur applied successfully. You can view the file in " + os.path.join(os.getcwd(), "rotation", filename))
                            elif os.path.isdir('blur') == True:
                                with globals()[filename] as im:
                                    output = im.filter(ImageFilter.BoxBlur(int(rate)))
                                    output.save(os.path.join(os.getcwd(), "blur", filename), "JPEG")
                                print("Box Blur applied successfully. You can view the file in " + os.path.join(os.getcwd(), "rotation", filename))
                        elif blur.upper() == 'GAUSSIAN':
                            if os.path.isdir('blur') == False:
                                os.mkdir('blur')
                                with globals()[filename] as im:
                                    output = im.filter(ImageFilter.GaussianBlur(int(rate)))
                                    output.save(os.path.join(os.getcwd(), "blur", filename), "JPEG")
                                print("Gaussian Blur applied successfully. You can view the file in " + os.path.join(os.getcwd(), "rotation", filename))
                            elif os.path.isdir('blur') == True:
                                with globals()[filename] as im:
                                    output = im.filter(ImageFilter.GaussianBlur(int(rate)))
                                    output.save(os.path.join(os.getcwd(), "blur", filename), "JPEG")
                                print("Gaussian Blur applied successfully. You can view the file in " + os.path.join(os.getcwd(), "rotation", filename))
                        else:
                            print("Invalid blur type specified. Valid options are: Box, Gaussian.")      
            else:
                print("Invalid blur intensity specified. Must be between 0-100.")
        else:
            print("Invalid blur intensity specified. Must be a numeric value.")
            
    elif choice == 'QUIT':
        quit()
    
    else:
        print("Invalid choice specified.")
