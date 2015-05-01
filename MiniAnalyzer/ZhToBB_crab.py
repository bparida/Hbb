from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'Zh_m125_PtZ-200'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ConfFile_cfg.py'
#config.JobType.outputFiles = ['output.root']
config.JobType.allowNonProductionCMSSW = True

config.section_("Data")
#config.Data.inputDataset = '/ZH_HToBB_ZToLL_M-125_13TeV_powheg-herwigpp/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM'
config.Data.inputDataset = '/Zh_m125_PtZ-200/jstupak-PHYS14_50_V2-MINIAODSIM-5aeef11518ff3267c48efc923ff0710e/USER'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publishDataName = 'Zh_m125_PtZ-200'
config.Data.outLFN = '/store/user/bparida/test_job/new/'
config.Data.ignoreLocality = True
config.General.transferLogs=True
config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
