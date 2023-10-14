import pandas as pd

def read_txt(filename):

	file = open(filename, "r")
	f = file.readlines()

	new_list = []
	for line in f:
			new_list.append(line[:-1])

	_df = pd.DataFrame(new_list, columns = ["Values"])

	output_list = []

	for index, row in _df.iterrows():
		# convert pd series into list
		results_string = row.tolist()

		# split the list by spaces into a 3 index list
		results_list = results_string[0].split()
		
		# convert level separations into zeros
		if not results_list:
			results_list = [0, 0, 0]	

		output_list.append(results_list)

	prelim_df = pd.DataFrame(output_list, columns = ["x", "y", "z"])
	prelim_df = prelim_df.astype(float)

	# get prelim_df indices that separate levels
	separator = prelim_df.index[prelim_df['x'] == 0].tolist()
	separator = separator[1:-1]

	# create a list with levels based on separators (zeros)
	levels_data = []
	level = 1
	counter = 0

	for n in range(0, len(prelim_df)):
		if counter not in separator:
			levels_data.append(level)
		else:
			level += 1
			levels_data.append(level)		
		counter += 1

	df = prelim_df
	df["level"] = levels_data
	df = df[(df != 0).all(1)]

	file.close()

	return df