from configuration import *
from detector import *
from utils import *
import numpy as np
import copy
from collections import OrderedDict

eh0 = 135.22864168829545
mh0 = 125.0

# ______________________________________________________________________________
if len(sys.argv) < 2:
    print(" Usage: Example1.py input_file")
    sys.exit(1)

ROOT.gSystem.Load("libDelphes")

try:
    ROOT.gInterpreter.Declare('#include "classes/DelphesClasses.h"')
    ROOT.gInterpreter.Declare('#include "external/ExRootAnalysis/ExRootTreeReader.h"')
except:
    pass

# ______________________________________________________________________________

nev_debug = 1000
debug = False
debug2 = False

inputFile = sys.argv[1]
outputFile = sys.argv[2]

# Create chain of root trees
chain = ROOT.TChain("Delphes")
chain.Add(inputFile)

# Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

# Get pointers to branches used in this analysis
branchParticle = treeReader.UseBranch("Particle")

# import detector configs
idea_base = Detector(cfg_idea)

detectors = OrderedDict()
histograms = OrderedDict()


def calc_prof_params(binsize, xmin, xmax):
    nbins = float(xmax - xmin) / binsize
    hist_nbins = int(nbins + 1)
    float(xmax - xmin) / nbins
    hist_xmin = xmin - 0.5 * binsize
    hist_xmax = xmax + 0.5 * binsize
    cut_array = np.arange(xmin, xmax + binsize, binsize, dtype=int).astype(np.float)
    return hist_nbins, hist_xmin, hist_xmax, cut_array


# in MeV have to convert in GeV
p_binsize = 10
p_min = 0
p_max = 1000

p_params = calc_prof_params(p_binsize, p_min, p_max)
p_hist_nbins = p_params[0]
p_hist_xmin = p_params[1]
p_hist_xmax = p_params[2]
p_cuts = p_params[3]


# divide by 10
theta_binsize = 1
theta_min = 1
theta_max = 30
theta_params = calc_prof_params(theta_binsize, theta_min, theta_max)
theta_hist_nbins = theta_params[0]
theta_hist_xmin = theta_params[1]
theta_hist_xmax = theta_params[2]
theta_cuts = theta_params[3]

eta_cuts = theta_to_eta(theta_cuts)


# mass plots
mass_binsize = 0.001
mass_min = 0
mass_max = 2
mass_nbins = int(float(mass_max - mass_min) / mass_binsize)

# evis plots
evis_binsize = 0.001
evis_min = 0
evis_max = 2
evis_nbins = int(float(evis_max - evis_min) / evis_binsize)

""" cumulative plots """
for collname in ["gentracks", "genphotons", "gennhadrons"]:

    hname_p = "hp_{}".format(collname)

    hname_nleftp = "hnleftp_{}".format(collname)
    hname_nlefttheta = "hnlefttheta_{}".format(collname)
    hname_eleftp = "heleftp_{}".format(collname)
    hname_elefttheta = "helefttheta_{}".format(collname)

    hname_fracp = "hfracp_{}".format(collname)
    hname_fractheta = "hfractheta_{}".format(collname)

    histograms[hname_p] = ROOT.TH1F(
        hname_p,
        hname_p,
        200,
        0,
        10,
    )

    histograms[hname_nlefttheta] = ROOT.TProfile(
        hname_nlefttheta,
        hname_nlefttheta,
        theta_hist_nbins,
        theta_hist_xmin,
        theta_hist_xmax,
    )
    histograms[hname_nleftp] = ROOT.TProfile(
        hname_nleftp,
        hname_nleftp,
        p_hist_nbins,
        0.001 * p_hist_xmin,
        0.001 * p_hist_xmax,
    )
    histograms[hname_elefttheta] = ROOT.TProfile(
        hname_elefttheta,
        hname_elefttheta,
        theta_hist_nbins,
        theta_hist_xmin,
        theta_hist_xmax,
    )
    histograms[hname_eleftp] = ROOT.TProfile(
        hname_eleftp,
        hname_eleftp,
        p_hist_nbins,
        0.001 * p_hist_xmin,
        0.001 * p_hist_xmax,
    )

    histograms[hname_fractheta] = ROOT.TProfile(
        hname_fractheta,
        hname_fractheta,
        theta_hist_nbins,
        theta_hist_xmin,
        theta_hist_xmax,
    )
    histograms[hname_fracp] = ROOT.TProfile(
        hname_fracp, hname_fracp, p_hist_nbins, 0.001 * p_hist_xmin, 0.001 * p_hist_xmax
    )

for subdet in ["tracker", "ecal", "hcal"]:
    hname_mass = "hmass_{}_idea".format(subdet)
    hname_evis = "hevis_{}_idea".format(subdet)

    histograms[hname_mass] = ROOT.TH1F(hname_mass, hname_mass, 200, 50, 150)
    histograms[hname_evis] = ROOT.TH1F(hname_evis, hname_evis, 200, 50, 150)

""" p min plots """
for pcut in p_cuts:
    detname = "perfect_pcut_{}".format(pcut)
    cfg_det = copy.deepcopy(cfg_perfect)
    cfg_det["name"] = detname

    for subdet in ["tracker", "ecal", "hcal"]:
        hname_mass = "hmass_{}_{}".format(subdet, detname)
        hname_evis = "hevis_{}_{}".format(subdet, detname)

        cfg_det[subdet]["eff"] = (0.001 * float(pcut), cfg_det[subdet]["eff"][1])
        histograms[hname_mass] = ROOT.TH1F(
            hname_mass, hname_mass, mass_nbins, mass_min, mass_max
        )
        histograms[hname_evis] = ROOT.TH1F(
            hname_evis, hname_evis, evis_nbins, evis_min, evis_max
        )

    detectors[detname] = Detector(cfg_det)


