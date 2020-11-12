# Implemntating a Variational Autoencoder in keras on images.

Variational Autoencoders differ from regular autoencoders in the fact that they have a continous latent space, allowing linear interpolation to genearte realistic looking images by combining multiple images. The animation below cycles through different images. Every tenth frame in the animation is a reconstruted image from the dataset, with the rest of the frames generated from linear interpolation of the encoding of 2 images, generating an image not in the dataset.
<br><br>
<p align="center">
  <img width="256" height="256" src="https://github.com/Yasaswi124/AnimeVAE/blob/main/visualizations/faces_loop.gif">
</p>
<p align="center">
  <sub> GIF of images reconstructed from latent space interpolation</sub>
</p>
<br>

The frames for this images were created using latent interpolation, an example can be seen in the animtion below.


<p align="center">
  <img width="256" height="256" src="https://github.com/Yasaswi124/AnimeVAE/blob/main/visualizations/linear_interpolation.gif">
</p>
<p align="center">
  <sub>Linear Interpolation in 2D space</sub>
</p>

In the animation above, the point that moves is a combination of x% of point A and y% of point B. In each frame, the percent of point A decrease and B increases, so the point travels from A to B. By doing this in the latent space to get a new latent encoding and using the decoder, a new image can be generated as a blend of the 2 or more images.
