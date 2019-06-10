#!/usr/bin/python3

import numpy as np
import open3d as o3d

pcd = o3d.io.read_point_cloud("./data/fragment.ply")
downpcd = pcd.voxel_down_sample(voxel_size=0.05)
o3d.visualization.draw_geometries([downpcd])