#!/usr/bin/env python
import sys
import ROOT, math
from ROOT import TLorentzVector
import array
import random as rnd

m_kl = 0.497611
m_pi = 0.13957039

# _______________________________________________________________________________
""" sensor class for easier manipulation """


class Detector:
    def __init__(self, cfg):
        self.cfg = cfg

    def reco_event(self, gen_charged, gen_photons, gen_neutralhadrons, debug=False):
        event = {
            "tracks": [],
            "photons": [],
            "neutral_hadrons": [],
        }
        if debug:
            print("---- new reco event ----")
            print("")

        """ process tracks """
        for trk in gen_charged:
            if debug:
                print(
                    "    gen track: , St: ",
                    trk.Status,
                    ", PID: ",
                    trk.PID,
                    ", PT: ",
                    trk.PT,
                    ", Eta: ",
                    trk.Eta,
                    ", Phi: ",
                    trk.Phi,
                    ", M: ",
                    trk.Mass,
                )
            # apply p/e , eta efficiencies first
            pt = trk.PT
            eta = trk.Eta
            phi = trk.Phi
            # mass = trk.Mass
            mass = m_pi

            # track pt rel resolution
            pt_res = pt * math.sqrt(
                self.cfg["tracker"]["pt_res"][0] ** 2
                + pt * self.cfg["tracker"]["pt_res"][1] ** 2
                + pt ** 2 * self.cfg["tracker"]["pt_res"][2] ** 2
            )

            angle_res = self.cfg["tracker"]["angular_res"]

            reco_pt = rnd.gauss(pt, pt_res)

            if reco_pt < 0:
                continue

            reco_eta = rnd.gauss(eta, angle_res)
            reco_phi = rnd.gauss(phi, angle_res)
            reco_mass = mass

            reco_p4 = TLorentzVector()
            reco_p4.SetPtEtaPhiM(reco_pt, reco_eta, reco_phi, reco_mass)

            if debug:
                print(
                    "    reco track: PT: ",
                    reco_p4.Pt(),
                    ", Eta: ",
                    reco_p4.Eta(),
                    ", Phi: ",
                    reco_p4.Phi(),
                    ", M: ",
                    reco_p4.M(),
                )

            if reco_pt < self.cfg["tracker"]["eff"][0]:
                continue
            if abs(eta) > self.cfg["tracker"]["eff"][1]:
                continue

            # create output collection
            event["tracks"].append(reco_p4)

        """ process photons """
        for gamma in gen_photons:

            if debug:
                print(
                    "    gen gamma : , St: ",
                    gamma.Status,
                    ", PID: ",
                    gamma.PID,
                    ", E: ",
                    gamma.E,
                    ", Eta: ",
                    gamma.Eta,
                    ", Phi: ",
                    gamma.Phi,
                    ", M: ",
                    gamma.Mass,
                )
            # apply p/e , eta efficiencies first
            e = gamma.E
            pt = gamma.PT
            p = gamma.P4().P()
            eta = gamma.Eta
            phi = gamma.Phi
            mass = 0.0

            # track pt rel resolution
            e_res = e * math.sqrt(
                self.cfg["ecal"]["energy_res"][0] ** 2 / e ** 2
                + self.cfg["ecal"]["energy_res"][1] ** 2 / e
                + self.cfg["ecal"]["energy_res"][2] ** 2
            )

            angle_res = self.cfg["ecal"]["angular_res"]

            reco_e = rnd.gauss(e, e_res)

            if reco_e < mass:
                continue

            scale = math.sqrt(reco_e ** 2 - mass ** 2) / p
            reco_pt = scale * pt
            reco_eta = rnd.gauss(eta, angle_res)
            reco_phi = rnd.gauss(phi, angle_res)
            reco_mass = mass

            reco_p4 = TLorentzVector()
            reco_p4.SetPtEtaPhiM(reco_pt, reco_eta, reco_phi, reco_mass)

            if debug:
                print(
                    "    reco gamma : E: ",
                    reco_p4.E(),
                    ", Eta: ",
                    reco_p4.Eta(),
                    ", Phi: ",
                    reco_p4.Phi(),
                    ", M: ",
                    reco_p4.M(),
                )

            if reco_e < self.cfg["ecal"]["eff"][0]:
                continue
            if abs(eta) > self.cfg["ecal"]["eff"][1]:
                continue

            # create output collection
            event["photons"].append(reco_p4)

        """ process neutral hadrons """
        for neutralhad in gen_neutralhadrons:

            if debug:
                print(
                    "    gen neutral had : , St: ",
                    neutralhad.Status,
                    ", PID: ",
                    neutralhad.PID,
                    ", E: ",
                    neutralhad.E,
                    ", Eta: ",
                    neutralhad.Eta,
                    ", Phi: ",
                    neutralhad.Phi,
                    ", M: ",
                    neutralhad.Mass,
                )
            # apply p/e , eta efficiencies first
            e = neutralhad.E
            pt = neutralhad.PT
            p = neutralhad.P4().P()
            eta = neutralhad.Eta
            phi = neutralhad.Phi
            # mass = neutralhad.Mass
            mass = m_kl

            # track pt rel resolution
            e_res = e * math.sqrt(
                self.cfg["hcal"]["energy_res"][0] ** 2 / e ** 2
                + self.cfg["hcal"]["energy_res"][1] ** 2 / e
                + self.cfg["hcal"]["energy_res"][2] ** 2
            )

            angle_res = self.cfg["hcal"]["angular_res"]

            reco_e = rnd.gauss(e, e_res)

            if reco_e < mass:
                continue

            scale = math.sqrt(reco_e ** 2 - mass ** 2) / p
            reco_pt = scale * pt
            reco_eta = rnd.gauss(eta, angle_res)
            reco_phi = rnd.gauss(phi, angle_res)
            reco_mass = mass

            reco_p4 = TLorentzVector()
            reco_p4.SetPtEtaPhiM(reco_pt, reco_eta, reco_phi, reco_mass)

            if debug:
                print(
                    "    reco neutralhad : E: ",
                    reco_p4.E(),
                    ", Eta: ",
                    reco_p4.Eta(),
                    ", Phi: ",
                    reco_p4.Phi(),
                    ", M: ",
                    reco_p4.M(),
                )

            if reco_e < self.cfg["hcal"]["eff"][0]:
                continue
            if abs(eta) > self.cfg["hcal"]["eff"][1]:
                continue

            # create output collection
            event["neutral_hadrons"].append(reco_p4)

        return (
            event["tracks"],
            event["photons"],
            event["neutral_hadrons"],
        )
