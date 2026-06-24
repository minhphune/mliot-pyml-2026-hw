import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Task 1: Linear Transformation
# Rotation Transformation
theta = np.radians(135)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
# Scaling Transformation
S = np.array([[0.5, 0],
             [0, 0.5]])

square = np.array([[0, 1, 1, 0, 0],
                   [0, 0, 1, 1, 0]])
square_R = R @ square
square_R_S = S @ square_R

plt.plot(square[0], square[1], color='r', label="raw square")
plt.plot(square_R[0], square_R[1], color='g', label='rotating square')
plt.plot(square_R_S[0], square_R_S[1], color='y', label = 'scaling and roatating square')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.ion()
plt.show()

# Task 2: SVD
M = np.array(Image.open("person.png").convert("L"), dtype=float)
Mc = M - M.mean(axis=0)
# print(Mc.shape)
U, S, Vt = np.linalg.svd(Mc, full_matrices=False)
# print(U.shape, S.shape, Vt.shape)
def reconstruct(k):
    return (U[:, :k] * S[:k]) @ Vt[:k, :]

compress_ratio = []
reconstruct_error = []

h, w = M.shape
max_k = min(h, w)
k_values = np.unique(
    np.geomspace(1, max_k, 100).astype(int)
)

for k in k_values:
    M_reconstruct = reconstruct(k)
    M_reconstruct = M_reconstruct + M.mean(axis=0)
    cr = (h*w)/(h*k + k + k*w) * 100
    error = (np.linalg.norm(M - M_reconstruct, 'fro'))/np.linalg.norm(M, 'fro') * 100
    compress_ratio.append(cr)
    reconstruct_error.append(error)

plt.figure(figsize=(8, 5))
plt.plot(k_values, compress_ratio, label="Compress ratio", linewidth=1)
plt.plot(k_values, reconstruct_error, label="Error", linewidth=1)
plt.title(f"SVD Compression Performance")
plt.xlabel("k")
plt.ylabel("Percentage (%)")
plt.legend()
plt.ion()
plt.show()

print("Type 'stop' to stop the program")
print("Choose the suitable k: (int/stop)")
k = input()
while k != "stop":
    try:
        k = int(k)
        M_reconstruct = reconstruct(k)
        M_reconstruct = M_reconstruct + M.mean(axis=0)
        
        cr = (h*w)/(h*k + k + k*w) * 100
        error = (np.linalg.norm(M - M_reconstruct, 'fro'))/np.linalg.norm(M, 'fro') * 100
        print(f"Compress Ratio: {round(cr, 3)}% ---- Error: {round(error, 3)}%")

        M_reconstruct = np.clip(M_reconstruct, 0, 255).astype(np.uint8)
        reconstruct_image = Image.fromarray(M_reconstruct, mode='L')
        reconstruct_image.save("person_reconstruct.png")

    except ValueError:
        print("Invalid input. Please enter a decimal number or 'good'.")
    
    print("Type 'stop' to stop the program")
    print("Choose the suitable k: (int/stop)")
    k = input()

print("Please check your reconstructed image")