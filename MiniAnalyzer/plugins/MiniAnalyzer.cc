// -*- C++ -*-
//
// Package:    Test/MiniAnalyzer
// Class:      MiniAnalyzer
// 
/**\class MiniAnalyzer MiniAnalyzer.cc Test/MiniAnalyzer/plugins/MiniAnalyzer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  bibhuti parida
//         Created:  Thu, 02 Apr 2015 20:55:24 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include <iostream>
using namespace std;
//
// class declaration
//

class MiniAnalyzer : public edm::EDAnalyzer {
	public:
		explicit MiniAnalyzer(const edm::ParameterSet&);
		~MiniAnalyzer();

		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	TH1D *h1;// = new TH1D("h1", "Mass", 100, 0., 200.);


	private:
		virtual void beginJob() override;
		virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
		virtual void endJob() override;

		//virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
		//virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
		//virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
		//virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

		// ----------member data ---------------------------



};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor

//
MiniAnalyzer::MiniAnalyzer(const edm::ParameterSet& iConfig)
{
	//now do what ever initialization is needed

	//edm::Service<TFileService> fs;   
	//histo = fs->make<TH1D>("tracks","Tracks",100,0,5000);


}
MiniAnalyzer::~MiniAnalyzer()
{

	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
MiniAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;
	edm::InputTag _packedCandidateSource, _prunedGenParticleSource, _packedGenParticleSource;

	edm::Handle< edm::View<reco::GenParticle> > prunedGenParticles;
	//iEvent.getByLabel(_prunedGenParticleSource, prunedGenParticles);
	edm::Handle< edm::View<reco::Candidate> > packedGenParticles;
	//iEvent.getByLabel(_packedGenParticleSource, packedGenParticles);




	//#ifdef THIS_IS_AN_EVENT_EXAMPLE
	edm::Handle< edm::View<reco::GenJet> > pIn;
	iEvent.getByLabel("slimmedGenJets",pIn);
	//##endif
	std::cout << pIn->size() << std::endl; 

	if(pIn->size()>0){
		for (auto input=pIn->begin(); input!=pIn->end(); ++input){
			//std::cout << input->pt() << std::endl;
			//std::cout << input->eta() << std::endl;
			//std::cout << input->phi() << std::endl;
		}

		if(pIn->size()>1){

		}

	}

	int jet1=0;
	int jet2=0;
	double max_sumpT=0;
	double sumpT=0;
	double Mass=0;
	double njets=pIn->size();
	for(unsigned int i=0; i < njets; i++){
		for (int j= i+1; j < njets; j++){
			std::cout << "i=" << i << ", j=" << j << std::endl; 
			//        pIn->at(i)->pt();
			//		  std::cout <<  pIn->at(i).pt() << std::endl;


sumpT=sqrt((pIn->at(i).px() + pIn->at(j).px())*(pIn->at(i).px() + pIn->at(j).px()) + (pIn->at(i).py() + pIn->at(j).py())*(pIn->at(i).py() + pIn->at(j).py())) ;

			if (sumpT > max_sumpT ){
				max_sumpT = sumpT;
				jet1 = i;
				jet2 = j;
			}
			std::cout << "sumpT=" << sumpT << ", max_sumpT=" << max_sumpT << std::endl;
		}
	}

	std:: cout << max_sumpT << std::endl;
	std:: cout << jet1 << std::endl;
	std:: cout << jet2 << std::endl;

	Mass=(pIn->at(jet1).p4() + pIn->at(jet2).p4()).M();
	std:: cout << "Mass="<< Mass << std::endl;


	//h1->Fill((pIn->at(jet1).p4() + pIn->at(jet2).p4()).M());
	h1->Fill(Mass);





	//#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
	//   ESHandle<SetupData> pSetup;
	//   iSetup.get<SetupRecord>().get(pSetup);
	//#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
MiniAnalyzer::beginJob()
{

	h1 = new TH1D("h1", "Mass", 100, 0., 200.);
	cout<<"Start a new Job! haha";

}

// ------------ method called once each job just after ending the event loop  ------------
void 
MiniAnalyzer::endJob() 
{
	TFile *myfile = new TFile("output.root", "RECREATE");
	h1->Write();
	myfile->Close();
	delete myfile;
	delete h1;
	cout<<"End a new Job! ha";
}

// ------------ method called when starting to processes a run  ------------
/*
   void 
   MiniAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
   {
   }
   */

// ------------ method called when ending the processing of a run  ------------
/*
   void 
   MiniAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
   {
   }
   */

// ------------ method called when starting to processes a luminosity block  ------------
/*
   void 
   MiniAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
   {
   }
   */
// ------------ method called when ending the processing of a luminosity block  ------------
/*
   void 
   MiniAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
   {
   }
   */

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MiniAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MiniAnalyzer);
