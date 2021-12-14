# VRDL_HW3
-------------------------------------------------------------------------
This repository is the official implementation of My VRDL_HW3: Instance segmentation


Requirements
-------------------------------------------------------------------------
Python version:
	
	Python 3.7.11

pytorch:
	
	pip3 install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio===0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

mmdetection:
  
  mmdet 2.19.0 
  
  Please follow the mmedetection github tutorial to install packages:
    
Link: https://github.com/open-mmlab/mmdetection/blob/master/docs/get_started.md


pycocotools:

	pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI


pycococreator:

  	pip install git+git://github.com/waspinator/pycococreator.git@0.2.0



Training
-------------------------------------------------------------------------
To train the models, we first need to put every file into the right directory to ensure the whole process can run normally, and I will specify the steps to handle it below.

	1. Create a directory "pj" first, and move to the "pj" directory 
	
	2. Since this implementation is based on mmdetectoin, run this: git clone https://github.com/open-mmlab/mmdetection
	
	3. Move to mmdetection directory, and create a directory "dataset".
	
	4. We copy our "train" and "test" directory and "test_img_ids.json" into "dataset", they are provided by TAs.
	
	5. Also put "data_process.py","defuse.py", and "trans.py" into "dataset" directory
	
	6. Run "data_process.py", this would generate files needed for training.
	
	7. Now we have the "dataset" directory properly set up, next, we need to move some more flies.
  
  	8. Create a directory "HW" in ./configs, and move HW.py into "HW"
  
  	9. Move coco_instance.py to  ./configs/_base_/datasets

  	10. Move mask_rcnn_r50_fpn.py to ./configs/_base_/models

  	11. Move schedule_1x.py to ./configs/_base_/schedules

  	12. Move mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py to ./configs/mask_rcnn

  	13. Move resnet.py to ./mmdet/models/backbones
 
	14. All data are now in the right place, and it should look like this, note that if there is no (F) postfix, that is a directory
	
	
        pj ----- mmdetection ---- configs ---- _base_ ----- datasets ---- coco_instance.py (F)
                             |            |           |
                             |            |           ----- models ---- mask_rcnn_r50_fpn.py (F)
                             |            |           |
                             |            |           ----- schdules ---- schedule_1x.py (F)
                             |            |
                             |            ---- mask_rcnn ---- mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py(F)
                             |            |
                             |            ---- HW ---- HW.py(F)
                             |
                             ---- dataset---- train         
                             |           |                     
                             |           ---- test      
                             |           |
                             |           ---- data_process.py(F)   
                             |           |
                             |           ---- defuse.py(F)
                             |           |
                             |           ---- test_img_ids.json(F)
                             |           |
                             |	         ---- trans.py(F)
                             ---- mmdet ---- models ---- backbones ---- resnet.py(F)
                      
Now we are prepared to train the model.

To train the model, run this command in "mmdetection" directory:

	python3 tools/train.py configs/HW/HW.py

You may need network while running this, for pretrained model would be download from internet

The files mentioned above in included either in the "programs" directory or the "configs" directory in this repo.


Evaluation
-------------------------------------------------------------------------

First You need to handle the file as the training part has done, then, 

run the trans.py, this would transform the test_img_ids.json a little to match the format.

To evaluate the model, download the model from link in the below.
	
Put the latest.pth into the "mmdetection" directory, then run:

        python3 tools/test.py configs/HW/HW.py  ./latest.pth --out ./result.pkl --show-dir ./test_results
	

After running, a file "result.pkl" would be generated in ./

Move the result.pkl to "dataset" directory and run defuse.py
        
        python3 defuse.py
        
This would generate answer.json, just zip it and upload to colab to evaluate the performance.		

Model(latest.pth): https://drive.google.com/file/d/1Mc9ts3-ChO_9GNzbLhPwVQpAO7_K7_p7/view?usp=sharing


	
Pre-trained Models
-------------------------------------------------------------------------
You can download and use pretrained models by simply running training command above:
    
	python3 tools/train.py configs/HW/HW.py

This will download the model if not downloaded yet.
    
    
Results
-------------------------------------------------------------------------
Our model achieves the following performance on :

mAP: HW3 challenge on codalab	

![img1](https://github.com/egghead2630/VRDL_HW3/blob/main/result.png)


Reproducing without retraining
-------------------------------------------------------------------------
Please refer to evaluation part, there is a detailed explaination.





Thanks for reading this README.
