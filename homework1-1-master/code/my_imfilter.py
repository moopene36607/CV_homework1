import numpy as np
#for testing
#import scipy.ndimage as ndimage

#done
def my_imfilter(image, imfilter):
    
    imfilter = np.asarray(imfilter, dtype=np.float64)
    frow_num = len(imfilter)
    fcol_num = len(imfilter[0])
    pad_x = int((fcol_num - 1 ) / 2)
    pad_y = int((frow_num - 1 ) / 2)
    #reflect padding
    image_pad = np.pad(image, ((pad_x, pad_x), (pad_y, pad_y), (0, 0)), 'reflect')
    
    irow_num = len(image)       
    icol_num = len(image[0])     
    channel  = len(image[0][0])
    #create a same size array to save output
    output = np.zeros_like(image)
    for ro in range(0,irow_num):
        for co in range(0,icol_num):
            for ch in range(0,channel):
                #faster method
                output[ro][co][ch] = np.sum(imfilter * image_pad[ro:ro+frow_num, co:co+fcol_num, ch])
                #slower method (brutal)
                '''
                temp = 0
                for f_ro in range(0, frow_num):
                    for f_co in range(0, fcol_num,):
                        temp = temp + imfilter[f_ro][f_co] *image_pad[ro+f_ro][co+f_co][ch] 
                        #print(image_pad[ro+f_ro][co+f_co][ch])
                output[ro][co][ch] = temp      
                '''
    '''
    #for testing
    output = np.zeros_like(image)
    for ch in range(image.shape[2]):
         output[:,:,ch] = ndimage.filters.correlate(image[:,:,ch], imfilter, mode='constant')
         #a = ndimage.filters.correlate(123,123,mode = 'peak')
    '''
    '''
    Input:
        image: A 3d array represent the input image.
        imfilter: The gaussian filter.
    Output:
        output: The filtered image.
    '''
    ###################################################################################
    # TODO:                                                                           #
    # This function is intended to behave like the scipy.ndimage.filters.correlate    #
    # (2-D correlation is related to 2-D convolution by a 180 degree rotation         #
    # of the filter matrix.)                                                          #
    # Your function should work for color images. Simply filter each color            #
    # channel independently.                                                          #
    # Your function should work for filters of any width and height                   #
    # combination, as long as the width and height are odd (e.g. 1, 7, 9). This       #
    # restriction makes it unambigious which pixel in the filter is the center        #
    # pixel.                                                                          #
    
    # Boundary handling can be tricky. The filter can't be centered on pixels         #
    # at the image boundary without parts of the filter being out of bounds. You      #
    # should simply recreate the default behavior of scipy.signal.convolve2d --       #
    # pad the input image with zeros, and return a filtered image which matches the   #
    # input resolution. A better approach is to mirror the image content over the     #
    # boundaries for padding.                                                         #
    
    # Uncomment if you want to simply call scipy.ndimage.filters.correlate so you can # 
    # see the desired behavior.                                                       #
    # When you write your actual solution, you can't use the convolution functions    #
    # from numpy scipy ... etc. (e.g. numpy.convolve, scipy.signal)                   #
    # Simply loop over all the pixels and do the actual computation.                  #
    # It might be slow.                                                               #
    ###################################################################################
    
    ###################################################################################
    # NOTE:                                                                           #
    # Some useful functions                                                           #
    #     numpy.pad or numpy.lib.pad                                                  #
    # #################################################################################
    
    # Uncomment if you want to simply call scipy.ndimage.filters.correlate so you can 
    # see the desired behavior.

    ###################################################################################
    #                                 END OF YOUR CODE                                #
    ###################################################################################
    return output

