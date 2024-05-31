# IP-Expand
I just needed to expand IP ranges for some data processing so I wrote this script to expand a list of IP ranges to a list of individual IP addresses

The input file is called ip-ranges.txt and is a TAB separated file with 4 fields
1. Range ID
2. Range START IP
3. Range END IP
4. Range Description

The Output file is called ip-ranges-expanded.csv and is a CSV file with 4 fields:
1. IP address
2. Original IP Range
3. Y/N flag to indicate if this came from a range in the input file or the range was actually one single IP
4. Description
