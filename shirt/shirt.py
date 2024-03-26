import os
import sys
from PIL import Image, ImageOps


if len(sys.argv)==3:
    extensions=(".jpg",".jpeg",".png")
    if not sys.argv[1].endswith(extensions):
        sys.exit("Invalid input")
    if not sys.argv[2].endswith(extensions):
        sys.exit("Invalid output")

    before=os.path.splitext(sys.argv[1])
    after=os.path.splitext(sys.argv[2])



    if (before[1]==after[1]) and before[1] in extensions:
        try :
            uimage=Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("Input does not exist")

        shirt = Image.open("shirt.png")
        size= shirt.size #sends tuple of dimensions of shirt
        uimage= ImageOps.fit(uimage, size)# resizing the before1 muppet to the shirt size
        uimage.paste(shirt, shirt)
        uimage.save(sys.argv[2])
    else:
        sys.exit("Input and output have different extensions")

elif len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")



