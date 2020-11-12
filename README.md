# Implemntating a Variational Autoencoder in keras on images.

Variational Autoencoders differ from regular autoencoders in the fact that they have a continous latent space, allowing linear interpolation to genearte realistic looking images by combining multiple images. The animation below cycles through different images. Every tenth frame in the animation is a reconstruted image from the dataset, with the rest of the frames generated from linear interpolation of the encoding of 2 images, generating an image not in the dataset.
<br><br><br><br>
<p align="center">
  <img width="256" height="256" src="https://github.com/Yasaswi124/AnimeVAE/blob/main/visualizations/faces_loop.gif">
</p>
<p align="center">
  <sub> GIF of images reconstructed from latent space interpolation</sub>
</p>
<br><br>

The frames for this images were created using latent interpolation, an example can be seen in the animtion below.
