#!/usr/bin/env python3

import os
import sys
from PTL import Image
import numpy as np

def open_image(path):                                                            #Function to open the image 
    image=Image.open(path)    
    #Return image in the form of an array of tuples with each element containing the RGB value for each pixel
    return np.asarray(image)/255

def K_random_centroid( A , K):
    m=len(A)
                                              #Randomly pick K different elements of the linear array and return their indices
    return A[np.random.choice(m,K,replace=False),:]
   
def closest_centroid(A,centroids):
    m=len(A)
    c=np.zeros(m)                                            #defines an array of size m and initialize it to zero
    for i in range(m):
        distance=np.linalg.norm(A[i]-centroids,axis=1)
                                                               '''Here we take RGB as the three main axis and calculate the
                                                                   norm of the colour of a point and the centroids'''
        c[i]=np.argmin(distances)                          #We take the index of the centroid which is closest to a given point
    return c

def mean_centroids(A,index,K):                                    #Function to find the finer adjustment for each centroid 
    a,s=A.shape
    centroids=np.zero((K,s))                        
    for i in range(K):
        temp=A[np.where(index==k)]                                  
        mean=[np.mean(column) for column in temp.T]         #Mean of RGB values of points coresseponding to each point which has the centroid as it's closest
        centroids[k]=mean
    return centroids

def find_K(A,K,max_iters):
    m=len(a)
    centroids=K_random_centroid
    prev_centroids=centroids
    for _ in range(max_iters=20):
        index=closest_centroid(A,centroids)               #The index of the centroid closest to every point in the image
        centroids=mean_centroid(A,index,K)                #Update the centroids to a more closer value
        if (centroids==prev_centroids).all():
            return centroids                              #No better value exist
        else:
            prev_centroids=centroids
    return centroids,index
        
    
    def main():
                                                           #Load the image and get it's RGB values in an array
        image=open_image('''path''')
        
        w,h,d=image.shape                                  #Get the image dimensions the width height and the depth
        
        A=image.reshape((w*h,d))                          #reshape the image array obtained from the image into a linear array 
        
        K=int(input("Enter the number of different colours : "))      # The number of colors in the output image
        
        colors,_=find_K(A,K,max_iters=20)                 #Best centroid values
        
        index=closest_centroid(A ,colors)                 #Index of centroid closest to a point in the image
        ch=int(input("Enter the shade value : ")
        #Reconstruct the image
        index=np.array(index,dtype=np.uint8)
        A_reconstructed=np.array(colors[index,:]*ch,dtype=np.uint8).reshape((w,h,d))
               compressed_image=Image.fromarray(A_reconstructed)
               
               compressed_image.save('out.png')
               
if __name__=='__main__':
          main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
