"""Framing text for this framework's diagrams.

Phase content comes from the reference design; only the framing below is
authored, and each line is drawn from that document's stated scope.
"""

FRAMING = {'kicker': 'CIP-002 &ndash; CIP-014',
 'title_tail': '&mdash; NERC CIP',
 'sub': 'From agent coverage to continuous proof between audits &mdash; exports map '
        'to control IDs in the Reporting &amp; Evidence section.',
 'caution_label': 'IT side of the boundary &rsaquo;',
 'caution': 'CSW addresses the <b>IT side</b> of the IT/OT boundary &mdash; EMS and '
            'SCADA support hosts, historians, engineering workstations, '
            'vendor-access hosts. Enforcement on relays, RTUs, PLCs and IEDs comes '
            'from your OT controls.',
 'takeaway': 'CSW produces workload-level ESP evidence for the server tier inside '
             'the perimeter. <b>Pair it with your OT-aware sensors and IT/OT '
             'firewalls</b>, which remain the controlling artifacts at the device '
             'layer.',
 'rail': ['Workload-level evidence for the ESP server tier',
          'Simulation proves the policy before anything is enforced',
          'OT device layer stays with your OT-aware controls']}
