# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_mcafee_opendxl"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     mcafee_dxl_payload
    #     mcafee_publish_method
    #     mcafee_topic_name
    #     mcafee_wait_for_response
    #   Message Destinations:
    #     mcafee_dxl_message_destination
    #   Functions:
    #     mcafee_publish_to_dxl
    #   Workflows:
    #     example_mcafee_publish_to_dxl_set_tie_reputation
    #     example_mcafee_publish_to_dxl_tag_system
    #   Rules:
    #     (Example) McAfee Publish to DXL (Set TIE Reputation Known Malicious)
    #     (Example) McAfee Publish to DXL (Tag System Shut Down)


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJwcm9ncmFtbWF0aWNfbmFtZSI6ICJl
eGFtcGxlX21jYWZlZV9wdWJsaXNoX3RvX2R4bF90YWdfc3lzdGVtIiwgIm9iamVjdF90eXBlIjog
ImluY2lkZW50IiwgImV4cG9ydF9rZXkiOiAiZXhhbXBsZV9tY2FmZWVfcHVibGlzaF90b19keGxf
dGFnX3N5c3RlbSIsICJ1dWlkIjogIjI1MjJlNTllLTM1NjUtNGI4Mi05MjA0LWNmMzY2ZDA0NjM3
YyIsICJsYXN0X21vZGlmaWVkX2J5IjogImJ3YWxzaEByZXNpbGllbnRzeXN0ZW1zLmNvbSIsICJu
YW1lIjogIihFeGFtcGxlKSBNY0FmZWUgUHVibGlzaCB0byBEWEwgKFRhZyBTeXN0ZW0pIiwgImNv
bnRlbnQiOiB7InhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwi
Pz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAw
NTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8y
MDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAx
MDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAw
NTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5c
IiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhz
aT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFt
ZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJleGFt
cGxlX21jYWZlZV9wdWJsaXNoX3RvX2R4bF90YWdfc3lzdGVtXCIgaXNFeGVjdXRhYmxlPVwidHJ1
ZVwiIG5hbWU9XCIoRXhhbXBsZSkgTWNBZmVlIFB1Ymxpc2ggdG8gRFhMIChUYWcgU3lzdGVtKVwi
Pjxkb2N1bWVudGF0aW9uPldvcmtmbG93IHRvIHRyaWdnZXIgdGhlIE1jQWZlZSBQdWJsaXNoIHRv
IERYTCBmdW5jdGlvbiBhbmQgc2V0IGEgc3lzdGVtIHRhZy48L2RvY3VtZW50YXRpb24+PHN0YXJ0
RXZlbnQgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzBv
aXN3aWU8L291dGdvaW5nPjwvc3RhcnRFdmVudD48c2VydmljZVRhc2sgaWQ9XCJTZXJ2aWNlVGFz
a18wMHdlaW9xXCIgbmFtZT1cIk1jQWZlZSBQdWJsaXNoIHRvIERYTFwiIHJlc2lsaWVudDp0eXBl
PVwiZnVuY3Rpb25cIj48ZXh0ZW5zaW9uRWxlbWVudHM+PHJlc2lsaWVudDpmdW5jdGlvbiB1dWlk
PVwiZjk4N2VkMjItMjdkNC00MzgzLTlhYTQtODFlMzk5OWVkZTI1XCI+e1wiaW5wdXRzXCI6e1wi
N2U1NjkwNTItYjc4Ni00OTMzLTlkODctZWFiNTcyODA2MjRmXCI6e1wiaW5wdXRfdHlwZVwiOlwi
c3RhdGljXCIsXCJzdGF0aWNfaW5wdXRcIjp7XCJtdWx0aXNlbGVjdF92YWx1ZVwiOltdLFwidGV4
dF92YWx1ZVwiOlwiL21jYWZlZS9zZXJ2aWNlL2Vwby9yZW1vdGUvZXBvMVwifX0sXCI4NWUwNzEx
ZS1jNTczLTQwNWEtYjU5MC00N2FlMDRiYTY3ZGNcIjp7XCJpbnB1dF90eXBlXCI6XCJzdGF0aWNc
IixcInN0YXRpY19pbnB1dFwiOntcIm11bHRpc2VsZWN0X3ZhbHVlXCI6W10sXCJ0ZXh0X3ZhbHVl
XCI6XCJ7XFxcImNvbW1hbmRcXFwiOiBcXFwic3lzdGVtLmFwcGx5VGFnXFxcIiwgXFxcIm91dHB1
dFxcXCI6IFxcXCJqc29uXFxcIiwgXFxcInBhcmFtc1xcXCI6IHtcXFwibmFtZXNcXFwiOiBcXFwi
MTAuMC4yLjE1XFxcIiwgXFxcInRhZ05hbWVcXFwiOiBcXFwiU2h1dCBEb3duXFxcIn19XCJ9fSxc
IjNlNDRjNTFiLTIyYTgtNDM1MC05MDZkLTZhZTAzOGJiNjc3OVwiOntcImlucHV0X3R5cGVcIjpc
InN0YXRpY1wiLFwic3RhdGljX2lucHV0XCI6e1wibXVsdGlzZWxlY3RfdmFsdWVcIjpbXSxcInNl
bGVjdF92YWx1ZVwiOlwiY2ZjZGJmN2UtMTc2NS00Yjg3LWIxNjQtNDZjMGM3Mjk3ZTVhXCJ9fSxc
ImRiZWVkMzZhLTIzYmYtNDE4OS05ZjViLWI1M2VlNTRlY2RjM1wiOntcImlucHV0X3R5cGVcIjpc
InN0YXRpY1wiLFwic3RhdGljX2lucHV0XCI6e1wibXVsdGlzZWxlY3RfdmFsdWVcIjpbXSxcInNl
bGVjdF92YWx1ZVwiOlwiYjQ1ZmM4MzQtN2NhYi00OGJjLTg0MzctYjIxNGVjZTQ3Njc4XCJ9fX0s
XCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJcXFwiXFxcIlxcXCJcXG5SZXNwb25zZSByZXR1
cm5lZCBwcm92aWRlcyB0aGUgaW5wdXQgdmFsdWVzIGluIHRoZSBmb2xsb3dpbmcgZm9ybWF0XFxu
e1xcbiAgXFxcIm1jYWZlZV90b3BpY19uYW1lXFxcIjogXFxcIiZsdDt0b3BpY19uYW1lJmd0O1xc
XCIsXFxuICBcXFwibWNhZmVlX2R4bF9wYXlsb2FkXFxcIjogXFxcIiZsdDtwYXlsb2FkJmd0O1xc
XCIsXFxuICBcXFwibWNhZmVlX3B1Ymxpc2hfbWV0aG9kXFxcIjogXFxcIiZsdDttZXRob2QmZ3Q7
XFxcIixcXG4gIFxcXCJtY2FmZWVfd2FpdF9mb3JfcmVzcG9uc2VcXFwiOiBcXFwiJmx0O3dhaXQg
Zm9yIHJlc3BvbnNlJmd0O1xcXCJcXG4gIFxcXCJyZXNwb25zZVxcXCI6IFxcXCImbHQ7cG9zc2li
bGUgcmVzcG9uc2UgcmV0dXJuZWQmZ3Q7XFxuXFxcIlxcXCJcXFwiXFxuXFxuXFxuXFxudGV4dCA9
IFxcXCJcXFwiXFxcIlRoZSBmb2xsb3dpbmcgd2FzIHB1Ymxpc2hlZCB0byBEWExcXG4mbHQ7YiZn
dDtQYXlsb2FkOiZsdDsvYiZndDsge31cXG4mbHQ7YiZndDtUb3BpYzombHQ7L2ImZ3Q7IHt9XFxu
Jmx0O2ImZ3Q7TWV0aG9kOiZsdDsvYiZndDsge31cXG5cXFwiXFxcIlxcXCIuZm9ybWF0KHJlc3Vs
dHNbXFxcIm1jYWZlZV9keGxfcGF5bG9hZFxcXCJdLCByZXN1bHRzW1xcXCJtY2FmZWVfdG9waWNf
bmFtZVxcXCJdLCByZXN1bHRzW1xcXCJtY2FmZWVfcHVibGlzaF9tZXRob2RcXFwiXSlcXG5cXG5u
b3RlVGV4dCA9IGhlbHBlci5jcmVhdGVSaWNoVGV4dCh0ZXh0KVxcbmluY2lkZW50LmFkZE5vdGUo
bm90ZVRleHQpXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+PC9leHRlbnNpb25FbGVtZW50cz48aW5j
b21pbmc+U2VxdWVuY2VGbG93XzBvaXN3aWU8L2luY29taW5nPjxvdXRnb2luZz5TZXF1ZW5jZUZs
b3dfMXc0MnN5Mzwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFzaz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVu
dF8xNjZreWY2XCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18xdzQyc3kzPC9pbmNvbWluZz48L2Vu
ZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMXc0MnN5M1wiIHNvdXJjZVJl
Zj1cIlNlcnZpY2VUYXNrXzAwd2Vpb3FcIiB0YXJnZXRSZWY9XCJFbmRFdmVudF8xNjZreWY2XCIv
PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMG9pc3dpZVwiIHNvdXJjZVJlZj1cIlN0
YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzAwd2Vpb3FcIi8+PHRl
eHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiPjx0ZXh0PlN0YXJ0IHlv
dXIgd29ya2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1c
IkFzc29jaWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0
YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIvPjwvcHJvY2Vzcz48YnBtbmRpOkJQ
TU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6QlBNTlBsYW5lIGJwbW5FbGVt
ZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxicG1uZGk6QlBNTlNoYXBlIGJw
bW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1f
ZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCIxNjJcIiB5
PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMFwiIHdp
ZHRoPVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1u
ZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRp
b25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dF9kaVwiPjxvbWdkYzpCb3Vu
ZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwiIHk9XCIyNTRcIi8+PC9icG1u
ZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8x
c2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9
XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIyMFwiLz48b21nZGk6d2F5cG9p
bnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjU0XCIvPjwvYnBtbmRp
OkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU2VydmljZVRhc2tfMDB3
ZWlvcVwiIGlkPVwiU2VydmljZVRhc2tfMDB3ZWlvcV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0
PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIzMzJcIiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5T
aGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzE2Nmt5ZjZcIiBp
ZD1cIkVuZEV2ZW50XzE2Nmt5ZjZfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lk
dGg9XCIzNlwiIHg9XCI1ODNcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpC
b3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNjAxXCIgeT1cIjIyN1wiLz48L2Jw
bW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVs
ZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMXc0MnN5M1wiIGlkPVwiU2VxdWVuY2VGbG93XzF3NDJzeTNf
ZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjQzMlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5
PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNTgzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2lu
dFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIx
M1wiIHdpZHRoPVwiMFwiIHg9XCI1MDcuNVwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVs
PjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5j
ZUZsb3dfMG9pc3dpZVwiIGlkPVwiU2VxdWVuY2VGbG93XzBvaXN3aWVfZGlcIj48b21nZGk6d2F5
cG9pbnQgeD1cIjE5OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdk
aTp3YXlwb2ludCB4PVwiMzMyXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+
PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwi
IHg9XCIyNjVcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRn
ZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4i
LCAid29ya2Zsb3dfaWQiOiAiZXhhbXBsZV9tY2FmZWVfcHVibGlzaF90b19keGxfdGFnX3N5c3Rl
bSIsICJ2ZXJzaW9uIjogMTZ9LCAid29ya2Zsb3dfaWQiOiA2LCAiYWN0aW9ucyI6IFtdLCAibGFz
dF9tb2RpZmllZF90aW1lIjogMTUyMzU3OTM3MTI0MywgImNyZWF0b3JfaWQiOiAiYndhbHNoQHJl
c2lsaWVudHN5c3RlbXMuY29tIiwgImRlc2NyaXB0aW9uIjogIldvcmtmbG93IHRvIHRyaWdnZXIg
dGhlIE1jQWZlZSBQdWJsaXNoIHRvIERYTCBmdW5jdGlvbiBhbmQgc2V0IGEgc3lzdGVtIHRhZy4i
fSwgeyJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX21jYWZlZV9wdWJsaXNoX3RvX2R4bF9z
ZXRfdGllX3JlcHV0YXRpb24iLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAiZXhwb3J0X2tl
eSI6ICJleGFtcGxlX21jYWZlZV9wdWJsaXNoX3RvX2R4bF9zZXRfdGllX3JlcHV0YXRpb24iLCAi
dXVpZCI6ICIxZjY1ZDhhMS05NzVjLTQyYjAtYjEwZS0yMGI1ZjFmYTYwNWEiLCAibGFzdF9tb2Rp
ZmllZF9ieSI6ICJid2Fsc2hAcmVzaWxpZW50c3lzdGVtcy5jb20iLCAibmFtZSI6ICIoRXhhbXBs
ZSkgTWNBZmVlIFB1Ymxpc2ggdG8gRFhMIChTZXQgVElFIFJlcHV0YXRpb24pIiwgImNvbnRlbnQi
OiB7InhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVm
aW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01P
REVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUy
NC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQv
RENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJ
XCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxu
czp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0
dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNl
PVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJleGFtcGxlX21j
YWZlZV9wdWJsaXNoX3RvX2R4bF9zZXRfdGllX3JlcHV0YXRpb25cIiBpc0V4ZWN1dGFibGU9XCJ0
cnVlXCIgbmFtZT1cIihFeGFtcGxlKSBNY0FmZWUgUHVibGlzaCB0byBEWEwgKFNldCBUSUUgUmVw
dXRhdGlvbilcIj48ZG9jdW1lbnRhdGlvbj5Xb3JrZmxvdyB0byB0cmlnZ2VyIHRoZSBNY0FmZWUg
UHVibGlzaCB0byBEWEwgZnVuY3Rpb24gYW5kIHNldCBhIFRJRSByZXB1dGF0aW9uLjwvZG9jdW1l
bnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5T
ZXF1ZW5jZUZsb3dfMDVkNngycDwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBp
ZD1cIlNlcnZpY2VUYXNrXzBhaGlvNXpcIiBuYW1lPVwiTWNBZmVlIFB1Ymxpc2ggdG8gRFhMXCIg
cmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50
OmZ1bmN0aW9uIHV1aWQ9XCJmOTg3ZWQyMi0yN2Q0LTQzODMtOWFhNC04MWUzOTk5ZWRlMjVcIj57
XCJpbnB1dHNcIjp7XCI3ZTU2OTA1Mi1iNzg2LTQ5MzMtOWQ4Ny1lYWI1NzI4MDYyNGZcIjp7XCJp
bnB1dF90eXBlXCI6XCJzdGF0aWNcIixcInN0YXRpY19pbnB1dFwiOntcIm11bHRpc2VsZWN0X3Zh
bHVlXCI6W10sXCJ0ZXh0X3ZhbHVlXCI6XCIvbWNhZmVlL3NlcnZpY2UvdGllL2ZpbGUvcmVwdXRh
dGlvbi9zZXRcIn19LFwiODVlMDcxMWUtYzU3My00MDVhLWI1OTAtNDdhZTA0YmE2N2RjXCI6e1wi
aW5wdXRfdHlwZVwiOlwic3RhdGljXCIsXCJzdGF0aWNfaW5wdXRcIjp7XCJtdWx0aXNlbGVjdF92
YWx1ZVwiOltdLFwidGV4dF92YWx1ZVwiOlwie1xcXCJoYXNoZXNcXFwiOiBbe1xcXCJ0eXBlXFxc
IjogXFxcIm1kNVxcXCIsIFxcXCJ2YWx1ZVxcXCI6IFxcXCJEazBUekpyd1RNWkxhUHc0L2dvTnJB
PT1cXFwifV0sIFxcXCJwcm92aWRlcklkXFxcIjogMywgXFxcInRydXN0TGV2ZWxcXFwiOiAxfVwi
fX0sXCIzZTQ0YzUxYi0yMmE4LTQzNTAtOTA2ZC02YWUwMzhiYjY3NzlcIjp7XCJpbnB1dF90eXBl
XCI6XCJzdGF0aWNcIixcInN0YXRpY19pbnB1dFwiOntcIm11bHRpc2VsZWN0X3ZhbHVlXCI6W10s
XCJzZWxlY3RfdmFsdWVcIjpcImNmY2RiZjdlLTE3NjUtNGI4Ny1iMTY0LTQ2YzBjNzI5N2U1YVwi
fX0sXCJkYmVlZDM2YS0yM2JmLTQxODktOWY1Yi1iNTNlZTU0ZWNkYzNcIjp7XCJpbnB1dF90eXBl
XCI6XCJzdGF0aWNcIixcInN0YXRpY19pbnB1dFwiOntcIm11bHRpc2VsZWN0X3ZhbHVlXCI6W10s
XCJzZWxlY3RfdmFsdWVcIjpcIjY2ODM3YmM3LTY1ZmQtNGZmNC1iNzlmLWI3ZjM4ZDY4NDMyN1wi
fX19LFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCIjIFJlcGxhY2VzIHRydXN0IGxldmVsIHN0
cmluZyB3aXRoIGFjY2VwdGFibGUgdmFsdWUgdG8gcHVibGlzaCB0byB0b3BpY1xcblxcbmlucHV0
cy5tY2FmZWVfZHhsX3BheWxvYWQgPSBpbnB1dHMubWNhZmVlX2R4bF9wYXlsb2FkLnJlcGxhY2Uo
XFxcIlxcXFxcXFwiS25vd24gTWFsaWNpb3VzXFxcXFxcXCJcXFwiLCBcXFwiMVxcXCIpXFxuXFxu
aW5wdXRzLm1jYWZlZV9keGxfcGF5bG9hZCA9IGlucHV0cy5tY2FmZWVfZHhsX3BheWxvYWQucmVw
bGFjZShcXFwiXFxcXFxcXCJNb3N0IExpa2VseSBNYWxpY2lvdXNcXFxcXFxcIlxcXCIsIFxcXCIx
NVxcXCIpXFxuXFxuaW5wdXRzLm1jYWZlZV9keGxfcGF5bG9hZCA9IGlucHV0cy5tY2FmZWVfZHhs
X3BheWxvYWQucmVwbGFjZShcXFwiXFxcXFxcXCJNaWdodCBCZSBNYWxpY2lvdXNcXFxcXFxcIlxc
XCIsIFxcXCIzMFxcXCIpXFxuXCIsXCJyZXN1bHRfbmFtZVwiOlwiXCIsXCJwb3N0X3Byb2Nlc3Np
bmdfc2NyaXB0XCI6XCJcXFwiXFxcIlxcXCJcXG5SZXNwb25zZSByZXR1cm5lZCBwcm92aWRlcyB0
aGUgaW5wdXQgdmFsdWVzIGluIHRoZSBmb2xsb3dpbmcgZm9ybWF0XFxue1xcbiAgXFxcIm1jYWZl
ZV90b3BpY19uYW1lXFxcIjogXFxcIiZsdDt0b3BpY19uYW1lJmd0O1xcXCIsXFxuICBcXFwibWNh
ZmVlX2R4bF9wYXlsb2FkXFxcIjogXFxcIiZsdDtwYXlsb2FkJmd0O1xcXCIsXFxuICBcXFwibWNh
ZmVlX3B1Ymxpc2hfbWV0aG9kXFxcIjogXFxcIiZsdDttZXRob2QmZ3Q7XFxcIixcXG4gIFxcXCJt
Y2FmZWVfd2FpdF9mb3JfcmVzcG9uc2VcXFwiOiBcXFwiJmx0O3dhaXQgZm9yIHJlc3BvbnNlJmd0
O1xcXCJcXG5cXFwiXFxcIlxcXCJcXG5cXG50cnVzdF9sZXZlbCA9IFxcXCJcXFwiXFxuXFxuaWYg
cmVzdWx0c1tcXFwibWNhZmVlX2R4bF9wYXlsb2FkXFxcIl0uZmluZChcXFwiMzBcXFwiKSAmZ3Q7
IDA6XFxuICB0cnVzdF9sZXZlbCA9IFxcXCJNaWdodCBCZSBNYWxpY2lvdXNcXFwiXFxuICBcXG5l
bGlmIHJlc3VsdHNbXFxcIm1jYWZlZV9keGxfcGF5bG9hZFxcXCJdLmZpbmQoXFxcIjE1XFxcIikg
Jmd0OyAwOlxcbiAgdHJ1c3RfbGV2ZWwgPSBcXFwiTW9zdCBMaWtlbHkgTWFsaWNpb3VzXFxcIlxc
blxcbmVsaWYgcmVzdWx0c1tcXFwibWNhZmVlX2R4bF9wYXlsb2FkXFxcIl0uZmluZChcXFwiMVxc
XCIpICZndDsgMDpcXG4gIHRydXN0X2xldmVsID0gXFxcIktub3duIE1hbGljaW91c1xcXCJcXG5c
XG5cXG5cXG50ZXh0ID0gXFxcIlxcXCJcXFwiVGhlIGZvbGxvd2luZyB3YXMgcHVibGlzaGVkIHRv
IERYTFxcbiZsdDtiJmd0O1BheWxvYWQ6Jmx0Oy9iJmd0OyB7fVxcbiZsdDtiJmd0O1RvcGljOiZs
dDsvYiZndDsge31cXG4mbHQ7YiZndDtNZXRob2Q6Jmx0Oy9iJmd0OyB7fVxcblxcblNldHRpbmcg
VHJ1c3QgTGV2ZWwgdG8ge31cXG5cXFwiXFxcIlxcXCIuZm9ybWF0KHJlc3VsdHNbXFxcIm1jYWZl
ZV9keGxfcGF5bG9hZFxcXCJdLCByZXN1bHRzW1xcXCJtY2FmZWVfdG9waWNfbmFtZVxcXCJdLCBy
ZXN1bHRzW1xcXCJtY2FmZWVfcHVibGlzaF9tZXRob2RcXFwiXSwgdHJ1c3RfbGV2ZWwpXFxuXFxu
bm90ZVRleHQgPSBoZWxwZXIuY3JlYXRlUmljaFRleHQodGV4dClcXG5pbmNpZGVudC5hZGROb3Rl
KG5vdGVUZXh0KVwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGlu
Y29taW5nPlNlcXVlbmNlRmxvd18wNWQ2eDJwPC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VG
bG93XzFxNHNjamY8L291dGdvaW5nPjwvc2VydmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNl
cXVlbmNlRmxvd18wNWQ2eDJwXCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFy
Z2V0UmVmPVwiU2VydmljZVRhc2tfMGFoaW81elwiLz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8x
Nzk4Z2tmXCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18xcTRzY2pmPC9pbmNvbWluZz48L2VuZEV2
ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMXE0c2NqZlwiIHNvdXJjZVJlZj1c
IlNlcnZpY2VUYXNrXzBhaGlvNXpcIiB0YXJnZXRSZWY9XCJFbmRFdmVudF8xNzk4Z2tmXCIvPjx0
ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFydCB5
b3VyIHdvcmtmbG93IGhlcmU8L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9
XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIg
dGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpC
UE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxl
bWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBi
cG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3ht
X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIg
eT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3
aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBt
bmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0
aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91
bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBt
bmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25f
MXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4
PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBv
aW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5k
aTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzBh
aGlvNXpcIiBpZD1cIlNlcnZpY2VUYXNrXzBhaGlvNXpfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdo
dD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMzE5XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1O
U2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wNWQ2eDJw
XCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMDVkNngycF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4
XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9
XCIzMTlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5M
YWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEyXCIgd2lkdGg9XCIwXCIgeD1cIjI1OC41XCIg
eT1cIjE4NVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpC
UE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8xNzk4Z2tmXCIgaWQ9XCJFbmRFdmVudF8x
Nzk4Z2tmX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwi
NTY4XCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1c
IjEyXCIgd2lkdGg9XCIwXCIgeD1cIjU4NlwiIHk9XCIyMjhcIi8+PC9icG1uZGk6QlBNTkxhYmVs
PjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVu
Y2VGbG93XzFxNHNjamZcIiBpZD1cIlNlcXVlbmNlRmxvd18xcTRzY2pmX2RpXCI+PG9tZ2RpOndh
eXBvaW50IHg9XCI0MTlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21n
ZGk6d2F5cG9pbnQgeD1cIjU2OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIv
PjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTJcIiB3aWR0aD1cIjBc
IiB4PVwiNDkzLjVcIiB5PVwiMTg1XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1O
RWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9u
cz4iLCAid29ya2Zsb3dfaWQiOiAiZXhhbXBsZV9tY2FmZWVfcHVibGlzaF90b19keGxfc2V0X3Rp
ZV9yZXB1dGF0aW9uIiwgInZlcnNpb24iOiAzMn0sICJ3b3JrZmxvd19pZCI6IDcsICJhY3Rpb25z
IjogW10sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTIzOTA2MjI1OTg4LCAiY3JlYXRvcl9pZCI6
ICJid2Fsc2hAcmVzaWxpZW50c3lzdGVtcy5jb20iLCAiZGVzY3JpcHRpb24iOiAiV29ya2Zsb3cg
dG8gdHJpZ2dlciB0aGUgTWNBZmVlIFB1Ymxpc2ggdG8gRFhMIGZ1bmN0aW9uIGFuZCBzZXQgYSBU
SUUgcmVwdXRhdGlvbi4ifV0sICJhY3Rpb25zIjogW3sibG9naWNfdHlwZSI6ICJhbGwiLCAibmFt
ZSI6ICIoRXhhbXBsZSkgTWNBZmVlIFB1Ymxpc2ggdG8gRFhMIChTZXQgVElFIFJlcHV0YXRpb24g
S25vd24gTWFsaWNpb3VzKSIsICJ2aWV3X2l0ZW1zIjogW10sICJ0eXBlIjogMSwgIndvcmtmbG93
cyI6IFsiZXhhbXBsZV9tY2FmZWVfcHVibGlzaF90b19keGxfc2V0X3RpZV9yZXB1dGF0aW9uIl0s
ICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIsICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInV1
aWQiOiAiNTU5NjYxMWMtOTA5Yy00NTQ0LTkwMGMtZGE0YTgyNzc3NjY4IiwgImF1dG9tYXRpb25z
IjogW10sICJleHBvcnRfa2V5IjogIihFeGFtcGxlKSBNY0FmZWUgUHVibGlzaCB0byBEWEwgKFNl
dCBUSUUgUmVwdXRhdGlvbiBLbm93biBNYWxpY2lvdXMpIiwgImNvbmRpdGlvbnMiOiBbXSwgImlk
IjogMzQsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdfSwgeyJsb2dpY190eXBlIjogImFsbCIs
ICJuYW1lIjogIihFeGFtcGxlKSBNY0FmZWUgUHVibGlzaCB0byBEWEwgKFRhZyBTeXN0ZW0gU2h1
dCBEb3duKSIsICJ2aWV3X2l0ZW1zIjogW10sICJ0eXBlIjogMSwgIndvcmtmbG93cyI6IFsiZXhh
bXBsZV9tY2FmZWVfcHVibGlzaF90b19keGxfdGFnX3N5c3RlbSJdLCAib2JqZWN0X3R5cGUiOiAi
aW5jaWRlbnQiLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogImI0YWIwODVlLWE0
MWUtNDMyYS1hMTUzLTc2OThlMTBjNDNlOCIsICJhdXRvbWF0aW9ucyI6IFtdLCAiZXhwb3J0X2tl
eSI6ICIoRXhhbXBsZSkgTWNBZmVlIFB1Ymxpc2ggdG8gRFhMIChUYWcgU3lzdGVtIFNodXQgRG93
bikiLCAiY29uZGl0aW9ucyI6IFtdLCAiaWQiOiAzNSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjog
W119XSwgImxheW91dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDEw
LCAiaW5kdXN0cmllcyI6IG51bGwsICJwaGFzZXMiOiBbXSwgImFjdGlvbl9vcmRlciI6IFtdLCAi
Z2VvcyI6IG51bGwsICJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMCwgInZlcnNpb24iOiAi
MzAuMC4zNDEwIiwgImJ1aWxkX251bWJlciI6IDM0MTAsICJtaW5vciI6IDB9LCAidGltZWZyYW1l
cyI6IG51bGwsICJ3b3Jrc3BhY2VzIjogW10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgImZ1bmN0
aW9ucyI6IFt7ImRpc3BsYXlfbmFtZSI6ICJNY0FmZWUgUHVibGlzaCB0byBEWEwiLCAidXVpZCI6
ICJmOTg3ZWQyMi0yN2Q0LTQzODMtOWFhNC04MWUzOTk5ZWRlMjUiLCAiY3JlYXRvciI6IHsiZGlz
cGxheV9uYW1lIjogIlJlc2lsaWVudCBTeXNhZG1pbiIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiAy
LCAibmFtZSI6ICJid2Fsc2hAcmVzaWxpZW50c3lzdGVtcy5jb20ifSwgInZpZXdfaXRlbXMiOiBb
eyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtf
aGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICI3ZTU2
OTA1Mi1iNzg2LTQ5MzMtOWQ4Ny1lYWI1NzI4MDYyNGYiLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7
InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfbGlua19o
ZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJjb250ZW50IjogIjg1ZTA3
MTFlLWM1NzMtNDA1YS1iNTkwLTQ3YWUwNGJhNjdkYyIsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsi
c2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hl
YWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRlbnQiOiAiM2U0NGM1
MWItMjJhOC00MzUwLTkwNmQtNmFlMDM4YmI2Nzc5IiwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJz
aG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVh
ZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICJkYmVlZDM2
YS0yM2JmLTQxODktOWY1Yi1iNTNlZTU0ZWNkYzMiLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgImV4
cG9ydF9rZXkiOiAibWNhZmVlX3B1Ymxpc2hfdG9fZHhsIiwgImxhc3RfbW9kaWZpZWRfYnkiOiB7
ImRpc3BsYXlfbmFtZSI6ICJSZXNpbGllbnQgU3lzYWRtaW4iLCAidHlwZSI6ICJ1c2VyIiwgImlk
IjogMiwgIm5hbWUiOiAiYndhbHNoQHJlc2lsaWVudHN5c3RlbXMuY29tIn0sICJuYW1lIjogIm1j
YWZlZV9wdWJsaXNoX3RvX2R4bCIsICJ2ZXJzaW9uIjogNSwgIndvcmtmbG93cyI6IFt7InByb2dy
YW1tYXRpY19uYW1lIjogImV4YW1wbGVfbWNhZmVlX3B1Ymxpc2hfdG9fZHhsX3NldF90aWVfcmVw
dXRhdGlvbiIsICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIsICJ1dWlkIjogbnVsbCwgImFjdGlv
bnMiOiBbXSwgIm5hbWUiOiAiKEV4YW1wbGUpIE1jQWZlZSBQdWJsaXNoIHRvIERYTCAoU2V0IFRJ
RSBSZXB1dGF0aW9uKSIsICJ3b3JrZmxvd19pZCI6IDcsICJkZXNjcmlwdGlvbiI6IG51bGx9LCB7
InByb2dyYW1tYXRpY19uYW1lIjogImV4YW1wbGVfbWNhZmVlX3B1Ymxpc2hfdG9fZHhsX3RhZ19z
eXN0ZW0iLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAidXVpZCI6IG51bGwsICJhY3Rpb25z
IjogW10sICJuYW1lIjogIihFeGFtcGxlKSBNY0FmZWUgUHVibGlzaCB0byBEWEwgKFRhZyBTeXN0
ZW0pIiwgIndvcmtmbG93X2lkIjogNiwgImRlc2NyaXB0aW9uIjogbnVsbH1dLCAibGFzdF9tb2Rp
ZmllZF90aW1lIjogMTUyMzU3NTY3NDU0MCwgImRlc3RpbmF0aW9uX2hhbmRsZSI6ICJtY2FmZWVf
ZHhsX21lc3NhZ2VfZGVzdGluYXRpb24iLCAiaWQiOiA1LCAiZGVzY3JpcHRpb24iOiB7ImNvbnRl
bnQiOiAiQSBmdW5jdGlvbiB3aGljaCB0YWtlcyA0IGlucHV0czpcblxubWNhZmVlX3RvcGljX25h
bWU6IFN0cmluZyBvZiB0aGUgdG9waWMgbmFtZS4gaWU6IC9tY2FmZWUvc2VydmljZS9lcG8vcmVt
b3RlL2VwbzEuXG5tY2FmZWVfZHhsX3BheWxvYWQ6IFRoZSB0ZXh0IG9mIHRoZSBwYXlsb2FkIHRv
IHB1Ymxpc2ggdG8gdGhlIHRvcGljLlxubWNhZmVlX3B1Ymxpc2hfbWV0aG9kOiBTcGVjaWZ5IHdo
ZXRoZXIgdG8gcHVibGlzaCBhbiBldmVudCBvciBpbnZva2UgYSBzZXJ2aWNlLlxubWNhZmVlX3dh
aXRfZm9yX3Jlc3BvbnNlOiBTcGVjaWZ5IHdoZXRoZXIgb3Igbm90IHRvIHdhaXQgZm9yIHRoZSBy
ZXNwb25zZS4gVXNlcyBzeW5jaHJvbm91cy9hc3luY2hyb25vdXMgc2VydmljZS5cblxuXG5UaGUg
ZnVuY3Rpb24gd2lsbCBzZW5kIHRoZSBwcm92aWRlZCBtZXNzYWdlIHRvIHRoZSBwcm92aWRlZCB0
b3BpYy4iLCAiZm9ybWF0IjogInRleHQifX1dLCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJyZWd1
bGF0b3JzIjogbnVsbCwgImluY2lkZW50X3R5cGVzIjogW3siY3JlYXRlX2RhdGUiOiAxNTIzOTg1
NDc1NzUxLCAiZGVzY3JpcHRpb24iOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwp
IiwgImV4cG9ydF9rZXkiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImlk
IjogMCwgIm5hbWUiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgInVwZGF0
ZV9kYXRlIjogMTUyMzk4NTQ3NTc1MSwgInV1aWQiOiAiYmZlZWMyZDQtMzc3MC0xMWU4LWFkMzkt
NGEwMDA0MDQ0YWEwIiwgImVuYWJsZWQiOiBmYWxzZSwgInN5c3RlbSI6IGZhbHNlLCAicGFyZW50
X2lkIjogbnVsbCwgImhpZGRlbiI6IGZhbHNlfV0sICJzY3JpcHRzIjogW10sICJ0eXBlcyI6IFtd
LCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbeyJ1dWlkIjogIjA1NTdkNjZiLThmNzYtNDljMC05
Y2Q3LTk0ZmVkMjFlOGMwYyIsICJleHBvcnRfa2V5IjogIm1jYWZlZV9keGxfbWVzc2FnZV9kZXN0
aW5hdGlvbiIsICJuYW1lIjogIk1jQWZlZSBEWEwgTWVzc2FnZSBEZXN0aW5hdGlvbiIsICJkZXN0
aW5hdGlvbl90eXBlIjogMCwgInByb2dyYW1tYXRpY19uYW1lIjogIm1jYWZlZV9keGxfbWVzc2Fn
ZV9kZXN0aW5hdGlvbiIsICJleHBlY3RfYWNrIjogdHJ1ZSwgInVzZXJzIjogWyJid2Fsc2hAcmVz
aWxpZW50c3lzdGVtcy5jb20iXX1dLCAiaW5jaWRlbnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgInJv
bGVzIjogW10sICJmaWVsZHMiOiBbeyJvcGVyYXRpb25zIjogW10sICJyZWFkX29ubHkiOiB0cnVl
LCAidXVpZCI6ICJjM2YwZTNlZC0yMWUxLTRkNTMtYWZmYi1mZTVjYTMzMDhjY2EiLCAidGVtcGxh
dGVzIjogW10sICJ0eXBlX2lkIjogMCwgImNob3NlbiI6IGZhbHNlLCAidGV4dCI6ICJTaW11bGF0
aW9uIiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJp
bmNpZGVudC9pbmNfdHJhaW5pbmciLCAidG9vbHRpcCI6ICJXaGV0aGVyIHRoZSBpbmNpZGVudCBp
cyBhIHNpbXVsYXRpb24gb3IgYSByZWd1bGFyIGluY2lkZW50LiAgVGhpcyBmaWVsZCBpcyByZWFk
LW9ubHkuIiwgInJpY2hfdGV4dCI6IGZhbHNlLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJwcmVm
aXgiOiBudWxsLCAiaW50ZXJuYWwiOiBmYWxzZSwgInZhbHVlcyI6IFtdLCAiYmxhbmtfb3B0aW9u
IjogZmFsc2UsICJpbnB1dF90eXBlIjogImJvb2xlYW4iLCAiY2hhbmdlYWJsZSI6IHRydWUsICJo
aWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAzNywgIm5hbWUiOiAiaW5jX3RyYWluaW5n
In0sIHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjog
e30sICJ0ZXh0IjogIm1jYWZlZV90b3BpY19uYW1lIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAi
cHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAxNjYsICJyZWFkX29ubHki
OiBmYWxzZSwgInV1aWQiOiAiN2U1NjkwNTItYjc4Ni00OTMzLTlkODctZWFiNTcyODA2MjRmIiwg
ImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiU3RyaW5n
IG9mIHRoZSB0b3BpYyBuYW1lLiBpZTogL21jYWZlZS9zZXJ2aWNlL2Vwby9yZW1vdGUvZXBvMSIs
ICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwg
ImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9tY2FmZWVfdG9waWNfbmFtZSIsICJoaWRlX25vdGlm
aWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAibWNhZmVlX3RvcGlj
X25hbWUiLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJyZXF1aXJlZCI6ICJh
bHdheXMiLCAidmFsdWVzIjogW119LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwg
Im9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJtY2FmZWVfd2FpdF9mb3JfcmVzcG9uc2Ui
LCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRy
dWUsICJpZCI6IDE2OCwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICJkYmVlZDM2YS0yM2Jm
LTQxODktOWY1Yi1iNTNlZTU0ZWNkYzMiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjog
InNlbGVjdCIsICJ0b29sdGlwIjogIlNwZWNpZnkgd2hldGhlciBvciBub3QgdG8gd2FpdCBmb3Ig
dGhlIHJlc3BvbnNlLiBVc2VzIHN5bmNocm9ub3VzL2FzeW5jaHJvbm91cyBzZXJ2aWNlIiwgImlu
dGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhw
b3J0X2tleSI6ICJfX2Z1bmN0aW9uL21jYWZlZV93YWl0X2Zvcl9yZXNwb25zZSIsICJoaWRlX25v
dGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAibWNhZmVlX3dh
aXRfZm9yX3Jlc3BvbnNlIiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFs
dWVzIjogW3sidXVpZCI6ICJiNDVmYzgzNC03Y2FiLTQ4YmMtODQzNy1iMjE0ZWNlNDc2NzgiLCAi
ZGVmYXVsdCI6IHRydWUsICJlbmFibGVkIjogdHJ1ZSwgInZhbHVlIjogMjAwLCAibGFiZWwiOiAi
WWVzIiwgImhpZGRlbiI6IGZhbHNlLCAicHJvcGVydGllcyI6IG51bGx9LCB7InV1aWQiOiAiNjY4
MzdiYzctNjVmZC00ZmY0LWI3OWYtYjdmMzhkNjg0MzI3IiwgImRlZmF1bHQiOiBmYWxzZSwgImVu
YWJsZWQiOiB0cnVlLCAidmFsdWUiOiAyMDEsICJsYWJlbCI6ICJObyIsICJoaWRkZW4iOiBmYWxz
ZSwgInByb3BlcnRpZXMiOiBudWxsfV19LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAx
MSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJtY2FmZWVfcHVibGlzaF9tZXRob2Qi
LCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRy
dWUsICJpZCI6IDE3MCwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICIzZTQ0YzUxYi0yMmE4
LTQzNTAtOTA2ZC02YWUwMzhiYjY3NzkiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjog
InNlbGVjdCIsICJ0b29sdGlwIjogIlNwZWNpZnkgd2hldGhlciB0byBwdWJsaXNoIGFuIGV2ZW50
IG9yIGludm9rZSBhIHNlcnZpY2UiLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZh
bHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vbWNhZmVlX3B1
Ymxpc2hfbWV0aG9kIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6
ICIiLCAibmFtZSI6ICJtY2FmZWVfcHVibGlzaF9tZXRob2QiLCAiZGVmYXVsdF9jaG9zZW5fYnlf
c2VydmVyIjogZmFsc2UsICJyZXF1aXJlZCI6ICJhbHdheXMiLCAidmFsdWVzIjogW3sidXVpZCI6
ICJhNTFhZWM3ZS00MmE4LTQ3MTYtODRmZi02YmQyOTk2NjdmOGQiLCAiZGVmYXVsdCI6IHRydWUs
ICJlbmFibGVkIjogdHJ1ZSwgInZhbHVlIjogMjAyLCAibGFiZWwiOiAiRXZlbnQiLCAiaGlkZGVu
IjogZmFsc2UsICJwcm9wZXJ0aWVzIjogbnVsbH0sIHsidXVpZCI6ICJjZmNkYmY3ZS0xNzY1LTRi
ODctYjE2NC00NmMwYzcyOTdlNWEiLCAiZGVmYXVsdCI6IGZhbHNlLCAiZW5hYmxlZCI6IHRydWUs
ICJ2YWx1ZSI6IDIwMywgImxhYmVsIjogIlNlcnZpY2UiLCAiaGlkZGVuIjogZmFsc2UsICJwcm9w
ZXJ0aWVzIjogbnVsbH1dfSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVy
YXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAibWNhZmVlX2R4bF9wYXlsb2FkIiwgImJsYW5rX29w
dGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAx
NjcsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiODVlMDcxMWUtYzU3My00MDVhLWI1OTAt
NDdhZTA0YmE2N2RjIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRv
b2x0aXAiOiAiVGhlIHRleHQgb2YgdGhlIHBheWxvYWQgdG8gcHVibGlzaCB0byB0aGUgdG9waWMi
LCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10s
ICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vbWNhZmVlX2R4bF9wYXlsb2FkIiwgImhpZGVfbm90
aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJtY2FmZWVfZHhs
X3BheWxvYWQiLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJyZXF1aXJlZCI6
ICJhbHdheXMiLCAidmFsdWVzIjogW119XSwgIm92ZXJyaWRlcyI6IFtdLCAiZXhwb3J0X2RhdGUi
OiAxNTIzOTIzNDMwODgzfQ==
"""
    )
