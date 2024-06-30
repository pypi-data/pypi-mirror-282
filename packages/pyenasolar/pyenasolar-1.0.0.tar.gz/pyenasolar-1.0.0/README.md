# pyenasolar

This library was created to communicate with EnaSolar solar inverters within Home Assistant.
It is based on the pysma and pysaj components written by @kellerza and @fredericvl

Data regarding the capabilities and serial number are extracted by applying regular expressions
to the javascript in the header of the root and Settings.html web pages.

It was established that requesting the metrics at the same rate as the website i.e. every 1
second for a extended period of time (several hours) resulted in the site denying further requests.
A polling frequency of approx every minute seems to be stable and provides sufficiently
granular data to enable Home Assistant to plot decent graphs.

If the website becomes unresponsive, the only cure found was to reset the inverter by turning
the AC switch off and on again.

