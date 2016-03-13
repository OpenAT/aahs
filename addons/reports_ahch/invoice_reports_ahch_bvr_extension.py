from openerp import models, fields

class invoice_reports_ahch_bvr_extension(models.Model):
    _inherit = "res.company"

    """override company in order to add bvr vertical and
    Horizontal print delta"""


    bvr_ammount_delta_horz = fields.Integer(
        'BVR Ammount Horz. Delta (mm)',
        help='horiz. delta in mm  will print the bvr  mm lefter, '
        'negative value is possible'
    )

    bvr_ammount_left_delta_vert = fields.Integer(
        'BVR Ammount left column Vert. Delta (mm)',
        help='vert. delta in mm  will print the bvr  mm lower, '
             'negative value is possible'
    )
    bvr_ammountdec_left_delta_vert = fields.Integer(
        'BVR Ammount decimal left column Vert. Delta (mm)',
        help='vert. delta in mm  will print the bvr  mm lower, '
             'negative value is possible'
    )

    bvr_ammount_right_delta_vert = fields.Integer(
        'BVR Ammount right column Vertical. Delta (mm)',
        help='Vert. delta in mm  will print the bvr  mm lefter, '
        'negative value is possible'
    )

    bvr_ammountdec_right_delta_vert = fields.Integer(
        'BVR Ammount decimal right column Vert. Delta (mm)',
        help='Vert. delta in mm  will print the bvr  mm lefter, '
        'negative value is possible'
    )

    bvr_kodierline_delta_vert = fields.Integer(
        'BVR Kodierzeile bottom Vertical. Delta (mm)',
        help='Vert. delta in mm  will print the bvr  mm lefter, '
        'negative value is possible'
    )

    bvr_kodierline_delta_horz = fields.Integer(
        'BVR Kodierzeile bottom Horizontal. Delta (mm)',
        help='horiz. delta in mm  will print the bvr  mm lefter, '
        'negative value is possible'
    )

    bvr_esr_right_delta_horz = fields.Integer(
        'BVR ESR Code right Horizontal. Delta (mm)',
        help='horiz. delta in mm  will print the bvr  mm lefter, '
        'negative value is possible'
    )

    bvr_esr_right_delta_vert = fields.Integer(
        'BVR ESR Code right Vertical. Delta (mm)',
        help='Vert. delta in mm  will print the bvr  mm lefter, '
        'negative value is possible'
    )

    bvr_address_left_top_horz = fields.Integer(
        'BVR Address Left Top Horizontal. position for scan line (mm)',
        help='Horiz. position in mm for Address Line'
    )

    bvr_address_left_top_vert = fields.Integer(
        'BVR Address Left Top Vertical. position for scan line(mm)',
        help='Vert. position in mm for adress Line'
    )

    bvr_address2_left_top_vert = fields.Integer(
        'BVR Address vert. Left Top position for address (mm)',
        help='Vert. position in mm for address'
    )

    bvr_esr_left_delta_vert = fields.Integer(
        'BVR ESR 27 Digit Code Vert. position address (mm)',
        help='Vertical. position in mm for esr code'
    )

    bvr_esr_left_delta_horz = fields.Integer(
        'BVR ESR 27 Digit Code Horz. position address (mm)',
        help='Horozontal. position in mm for esr code'
    )

    bvr_address_left_bottom_horz = fields.Integer(
        'BVR Address Left bottom Horizontal. position for scan line (mm)',
        help='Horiz. position in mm for Address Line'
    )

    bvr_address_left_bottom_vert = fields.Integer(
        'BVR Address Left bottom Vertical. position for scan line(mm)',
        help='Vert. position in mm for adress Line'
    )

    bvr_address2_left_bottom_vert = fields.Integer(
        'BVR Address vert. Left bottom position for address (mm)',
        help='Vert. position in mm for address'
    )

    bvr_accountnr_left_delta_horz = fields.Integer(
        'BVR ESR 27 Digit Code Vert. position address (mm)',
        help='Vertical. position in mm for esr code'
    )

    bvr_accountnr2_left_delta_vert = fields.Integer(
        'BVR ESR 27 Digit Code Horz. position address (mm)',
        help='Horozontal. position in mm for esr code'
    )

    bvr_address_right_bottom_horz = fields.Integer(
        'BVR Address right Horz. position address (mm)',
        help='Horizontal. position in mm for address line'
    )

    bvr_address_right_bottom_vert = fields.Integer(
        'BVR Address right Vert. position address (mm)',
        help='Vertical. position in mm for address line'
    )

    bvr_scan_line_font_size = fields.Integer(
        'BVR scan line font size (pt)'
    )

    bvr_scan_line_letter_spacing = fields.Integer(
        'BVR scan line letter spacing'
    )

