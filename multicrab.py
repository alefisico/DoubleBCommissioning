##################################################################
########   TO RUN THIS: python crab3_QCD.py -d dataset -v 9_4_X_V1 -s T3_US_FNALLPC
########   In --dataset, if you specify for instance QCD it runs ALL the keys in datasamples that starts with QCD. 
########   DO NOT DO: crab submit crab3_QCD.py
##################################################################

from CRABClient.UserUtilities import config
import argparse, sys, os
from httplib import HTTPException
from CRABAPI.RawCommand import crabCommand

#############################################
#### This are general parameters. 
#### Change them if needed
listParam = ['defaults=Moriond18', 'miniAOD=True', 'doBoostedCommissioning=True', 'groups=DoubleBCommissioning' ]   ### dont include runOnData, it is added automatically later

#### General crab parameters
config = config()
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = os.environ['CMSSW_BASE']+'/src/RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py'
config.Data.inputDBS = 'global'
config.Data.publication = False
#config.Data.ignoreLocality = True
###############################################################

def submit(config):
	try:
		if args.dryrun: crabCommand('submit', '--dryrun', config = config)
		else: crabCommand('submit', config = config)
	except HTTPException, hte:
		print 'Cannot execute commend'
		print hte.headers


#######################################################################################
if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--dataset', action='store', default='all', dest='dataset', help='Sample to process. Example: QCD, BTagMu.' )
	parser.add_argument('-v', '--version', action='store', default='9_4_X_v2', dest='version', help='Version. Example: 9_4_X_v1' )
	parser.add_argument('-s', '--storageSite', action='store', default='T3_CH_PSI', dest='storageSite', help='storageSite. Example: T2_CH_CERN or T3_US_FNAL' )
	parser.add_argument('-D', '--dryrun', action='store_true', default=False, help='To run dryrun crab mode.' )
	parser.add_argument('-t', '--testNoSend', action='store_true', default=False, help='To print crab config without send it. Helpful to debug' )

	try: args = parser.parse_args()
	except:
		parser.print_help()
		sys.exit(0)

	Samples = {}
	###  Samples[Dataset nickname] = [ 'dataset name', splitting number  ]
	Samples[ 'BTagMuB' ] = [ '/BTagMu/Run2017B-17Nov2017-v1/MINIAOD', 10 ]
	Samples[ 'BTagMuC' ] = [ '/BTagMu/Run2017C-17Nov2017-v1/MINIAOD', 10 ]
	Samples[ 'BTagMuD' ] = [ '/BTagMu/Run2017D-17Nov2017-v1/MINIAOD', 10 ]
	Samples[ 'BTagMuE' ] = [ '/BTagMu/Run2017E-17Nov2017-v1/MINIAOD', 10 ]
	Samples[ 'BTagMuF' ] = [ '/BTagMu/Run2017F-17Nov2017-v1/MINIAOD', 10 ]

	Samples[ 'QCDPt170' ] = [ '/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]
	Samples[ 'QCDPt300' ] = [ '/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]
	Samples[ 'QCDPt470' ] = [ '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]
	Samples[ 'QCDPt600' ] = [ '/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]
	Samples[ 'QCDPt800' ] = [ '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]
	Samples[ 'QCDPt1000' ] = [ '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]


	processingSamples = {}
	if 'all' in args.dataset: 
		for sam in Samples: processingSamples[ sam ] = Samples[ sam ]
	else:
		for sam in Samples: 
			if sam.startswith( args.dataset ): processingSamples[ sam ] = Samples[ sam ]
	if len(processingSamples)==0: print 'No sample found. \n Have a nice day :)'
		
	for sam in processingSamples:
		dataset = processingSamples[sam][0]
		
		config.Data.inputDataset = dataset
		config.Data.unitsPerJob = processingSamples[sam][1]
		config.Site.storageSite = args.storageSite
		config.Data.outLFNDirBase = '/store/user/'+os.environ['USER']+'/DoubleBTagCommissioning/'+args.version

		if 'BTagMu' in dataset: 
			procName = dataset.split('/')[1]+'_'+dataset.split('/')[2]+'_'+args.version
			config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'
			config.Data.splitting = 'LumiBased'
			config.General.workArea = 'crab_projects/Data'
			listParam.append('runOnData=True')

		else:
			procName = dataset.split('/')[1]+'_'+args.version
			config.Data.splitting = 'FileBased'
			config.General.workArea = 'crab_projects/MC'
			listParam.append('runOnData=False')

		config.JobType.pyCfgParams = listParam
		config.General.requestName = procName

		print config
		print '|--- Submmiting sample: ', procName
		if not args.testNoSend: submit(config)
