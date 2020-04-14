#!/usr/bin/env python

from construct import *

TAG_ENUM = {
    "subfile_type": 0x00fe,
    "image_width": 0x0100,
    "image_height": 0x0101,
    "bits_per_sample": 0x0102,
    "compression": 0x0103,
    "photometric_interpretation": 0x0106,
    "thresholding": 0x0107,
    "cell_width": 0x0108,
    "cell_length": 0x0109,
    "fill_order": 0x010a,
    "document_name": 0x010d,
    "image_description": 0x010e,
    "make": 0x010f,
    "model": 0x0110,
    "strip_offsets": 0x0111,
    "orientation": 0x0112,
    "samples_per_pixel": 0x0115,
    "rows_per_strip": 0x0116,
    "strip_byte_counts": 0x0117,
    "min_sample_value": 0x0118,
    "max_sample_value": 0x0119,
    "x_resolution": 0x011a,
    "y_resolution": 0x011b,
    "planar_configuration": 0x011c,
    "page_name": 0x011d,
    "x_position": 0x011e,
    "y_position": 0x011f,
    "free_offsets": 0x0120,
    "free_byte_counts": 0x0121,
    "gray_response_unit": 0x0122,
    "gray_response_curve": 0x0123,
    "t4_options": 0x0124,
    "t6_options": 0x0125,
    "resolution_unit": 0x0128,
    "page_number": 0x0129,
    "color_response_unit": 0x012c,
    "transfer_function": 0x012d,
    "software": 0x0131,
    "modify_date": 0x0132,
    "artist": 0x013b,
    "host_computer": 0x013c,
    "predictor": 0x013d,
    "white_point": 0x013e,
    "primary_chromaticities": 0x013f,
    "color_map": 0x0140,
    "halftone_hints": 0x0141,
    "tile_width": 0x0142,
    "tile_length": 0x0143,
    "tile_offsets": 0x0144,
    "tile_byte_counts": 0x0145,
    "bad_fax_lines": 0x0146,
    "clean_fax_data": 0x0147,
    "consecutive_bad_fax_lines": 0x0148,
    "sub_ifd": 0x014a,
    "ink_set": 0x014c,
    "ink_names": 0x014d,
    "numberof_inks": 0x014e,
    "dot_range": 0x0150,
    "target_printer": 0x0151,
    "extra_samples": 0x0152,
    "sample_format": 0x0153,
    "s_min_sample_value": 0x0154,
    "s_max_sample_value": 0x0155,
    "transfer_range": 0x0156,
    "clip_path": 0x0157,
    "x_clip_path_units": 0x0158,
    "y_clip_path_units": 0x0159,
    "indexed": 0x015a,
    "jpeg_tables": 0x015b,
    "opi_proxy": 0x015f,
    "global_parameters_ifd": 0x0190,
    "profile_type": 0x0191,
    "fax_profile": 0x0192,
    "coding_methods": 0x0193,
    "version_year": 0x0194,
    "mode_number": 0x0195,
    "decode": 0x01b1,
    "default_image_color": 0x01b2,
    "t82_options": 0x01b3,
    "jpeg_tables2": 0x01b5,
    "jpeg_proc": 0x0200,
    "thumbnail_offset": 0x0201,
    "thumbnail_length": 0x0202,
    "jpeg_restart_interval": 0x0203,
    "jpeg_lossless_predictors": 0x0205,
    "jpeg_point_transforms": 0x0206,
    "jpegq_tables": 0x0207,
    "jpegdc_tables": 0x0208,
    "jpegac_tables": 0x0209,
    "y_cb_cr_coefficients": 0x0211,
    "y_cb_cr_sub_sampling": 0x0212,
    "y_cb_cr_positioning": 0x0213,
    "reference_black_white": 0x0214,
    "strip_row_counts": 0x022f,
    "application_notes": 0x02bc,
    "uspto_miscellaneous": 0x03e7,
    "related_image_file_format": 0x1000,
    "related_image_width": 0x1001,
    "related_image_height": 0x1002,
    "rating": 0x4746,
    "xp_dip_xml": 0x4747,
    "stitch_info": 0x4748,
    "rating_percent": 0x4749,
    "sony_raw_file_type": 0x7000,
    "light_falloff_params": 0x7032,
    "chromatic_aberration_corr_params": 0x7035,
    "distortion_corr_params": 0x7037,
    "image_id": 0x800d,
    "wang_tag1": 0x80a3,
    "wang_annotation": 0x80a4,
    "wang_tag3": 0x80a5,
    "wang_tag4": 0x80a6,
    "image_reference_points": 0x80b9,
    "region_xform_tack_point": 0x80ba,
    "warp_quadrilateral": 0x80bb,
    "affine_transform_mat": 0x80bc,
    "matteing": 0x80e3,
    "data_type": 0x80e4,
    "image_depth": 0x80e5,
    "tile_depth": 0x80e6,
    "image_full_width": 0x8214,
    "image_full_height": 0x8215,
    "texture_format": 0x8216,
    "wrap_modes": 0x8217,
    "fov_cot": 0x8218,
    "matrix_world_to_screen": 0x8219,
    "matrix_world_to_camera": 0x821a,
    "model2": 0x827d,
    "cfa_repeat_pattern_dim": 0x828d,
    "cfa_pattern2": 0x828e,
    "battery_level": 0x828f,
    "kodak_ifd": 0x8290,
    "copyright": 0x8298,
    "exposure_time": 0x829a,
    "f_number": 0x829d,
    "md_file_tag": 0x82a5,
    "md_scale_pixel": 0x82a6,
    "md_color_table": 0x82a7,
    "md_lab_name": 0x82a8,
    "md_sample_info": 0x82a9,
    "md_prep_date": 0x82aa,
    "md_prep_time": 0x82ab,
    "md_file_units": 0x82ac,
    "pixel_scale": 0x830e,
    "advent_scale": 0x8335,
    "advent_revision": 0x8336,
    "uic1_tag": 0x835c,
    "uic2_tag": 0x835d,
    "uic3_tag": 0x835e,
    "uic4_tag": 0x835f,
    "iptc_naa": 0x83bb,
    "intergraph_packet_data": 0x847e,
    "intergraph_flag_registers": 0x847f,
    "intergraph_matrix": 0x8480,
    "ingr_reserved": 0x8481,
    "model_tie_point": 0x8482,
    "site": 0x84e0,
    "color_sequence": 0x84e1,
    "it8_header": 0x84e2,
    "raster_padding": 0x84e3,
    "bits_per_run_length": 0x84e4,
    "bits_per_extended_run_length": 0x84e5,
    "color_table": 0x84e6,
    "image_color_indicator": 0x84e7,
    "background_color_indicator": 0x84e8,
    "image_color_value": 0x84e9,
    "background_color_value": 0x84ea,
    "pixel_intensity_range": 0x84eb,
    "transparency_indicator": 0x84ec,
    "color_characterization": 0x84ed,
    "hc_usage": 0x84ee,
    "trap_indicator": 0x84ef,
    "cmyk_equivalent": 0x84f0,
    "sem_info": 0x8546,
    "afcp_iptc": 0x8568,
    "pixel_magic_jbig_options": 0x85b8,
    "jpl_carto_ifd": 0x85d7,
    "model_transform": 0x85d8,
    "wb_grgb_levels": 0x8602,
    "leaf_data": 0x8606,
    "photoshop_settings": 0x8649,
    "exif_offset": 0x8769,
    "icc_profile": 0x8773,
    "tiff_fx_extensions": 0x877f,
    "multi_profiles": 0x8780,
    "shared_data": 0x8781,
    "t88_options": 0x8782,
    "image_layer": 0x87ac,
    "geo_tiff_directory": 0x87af,
    "geo_tiff_double_params": 0x87b0,
    "geo_tiff_ascii_params": 0x87b1,
    "jbig_options": 0x87be,
    "exposure_program": 0x8822,
    "spectral_sensitivity": 0x8824,
    "gps_info": 0x8825,
    "iso": 0x8827,
    "opto_electric_conv_factor": 0x8828,
    "interlace": 0x8829,
    "time_zone_offset": 0x882a,
    "self_timer_mode": 0x882b,
    "sensitivity_type": 0x8830,
    "standard_output_sensitivity": 0x8831,
    "recommended_exposure_index": 0x8832,
    "iso_speed": 0x8833,
    "iso_speed_latitudeyyy": 0x8834,
    "iso_speed_latitudezzz": 0x8835,
    "fax_recv_params": 0x885c,
    "fax_sub_address": 0x885d,
    "fax_recv_time": 0x885e,
    "fedex_edr": 0x8871,
    "leaf_sub_ifd": 0x888a,
    "exif_version": 0x9000,
    "date_time_original": 0x9003,
    "create_date": 0x9004,
    "google_plus_upload_code": 0x9009,
    "offset_time": 0x9010,
    "offset_time_original": 0x9011,
    "offset_time_digitized": 0x9012,
    "components_configuration": 0x9101,
    "compressed_bits_per_pixel": 0x9102,
    "shutter_speed_value": 0x9201,
    "aperture_value": 0x9202,
    "brightness_value": 0x9203,
    "exposure_compensation": 0x9204,
    "max_aperture_value": 0x9205,
    "subject_distance": 0x9206,
    "metering_mode": 0x9207,
    "light_source": 0x9208,
    "flash": 0x9209,
    "focal_length": 0x920a,
    "flash_energy": 0x920b,
    "spatial_frequency_response": 0x920c,
    "noise": 0x920d,
    "focal_plane_x_resolution": 0x920e,
    "focal_plane_y_resolution": 0x920f,
    "focal_plane_resolution_unit": 0x9210,
    "image_number": 0x9211,
    "security_classification": 0x9212,
    "image_history": 0x9213,
    "subject_area": 0x9214,
    "exposure_index": 0x9215,
    "tiff_ep_standard_id": 0x9216,
    "sensing_method": 0x9217,
    "cip3_data_file": 0x923a,
    "cip3_sheet": 0x923b,
    "cip3_side": 0x923c,
    "sto_nits": 0x923f,
    "maker_note": 0x927c,
    "user_comment": 0x9286,
    "sub_sec_time": 0x9290,
    "sub_sec_time_original": 0x9291,
    "sub_sec_time_digitized": 0x9292,
    "ms_document_text": 0x932f,
    "ms_property_set_storage": 0x9330,
    "ms_document_text_position": 0x9331,
    "image_source_data": 0x935c,
    "ambient_temperature": 0x9400,
    "humidity": 0x9401,
    "pressure": 0x9402,
    "water_depth": 0x9403,
    "acceleration": 0x9404,
    "camera_elevation_angle": 0x9405,
    "xp_title": 0x9c9b,
    "xp_comment": 0x9c9c,
    "xp_author": 0x9c9d,
    "xp_keywords": 0x9c9e,
    "xp_subject": 0x9c9f,
    "flashpix_version": 0xa000,
    "color_space": 0xa001,
    "exif_image_width": 0xa002,
    "exif_image_height": 0xa003,
    "related_sound_file": 0xa004,
    "interop_offset": 0xa005,
    "samsung_raw_pointers_offset": 0xa010,
    "samsung_raw_pointers_length": 0xa011,
    "samsung_raw_byte_order": 0xa101,
    "samsung_raw_unknown": 0xa102,
    "flash_energy2": 0xa20b,
    "spatial_frequency_response2": 0xa20c,
    "noise2": 0xa20d,
    "focal_plane_x_resolution2": 0xa20e,
    "focal_plane_y_resolution2": 0xa20f,
    "focal_plane_resolution_unit2": 0xa210,
    "image_number2": 0xa211,
    "security_classification2": 0xa212,
    "image_history2": 0xa213,
    "subject_location": 0xa214,
    "exposure_index2": 0xa215,
    "tiff_ep_standard_id2": 0xa216,
    "sensing_method2": 0xa217,
    "file_source": 0xa300,
    "scene_type": 0xa301,
    "cfa_pattern": 0xa302,
    "custom_rendered": 0xa401,
    "exposure_mode": 0xa402,
    "white_balance": 0xa403,
    "digital_zoom_ratio": 0xa404,
    "focal_length_in35mm_format": 0xa405,
    "scene_capture_type": 0xa406,
    "gain_control": 0xa407,
    "contrast": 0xa408,
    "saturation": 0xa409,
    "sharpness": 0xa40a,
    "device_setting_description": 0xa40b,
    "subject_distance_range": 0xa40c,
    "image_unique_id": 0xa420,
    "owner_name": 0xa430,
    "serial_number": 0xa431,
    "lens_info": 0xa432,
    "lens_make": 0xa433,
    "lens_model": 0xa434,
    "lens_serial_number": 0xa435,
    "gdal_metadata": 0xa480,
    "gdal_no_data": 0xa481,
    "gamma": 0xa500,
    "expand_software": 0xafc0,
    "expand_lens": 0xafc1,
    "expand_film": 0xafc2,
    "expand_filter_lens": 0xafc3,
    "expand_scanner": 0xafc4,
    "expand_flash_lamp": 0xafc5,
    "pixel_format": 0xbc01,
    "transformation": 0xbc02,
    "uncompressed": 0xbc03,
    "image_type": 0xbc04,
    "image_width2": 0xbc80,
    "image_height2": 0xbc81,
    "width_resolution": 0xbc82,
    "height_resolution": 0xbc83,
    "image_offset": 0xbcc0,
    "image_byte_count": 0xbcc1,
    "alpha_offset": 0xbcc2,
    "alpha_byte_count": 0xbcc3,
    "image_data_discard": 0xbcc4,
    "alpha_data_discard": 0xbcc5,
    "oce_scanjob_desc": 0xc427,
    "oce_application_selector": 0xc428,
    "oce_id_number": 0xc429,
    "oce_image_logic": 0xc42a,
    "annotations": 0xc44f,
    "print_im": 0xc4a5,
    "original_file_name": 0xc573,
    "uspto_original_content_type": 0xc580,
    "dng_version": 0xc612,
    "dng_backward_version": 0xc613,
    "unique_camera_model": 0xc614,
    "localized_camera_model": 0xc615,
    "cfa_plane_color": 0xc616,
    "cfa_layout": 0xc617,
    "linearization_table": 0xc618,
    "black_level_repeat_dim": 0xc619,
    "black_level": 0xc61a,
    "black_level_delta_h": 0xc61b,
    "black_level_delta_v": 0xc61c,
    "white_level": 0xc61d,
    "default_scale": 0xc61e,
    "default_crop_origin": 0xc61f,
    "default_crop_size": 0xc620,
    "color_matrix1": 0xc621,
    "color_matrix2": 0xc622,
    "camera_calibration1": 0xc623,
    "camera_calibration2": 0xc624,
    "reduction_matrix1": 0xc625,
    "reduction_matrix2": 0xc626,
    "analog_balance": 0xc627,
    "as_shot_neutral": 0xc628,
    "as_shot_white_xy": 0xc629,
    "baseline_exposure": 0xc62a,
    "baseline_noise": 0xc62b,
    "baseline_sharpness": 0xc62c,
    "bayer_green_split": 0xc62d,
    "linear_response_limit": 0xc62e,
    "camera_serial_number": 0xc62f,
    "dng_lens_info": 0xc630,
    "chroma_blur_radius": 0xc631,
    "anti_alias_strength": 0xc632,
    "shadow_scale": 0xc633,
    "sr2_private": 0xc634,
    "maker_note_safety": 0xc635,
    "raw_image_segmentation": 0xc640,
    "calibration_illuminant1": 0xc65a,
    "calibration_illuminant2": 0xc65b,
    "best_quality_scale": 0xc65c,
    "raw_data_unique_id": 0xc65d,
    "alias_layer_metadata": 0xc660,
    "original_raw_file_name": 0xc68b,
    "original_raw_file_data": 0xc68c,
    "active_area": 0xc68d,
    "masked_areas": 0xc68e,
    "as_shot_icc_profile": 0xc68f,
    "as_shot_pre_profile_matrix": 0xc690,
    "current_icc_profile": 0xc691,
    "current_pre_profile_matrix": 0xc692,
    "colorimetric_reference": 0xc6bf,
    "s_raw_type": 0xc6c5,
    "panasonic_title": 0xc6d2,
    "panasonic_title2": 0xc6d3,
    "camera_calibration_sig": 0xc6f3,
    "profile_calibration_sig": 0xc6f4,
    "profile_ifd": 0xc6f5,
    "as_shot_profile_name": 0xc6f6,
    "noise_reduction_applied": 0xc6f7,
    "profile_name": 0xc6f8,
    "profile_hue_sat_map_dims": 0xc6f9,
    "profile_hue_sat_map_data1": 0xc6fa,
    "profile_hue_sat_map_data2": 0xc6fb,
    "profile_tone_curve": 0xc6fc,
    "profile_embed_policy": 0xc6fd,
    "profile_copyright": 0xc6fe,
    "forward_matrix1": 0xc714,
    "forward_matrix2": 0xc715,
    "preview_application_name": 0xc716,
    "preview_application_version": 0xc717,
    "preview_settings_name": 0xc718,
    "preview_settings_digest": 0xc719,
    "preview_color_space": 0xc71a,
    "preview_date_time": 0xc71b,
    "raw_image_digest": 0xc71c,
    "original_raw_file_digest": 0xc71d,
    "sub_tile_block_size": 0xc71e,
    "row_interleave_factor": 0xc71f,
    "profile_look_table_dims": 0xc725,
    "profile_look_table_data": 0xc726,
    "opcode_list1": 0xc740,
    "opcode_list2": 0xc741,
    "opcode_list3": 0xc74e,
    "noise_profile": 0xc761,
    "time_codes": 0xc763,
    "frame_rate": 0xc764,
    "t_stop": 0xc772,
    "reel_name": 0xc789,
    "original_default_final_size": 0xc791,
    "original_best_quality_size": 0xc792,
    "original_default_crop_size": 0xc793,
    "camera_label": 0xc7a1,
    "profile_hue_sat_map_encoding": 0xc7a3,
    "profile_look_table_encoding": 0xc7a4,
    "baseline_exposure_offset": 0xc7a5,
    "default_black_render": 0xc7a6,
    "new_raw_image_digest": 0xc7a7,
    "raw_to_preview_gain": 0xc7a8,
    "default_user_crop": 0xc7b5,
    "padding": 0xea1c,
    "offset_schema": 0xea1d,
    "owner_name2": 0xfde8,
    "serial_number2": 0xfde9,
    "lens": 0xfdea,
    "kdc_ifd": 0xfe00,
    "raw_file": 0xfe4c,
    "converter": 0xfe4d,
    "white_balance2": 0xfe4e,
    "exposure": 0xfe51,
    "shadows": 0xfe52,
    "brightness": 0xfe53,
    "contrast2": 0xfe54,
    "saturation2": 0xfe55,
    "sharpness2": 0xfe56,
    "smoothness": 0xfe57,
    "moire_filter": 0xfe58,
}

