from SheetCode import Sheet
sheet = Sheet(__file__)

sheet.Name = "Inspection of RBC Static XML"
sheet.Description =["Inspection of parameter values in RBC Datapreparation."
                    "Whenever possible, a functional tests is performed through other test sheets.",
                    "When not possible, an inspection of the parameter value is realized.",
                    "Also, we check that parameters related to unused functions are set to default values and to 'N_of' parameters are set to 0."]

sheet.StartConditions = ["n.a."]

# ---------------------------------------------------------------------------------------------------------------------------------------------
sheet.Case("Miscellaneous parameters")

sheet.Action("Inspect RBC static.xml")
sheet.ExpectedResult("Nmax_n_iter_packet_21 = 31",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00678]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/sizing_parameters/Nmax_n_iter_packet_21"])
sheet.ExpectedResult("Nmax_n_iter_packet_27 = 31",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00255]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/sizing_parameters/Nmax_n_iter_packet_27"])
sheet.ExpectedResult("Nmax_n_iter = Nmax_n_iter_packet_27 + 1 = 28",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00259]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/sizing_parameters/Nmax_n_iter"])
sheet.ExpectedResult("MA_sending_on_path_extension = TRUE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00271]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/MA_sending_on_path_extension"])
sheet.ExpectedResult("path_extension_on_MA_request = FALSE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00272]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/path_extension_on_MA_request"])
sheet.ExpectedResult("path_extend_only_when_position_report_validated = TRUE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00273]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/Path_Extend_Only_When_Position_Report_Validated"])
sheet.ExpectedResult("Nmax_path_blocks = 5",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00274]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/Nmax_path_blocks"])
sheet.ExpectedResult("track_occupation_available = TRUE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00275]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/track_occupation_available"])
sheet.ExpectedResult("use_proximity_window_for_permissive_block = TRUE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00278]",
                                    "[L161_ETCS2-TRK_sSyRS_00688]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/use_proximity_window_for_permissive_block"])
sheet.ExpectedResult("start_on_new_balise_group = TRUE for all PBG (Point Balise Groups)",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00365]"],
                    parameters = ["Route_Map/RM_RTM_layer/balise_groups/balise_group/start_on_new_balise_group"])
sheet.ExpectedResult("ignore_cnn_locking_under_train = TRUE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00687]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/ignore_cnn_locking_under_train"])
sheet.ExpectedResult("For all Mode Profiles, MP_activation_status = DISABLED",
                    parameters = ["Route_Map/RM_operational_conditions_layer/MPs/MP/MP_activation_status"])
sheet.ExpectedResult("min_track_ahead_free_distance = max_track_ahead_free_distance = 150 m, for all main stopping point connections, except for L1 S3, L2 S1 and the signal leading to L2 S1",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00146]",
                                    "[L161_ETCS2-TRK_sSyRS_00147]"],
                    parameters = ["Route_Map/RM_interlocking_layer/TAF_windows/TAF_window/min_track_ahead_free_distance",
                                  "Route_Map/RM_interlocking_layer/TAF_windows/TAF_window/max_track_ahead_free_distance"])
sheet.ExpectedResult("min_track_ahead_free_distance = max_track_ahead_free_distance = 0 m, for main stopping point connections associated to L1 S3, L2 S1 and the signal leading to L2 S1",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00146]",
                                    "[L161_ETCS2-TRK_sSyRS_00148]"],
                    parameters = ["Route_Map/RM_interlocking_layer/TAF_windows/TAF_window/min_track_ahead_free_distance",
                                  "Route_Map/RM_interlocking_layer/TAF_windows/TAF_window/max_track_ahead_free_distance"])
sheet.ExpectedResult("ATAF_allowed = TRUE for all main stoppng point connection, except for L1 S3, L2 S1 and the signal leading to L2 S1",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00149]"],
                    parameters = ["Route_Map/RM_interlocking_layer/TAF_windows/TAF_window/ATAF_allowed"])
sheet.ExpectedResult("TAF_request_only_for_SB_PT_train_in_TAF_window = FALSE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00151]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/TAF_request_only_for_SB_PT_train_in_TAF_window"])
sheet.ExpectedResult("CES_ignored_if_entering_train = FALSE for all main stopping point connection",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00580]"],
                    parameters = ["Route_Map/RM_interlocking_layer/connections/connection/CES_ignored_if_entering_train"])

