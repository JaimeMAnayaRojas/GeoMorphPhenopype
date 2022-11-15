#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:15:58 2022

@author: jaime
"""

import phenopype as pp
import os

## change working dir - will contain project folder
os.chdir(r"/home/jaime/sciebo/GeoMorph/_temp/")

## set project name
project_name = "project_2"

## fetch template from downloaded template repo (https://github.com/phenopype/phenopype-templates)
template_path = r"/home/jaime/sciebo/GeoMorph/landmarks_ref.yaml"

## set directory with images  
image_dir = r"/home/jaime/sciebo/GeoMorph/data/photos"


proj = pp.Project(project_name)


## add all stickleback-images from the data folder, but exclude the two that don't belong to the series 
proj.add_files(image_dir = image_dir)

## add the config template; provide a tag
proj.add_config(template_path=template_path, tag="v1", overwrite=True)

## set the project-wide reference. the reference has its own tag, in case your project uses multiple reference cards
## How should I do it when each picture are likely to have a different reference
proj.dir_paths[0]

fileList = os.listdir(image_dir)
#proj.add_reference(reference_image_path= os.path.join(image_dir,"stickleback_side.jpg"), reference_tag="stickle-scale")
proj.add_reference(reference_image_path= os.path.join(image_dir,fileList[0]), reference_tag="stickle-scale")


# I am not able to continue to the next picture or to change the settings
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