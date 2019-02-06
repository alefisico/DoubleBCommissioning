##################################################################
########   TO RUN THIS: python multicrab.py -d dataset -v 9_4_X_v2 -s T3_US_FNALLPC
########   In --dataset, if you specify for instance QCD it runs ALL the keys in datasamples that starts with QCD.
########   DO NOT DO: crab submit multicrab.py
##################################################################

from CRABClient.UserUtilities import config
import argparse, sys, os
from httplib import HTTPException
from CRABAPI.RawCommand import crabCommand

#############################################
#### This are general parameters.
#### Change them if needed
listParam = ['miniAOD=True', 'doBoostedCommissioning=True', 'groups=DoubleBCommissioning' ]   ### dont include runOnData, it is added automatically later

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
	Samples[ '2016-BTagMuBv1' ] = [ '/BTagMu/Run2016B-17Jul2018_ver1-v1/MINIAOD', 10 ]
	Samples[ '2016-BTagMuBv2' ] = [ '/BTagMu/Run2016B-17Jul2018_ver2-v1/MINIAOD', 10 ]
	Samples[ '2016-BTagMuC' ] = [ '/BTagMu/Run2016C-17Jul2018-v1/MINIAOD', 10 ]
	Samples[ '2016-BTagMuD' ] = [ '/BTagMu/Run2016D-17Jul2018-v1/MINIAOD', 10 ]
	Samples[ '2016-BTagMuE' ] = [ '/BTagMu/Run2016E-17Jul2018-v1/MINIAOD', 10 ]
	Samples[ '2016-BTagMuF' ] = [ '/BTagMu/Run2016F-17Jul2018-v1/MINIAOD', 10 ]
	Samples[ '2016-BTagMuG' ] = [ '/BTagMu/Run2016G-17Jul2018-v1/MINIAOD', 10 ]
	Samples[ '2016-BTagMuH' ] = [ '/BTagMu/Run2016H-17Jul2018-v1/MINIAOD', 10 ]

	Samples[ '2017-BTagMuB' ] = [ '/BTagMu/Run2017B-17Nov2017-v1/MINIAOD', 10 ]
	Samples[ '2017-BTagMuC' ] = [ '/BTagMu/Run2017C-17Nov2017-v1/MINIAOD', 10 ]
	Samples[ '2017-BTagMuD' ] = [ '/BTagMu/Run2017D-17Nov2017-v1/MINIAOD', 10 ]
	Samples[ '2017-BTagMuE' ] = [ '/BTagMu/Run2017E-17Nov2017-v1/MINIAOD', 10 ]
	Samples[ '2017-BTagMuF' ] = [ '/BTagMu/Run2017F-17Nov2017-v1/MINIAOD', 10 ]

	Samples[ '2018-BTagMuA' ] = [ '/BTagMu/Run2018A-17Sep2018-v1/MINIAOD', 10 ]
	Samples[ '2018-BTagMuB' ] = [ '/BTagMu/Run2018B-17Sep2018-v1/MINIAOD', 10 ]
	Samples[ '2018-BTagMuC' ] = [ '/BTagMu/Run2018C-17Sep2018-v1/MINIAOD', 10 ]
	Samples[ '2018-BTagMuDv2' ] = [ '/BTagMu/Run2018D-PromptReco-v2/MINIAOD', 20 ]

	Samples[ '2016-QCDExtPt170' ] = [ '/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', 1 ]
	Samples[ '2016-QCDExtPt300' ] = [ '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM', 1 ]
	Samples[ '2016-QCDExtPt470' ] = [ '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', 1 ]
	Samples[ '2016-QCDExtPt600' ] = [ '/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', 1 ]
	Samples[ '2016-QCDExtPt800' ] = [ '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', 1 ]
	Samples[ '2016-QCDExtPt1000' ] = [ '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', 1 ]
	Samples[ '2016-QCDPt170' ] = [ '/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM', 1 ]
	Samples[ '2016-QCDPt300' ] = [ '/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', 1 ]
	Samples[ '2016-QCDPt470' ] = [ '/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', 1 ]
	Samples[ '2016-QCDPt600' ] = [ '/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', 1 ]
	Samples[ '2016-QCDPt800' ] = [ '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', 1 ]
	Samples[ '2016-QCDPt1000' ] = [ '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM', 1 ]
	Samples[ '2017-QCDPt170' ] = [ '/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]
	Samples[ '2017-QCDPt300' ] = [ '/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]
	Samples[ '2017-QCDPt470' ] = [ '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]
	Samples[ '2017-QCDPt600' ] = [ '/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]
	Samples[ '2017-QCDPt800' ] = [ '/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]
	Samples[ '2017-QCDPt1000' ] = [ '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM', 1 ]

	#Samples[ '2018-QCDPt170' ] = [ '/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM', 1 ]
	Samples[ '2018-QCDPt300' ] = [ '/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v3/MINIAODSIM', 1 ]
	Samples[ '2018-QCDPt470' ] = [ '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', 1 ]
	Samples[ '2018-QCDPt600' ] = [ '/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', 1 ]
	#Samples[ '2018-QCDPt800' ] = [ '', 1 ]
	Samples[ '2018-QCDPt1000' ] = [ '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM', 1 ]


	processingSamples = {}
	if 'all' in args.dataset:
		for sam in Samples: processingSamples[ sam ] = Samples[ sam ]
	else:
		for sam in Samples:
			if sam.startswith( args.dataset ): processingSamples[ sam ] = Samples[ sam ]
	if len(processingSamples)==0: print 'No sample found. \n Have a nice day :)'

        if '2017' in args.dataset: listParam.append('defaults=Moriond18')
        elif '2018' in args.dataset: listParam.append('defaults=Prompt18')
        else: listParam.append('defaults=2016_SF')
        if 'QCD' in args.dataset: listParam.append('runOnData=False')
        else: listParam.append('runOnData=True')

	for sam in processingSamples:
		dataset = processingSamples[sam][0]

		config.Data.inputDataset = dataset
		config.Data.unitsPerJob = processingSamples[sam][1]
		config.Site.storageSite = args.storageSite
		config.Data.outLFNDirBase = '/store/user/'+os.environ['USER']+'/DoubleBTagCommissioning/'+args.version

		if 'BTagMu' in dataset:
			procName = dataset.split('/')[1]+'_'+dataset.split('/')[2]+'_'+args.version
                        if '2017' in sam: config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'
                        elif '2018' in sam: config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
                        else: '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
			config.Data.splitting = 'LumiBased'
			config.General.workArea = 'crab_projects/Data'

		else:
			procName = dataset.split('/')[1]+('Ext' if 'Ext' in sam else '')+'_'+args.version
			config.Data.splitting = 'FileBased'
			config.General.workArea = 'crab_projects/MC'

		config.JobType.pyCfgParams = listParam
		config.General.requestName = procName

		print config
		print '|--- Submmiting sample: ', procName
		if not args.testNoSend: submit(config)
