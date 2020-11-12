import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import imageio

def linear_interpolation_frames(im1, im2, encoder, decoder, steps = 10):
    im1 = im1.reshape(1, 64, 64, 3)
    im2 = im2.reshape(1, 64, 64, 3)
    
    encoded1 = encoder.predict(im1)[2]
    encoded2 = encoder.predict(im2)[2]
    
    frames = []
    
    for i in range(steps+1):
        im = ((1 - (i/steps)) * encoded1) + ((i/steps) * encoded2)
        im = decoder.predict(im)
        im = im.reshape(64, 64, 3)
        frames.append(im)
        
        
    return frames

def linear_interpolation(im1, im2, encoder, decoder, steps = 10):
    
    im1 = im1.reshape(1, 64, 64, 3)
    im2 = im2.reshape(1, 64, 64, 3)
    
    encoded1 = encoder.predict(im1)[2]
    encoded2 = encoder.predict(im2)[2]
    
    display = np.zeros((64, 64*(steps+1), 3))
    
    for i in range(steps+1):
        im = ((1 - (i/steps)) * encoded1) + ((i/steps) * encoded2)
        im = decoder.predict(im)
        im = im.reshape(64, 64, 3)
        display[:,64*i:64*(i+1)] = im
        
        
    plt.imshow(display)
    plt.show()
    

def grid(tl, tr, bl, br, encoder, decoder, steps = 10, save=(False, None)):
    
    encoded1 = encoder.predict(tl.reshape(1, 64, 64, 3))[2]
    encoded2 = encoder.predict(tr.reshape(1, 64, 64, 3))[2]
    encoded3 = encoder.predict(bl.reshape(1, 64, 64, 3))[2]
    encoded4 = encoder.predict(br.reshape(1, 64, 64, 3))[2]
    
    grid = np.zeros((64*(steps+1), 64*(steps+1), 3))
    
    for row in range(steps+1):
        for column in range(steps+1):
            
            imp1 = (((1 - (column/steps)) * encoded1) + ((column/steps) * encoded2))
            imp2 = (((1 - (column/steps)) * encoded3) + ((column/steps) * encoded4))
            
            im = ((1 - (row/steps)) * imp1) + ((row/steps) * imp2)
            
            im = decoder.predict(im).reshape(64, 64, 3)
            
            
            grid[64*row:64*(row+1), 64*column:64*(column+1)] = im
            
            
    plt.imshow(grid)
    plt.show()

    
    
def save_gif(arr, name):
    
    arr = (arr * 255).round().astype(np.uint8)
    
    imageio.mimwrite(name, arr)
 
