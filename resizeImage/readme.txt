# resizeImage

resizeImage: an application using the Django Framework. The application is a service that reduces images.

The input receives 3 parameters:
file - image file (required)
width - width (required)
height - height (optional). If this parameter is not passed, the image height changes in proportion to the width.

The method returns a reference to the modified image. 
The output image file name is formed as:
<md5>_<width>x<height>.<extension>, where md5 is the md5 hash of the received file name.

The application  checks for the presence of a previously created image. That is, if it was already created earlier, the application does not create it again.