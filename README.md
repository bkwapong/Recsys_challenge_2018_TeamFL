# Recsys_challenge_2018_TeamFL

How to run the codes:

Step 1:
Run mpd_slicer.py on the mpd dataset to generate 1000 different json files.You need to create a folder named 1000_playlists before running the code. The 1000 different json files will be saved in that folder:
  python mpd_slicer.py

Step 2:
Run mpd_dataset_generator.py to pull relevant information from the mpd for training. This code takes one command line argument which is the path to the folder where the 1000 json files are kept:
  python mpd_dataset_generator.py 1000_playlists
  
Step 3:
Run word2vec.py to train the model on the generated mpd_dataset:
  python word2vec.py
  
Step 4:
Run challenge_slicer.py on the challenge dataset to generate 1 json file. You need to create a folder named 1_playlist before running the code. The json file will be saved in that folder:
  python challenge_slicer.py

Step 5:
Run challenge_dataset_generator.py to pull relevant information from the challenge dataset for prediction. This code takes one command line argument which is the path to the folder where the json file is kept:
  python challenge_dataset_generator.py 1_playlist

Step 6:
Run word2vec_prediction.py to generate the prediction.

Step 7:
Run clean_prediction.py to clean up the prediction.

Step8:
Run submission.py to get the 500 tracks for each prediction.
