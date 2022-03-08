import numpy as np
import os
import subprocess
# import matlab.engine
import shutil
# import stl
import scipy.io as sio
from scipy.io import loadmat
from scipy.spatial import distance
# from pymatreader import read_mat
# import re
# import vtk
# import trimesh

class SeegClass:
    def __init__(self, scirun_bin, scirun_net_dir, subject_id, subject_dir):
        self.scirun_bin = scirun_bin
        self.scirun_net_dir = scirun_net_dir
        self.subject_id = subject_id
        self.subject_dir = subject_dir
        self.simnibs_dir = os.path.normpath(os.path.join(subject_dir, 'Imaging', 'm2m_' + subject_id))

