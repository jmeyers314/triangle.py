#!/usr/bin/env python

import numpy as np
import triangle

# Generate a fake correlation matrix.

# Variances between 0 and 1
xx = np.random.rand(1)
yy = np.random.rand(1)
zz = np.random.rand(1)
# Correlation coefficients between -1 and 1
rhoxy = np.random.rand(1)*2.0 - 1.0
rhoyz = np.random.rand(1)*2.0 - 1.0
rhoxz = np.random.rand(1)*2.0 - 1.0
# Implied covariances
xy = rhoxy * np.sqrt(xx*yy)
yz = rhoyz * np.sqrt(yy*zz)
xz = rhoxz * np.sqrt(xx*zz)

cov = np.zeros((3,3))
cov[0,0] = xx
cov[1,1] = yy
cov[2,2] = zz
cov[0,1] = cov[1,0] = xy
cov[1,2] = cov[2,1] = yz
cov[0,2] = cov[2,0] = xz

# Plot it.
# figure = triangle.corner(cov=cov, mu=mu, labels=[r"$x$", r"$y$", r"$\log \alpha$",
#                                                  r"$\Gamma \, [\mathrm{parsec}]$"])
figure = triangle.corner(cov=cov, mu=[0]*3, labels=[r"V1", r"V2", r"V3"])
#figure.gca().annotate("A Title", xy=(0.5, 1.0), xycoords="figure fraction",
#                      xytext=(0, -5), textcoords="offset points",
#                      ha="center", va="top")
figure.savefig("demo2.png")
