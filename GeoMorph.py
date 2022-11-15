#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:15:58 2022

@author: jaime
"""

import phenopype as pp
import os

## change working dir - will contain project folder
os.chdir(r"/home/jaime/sciebo/GeoMorphPhenopype/_temp")

## set project name
project_name = "project_2"

## fetch template from downloaded template repo (https://github.com/phenopype/phenopype-templates)
template_path = r"/home/jaime/sciebo/GeoMorphPhenopype/detection_mask_ref.yaml"

## set directory with images  
image_dir = r"/home/jaime/sciebo/GeoMorphPhenopype/data/photos"


proj = pp.Project(project_name)

os.listdir(image_dir)
## add all stickleback-images from the data folder, but exclude the two that don't belong to the series 
proj.add_files(image_dir = image_dir, include="IMG", exclude=["side","top"])

## add the config template; provide a tag
proj.add_config(template_path=template_path, tag="v1", overwrite=True)



## modify the "preprocessing" section

target1 = """    - preprocessing:"""
replacement1 = """    - preprocessing:
        - add_reference"""

proj.edit_config(
    tag="v1",
    target=target1,
    replacement=replacement1
)


replacement2 = """    - preprocessing:
        - detect_reference"""

proj.edit_config(
    tag="v1",
    target=target1,
    replacement=replacement2
)



## set the project-wide reference. the reference has its own tag, in case your project uses multiple reference cards
# proj.add_reference(reference_image_path= os.path.join(image_dir,"stickleback_side.jpg"), reference_tag="stickle-scale")
# how to add reference for all?

## run image processing
for path in proj.dir_paths:
    pp.Pype(path, tag="v1")


## collect results and store in folder "<project-root>/results/annotations"
proj.collect_results("v1", "annotations", "annotations")


## display results
import ipyplot ## install with `pip install ipyplot`

canvas_list = []
for path in proj.dir_paths:
    canvas_list.append(pp.load_image(os.path.join(path, "canvas_v1.jpg"), mode="rgb"))

ipyplot.plot_images(canvas_list, img_width=300)