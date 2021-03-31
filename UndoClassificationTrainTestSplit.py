'''
Run this script after data has been split into training and test
subfolders using ClassificationTrainTestSplit.py
(returns all images to the class subfolder, undos any random sorting)
'''

def undoTTSplit():
	import os, shutil

	# specify parent directory
	path = '/home/aj/Projects/Coursera/DeepLearningTensorFlow/PetImages'
	folders = ('Training', 'Testing')

	for f in folders:
		# set the path to the current class
		folderpath = path + '/' + f

		# change directories to this class's subfolder
		os.chdir(folderpath)

		# get current directories (should be train and test)
		for c in ('Cat', 'Dog'):
			# set the path to the current subfolder
			cpath = folderpath + '/' + c

			# change directories to tpath
			os.chdir(cpath)

			# move all items from this path to original folder
			for s in os.listdir(cpath):
				shutil.move(s, path + '/' + c)

		# remove the current folder (either Training or Testing)
		shutil.rmtree(folderpath)

if __name__ == '__main__':
	# UndoClassificationTrainTestSplit.py executed as script
	undoTTSplit()