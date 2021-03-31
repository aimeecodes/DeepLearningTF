'''
This script assumes you're performing classification, and 
have your data stored in the following format:
(1) parent directory containing 2 folders: training and testing
(2) inside each training and testing folder needs to be whatever classes
	you're going to give the model to predict (Cat / Dog / whatever else)
Sets up directories for tensorflow's generator library
'''

def createTTSplit():
	import os, sys, math, random, shutil

	# specify parent directory
	path = '/home/aj/Projects/Coursera/DeepLearningTensorFlow/PetImages'
	classes = os.listdir(path)

	#################################################
	#                                               #
	#                  parameters                   #
	#                                               #
	#################################################

	# specify what percentage of your dataset should be
	# used for training data between 0 and 1
	train_split = 0.7

	def getSize(directory):
		return len(os.listdir(directory))

	def getSplit(number, ratio):
		'''
		this method takes in a number of samples, and returns
		the number of (ratio)% of number
		'''
		return math.floor(number*ratio)

	for c in classes:
		# set the path to the current class
		classpath = path + '/' + c

		# change directories to this class's subfolder
		os.chdir(classpath)

		# get a set of all names of samples in this class
		samples = set(os.listdir(classpath))

		# get the overall number of samples for the class
		numsamples = len(samples)

		# get the number of samples that need to go into
		# training subfolder
		trainsize = getSplit(numsamples, train_split)

		# create two subfolders for training and test datasets
		os.mkdir(c + '_train')
		os.mkdir(c + '_test')

		# randomly pick trainsize samples from numsamples
		trainsamples = set(random.sample(samples, trainsize))
		testsamples = samples - trainsamples

		# fill the train subfolder
		for sample in trainsamples:
			shutil.move(sample, c + '_train')

		# fill the test subfolder
		for sample in testsamples:
			shutil.move(sample, c + '_test')

	# now that the subfolders are created, have to rearrange
	os.chdir(path)

	# make training and validation subfolders
	os.mkdir('Training')
	os.mkdir('Testing')

	for c in classes:
		# move the subfolders out of the class and into Training or Testing
		shutil.move(path + '/' + c + '/' + c + '_train', path + '/Training')
		shutil.move(path + '/' + c + '/' + c + '_test', path + '/Testing')
		
		# once inside the Training / Testing folder, rename to class
		os.rename(path + '/Training/' + c + '_train', path + '/Training/' + c)
		os.rename(path + '/Testing/' + c + '_test', path + '/Testing/' + c)

if __name__ == '__main__':
	# ClassificationTrainTestSplit.py executed as script
	createTTSplit()