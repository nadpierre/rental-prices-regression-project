import os
import pandas as pd

def export_list_to_csv(data:list, csv_path:str) -> None:
	df = pd.DataFrame(data)
	if not os.path.isfile(csv_path):
		df.to_csv(csv_path, index=False)
	else:
		df.to_csv(csv_path, index=False, header=False, mode='a')