DNG_ENDIAN_HE, DNG_ENDIAN_LE = range(2)

Int16 = Switch(this._endian == DNG_ENDIAN_HE, {
    True: Int16ub,
    False: Int16ul})
Int32 = Switch(this._endian == DNG_ENDIAN_HE, {
    True: Int32ub,
    False: Int32ul})
SInt16 = Switch(this._endian == DNG_ENDIAN_HE, {
    True: Int16sb,
    False: Int16sl})
SInt32 = Switch(this._endian == DNG_ENDIAN_HE, {
    True: Int32sb,
    False: Int32sl})
Float = Switch(this._endian == DNG_ENDIAN_HE, {
    True: Float16b,
    False: Float16l})
Double = Switch(this._endian == DNG_ENDIAN_HE, {
    True: Float32b,
    False: Float32l})

TagEnum = Enum(Int16,
               **TAG_ENUM
               )

TagTypeEnum = Enum(Int16,
                   byte=1,
                   string=2,
                   word=3,
                   dword=4,
                   rational=5,
                   undefined=7,
                   srational=10,
                   float=11,
                   double=12,
                   )

Rational = Struct(
    "_endian" / Computed(this._._endian),
    "a" / Int32,
    "b" / Int32,
)

SRational = Struct(
    "_endian" / Computed(this._._endian),
    "a" / SInt32,
    "b" / SInt32,
)

