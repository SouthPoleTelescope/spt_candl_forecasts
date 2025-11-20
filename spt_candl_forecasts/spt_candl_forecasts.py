"""
Short cuts to ``.yaml`` files for released mock data sets.

"""

# Grab Data Path
import os

data_path = os.path.dirname(os.path.realpath(__file__))

# --------------------------------------#
# DATA SETS
# --------------------------------------#

# SPT-3G Main TnE
SPT3G_Main_TnE_folder = "SPT3G_Main_TnE_v0"
SPT3G_Main_TnE = f"{data_path}/{SPT3G_Main_TnE_folder}/SPT3G_Main_TnE.yaml"

# SPT-3G Summer TnE
SPT3G_Summer_a_TnE_folder = "SPT3G_Summer_a_TnE_v0"
SPT3G_Summer_a_TnE = f"{data_path}/{SPT3G_Summer_a_TnE_folder}/SPT3G_Summer_a_TnE.yaml"
SPT3G_Summer_b_TnE_folder = "SPT3G_Summer_b_TnE_v0"
SPT3G_Summer_b_TnE = f"{data_path}/{SPT3G_Summer_b_TnE_folder}/SPT3G_Summer_b_TnE.yaml"
SPT3G_Summer_c_TnE_folder = "SPT3G_Summer_c_TnE_v0"
SPT3G_Summer_c_TnE = f"{data_path}/{SPT3G_Summer_c_TnE_folder}/SPT3G_Summer_c_TnE.yaml"

# SPT-3G Wide TnE
SPT3G_Wide_a_TnE_folder = "SPT3G_Wide_a_TnE_v0"
SPT3G_Wide_a_TnE = f"{data_path}/{SPT3G_Wide_a_TnE_folder}/SPT3G_Wide_a_TnE.yaml"
SPT3G_Wide_b_TnE_folder = "SPT3G_Wide_b_TnE_v0"
SPT3G_Wide_b_TnE = f"{data_path}/{SPT3G_Wide_b_TnE_folder}/SPT3G_Wide_b_TnE.yaml"
SPT3G_Wide_c_TnE_folder = "SPT3G_Wide_c_TnE_v0"
SPT3G_Wide_c_TnE = f"{data_path}/{SPT3G_Wide_c_TnE_folder}/SPT3G_Wide_c_TnE.yaml"
SPT3G_Wide_d_TnE_folder = "SPT3G_Wide_d_TnE_v0"
SPT3G_Wide_d_TnE = f"{data_path}/{SPT3G_Wide_d_TnE_folder}/SPT3G_Wide_d_TnE.yaml"
SPT3G_Wide_e_TnE_folder = "SPT3G_Wide_e_TnE_v0"
SPT3G_Wide_e_TnE = f"{data_path}/{SPT3G_Wide_e_TnE_folder}/SPT3G_Wide_e_TnE.yaml"
SPT3G_Wide_f_TnE_folder = "SPT3G_Wide_f_TnE_v0"
SPT3G_Wide_f_TnE = f"{data_path}/{SPT3G_Wide_f_TnE_folder}/SPT3G_Wide_f_TnE.yaml"
SPT3G_Wide_g_TnE_folder = "SPT3G_Wide_g_TnE_v0"
SPT3G_Wide_g_TnE = f"{data_path}/{SPT3G_Wide_g_TnE_folder}/SPT3G_Wide_g_TnE.yaml"
SPT3G_Wide_h_TnE_folder = "SPT3G_Wide_h_TnE_v0"
SPT3G_Wide_h_TnE = f"{data_path}/{SPT3G_Wide_h_TnE_folder}/SPT3G_Wide_h_TnE.yaml"
SPT3G_Wide_i_TnE_folder = "SPT3G_Wide_i_TnE_v0"
SPT3G_Wide_i_TnE = f"{data_path}/{SPT3G_Wide_i_TnE_folder}/SPT3G_Wide_i_TnE.yaml"

# SPT-3G Main PP
SPT3G_Main_PP_folder = "SPT3G_Main_PP_v0"
SPT3G_Main_PP = f"{data_path}/{SPT3G_Main_PP_folder}/SPT3G_Main_PP.yaml"

# SPT-3G Summer PP
SPT3G_Summer_a_PP_folder = "SPT3G_Summer_a_PP_v0"
SPT3G_Summer_a_PP = f"{data_path}/{SPT3G_Summer_a_PP_folder}/SPT3G_Summer_a_PP.yaml"
SPT3G_Summer_b_PP_folder = "SPT3G_Summer_b_PP_v0"
SPT3G_Summer_b_PP = f"{data_path}/{SPT3G_Summer_b_PP_folder}/SPT3G_Summer_b_PP.yaml"
SPT3G_Summer_c_PP_folder = "SPT3G_Summer_c_PP_v0"
SPT3G_Summer_c_PP = f"{data_path}/{SPT3G_Summer_c_PP_folder}/SPT3G_Summer_c_PP.yaml"

# SPT-3G Wide PP
SPT3G_Wide_PP_folder = "SPT3G_Wide_PP_v0"
SPT3G_Wide_PP = f"{data_path}/{SPT3G_Wide_PP_folder}/SPT3G_Wide_PP.yaml"

# --------------------------------------#
# PREPARE SHORCUTS
# --------------------------------------#


# Define Shortcuts
shortcuts = {
    "SPT-3G Main TnE": "SPT3G_Main_TnE",
    "SPT-3G Summer a TnE": "SPT3G_Summer_a_TnE",
    "SPT-3G Summer b TnE": "SPT3G_Summer_b_TnE",
    "SPT-3G Summer c TnE": "SPT3G_Summer_c_TnE",
    "SPT-3G Wide a TnE": "SPT3G_Wide_a_TnE",
    "SPT-3G Wide b TnE": "SPT3G_Wide_b_TnE",
    "SPT-3G Wide c TnE": "SPT3G_Wide_c_TnE",
    "SPT-3G Wide d TnE": "SPT3G_Wide_d_TnE",
    "SPT-3G Wide e TnE": "SPT3G_Wide_e_TnE",
    "SPT-3G Wide f TnE": "SPT3G_Wide_f_TnE",
    "SPT-3G Wide g TnE": "SPT3G_Wide_g_TnE",
    "SPT-3G Wide h TnE": "SPT3G_Wide_h_TnE",
    "SPT-3G Wide i TnE": "SPT3G_Wide_i_TnE",
    "SPT-3G Main PP": "SPT3G_Main_PP",
    "SPT-3G Summer a PP": "SPT3G_Summer_a_PP",
    "SPT-3G Summer b PP": "SPT3G_Summer_b_PP",
    "SPT-3G Summer c PP": "SPT3G_Summer_c_PP",
    "SPT-3G Wide PP": "SPT3G_Wide_PP"
}

# --------------------------------------#
# PRINT SHORTCUTS
# --------------------------------------#


def print_all_shortcuts():
    """
    Prints all available shortcuts to mock data sets.
    """
    for ky in list(shortcuts.keys()):
        print(f"{ky}: 'spt_candl_data.{shortcuts[ky]}'\n(data files located at: {globals()[shortcuts[ky]]})")

