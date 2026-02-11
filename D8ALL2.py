import numpy as np
scores = np.random.randint(50, 101, size=(5, 3))
subject_means = scores.mean(axis=0)
centered_scores = scores - subject_means
print("Original Scores:\n", scores)
print("\nSubject Means:\n", subject_means)
print("\nCentered Scores:\n", centered_scores)

import numpy as np
readings = np.arange(24)
reshaped = readings.reshape(4, 3, 2)
transposed = reshaped.transpose(0, 2, 1)
print("Final Shape:", transposed.shape)
print("Final Array:\n", transposed)