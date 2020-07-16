# Author: Christoph Giese @cgi1
# Script to find needles in haystack.

import os

if __name__ == '__main__':

	fin_haystack_path='/Users/g/PycharmProjects/g2/g2/modules/data_sources/data/border_monitoring_dtag/LATEST-top100k.csv'
	fin_needle_path='/Users/g/akamai_identification/akamai_deploy_ips.txt'

	with open(fin_haystack_path, 'r') as fin_haystack:
		with open(fin_needle_path, 'r') as fin_needle:
			haystack_lines = [line.rstrip() for line in fin_haystack]
			needle_lines = [line.rstrip() for line in fin_needle]
			print("Loaded %s haystack_lines and %s needle_lines" % (len(haystack_lines), len(needle_lines)))


			in_haystack = []
			not_in_haystack = []
			# yes, this is inefficient, but i want row based manipulation in case
			for needle in needle_lines:
				#print(needle)
				matching = [(pos,s) for pos,s in enumerate(haystack_lines) if needle in s]
				if len(matching) > 0:
					for match in matching:
						print("HIT>[%s] pos [%s] match [%s]" % (needle, match[0], match[1]))
						in_haystack.append((needle, match[0], match[1]))
				else:
					not_in_haystack.append(needle)
			print("Found %s needles in haystack and %s not." % (len(in_haystack), len(not_in_haystack)))
			print("---- Output in_haystack ---- \n")

			print(in_haystack)
	print("Finished")

