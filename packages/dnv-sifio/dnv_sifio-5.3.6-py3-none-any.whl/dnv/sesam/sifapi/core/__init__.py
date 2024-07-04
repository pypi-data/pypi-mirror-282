import sys

from dnv.net.runtime import enable_with_for_module
from dnv.sesam.sifapi import add_reference

package = "DNV.Sesam.SifApi.Core"
add_reference(package)

from DNV.Sesam.SifApi.Core import *
enable_with_for_module(sys.modules[package])