""" theta plots """
for thetacut in theta_cuts:
    detname = "perfect_thetacut_{}".format(thetacut)
    cfg_det = copy.deepcopy(cfg_perfect)
    cfg_det["name"] = detname

    for subdet in ["tracker", "ecal", "hcal"]:
        hname_mass = "hmass_{}_{}".format(subdet, detname)
        hname_evis = "hevis_{}_{}".format(subdet, detname)

        cfg_det[subdet]["eff"] = (cfg_det[subdet]["eff"][0], theta_to_eta(thetacut))
        histograms[hname_mass] = ROOT.TH1F(
            hname_mass, hname_mass, mass_nbins, mass_min, mass_max
        )
        histograms[hname_evis] = ROOT.TH1F(
            hname_evis, hname_evis, evis_nbins, evis_min, evis_max
        )

    detectors[detname] = Detector(cfg_det)


if debug:
    numberOfEntries = nev_debug

# Loop over all events
for entry in range(0, numberOfEntries):
    # Load selected branches with data from specified event
    treeReader.ReadEntry(entry)

    # DEFINE COLLECTIONHS HERE
    genall = []
    gentracks = []
    genphotons = []
    gennhadrons = []

    h_stable_daughters = []
    h_unstable_daughters = []

    if (entry + 1) % 100 == 0:
        print(" ... processed {} events ...".format(entry + 1))

    if debug2:
        print_genparticles(branchParticle)

    """ prepare gen input collections """
    # find_genpfcols(branchParticle, genall, gentracks, genphotons, gennhadrons)

    """ find higgs gen particle """
    higgs = find_particle(branchParticle, 25, 22)
    find_daughters(higgs, branchParticle, h_unstable_daughters, h_stable_daughters)

    # print_genparticles(h_stable_daughters)

    """ prepare gen input collections """
    # find_genpfcols(branchParticle, genall, gentracks, genphotons, gennhadrons)
    find_genpfcols(h_stable_daughters, genall, gentracks, genphotons, gennhadrons)

    for collname in ["gentracks", "genphotons", "gennhadrons"]:

        hname_nleftp = "hnleftp_{}".format(collname)
        hname_nlefttheta = "hnlefttheta_{}".format(collname)
        hname_eleftp = "heleftp_{}".format(collname)
        hname_elefttheta = "helefttheta_{}".format(collname)
        hname_fracp = "hfracp_{}".format(collname)
        hname_fractheta = "hfractheta_{}".format(collname)
        hname_p = "hp_{}".format(collname)

        fill_p_hist(globals()[collname], histograms[hname_p])

        """
        fill_nleft_hist_p(globals()[collname], p_cuts, histograms[hname_nleftp])
        fill_nleft_hist_theta(
            globals()[collname], eta_cuts, histograms[hname_nlefttheta]
        )
        fill_eleft_hist_p(globals()[collname], p_cuts, histograms[hname_eleftp])
        fill_eleft_hist_theta(
            globals()[collname], eta_cuts, histograms[hname_elefttheta]
        )
        fill_frac_hist_p(globals()[collname], genall, p_cuts, histograms[hname_fracp])
        fill_frac_hist_theta(
            globals()[collname], genall, eta_cuts, histograms[hname_fractheta]
        )
        """
    """ now perform reconstruction """

    reco_coll = idea_base.reco_event(gentracks, genphotons, gennhadrons)
    tracks, photons, nhadrons = reco_coll
    tracks_and_photons = tracks + photons
    all = tracks_and_photons + nhadrons

    fill_mass_hist(tracks, histograms["hmass_tracker_idea"])
    fill_mass_hist(tracks_and_photons, histograms["hmass_ecal_idea"])
    fill_mass_hist(all, histograms["hmass_hcal_idea"])

    fill_evis_hist(tracks, histograms["hevis_tracker_idea"])
    fill_evis_hist(tracks_and_photons, histograms["hevis_ecal_idea"])
    fill_evis_hist(all, histograms["hevis_hcal_idea"])

    """
    for detname, det in detectors.items():
        reco_coll = det.reco_event(gentracks, genphotons, gennhadrons)
        tracks, photons, nhadrons = reco_coll
        tracks_and_photons = tracks + photons
        all = tracks_and_photons + nhadrons

        hname_mass_tracker = "hmass_tracker_{}".format(detname)
        hname_mass_ecal = "hmass_ecal_{}".format(detname)
        hname_mass_hcal = "hmass_hcal_{}".format(detname)

        hname_evis_tracker = "hevis_tracker_{}".format(detname)
        hname_evis_ecal = "hevis_ecal_{}".format(detname)
        hname_evis_hcal = "hevis_hcal_{}".format(detname)


        fill_mass_hist(tracks, histograms[hname_mass_tracker], mh0)
        fill_mass_hist(tracks_and_photons, histograms[hname_mass_ecal], mh0)
        fill_mass_hist(all, histograms[hname_mass_hcal], mh0)

        fill_evis_hist(tracks, histograms[hname_evis_tracker], eh0)
        fill_evis_hist(tracks_and_photons, histograms[hname_evis_ecal], eh0)
        fill_evis_hist(all, histograms[hname_evis_hcal], eh0)
   """

# Show resulting histograms
out_root = ROOT.TFile(outputFile, "RECREATE")

for name, hist in histograms.items():
    hist.Write()
