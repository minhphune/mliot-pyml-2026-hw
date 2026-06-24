My choice is image
***Please open the folder Problem_2_Linear&SVD instead of week01 to run main.py because of probelems about the paths of images

When you the main.py, Figure1 is the result for task 1 and Figgure2 is the result for Task 2 and 3
After looking at the Figure2 (SVD Performance), you can type the input for k, then can see the reconstructed image. It is possible to try with other value of k again until you type "stop". Let see how the reconstructed image change with different value of k. When k incrase the reconstructed image look better. 

Analyst the most suitable value of k
    - Depending on our purpose of the image compression
    - In my program, we firstly draw the graph present for the performance of SVD method. Then we can base on this graph to try different values of k. I think the error should less than 10%. With this threshold, the visual difference is hardly noticeable to the human eye. In case this image (person.png), when k = 56 the compress ratio is approximately 6:1 (594.798%) and error is just 7.937% and the person_reconstruct looks still good.
    - The graph illustrates that when k increases, both compress ratio and error decrease.

Conection to Dimensionality Reduction and Compression in AI
    - When the input data has a lo of features (curse of dimensionality), the model spend a lot of memory and time to compute and it is easily overfiting
    - The target when we train the AI model is make it good at generalizing. The model does not need to learn every small variation in the data, as many of them may simply represent noise. Therefor, using SVD method to denoise the data, ignore irrelevant information before train the AI model is nessesary. Moreover, it also help to save memory and time.