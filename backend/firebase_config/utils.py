import numpy as np

def compare_face_encodings(target_encoding, reference_encodings, threshold=0.6):
    similarities = np.dot(reference_encodings, target_encoding.T)
    best_match_index = np.argmax(similarities)
    max_similarity = similarities[best_match_index]
    if max_similarity >= threshold:
        return best_match_index
    else:
        return None

# Example usage:
target_encoding = np.array([[269, 294, 271, 310, 273, 326, 276, 342, 281, 357, 290, 370, 302, 381, 318, 387, 335, 390, 352, 388, 367, 381, 379, 370, 386, 357, 391, 342, 394, 326, 395, 309, 396, 293, 279, 279, 287, 269, 299, 265, 312, 265, 324, 270, 340, 268, 353, 264, 366, 263, 378, 267, 386, 277, 334, 279, 334, 288, 335, 297, 335, 307, 324, 319, 330, 320, 335, 321, 341, 320, 346, 319, 295, 287, 302, 283, 309, 283, 317, 285, 310, 287, 302, 288, 348, 285, 356, 282, 364, 282, 370, 286, 364, 287, 356, 287, 310, 344, 320, 337, 329, 333, 335, 334, 342, 333, 350, 337, 359, 343, 350, 347, 342, 350, 335, 351, 328, 350, 320, 348, 314, 344, 329, 341, 335, 341, 342, 341, 355, 343, 342, 340, 335, 341, 329, 341]])
reference_encodings = np.array([[256, 279, 258, 306, 261, 332, 264, 358, 271, 385, 282, 410, 298, 433, 318, 450, 341, 457, 363, 453, 383, 438, 399, 416, 411, 393, 420, 368, 426, 343, 431, 317, 435, 290, 270, 281, 281, 269, 298, 266, 316, 270, 332, 277, 359, 277, 377, 272, 395, 270, 412, 274, 422, 286, 346, 292, 346, 308, 346, 325, 346, 342, 328, 354, 336, 357, 344, 359, 353, 357, 360, 355, 290, 293, 301, 291, 312, 290, 323, 295, 312, 297, 300, 297, 367, 298, 378, 294, 389, 296, 399, 299, 389, 303, 378, 302, 310, 389, 324, 387, 336, 383, 342, 386, 350, 384, 361, 388, 373, 391, 361, 401, 350, 407, 342, 408, 334, 407, 323, 401, 316, 390, 335, 394, 342, 395, 350, 394, 368, 392, 350, 394, 342, 396, 335, 394]])
match_index = compare_face_encodings(target_encoding, reference_encodings)
if match_index is not None:
    print(f"Match found with reference face at index {match_index}.")
    # Identify the person associated with the matched reference face
else:
    print("No match found.")
