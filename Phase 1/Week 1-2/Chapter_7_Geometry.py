import math
import pylab as pl
from matplotlib import collections as mc
import numpy as np
"The postmaster Problem"

# Define a point and a triangle
point = [0.2, 0.8]
triangle = [[0.2, 0.8], [0.5, 0.2], [0.8, 0.7]]

# Function to create a triangle from three points
def points_to_triangle(point1, point2, point3):
    triangle = [list(point1), list(point2), list(point3)]
    return triangle

# Function to generate lines from a list of points and an itinerary
def genlines(listpoints, itinerary):
    lines = []
    for j in range(len(itinerary) - 1):
        lines.append([listpoints[itinerary[j]], listpoints[itinerary[j + 1]]])
    return lines

# Function to plot a simple triangle
def plot_triangle_simple(triangle, thename):
    fig, ax = pl.subplots()
    xs = [triangle[0][0], triangle[1][0], triangle[2][0]]
    ys = [triangle[0][1], triangle[1][1], triangle[2][1]]
    itin = [0, 1, 2, 0]
    thelines = genlines(triangle, itin)
    lc = mc.LineCollection(genlines(triangle, itin), linewidths=2)
    ax.add_collection(lc)
    ax.margins(0.1)
    pl.scatter(xs, ys)
    pl.savefig(str(thename) + '.png')
    pl.close()

# Plot a simple triangle
plot_triangle_simple(points_to_triangle((0.2, 0.8), (0.5, 0.2), (0.8, 0.7)), 'tri')

# Function to calculate the distance between two points
def get_distance(point1, point2):
    distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    return distance

"Finding the Circumcenter"
# Function to find the circumcenter of a triangle
def triangle_to_circumcenter(triangle):
    x = complex(triangle[0][0], triangle[0][1])
    y = complex(triangle[1][0], triangle[1][1])
    z = complex(triangle[2][0], triangle[2][1])
    w = z - x
    w /= y - x
    c = (x - y) * (w - abs(w)**2) / (2j * w.imag) - x
    radius = abs(c + x)
    return (0 - c.real, 0 - c.imag), radius

"Imporved plotting capabilities"
# Improved plotting function to include circumcenters and circumcircles
def plot_triangle(triangles, centers, radii, thename):
    fig, ax = pl.subplots()
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    for i in range(len(triangles)):
        triangle = triangles[i]
        center = centers[i]
        radius = radii[i]
        itin = [0, 1, 2, 0]
        thelines = genlines(triangle, itin)
        xs = [triangle[0][0], triangle[1][0], triangle[2][0]]
        ys = [triangle[0][1], triangle[1][1], triangle[2][1]]
        lc = mc.LineCollection(genlines(triangle, itin), linewidths=2)
        ax.add_collection(lc)
        ax.margins(0.1)
        pl.scatter(xs, ys)
        pl.scatter(center[0], center[1])
        circle = pl.Circle(center, radius, color='b', fill=False)
        ax.add_artist(circle)
    pl.savefig(str(thename) + '.png')
    pl.close()

# Create and plot two triangles with their circumcenters and circumcircles
triangle1 = points_to_triangle((0.1, 0.1), (0.3, 0.6), (0.5, 0.2))
center1, radius1 = triangle_to_circumcenter(triangle1)
triangle2 = points_to_triangle((0.8, 0.1), (0.7, 0.5), (0.8, 0.9))
center2, radius2 = triangle_to_circumcenter(triangle2)
plot_triangle([triangle1, triangle2], [center1, center2], [radius1, radius2], 'two')

"Implementing Delaunay Triangulations"
# Implementing Delaunay Triangulations
delaunay = [points_to_triangle((0.2, 0.8), (0.5, 0.2), (0.8, 0.7))]
point_to_add = [0.5, 0.5]

