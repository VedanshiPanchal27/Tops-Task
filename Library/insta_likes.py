# 2 Create a NumPy array called followers using np.array() that stores the follower counts for 5 Instagram influencers: [1200, 15000, 67000, 340000, 1250000]. Print the array, its shape, number of dimensions, and data type.
import numpy as np
followers = np.array([1200, 15000, 67000, 340000, 1250000])

print("Followers array:", followers)
print("Shape:", followers.shape)
print("Number of dimensions:", followers.ndim)
print("Data type:", followers.dtype)

# 3.Use np.arange() to generate an array of order IDs for 10 consecutive Zomato orders starting from 101. Print the array and its size.
import numpy as np
order_ids = np.arange(101, 111)

print("\nZomato Order IDs:", order_ids)
print("Size:", order_ids.size)

# 4.Create a 3x3 NumPy array using np.eye() to represent a 'like' identity matrix for a new Spotify playlist feature. Print the matrix and explain what the diagonal values represent in a comment.
like_matrix = np.eye(3)

# The diagonal values are 1, representing that each
# playlist/user is matched with itself.
print("\nSpotify Like Identity Matrix:")
print(like_matrix)

# 5.Convert a Python list of cricket scores [45, 67, 120, 89, 54] to a NumPy array, then use the .itemsize attribute to print how many bytes each score takes in memory.<br><br><em><strong>Hint:</strong> Use np.array() for conversion and .itemsize for memory size.</em>
cricket_scores = [45, 67, 120, 89, 54]
cricket_array = np.array(cricket_scores)
print("\nCricket Scores Array:", cricket_array)
print("Bytes per score:", cricket_array.itemsize)