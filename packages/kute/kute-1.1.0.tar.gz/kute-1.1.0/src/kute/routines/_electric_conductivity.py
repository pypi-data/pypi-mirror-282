# Copyright (c) 2024 The KUTE contributors
import argparse
import numpy as np
import MDAnalysis as mda

from ._ascii_logo import print_logo
from kute import GreenKuboIntegral, IntegralEnsemble
from kute.loaders import load_electric_current
from kute.analysis import ElectricCurrent


def run_one_analysis(top, traj, filename, verbose=True):

    u = mda.Universe(top, traj)
    analysis = ElectricCurrent(universe=u, filename=filename)
    analysis.run(verbose=verbose)

def calculation_for_one(name, splits, weight=None):
    
    if weight is not None:
        weight = np.loadtxt(weight)
    else:
        weight = 1

    t, Jx, Jy, Jz = load_electric_current(name, splits)
    integral = GreenKuboIntegral(t, Jx, Jy, Jz)
    tavg, avg, u_avg = integral.get_isotropic_running_average()

    avg *= weight
    u_avg *= weight

    return tavg, avg, u_avg

def calculation_for_ensemble(names, splits, weights=None):

    if weights is not None:
        weights = np.loadtxt(weights)

    integrals = []
    for name in names:
        t, Jx, Jy, Jz = load_electric_current(name, splits)
        integrals.append(GreenKuboIntegral(t, Jx, Jy, Jz))
    
    ensemble = IntegralEnsemble(integrals, factors=weights)
    return ensemble.get_isotropic_average()

def save_results(out_file, tavg, avg, uavg):

    to_save = np.vstack([tavg, avg, uavg]).T
    np.savetxt(out_file, to_save, header="Time       Average         Uncertainty")


def main():

    description = 'Calculates the isotropic electric conductivity as a function of averaging cutoff'

    parser = argparse.ArgumentParser(description=description)

    ## Input arguments

    parser.add_argument("-f", required=False, type=str, dest="h5_files", metavar="current.h5", nargs="+", default=None,
                        help = ("List of h5 binary files containing the electric current for each replica."))

    
    parser.add_argument("--traj", required=False, type=str, dest="traj_files", metavar="traj.trr, traj.xtc", nargs="+",
                        help = ("List of trajectory files used to calculate the electric current. Note that they must contain velocities"))


    parser.add_argument("--topo", required=False, type=str, dest="topo_files", metavar="traj.tpr, data.lmp", nargs="+",
                        help = ("List of topology files used to calculate the electric current. They must contain charge, mass and residue information"))


    ## Calculation arguments

    parser.add_argument("--splits", required=False, type=int, dest="splits", metavar="slipts", default=1,
                        help = ("Number of fragments of equal size into which to split the electric current of each replica"))

    parser.add_argument("--weights", required=False, type=str, default=None, metavar="weights.dat", dest="weights", 
                        help=("File containing the weighting factor for each replica. Can be used to change units or to include replica-dependent values such as the volume."))

    ## Output arguments

    parser.add_argument("-o", required=False, type=str, dest="out_file", metavar="conductivity.dat", default="conductivity.dat",
                        help = ("Name of the output file"))
    

    args = parser.parse_args()
    print_logo()

    ### Check if h5 file was given. If not, carry out the calcultions from the trajectories

    if args.h5_files is None:
        
        print("Didn't specify an h5 file. Falling back to current calculation from MD trajectories")
        for i, (top, traj) in enumerate(zip(args.topo_files, args.traj_files)):
            run_one_analysis(top, traj, f"current_from_traj_replica_{i+1}.h5")

        names = [ f"current_from_traj_replica_{i+1}.h5" for i in range(len(args.topo_files)) ]
    else:
        names = args.h5_files


    ### Carry out the Green-Kubo calculations


    if len(names) == 1:
        tavg, avg, uavg = calculation_for_one(names[0], args.splits, args.weights)
    
    else:
        tavg, avg, uavg = calculation_for_ensemble(names, args.splits, args.weights)

    ## Save the results

    save_results(args.out_file, tavg, avg, uavg)


if __name__ == 'main':
    main()