TagValue = Switch(this.type, {
    TagTypeEnum.byte: Switch(this.length <= 4, {
        True: Peek(Bytes(this.length)),
        False: Pointer(this._offset, Bytes(this.length)),
    }),
    TagTypeEnum.word: Switch(this.length <= 2, {
        True: Peek(Array(this.length, Int16)),
        False: Pointer(this._offset, Array(this.length, Int16)),
    }),
    TagTypeEnum.dword: Switch(this.length <= 1, {
        True: Peek(Array(this.length, Int32)),
        False: Pointer(this._offset,  Array(this.length, Int32)),
    }),
    TagTypeEnum.string: Pointer(this._offset, Bytes(this.length)),
    TagTypeEnum.rational: Pointer(this._offset, Array(this.length, Rational)),
    TagTypeEnum.srational: Pointer(this._offset, Array(this.length, SRational)),
    TagTypeEnum.float: Switch(this.length <= 2, {
        True: Peek(Array(this.length, Float)),
        False: Pointer(this._offset, Array(this.length, Float)),
    }),
    TagTypeEnum.double: Switch(this.length <= 1, {
        True: Peek(Array(this.length, Double)),
        False: Pointer(this._offset, Array(this.length, Double)),
    }),
    TagTypeEnum.undefined: Pointer(this._offset, Bytes(8)),
})

