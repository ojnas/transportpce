import os
import subprocess

def start_xpdra_honeynode():
    executable = ("./honeynode/2.2.1/honeynode-distribution/target/honeynode-distribution-1.18.01-hc"
                  "/honeynode-distribution-1.18.01/honeycomb-tpce")
    if os.path.isfile(executable):
        with open('honeynode1.log', 'w') as outfile:
            return subprocess.Popen(
                [executable, "17840", "sample_configs/openroadm/2.2.1/oper-XPDRA.xml"],
                stdout=outfile)

def start_roadma_honeynode():
    executable = ("./honeynode/2.2.1/honeynode-distribution/target/honeynode-distribution-1.18.01-hc"
                  "/honeynode-distribution-1.18.01/honeycomb-tpce")
    if os.path.isfile(executable):
        with open('honeynode2.log', 'w') as outfile:
            return subprocess.Popen(
                [executable, "17841", "sample_configs/openroadm/2.2.1/oper-ROADMA.xml"],
                stdout=outfile)

def start_roadmb_honeynode():
    executable = ("./honeynode/2.2.1/honeynode-distribution/target/honeynode-distribution-1.18.01-hc"
                  "/honeynode-distribution-1.18.01/honeycomb-tpce")
    if os.path.isfile(executable):
        with open('honeynode5.log', 'w') as outfile:
            return subprocess.Popen(
                [executable, "17842", "sample_configs/openroadm/2.2.1/oper-ROADMB.xml"],
                stdout=outfile)

def start_roadmc_honeynode():
    executable = ("./honeynode/2.2.1/honeynode-distribution/target/honeynode-distribution-1.18.01-hc"
                  "/honeynode-distribution-1.18.01/honeycomb-tpce")
    if os.path.isfile(executable):
        with open('honeynode3.log', 'w') as outfile:
            return subprocess.Popen(
                [executable, "17843", "sample_configs/openroadm/2.2.1/oper-ROADMC.xml"],
                stdout=outfile)

def start_xpdrc_honeynode():
    executable = ("./honeynode/2.2.1/honeynode-distribution/target/honeynode-distribution-1.18.01-hc"
                  "/honeynode-distribution-1.18.01/honeycomb-tpce")
    if os.path.isfile(executable):
        with open('honeynode4.log', 'w') as outfile:
            return subprocess.Popen(
                [executable, "17844", "sample_configs/openroadm/2.2.1/oper-XPDRC.xml"],
                stdout=outfile)

def start_tpce():
    if "USE_LIGHTY" in os.environ and os.environ['USE_LIGHTY'] == 'True':
        print ("starting LIGHTY.IO TransportPCE build...")
        executable = "../lighty/target/lighty-transportpce-12.0.0-SNAPSHOT/clean-start-controller.sh"
        with open('odl.log', 'w') as outfile:
            return subprocess.Popen(
                ["bash", executable], stdout=outfile,
                stdin=open(os.devnull))
    else:
        print ("starting KARAF TransportPCE build...")
        executable = "../karaf/target/assembly/bin/karaf"
        with open('odl.log', 'w') as outfile:
            return subprocess.Popen(
                ["bash", executable, "server"], stdout=outfile,
                stdin=open(os.devnull))
