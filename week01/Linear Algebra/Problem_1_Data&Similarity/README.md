I choose 14 images for the input data
***Please open the folder Problem_1_Data&Similarity instead of week01 to run main.py because of probelems about the paths of images

Task 1: Embedding images
    // image_to_vector()
    - Use Image from PIL to receive the input images 
    - Then convert them to grayscale
    - Also need to resize them to (256, 256) because when we create 2-D array X (number of image, H.W), these input data should have the same H.W 
    - However, when we directly resize the input to fixed size 256*256, it will make the image looks disorted
    - We need to resize but still keep its scale, then paste this to the midle of the black background whose shape 256*256
    - reshape the array img to 1-D because initially these pictures are 2-D
    // Comment
    - There are 8 given images and the size of each image is resize to 256x256 
    - Therefore, the shape of X is (8, 256*256) = (8, 65536)
    - Each row of X is the 1-D array of the given images which are flattened
    - Each column of X is the position of each pixel of the images after flattening
    - In this case the first row is cr7_goat image
    - The column 255 contains the value of 8 pixels which were at coordinate (0,255) of the input images

Task 2: Broadcasting for each column
    - I use np.mean to create the array contain the mean of each column
    - axis=0 because the purpose is calculate each column and axis=0 means the average is computed along the vertical axis (dimension 0). In other words, we calculate the mean for each pixel position across all images
    - keepdims=True because column_mean should be in the same shape with X to use X - column_mean
    - In this case, mean for each column, axis=0 and when we do not pass the parameter keepdims=True it still good. Because numpy can automaticly broadcast the (65536,) to (1, 65536) and then (8, 65536) perfectly
    - However, when we need mean for each row, axis=1 and do not pass keepdims=True then the row_mean.shape is (14,) and then numpy can not broadcast it to (14, 1) and (14, 65536) to use X - row_mean

Task 3: Cosine Similarity
    - I just bonous the case Y.ndim == 1 (Y is the query image) then reshape it (1, -1) because the image in the dataset are also flattend
    - There also the case that the query image or some images in dataset are full black, therefore, theirs norm are 0 so i also change it to 1 to ignore divide by 0. The result will unchanged because thay are 0 initialy

Task 4: Retrieve the top-k most similar images to the query
    - Firstly computing the similarity matrix between the dataset and the query image
    - Reshape this matrix to 1-D for sorting
    - I use argsort because i need the idx after sort, [::-1] to take from the largest to the smallest and [:top_k] to take from the largest to top_k

Task 5: Analyst the similarity method
    - With top_k = 14 (full), it return the image 12th is the most similarity with the score 0.87113 and image 4 is the most different with the score 0.34852
    - It is easily explained that cosine method just compare by the value, feature and it does not depand on the shape, apearence. Because the image 12th has alot of white, bright zone like the query image, it has the highest point. And in image 4th this goat is black so it has the lowest point eventhough it has horn. However, the other images of goat like the 2th, 6th, 1st also have the high scores, 0.75881, 0.7069 and 0.67662 respectively



