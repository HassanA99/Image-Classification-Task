#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Hassan Wurie Jalloh
# DATE CREATED: Monday, July 5, 2024                              
# REVISED DATE: Monday, July 24, 2024 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function

    # Get list of files in the directory
    filename_list = listdir(image_dir)
    
    # Initialize an empty dictionary
    results_dic = dict()
    
    # Process each filename to create the pet label
    for filename in filename_list:
        # Skip files that start with '.' (like .DS_Store on Mac)
        if filename.startswith('.'):
            continue
        
        # Convert filename to lower case and split by '_'
        pet_label_list = filename.lower().split('_')
        
        # Create pet label by joining only the words (ignoring numbers)
        pet_label = ""
        for word in pet_label_list:
            if word.isalpha():
                pet_label += word + " "
        
        # Strip any leading or trailing whitespace characters
        pet_label = pet_label.strip()
        
        # Add to the dictionary, checking if the filename is not already in the dictionary
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print("** Warning: Key=", filename, 
                  "already exists in results_dic with value =", 
                  results_dic[filename])
    
    # Return the dictionary
    return results_dic