from WMCore.Configuration import Configuration
config = Configuration()

# from CRABClient.UserUtilities import config, getUsernameFromSiteDB                                                   
# config = config()                                                                                                    

config.section_("General")
config.General.transferOutputs = True
config.General.requestName = 'BTagMu_Run2017B-17Nov2017-v1_MINIAOD'
#config.General.requestName = 'my_CRAB_project_directory'                                                             
config.General.workArea = 'crabProjects/data'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runBTagAnalyzer_cfg.py'
config.JobType.pyCfgParams = ['defaults=Moriond18','runOnData=True', 'miniAOD=True', 'doBoostedCommissioning=True']

config.section_("Data")
config.Data.inputDataset = '/BTagMu/Run2017B-17Nov2017-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
#config.Data.totalUnits = 1                                                                                           
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'
#config.Data.runRange = ''                                                             
#config.Data.outLFNDirBase = '/store/user/%s/HbbTagVal/Validation' % (getUsernameFromSiteDB())                        
config.Data.outLFNDirBase = '/store/user/mrogulji/BoostedBTag/BTagNTuples/2017/9_4_9/'
config.Data.publication = False
config.Data.outputDatasetTag = 'BTagMu_Run2017B-17Nov2017-v1_MINIAOD'

config.section_("Site")
config.Site.storageSite = 'T3_HR_IRB'


