import numpy as np


def create_oriented_bounding_box(vertices):
    # Step 1: Compute the centroid
    centroid = np.mean(vertices, axis=0)

    # Step 2: Compute the covariance matrix
    centered_vertices = vertices - centroid
    covariance_matrix = np.cov(centered_vertices, rowvar=False)

    # Step 3: Eigen decomposition
    eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)

    # Step 4: Rotate the vertices
    aligned_vertices = np.dot(centered_vertices, eigen_vectors)

    # Step 5: Find the minimum and maximum extents
    min_extents = np.min(aligned_vertices, axis=0)
    max_extents = np.max(aligned_vertices, axis=0)

    # Constructing the OBB corners from the extents
    # Note: This assumes the OBB is aligned with the principal axes
    obb_corners = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                corner = np.array([min_extents[0] if i == 0 else max_extents[0],
                                   min_extents[1] if j == 0 else max_extents[1],
                                   min_extents[2] if k == 0 else max_extents[2]])
                # Rotate the corner back to the original orientation
                obb_corner = np.dot(corner, eigen_vectors.T) + centroid
                obb_corners.append(obb_corner)

    return np.array(obb_corners)


def create_oriented_bounding_box_openfoam_order(vertices):
    obb_corners = create_oriented_bounding_box(vertices).round(6)

    # Sorting the corners to approximate OpenFOAM's ordering
    # First, sort by z (bottom to top), then by y (lower to upper), then by x (front to back)
    # Rearrange the sorted corners to follow the OpenFOAM order

    return obb_corners[[0, 4, 6, 2, 1, 5, 7, 3]]


def check_points_inside_obb(points, obb_corners):
    """
    Check if all given points are inside the Oriented Bounding Box (OBB).

    :param points: A NumPy array of points to be tested, shape (N, 3).
    :param obb_corners: A NumPy array of the 8 corners of the OBB, shape (8, 3).
    :return: True if all points are inside the OBB, False otherwise.
    """
    # Compute the OBB's centroid
    obb_centroid = np.mean(obb_corners, axis=0)

    # Compute the covariance matrix of the OBB corners and perform Eigen decomposition
    centered_corners = obb_corners - obb_centroid
    covariance_matrix = np.cov(centered_corners, rowvar=False)
    _, eigen_vectors = np.linalg.eig(covariance_matrix)

    # Transform points to the OBB's coordinate system
    centered_points = points - obb_centroid
    aligned_points = np.dot(centered_points, eigen_vectors)

    # Get the OBB extents in its local coordinate system
    aligned_corners = np.dot(centered_corners, eigen_vectors)
    min_extents = np.min(aligned_corners, axis=0)
    max_extents = np.max(aligned_corners, axis=0)

    # Check if all points are within the OBB extents
    inside = np.all((aligned_points >= min_extents) & (aligned_points <= max_extents), axis=1)

    return np.all(inside)


# Example usage
if __name__ == '__main__':
    # Generate some random points for demonstration
    test_vertices = np.random.rand(10, 3) * 10
    test_obb_corners = create_oriented_bounding_box(test_vertices)
    print(check_points_inside_obb(test_vertices, test_obb_corners))
