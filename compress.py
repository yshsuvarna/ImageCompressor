# !/usr/bin/env python3

import os
import sys
from PIL import Image
import numpy as np

def open_image(path):                                                 #Open image and get the values for RGB for each pixel                                           
    image=Image.open(path)    
    
    return np.asarray(image)/255

def K_random_centroid(A , K):                                         #Randomly choose K points in the image array
    m=len(A)                                                   
    return A[np.random.choice(m,K,replace=False),:]

def closest_centroid(A,centroids):                                    #Find the centroid closest to any given image point by calculating the norm of RGB
    m=len(A)
    c=np.zeros(m)                            
    for i in range(m):
        distances = np.linalg.norm(A[i] - centroids, axis=1)
        c[i] = np.argmin(distances)            
    return c


def compute_means(A, idx, K):                                         #For any centroid find the mean of RGB values of the points for which it is the closest centroid
    _, n = A.shape
    centroids = np.zeros((K, n))
    for k in range(K):
        examples = A[np.where(idx == k)]
        mean = [np.mean(column) for column in examples.T]
        centroids[k] = mean
    return centroids

def find_K(A,K,max_iters=10):                                         #Tune the centroid to get the best set of K points that are best suited for the image
    centroids=K_random_centroid(A,K)
    prev_centroids=centroids
    for j in range(max_iters):
        idx=closest_centroid(A,centroids)               
        centroids = compute_means(A, idx, K)       
        if ( prev_centroids==centroids).all():
            return centroids                            
        else:
            prev_centroids=centroids
    return centroids,idx
        
    
def main():
    try:
       image_path = sys.argv[1]
       assert os.path.isfile('path.webp')
    except (IndexError, AssertionError):
        print('Please specify an image')
    image=open_image('imae.jpg')                                      
        
    w,h,d=image.shape                                  
        
    A=image.reshape((w*h,d))                          
        
    K=25#int(input("Enter the scale value : "))
    print("Procedure begins ....")
    colors,_=find_K(A,K,max_iters=10)                 
    ch=-255#int(input("Enter the output type"))
    idx=closest_centroid(A ,colors)      
    #Reconstruct the image           
    idx = np.array(idx, dtype=np.uint8)
    A_reconstructed = np.array(colors[idx, :] * ch, dtype=np.uint8).reshape((w,h,d))
    #Save the output file 
    compressed_image = Image.fromarray(A_reconstructed)
    compressed_image.save('out1.jpeg')
               
if __name__ == '__main__':
    main()