# ---------------------------------------------------------------------------------------------------------------------------------------------
sheet.Case("Entry boundaries")

sheet.Action("Inspect RBC static.xml")
sheet.ExpectedResult("Each BG-A and BG-A' is defined as an instance of <entry_balise_group/id>",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00515]"],
                    parameters = ["Route_Map/RM_RTM_layer/balise_groups/entry_balise_group/id"])
sheet.ExpectedResult("Each BG-A' is defined as an instance of <balise_group/id>",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00516]"],
                    parameters = ["Route_Map/RM_RTM_layer/balise_groups/balise_group/id"])
sheet.ExpectedResult("A buffer stop is placed on the single node upstream of each L2 entry boundary",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00517]"],
                    parameters = ["Route_Map/RM_civil_characteristics_layer/buffer_stops/buffer_stop/location/offset",
                                  "Route_Map/RM_civil_characteristics_layer/buffer_stops/buffer_stop/location/segment_id"])
sheet.ExpectedResult("Each BG located between BG-A' and the L2 entry border is defined as an instance of <balise_group/id>",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00520]"],
                    parameters = ["Route_Map/RM_RTM_layer/balise_groups/balise_group/id"])
sheet.ExpectedResult("Not point is located between BG-A and the L2 entry boundary, meaning that <Referential/Route/Points> is empty",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00521]"])
sheet.ExpectedResult("The BG-A and BG-A' associated to each boundary are not associated to another boundary",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00522]",
                                    "[L161_ETCS2-TRK_sSyRS_00523]"])
sheet.ExpectedResult("All instances of <entry_balise_group/v_min> = 0",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00524]"],
                    parameters = ["Route_Map/RM_RTM_layer/balise_groups/entry_balise_group/v_min"])
sheet.ExpectedResult("<Packet_41_to_Entering_Train> = TRUE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00526]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/Packet_41_to_Entering_Train"])
sheet.ExpectedResult("All instances of <boundary/packet_9_used> = FALSE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00530]"],
                    parameters = ["Route_Map/RM_RTM_layer/boundaries/boundary/packet_9_used"])
sheet.ExpectedResult("No instance of <boundary/cancel_boundary_identity> exists",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00531]"],
                    parameters = ["Route_Map/RM_RTM_layer/boundaries/boundary/cancel_boundary_identity"])
sheet.ExpectedResult("<additional_conditions_to_cancel_entry> = FALSE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00532]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/additional_conditions_to_cancel_entry"])
sheet.ExpectedResult("<boundary/location> for entries are located exactly at the BG-T / N_PIG=0 location",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00537]"],
                    parameters = ["Route_Map/RM_RTM_layer/boundaries/boundary/location/offset",
                                  "Route_Map/RM_RTM_layer/boundaries/boundary/location/segment_id"])
sheet.ExpectedResult("Each BG-T is defined as an instance of <boundary/border_balise_group_id>",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00538]"],
                    parameters = ["Route_Map/RM_RTM_layer/boundaries/boundary/border_balise_group_id"])
sheet.ExpectedResult("Each entry boundary has <boundary_activation_status> = ENFORCED",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00546]"],
                    parameters = ["Route_Map/RM_RTM_layer/boundaries/boundary/boundary_activation_status"])
sheet.ExpectedResult("Outside responsibility profile is defined between each upstream single node and L2 boundary")
sheet.ExpectedResult("For each Outside responsibility profile <leaving_RBC_area> = FALSE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00547]"],
                    parameters = ["Route_Map/RM_RTM_layer/Outside_Responsibility_Profiles/Outside_Responsibility_Profile/leaving_RBC_area"])
sheet.ExpectedResult("<enhanced_ambiguous_resolution> = TRUE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00552]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/enhanced_ambiguous_resolution"])
sheet.ExpectedResult("<ignore_cnn_locking_under_train> = TRUE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00553]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/ignore_cnn_locking_under_train"])
sheet.ExpectedResult("<check_point_position_for_path_creation> = FALSE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00554]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/check_point_position_for_path_creation"])


# ---------------------------------------------------------------------------------------------------------------------------------------------
sheet.Case("Exit boundaries")

