# pixel2image

[<img src="https://img.youtube.com/vi/03nbVihRpf0/maxresdefault.jpg" width="50%">](https://youtu.be/03nbVihRpf0)
  
  ## Steps to follow:
  #### 1. Collect images.
      In my case i scraped gettyimages site to get around 3000 images of MS Dhoni. 
      Try and get as many images as possible.
      (Also try to get some images with dark lighting and also with very bright lighting).
  #### 2. Resize and convert the images to greyscale.
      Convert all the images collected to grescale and 1:1 aspect ratio.
      I converted all the images to 100 by 100 pixels.
      It can done be with other resolutions as well, as long as they are 1:1. 
  #### 3. Calculate average intensity of a images.
      Add all the intensities of the pixels in the greyscale image and divide by total number of pixels.
      Sort the images based on their intensities.
  #### 4. Render the image
      Choose the picture you want to use for rendering and resize it. 
      Access each pixel intensity in the image and replace it with the corresponding image with same intensity.
      If there isnt a image with same intensity, then replace it with a image having closest intensity.
