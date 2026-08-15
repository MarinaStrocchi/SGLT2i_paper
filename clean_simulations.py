import os
import sys

import shutil

sims_folder = sys.argv[1]

compress = False
split_to_compress = 28
for i in range(split_to_compress+1):
	split_folder = os.path.join(sims_folder,"split_"+str(i))

	if compress:
		print("Compressing "+split_folder+"...")

		shutil.make_archive(split_folder, 'zip', split_folder)
	else:
		print("Deleting "+split_folder+"...")

	rm_cmd = "rm -r "+split_folder
	os.system(rm_cmd)
	
		
	