sheet.Action("Inspect RBC static.xml")
sheet.ExpectedResult("No exit boundaries are defined. Meaning no instance of boundary/boundary_type> = ENTRY",
                    requirements = ["[L161_ETCS2-TRK_SSyRS_00593]"],
                    parameters = ["Route_Map/RM_RTM_layer/boundaries/boundary/boundary_type"])
sheet.ExpectedResult("train_disconnection_on_lower_level_transition = TRUE",
                    requirements = ["[L161_ETCS2-TRK_SSyRS_00585]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/train_disconnection_on_lower_level_transition"])
sheet.ExpectedResult("A buffer stop is placed 2 meters downstream of the location of each L1 S3 signal",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00594]",
                                    "[L161_ETCS2-TRK_sSyRS_00595]",
                                    "[L161_ETCS2-TRK_sSyRS_00596]",
                                    "[L161_ETCS2-TRK_sSyRS_00599]"],
                    parameters = ["Route_Map/RM_civil_characteristics_layer/buffer_stops/buffer_stop/location/offset",
                                  "Route_Map/RM_civil_characteristics_layer/buffer_stops/buffer_stop/location/segment_id"])
sheet.ExpectedResult("The stopping point and danger points associated to each L1 S3 signal is located exactly at the signal",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00597]"])
sheet.ExpectedResult("For the connection associated to each L1 S3 signal, Route_Map/RM_interlocking_layer/connections/connection/locking_status = UNLOCKED",
                    requirements = ["[L161_ETCS2-TRK_SSyRS_00598]"])

# ---------------------------------------------------------------------------------------------------------------------------------------------
sheet.Case("Inspection of RBC parameters linked to VIP")

sheet.Action("Inspect RBC static.xml")

sheet.ExpectedResult("<Nmax_virtual_information_point> = Count of <Referential/Route/PlainTextMessagePacket>",
                    parameters = ["Route_Map/RM_operational_conditions_layer/virtual_information_points/Nmax_virtual_information_point"])
sheet.ExpectedResult("<virtual_information_point/VIP_applicability> = ALL_TRAINS", 
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00487]"],
                    parameters = ["Route_Map/RM_operational_conditions_layer/virtual_information_points/virtual_information_point/VIP_applicability"])
sheet.ExpectedResult("<virtual_information_point/activation_status> = DISABLED (by default)",
                    parameters = ["Route_Map/RM_operational_conditions_layer/virtual_information_points/virtual_information_point/activation_status"])
sheet.ExpectedResult("<virtual_information_point/N_VIP_train_category> = 0",
                    parameters = ["Route_Map/RM_operational_conditions_layer/virtual_information_points/virtual_information_point/N_VIP_train_category"])

# ---------------------------------------------------------------------------------------------------------------------------------------------
sheet.Case("Inspection of RBC parameters linked to Emergency detectors")

sheet.Action("Inspect RBC static.xml")

sheet.ExpectedResult("For each non-controlled main stop signal including L1S1 and L1S2, but excluding L2S1, a Emergency detector is set at the signal location in the route direction.",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00196]"],
                    parameters = ["Route_Map/RM_operational_conditions_layer/emergency_detectors/emergency_detector/location/offset",
                                  "Route_Map/RM_operational_conditions_layer/emergency_detectors/emergency_detector/location/segment_id"])

sheet.ExpectedResult("<emergency_detector/only_applicable_to_electric_train> = FALSE", 
                    parameters = [ "Route_Map/RM_operational_conditions_layer/emergency_detectors/emergency_detector/only_applicable_to_electric_train"])

sheet.ExpectedResult("<emergency_detector/Nmax_emergency_detector> = Count of <Referential/Route/EmergencyDetectors>", 
                    parameters = ["Route_Map/RM_operational_conditions_layer/emergency_detectors/Nmax_emergency_detector"])

# ---------------------------------------------------------------------------------------------------------------------------------------------
sheet.Case("Inspection of RBC parameters linked to Start of Mission")

sheet.Action("Inspect RBC static.xml")

sheet.ExpectedResult("<shunting_request_always_accepted> = TRUE",
                    requirements = ["[L161_ETCS2-TRK_sSyRS_00107]"],
                    parameters = ["Customization_Data/RBC_configuration_layer/ERTMS_system_parameters/shunting_request_always_accepted"])

# ---------------------------------------------------------------------------------------------------------------------------------------------
sheet.Case("Unused functions")

sheet.Save()