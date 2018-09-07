from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'QCD_Pt_470to600_MuEnriched_v1_Jan3-2018' 
config.General.workArea = 'crabProjects/MC'
config.General.transferLogs = True
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runBTagAnalyzer_cfg.py'
config.JobType.pyCfgParams = ['defaults=Moriond18','runOnData=False','miniAOD=True', 'doBoostedCommissioning=True']

config.section_("Data")
config.Data.inputDataset = '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM'
config.Data.splitting = 'FileBased'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 1
config.Data.ignoreLocality = False
config.Data.publication = False
# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'QCD_Pt_470to600_MuEnriched_v1_Jan3-2018'
config.Data.outLFNDirBase = '/store/user/mrogulji/BoostedBTag/BTagNTuples/2017/9_4_9/'

config.section_("Site")
config.Site.storageSite = 'T3_HR_IRB'
