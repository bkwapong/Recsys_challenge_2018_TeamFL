# Recsys_challenge_2018_TeamFL

How to run the codes:

Step 1:
Run mpd_slicer.py on the mpd dataset to generate 1000 different json files:
  python mpd_slicer.py
You need to create a folder named 1000_playlists before running the code. The 1000 different json files will be saved in this folder.

Step2:
Run mpd_dataset_generator.py to pull relevant information from the mpd for training:
  python mpd_dataset_generator.py 1000_playlists



