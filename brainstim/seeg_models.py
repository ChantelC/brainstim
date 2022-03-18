import numpy as np
import os
import subprocess
# import matlab.engine
import shutil
import stl
import scipy.io as sio
from scipy.io import loadmat
from scipy.spatial import distance
# from pymatreader import read_mat
# import re
# import vtk
# import trimesh

class SeegClass:
    def __init__(self, subject_dict):
        subject_dict["simnibs_dir"] = os.path.normpath(os.path.join(subject_dict["subject_dir"],
                                                                    'Imaging',
                                                                    'm2m_' + subject_dict["subject"]
                                                                    ))
        self.subject_dict = subject_dict


    def visualize_leads(self):
        """
        Visualize SEEG leads from MATLAB lead generation output.
        Save csf_geostim as ascii stl
        Save contacts.fld and contacts.stl for head meshing and visualization in 3DSlicer.
        """

        # save csf_geostim.stl as ascii stl
        self.subject_dict["csf_geostim"] = os.path.join(self.subject_dict["simnibs_dir"], "csf_geostim.stl")
        self.stl2ascii(self.subject_dict["csf_geostim"], self.subject_dict["csf_geostim"])

        # setup environment variables for scirun network
        os.environ["CSF_GEOSTIM"] = os.path.normpath(self.subject_dict["csf_geostim"])

        os.environ["LEAD_GEO"] = os.path.normpath(os.path.join(self.subject_dict["subject_dir"],
                                                               'Imaging',
                                                               'Registered',
                                                               'Electrodes',
                                                               'GeoStim',
                                                               'Repositioned',
                                                               'cont_pos_N_S_C.stl'
                                                               ))
        os.environ["LEAD_DATA"] = os.path.normpath(os.path.join(self.subject_dict["subject_dir"],
                                                                'Imaging',
                                                                'Registered',
                                                                'Electrodes',
                                                                'GeoStim',
                                                                'Repositioned',
                                                                'cont_id_N_S_C.mat'))

        cmd = (self.subject_dict["scirun_bin"] + " -0 -e " +
               os.path.normpath(os.path.join(self.subject_dict["scirun_net_dir"], '00_visualize_leads.srn5')))
        print(cmd)
        subprocess.call(cmd, shell=True)

        return


    def stl2ascii(self, in_file, out_file):
        """
        Saves stl file to ascii stl to match SIMNIBS output
        :param self:
        :param in_file: filepath to ascii or binary stl
        :param out_file: filepath to saved ascii stl
        :return:
        """

        print(f"Saving {in_file} as ascii stl {out_file}...")
        root_ext = os.path.splitext(in_file)
        shutil.copy(in_file, root_ext[0] + '_tmp' + root_ext[1])
        mesh = stl.mesh.Mesh.from_file(in_file)
        try:
            mesh.save(out_file, mode=stl.Mode.ASCII)
            os.remove(root_ext[0] + '_tmp' + root_ext[1])
        except Exception as e:
            print(e)

        return



