def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    greyscale = []
    # Write code here
    for pixel in image:
        greypixel = []
        for i in (pixel):
          grey = 0.299*i[0]+0.587*i[1]+0.114*i[2]
          greypixel.append(round(grey,3))
        greyscale.append(greypixel)
    return (greyscale)