Tag = Struct(
    "_endian" / Computed(this._._endian),
    "enum" / TagEnum,
    "type" / TagTypeEnum,
    "length" / Int32,
    "_offset" / Int32,
    Seek(-4, 1),
    "data" / TagValue,
    Seek(4, 1),
)


@FuncPath
def subifd_offsets(tags):
    for t in tags:
        if str(t.enum) == "sub_ifd":
            return t.data
    return []


IFD = Struct(
    "_endian" / Computed(this._._endian),
    "items" / Int16, 
    "tags" / Array(this.items, Tag),
    "subifd_offsets" / Computed(subifd_offsets(this.tags)),
)


@FuncPath
def cal_endian(id):
    if id == b"\x4d\x4d\x00\x2a":
        return DNG_ENDIAN_HE
    else:
        return DNG_ENDIAN_LE

DNG = Struct(
    "id" / Bytes(4),
    "_endian" / Computed(cal_endian(this.id)),
    "ifd_offset" / Int32,
    Seek(this.ifd_offset),
    "ifd0" / IFD,

    # todo: using list with dynamic size instead.
    # Just workaround for this._index can't using as list indices.
    "subifd0" / If(len_(this.ifd0.subifd_offsets) > 0,
                   Pointer(this.ifd0.subifd_offsets[0], IFD)),
    "subifd1" / If(len_(this.ifd0.subifd_offsets) > 1,
                   Pointer(this.ifd0.subifd_offsets[1], IFD)),
    "subifd2" / If(len_(this.ifd0.subifd_offsets) > 2,
                   Pointer(this.ifd0.subifd_offsets[2], IFD)),
    "subifd3" / If(len_(this.ifd0.subifd_offsets) > 3,
                   Pointer(this.ifd0.subifd_offsets[3], IFD)),
)

