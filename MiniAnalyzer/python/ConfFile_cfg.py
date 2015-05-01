import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('Demo')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
        limit = cms.untracked.int32(-1)
        )
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

from RecoJets.JetProducers.GenJetParameters_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *

ak4GenJets = cms.EDProducer(
        "FastjetJetProducer",
        GenJetParameters,
        AnomalousCellParameters,
        jetAlgorithm = cms.string("AntiKt"),
        rParam       = cms.double(0.4)
        )


process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_15.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_10.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_100.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_101.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_102.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_103.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_104.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_105.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_106.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_107.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_108.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_109.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_110.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_111.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_112.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_113.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_114.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_115.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_116.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_117.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_118.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_119.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_120.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_121.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_122.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_123.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_124.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_125.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_126.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_127.root',
       # 'file:/eos/uscms/store/user/bparida/MINIAODSIM/CRAB_PrivateMC/Zh_pT200_MINIAODSIM/150207_232518/0000/step5_128.root'
       # 'file:/store/mc/Phys14DR/ZH_HToBB_ZToLL_M-125_13TeV_powheg-herwigpp/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/EEC4691D-D398-E411-8060-00266CFFC7CC.root'

        
    )
)

process.demo = cms.EDAnalyzer('MiniAnalyzer',
        slimmedGenJets=cms.untracked.uint32(0)
)
process.TFileService = cms.Service("TFileService",
        fileName = cms.string('output.root')
        )
#process.out = cms.OutputModule("PoolOutputModule",
#        fileName = cms.untracked.string('Hbb.root'),
#        outputCommands = cms.untracked.vstring(['keep *_MiniAnalyzer_*_*',
#             ])
#        )

 



process.p = cms.Path(process.demo)
