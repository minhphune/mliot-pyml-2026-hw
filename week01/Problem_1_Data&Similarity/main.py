import numpy as np
import matplotlib as plt
from PIL import Image

SIZE = (256,256)
np.set_printoptions(precision=5)

# Task 1: Embedding images
def image_to_vector(path, size=(256,256)):
    img = Image.open(path).convert("L")
    img.thumbnail(size)
    
    background = Image.new("L", size, color=0)
    x = (size[0] - img.width) // 2
    y = (size[1] - img.height) // 2
    background.paste(img, (x,y))

    return np.array(background, dtype=float).reshape(-1)

cr7_goat = image_to_vector("cr7_goat_0.jpg")
print("cr7_goat.shape = ", cr7_goat.shape)

goat1 = image_to_vector("goat1_1.jpg")
print("goat1.shape = ", goat1.shape)

goat2 = image_to_vector("goat2_2.jpg")
print("goat2.shape = ", goat2.shape)

goat3 = image_to_vector("goat3_3.jpg")
print("goat3.shape = ", goat3.shape)

goat4 = image_to_vector("goat4_4.jpg")
print("goat4.shape = ", goat4.shape)

goat5 = image_to_vector("goat5_5.jpg")
print("goat5.shape = ", goat5.shape)

goat6 = image_to_vector("goat6_6.jpg")
print("goat6.shape = ", goat6.shape)

goat7 = image_to_vector("goat7_7.jpg")
print("goat7.shape = ", goat7.shape)

m10_goat = image_to_vector("m10_goat_8.jpg")
print("m10_goat.shape = ", m10_goat.shape)

sheep1 = image_to_vector("sheep1_9.jpg")
print("sheep1.shape = ", sheep1.shape)

sheep2 = image_to_vector("sheep2_10.jpg")
print("sheep2.shape = ", sheep2.shape)

sheep3 = image_to_vector("sheep3_11.jpg")
print("sheep3.shape = ", sheep3.shape)

sheep4 = image_to_vector("sheep4_12.jpg")
print("sheep4.shape = ", sheep4.shape)

sheep5 = image_to_vector("sheep5_13.jpg")
print("sheep5.shape = ", sheep5.shape)

X = np.array([cr7_goat, goat1, goat2, goat3, goat4, goat5, goat6, goat7, m10_goat, sheep1, sheep2, sheep3, sheep4, sheep5])
print("X.shape = ", X.shape)

# Task 2: Broadcasting for each column
column_mean = np.mean(X, axis=0, keepdims=True)
print("X.shape before broadcasting = ", X.shape)
print("column_mean.shape before broadcasting = ", column_mean.shape)
X_broadcast = X - column_mean
print("column_mean.shape after broadcasting = ", column_mean.shape)
print("X.shape after broadcasting = ", X_broadcast.shape)

# Task 3: Cosine Similarity
def cosine_similarity(X, Y=None):
    if Y is None:
        Y = X
    elif Y.ndim == 1:
        Y = Y.reshape(1,-1)
    
    # norm for each vector (each image) in X, Y
    X_norm = np.linalg.norm(X, axis=1, keepdims=True)
    Y_norm = np.linalg.norm(Y, axis=1, keepdims=True)
    # ignore divide by 0 
    X_norm[X_norm == 0] = 1
    Y_norm[Y_norm == 0] = 1

    Xn = X / X_norm
    Yn = Y / Y_norm
    return Xn @ Yn.T  # if Y == X then this is the similarity matrix for each vector in X

# Task 4: Retrieve the top-k most similar images to the query
def search(query, top_k=3):
    similarity_matrix = cosine_similarity(X, query)
    print(similarity_matrix)
    scores = similarity_matrix.reshape(-1)
    top_k_similar = np.argsort(scores)[::-1][:top_k]
    
    res = np.array([[idx, scores[idx]] for idx in top_k_similar])
    
    return res

query = image_to_vector("query.jpg")
top_k_similar = search(query, 14)
print(top_k_similar)
print("top_k_similar.shape = ", top_k_similar.shape)



    