class TAGParser(object):
    def _translate(self,tag):
        self.enum = tag.enum
        self.type = tag.type
        self.offset = tag._offset
        self.data = tag.data
        self.len = tag.length

    def __init__(self,tag):
        self._translate(tag)

    def _brief(self):
        s = "%s : " %(self.enum)
        if self.type == TagTypeEnum.byte or self.type == TagTypeEnum.word or self.type == TagTypeEnum.dword:
            s += "".join("%d, " % v for v in self.data[:10])[:-2]
            if self.len > 10:
                s += "..."
        elif self.type == TagTypeEnum.float or self.type == TagTypeEnum.double:
            s += "".join("%f, " % v for v in self.data[:6])[:-2]
            if self.len > 6:
                s += "..."
        elif self.type == TagTypeEnum.string or self.type == TagTypeEnum.undefined:
            s += self.data.decode("ascii")[:30]
            if self.len > 30:
                s += "..."
        elif self.type == TagTypeEnum.rational or self.type == TagTypeEnum.srational:
            s += "".join("%.3f, " % (d.a / d.b) for d in self.data[:6])[:-2]
            if self.len > 6:
                s += "..."
        return s
    
    def __str__(self):
        return "%s : %s" %(self.enum, self.data)
        

class IFDParser(object):
    # translate construct object to dict
    def _translate(self, ifd):
        self.dict = {}
        self.tags = [TAGParser(t) for t in ifd.tags]

    def __init__(self, ifd):
        self._translate(ifd)

    def __str__(self):
        return "TAGS:\n" + "".join("%s \n" % t._brief() for t in self.tags) 


class DNGParser(object):
    def __init__(self, filename):
        self._dng = DNG.parse_file(filename)
        self.ifd0 = IFDParser(self._dng.ifd0)
        self.subifds = []
        for i in range(3):
            ifd = getattr(self._dng, "subifd%d"%(i))
            if ifd == None:
                break
            self.subifds.append(IFDParser(ifd))
    
    def __str__(self):
        s = "================================================================\n"
        s += "[IFD0]\n"
        s += "================================================================\n"
        s += str(self.ifd0)

        for i, ifd in enumerate(self.subifds):
            s += "================================================================\n"
            s += "[SUBIFD{0}]\n".format(i)
            s += "================================================================\n"
            s += str(ifd)
        return s

