#!/usr/bin/env python

"""
Background
----------

 allfilts.py
 
 Purpose:
 --------
 Provide basic filter routines for frequent manipulation of netcdf data.

 Must be able to handle CF and EPIC time conventions 

 History:
 --------

"""


# System Stack
import datetime
import argparse
import sys

# IO Stack
import xarray as xr

#
import calc.filters.lanzcos as lanzcos
from calc.EPIC2Datetime import EPIC2Datetime, get_UDUNITS
from io_utils.EcoFOCI_netCDF_read import EcoFOCI_netCDF


__author__   = 'Shaun Bell'
__email__    = 'shaun.bell@noaa.gov'
__created__  = datetime.datetime(2017, 01, 17)
__modified__ = datetime.datetime(2017, 01, 17)
__version__  = "0.1.0"
__status__   = "Development"

"""----------------------------- Main -------------------------------------"""

# parse incoming command line options
parser = argparse.ArgumentParser(description='Map')
parser.add_argument('ifile', metavar='ifile', type=str, 
	help='full path to file or pointer')
parser.add_argument('--isCF', action="store_true", 
	help='Flag if timeword is CF convention otherwise assume EPIC convention')
parser.add_argument('--tave', type=str, 
	help='10T:Ten Minute, 1H:Hourly, 1D:Daily, MS:Monthly average labeled at the end of the chosen time period')
parser.add_argument('--tdecim', type=str, 
	help='10T:Ten Minute, 1H:Hourly, 6H:Synoptic, 1D:Daily (12z) time decimation')
parser.add_argument('--filter', type=str, 
	help=', F35:35hr Lanzcos, F29:2.86hr Lanzcos lowpass filter ')
args = parser.parse_args()


"""----------------------------------------------
Get parameters from specified pointerfile - 
an example is shown in the readme description of
this program using .yaml form

"""
if args.ifile.split('.')[-1] == 'nc':
	ifile = [args.ifile]
elif args.ifile.split('.')[-1] == 'yaml':
	pointer_file = ConfigParserLocal.get_config_yaml(args.ifile)
else:
	print "Data file or pointer file format not recognized"
	sys.exit()



##############
# process optional time average string flag
if args.filter:
	for ind_file in ifile:
		df = EcoFOCI_netCDF(ind_file)
		global_atts = df.get_global_atts()
		vars_dic = df.get_vars()
		data = df.ncreadfile_dic()
		df.close()	
		if args.filter == 'F35':
			pass
		elif args.filter == 'F29':
			pass
		else:
			print "Choose a valid filter"



##############
# averaging/resampling
if args.tave and args.isCF:
	#use argument string to set up frequency
	for ind_file in ifile:
		ds = xr.open_dataset(ind_file)
		dsr = ds.resample(args.tave,dim='time',how='mean',closed='right',label='right')
		print dsr.to_dataframe().to_csv()
		ds.close()

elif args.tave and not args.isCF:
	for ind_file in ifile:
		ds = xr.open_dataset(ind_file, decode_times=False)
		ds['time'] = EPIC2Datetime(ds.time.data , ds.time2.data)
		ds = ds.drop('time2')
		dsr = ds.resample(args.tave,dim='time',how='mean',closed='right',label='right')
		print dsr.to_dataframe().to_csv()
		ds.close()	

if args.tdecim and not args.isCF:
	for ind_file in ifile:
		if args.tdecim in ['10T']:
			df = EcoFOCI_netCDF(ind_file)
			global_atts = df.get_global_atts()
			vars_dic = df.get_vars()
			data = df.ncreadfile_dic()
			df.close()
			for i, val in enumerate(data['time']):
				if ((EPIC2Datetime([data['time'][i],],[data['time2'][i],])[0]).minute) % 10 == 0:
					timestr = datetime.datetime.strftime(EPIC2Datetime([data['time'][i],],[data['time2'][i],])[0],"%Y-%m-%d %H:%M:%S" )
					line = ''
					header='time, '
					for k in vars_dic.keys():
						if k in ['time','time2']:
							pass
						elif k in ['lat','lon','dep','depth','depth01','latitude','longitude']:
							header = header + ', ' + k
							line = line + ', ' + str(data[k][0])
						else:
							header = header + ', ' + k
							line = line + ', ' + str(data[k][i,0,0,0])
					if i==0:
						print header						
					print timestr + ', ' + line
	for ind_file in ifile:
		if args.tdecim in ['1H']:
			df = EcoFOCI_netCDF(ind_file)
			global_atts = df.get_global_atts()
			vars_dic = df.get_vars()
			data = df.ncreadfile_dic()
			df.close()
			for i, val in enumerate(data['time']):
				if ((EPIC2Datetime([data['time'][i],],[data['time2'][i],])[0]).minute) == 0:
					timestr = datetime.datetime.strftime(EPIC2Datetime([data['time'][i],],[data['time2'][i],])[0],"%Y-%m-%d %H:%M:%S" )
					line = ''
					header='time, '
					for k in vars_dic.keys():
						if k in ['time','time2']:
							pass
						elif k in ['lat','lon','dep','depth','depth01','latitude','longitude']:
							header = header + ', ' + k
							line = line + ', ' + str(data[k][0])
						else:
							header = header + ', ' + k
							line = line + ', ' + str(data[k][i,0,0,0])
					if i==0:
						print header	
					print timestr + ', ' + line
		if args.tdecim in ['6H']:
			df = EcoFOCI_netCDF(ind_file)
			global_atts = df.get_global_atts()
			vars_dic = df.get_vars()
			data = df.ncreadfile_dic()
			df.close()
			for i, val in enumerate(data['time']):
				if (((EPIC2Datetime([data['time'][i],],[data['time2'][i],])[0]).minute) == 0) and (((EPIC2Datetime([data['time'][i],],[data['time2'][i],])[0]).hour) in [0,6,12,18]):
					timestr = datetime.datetime.strftime(EPIC2Datetime([data['time'][i],],[data['time2'][i],])[0],"%Y-%m-%d %H:%M:%S" )
					line = ''
					header='time, '
					for k in vars_dic.keys():
						if k in ['time','time2']:
							pass
						elif k in ['lat','lon','dep','depth','depth01','latitude','longitude']:
							header = header + ', ' + k
							line = line + ', ' + str(data[k][0])
						else:
							header = header + ', ' + k
							line = line + ', ' + str(data[k][i,0,0,0])
					if i==0:
						print header	
					print timestr + ', ' + line					