# Find invalid triangles that need to be removed
invalid_triangles = []
delaunay_index = 0
while delaunay_index < len(delaunay):
    circumcenter, radius = triangle_to_circumcenter(delaunay[delaunay_index])
    new_distance = get_distance(circumcenter, point_to_add)
    if new_distance < radius:
        invalid_triangles.append(delaunay[delaunay_index])
    delaunay_index += 1

# Collect points from invalid triangles
points_in_invalid = []
for i in range(len(invalid_triangles)):
    delaunay.remove(invalid_triangles[i])
    for j in range(0, len(invalid_triangles[i])):
        points_in_invalid.append(invalid_triangles[i][j])

# Remove duplicate points
points_in_invalid = [list(x) for x in set(tuple(x) for x in points_in_invalid)]

# Create new triangles with the new point
for i in range(len(points_in_invalid)):
    for j in range(i + 1, len(points_in_invalid)):
        # count the number of times both of these are in the bad triangles
        count_occurrences = 0
        for k in range(len(invalid_triangles)):
            count_occurrences += 1 * (points_in_invalid[i] in invalid_triangles[k]) * (points_in_invalid[j] in invalid_triangles[k])
        if count_occurrences == 1:
            delaunay.append(points_to_triangle(points_in_invalid[i], points_in_invalid[j], point_to_add))
        
# Function to generate Delaunay triangulation for a set of points
def gen_delaunay(points):
    delaunay = [points_to_triangle([-5, -5], [-5, 10], [10, -5])]
    number_of_points = 0
    while number_of_points < len(points):
        point_to_add = points[number_of_points]
        delaunay_index = 0
        invalid_triangles = []
        while delaunay_index < len(delaunay):
            circumcenter, radius = triangle_to_circumcenter(delaunay[delaunay_index])
            new_distance = get_distance(circumcenter, point_to_add)
            if new_distance < radius:
                invalid_triangles.append(delaunay[delaunay_index])
            delaunay_index += 1
        points_in_invalid = []
        for i in range(len(invalid_triangles)):
            delaunay.remove(invalid_triangles[i])
            for j in range(len(invalid_triangles[i])):
                points_in_invalid.append(invalid_triangles[i][j])
        points_in_invalid = [list(x) for x in set(tuple(x) for x in points_in_invalid)]
        for i in range(len(points_in_invalid)):
            for j in range(i + 1, len(points_in_invalid)):
                # count the number of times both of these are in the bad triangles
                count_occurrences = 0
                for k in range(len(invalid_triangles)):
                    count_occurrences += 1 * (points_in_invalid[i] in invalid_triangles[k]) * (points_in_invalid[j] in invalid_triangles[k])
                if count_occurrences == 1:
                    delaunay.append(points_to_triangle(points_in_invalid[i], points_in_invalid[j], point_to_add))
        number_of_points += 1
    return delaunay

# Generate random points and create Delaunay triangulation
N = 15
np.random.seed(5201314)
xs = np.random.rand(N)
ys = np.random.rand(N)
points = zip(xs, ys)
listpoints = list(points)
the_delaunay = gen_delaunay(listpoints)

"From Delaunay to Voronoi"
# Function to convert Delaunay triangulation to Voronoi diagram
def delaunay_to_voronoi(triangles, centers):
    lines = []
    for i in range(len(triangles)):
        for j in range(len(triangles)):
            commonpoints = 0
            for k in range(len(triangles[i])):
                for n in range(len(triangles[j])):
                    if triangles[i][k] == triangles[j][n]:
                        commonpoints += 1
            if commonpoints == 2:
                lines.append([list(centers[i]), list(centers[j])])
    return lines

# Generate Voronoi diagram from Delaunay triangulation
centers = [triangle_to_circumcenter(triangle)[0] for triangle in the_delaunay]
voronoi_lines = delaunay_to_voronoi(the_delaunay, centers)

# Plot Voronoi diagram
fig, ax = pl.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
lc = mc.LineCollection(voronoi_lines, linewidths=2)
ax.add_collection(lc)
ax.margins(0.1)
pl.scatter(xs, ys)
pl.savefig('voronoi.png')
pl.close()