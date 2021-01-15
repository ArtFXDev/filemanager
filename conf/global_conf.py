# -*- coding: utf-8 -*-

"""
================================
    JE S'APPELLE ROOOOOOOOT
================================
"""
import os
root = os.getenv('ROOT_PIPE') or "D:/SynologyDrive"

"""
=====================
     Variables
=====================
"""
projects_server = {
    "BACKSTAGE": "tars",
    "BARNEY": "ana",
    "COCORICA": "tars",
    "DIVE": "ana",
    "DREAMBLOWER": "tars",
    "FROM_ABOVE": "tars",
    "GOOD_MORNING_KITTY": "ana",
    "GREEN": "ana",
    "HAKAM": "ana",
    "HOSTILE": "tars",
    "PIR_HEARTH": "ana",
    "RELATIVITY": "tars",
    "TEST_PIPE": "ana",
}
projects = [
    "BACKSTAGE",
    "BARNEY",
    "COCORICA",
    "DIVE",
    "DREAMBLOWER",
    "FROM_ABOVE",
    "GOOD_MORNING_KITTY",
    "GREEN",
    "HAKAM",
    "HOSTILE",
    "PIR_HEARTH",
    "RELATIVITY",
    "TEST_PIPE",
]
# projects = ['ARAL', 'ASCEND', 'BREACH', 'FORGOT_YOUR_PASSWORD', 'VERLAN', 'ISSEN_SAMA',
#             'MOON_KEEPER', 'LONE', 'TIMES_DOWN', 'HARU', 'RESURGENCE', 'LOREE', 'CLAIR_DE_LUNE', 'DEMO', 'A_PIPE']
"""
Softwares
"""
shot_softwares = ['houdini', 'maya']
comp_softwares = ['nuke', 'pftrack']
"""
Categories
"""
asset_categories = ['01_characters',
                    '02_vehicles', '03_props', '04_sets', '05_FXs']
"""
Tasks
"""
shot_tasks = ['01_layout', '02_blocking',
              '03_anim', '04_fx', '05_render', '06_comp']
asset_tasks = ['01_modeling', '02_modelinglow',
               '03_uvs', '04_texturing', '05_setup', '06_lookdev', '07_fx', '08_anim']
"""
Asset Subtasks
"""
asset_subtasks_dic = {'01_modeling': ('houdini', 'maya', 'zbrush', 'marvelous', 'speedtree'),
                      '02_modelinglow': ('houdini', 'maya', 'zbrush'),
                      '03_uvs': ('houdini', 'maya', 'zbrush'),
                      '04_texturing': ('substance', 'mari', 'houdini', 'maya'),
                      '05_setup': ('houdini', 'maya'),
                      '06_lookdev': ('houdini', 'maya'),
                      '07_fx': ('houdini', 'maya'),
                      '08_anim': ('houdini', 'maya')
                      }
"""
Types ?
"""
types = {'asset': '01_ASSET_3D', 'shot': '02_SHOT'}
"""
Exts ?
"""
shot_ext_dir = {'maya': '.ma', 'houdini': '.hipnc',
                'nuke': '.nk', 'pftrack': '.PTP'}

asset_ext_dir = {'houdini': '.hipnc', 'maya': '.ma', 'zbrush': '.ztl',
                 'substance': '.spp', 'mari': '.mra', 'marvelous': '.Zprj', 'speedtree': '.spm'}
"""
=====================
SID
=====================
"""
sep = "/"

"""
=====================
PATH
=====================
"""
"""
=====================
Templates
=====================
"""
"""
Path
"""
shot_workspace_path = root + '/{project}/03_WORK_PIPE/02_SHOT/{dimension}'
asset_workspace_path = root + \
    '/{project}/03_WORK_PIPE/01_ASSET_3D/{cat}/{name}/3d'
recycle_bin_path = root + \
    r'/{project}/00_UTILITY/04_PIPELINE/pipeline_recycle_bin'
"""
Template
"""
default_scene_templates = '//multifct/tools/pipeline/global/misc/templates/scene_templates/{software}'
scene_templates = root + \
    '/{project}/00_UTILITY/04_PIPELINE/scene_templates/{software}'
default_workspace_template = '//multifct/tools/pipeline/global/misc/templates/workspace.mel'
workspace_template = '/{project}/00_UTILITY/04_PIPELINE/scene_templates/workspace.mel'
"""
Name
"""
shot_template_name = '{software}_shot_template.{ext}'
asset_template_name = '{subtask}_asset_template.{ext}'
"""
File name
"""
asset_file_name = '{name}.{ext}'
shot_file_name = '{sequence}_{shot}.{ext}'

"""
Extention
"""
# Default for creation is the first of the list
ext_by_soft = {
    'maya': ['ma', 'mb'],
    'houdini': ['hipnc', 'hip'],
    'nuke': ['nk'],
    'pftrack': ['ptp'],
    'zbrush': ['ztl'],
    'substance': ['spp'],
    'mari': ['mra'],
    'marvelous': ['zprj'],
    'speedtree': ['spm']
}


def get_soft_by_ext(ext_find):
  for soft_name, list_ext in ext_by_soft.iteritems():
    if ext_find in list_ext:
      return soft_name


# Make a list with all extensions
extensions = []
for key, val in ext_by_soft.iteritems():  # Replace iteritems by .items() for python3
  for ext in val:
    extensions.append(ext)

softwares = ext_by_soft.keys()

"""
=====================
    workspace
=====================
"""
folder_workspace = ['scenes', 'textures', 'images', 'data', 'caches']


"""
Other
"""
logo_path = r'\\multifct\tools\pipeline\global\misc\pipeline_logo_src\logo.png'
quote_path = r'\\multifct\tools\pipeline\global\misc\pipeline_quote_src\.quote.json'
doc_path = r'\\multifct\tools\pipeline\global\misc\documentation.pdf'
