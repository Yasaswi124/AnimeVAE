# Implemntating a Variational Autoencoder in keras on images.

Variational Autoencoders differ from regular autoencoders in the fact that they have a continous latent space, allowing linear interpolation to genearte realistic looking images by combining multiple images. The animation below cycles through different images. Every tenth frame in the animation is a reconstruted image from the dataset, with the rest of the frames generated from linear interpolation of the encoding of 2 images, generating an image not in the dataset.
<br><br>
<p align="center">
  <img width="256" height="256" src="https://github.com/Yasaswi124/CatsVAE/blob/main/visualizations/faces.gif">
</p>
<p align="center">
  <sub> GIF of images reconstructed from linear interpolation in latent space</sub>
</p>
<br>

The frames for this images were created using linear interpolation, an example can be seen in the animtion below.


<p align="center">
  <img width="256" height="256" src="https://github.com/Yasaswi124/AnimeVAE/blob/main/visualizations/linear_interpolation.gif">
</p>
<p align="center">
  <sub>Linear Interpolation in 2D space</sub>
</p>

In the animation above, the point that moves is a combination of X% of point A and Y% of point B. In each frame, the percent of point A decrease and B increases, so the point travels from A to B. By doing this in the latent space to get a new latent encoding and using the decoder, a new image can be generated as a blend of the 2 or more images.
<br><br>

This can be used to combine multiple images, as seen in the transition grid below.


<p align="center">
  <img width="512" height="512" src="https://github.com/Yasaswi124/AnimeVAE/blob/main/visualizations/transitiongrid.png">
</p>
<p align="center">
  <sub>Corners are images from dataset, remaining images are a blend of the first 4 images.</sub>
</p>


<br><br>

Data from [here](https://www.kaggle.com/soumikrakshit/anime-faces)

