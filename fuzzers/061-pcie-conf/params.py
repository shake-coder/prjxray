#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017-2020  The Project X-Ray Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

boolean_params = [
    ("AER_CAP_ECRC_CHECK_CAPABLE", 1),
    ("AER_CAP_ECRC_GEN_CAPABLE", 1),
    ("AER_CAP_PERMIT_ROOTERR_UPDATE", 1),
    ("AER_CAP_ON", 1),
    ("AER_CAP_MULTIHEADER", 1),
    ("CMD_INTX_IMPLEMENTED", 1),
    ("CPL_TIMEOUT_DISABLE_SUPPORTED", 1),
    ("DEV_CAP2_ARI_FORWARDING_SUPPORTED", 1),
    ("DEV_CAP2_ATOMICOP_ROUTING_SUPPORTED", 1),
    ("DEV_CAP2_ATOMICOP32_COMPLETER_SUPPORTED", 1),
    ("DEV_CAP2_ATOMICOP64_COMPLETER_SUPPORTED", 1),
    ("DEV_CAP2_CAS128_COMPLETER_SUPPORTED", 1),
    ("DEV_CAP2_NO_RO_ENABLED_PRPR_PASSING", 1),
    ("DEV_CAP2_LTR_MECHANISM_SUPPORTED", 1),
    ("DEV_CAP2_EXTENDED_FMT_FIELD_SUPPORTED", 1),
    ("DEV_CAP2_ENDEND_TLP_PREFIX_SUPPORTED", 1),
    ("ENDEND_TLP_PREFIX_FORWARDING_SUPPORTED", 1),
    ("DEV_CAP_ENABLE_SLOT_PWR_LIMIT_SCALE", 1),
    ("DEV_CAP_ENABLE_SLOT_PWR_LIMIT_VALUE", 1),
    ("DEV_CAP_EXT_TAG_SUPPORTED", 1),
    ("DEV_CAP_FUNCTION_LEVEL_RESET_CAPABLE", 1),
    ("DEV_CAP_ROLE_BASED_ERROR", 1),
    ("DEV_CONTROL_AUX_POWER_SUPPORTED", 1),
    ("DEV_CONTROL_EXT_TAG_DEFAULT", 1),
    ("DSN_CAP_ON", 1),
    ("INTERRUPT_STAT_AUTO", 1),
    ("IS_SWITCH", 1),
    ("LINK_CAP_CLOCK_POWER_MANAGEMENT", 1),
    ("LINK_CAP_DLL_LINK_ACTIVE_REPORTING_CAP", 1),
    ("LINK_CAP_LINK_BANDWIDTH_NOTIFICATION_CAP", 1),
    ("LINK_CAP_ASPM_OPTIONALITY", 1),
    ("LINK_CAP_SURPRISE_DOWN_ERROR_CAPABLE", 1),
    ("LINK_CTRL2_DEEMPHASIS", 1),
    ("LINK_CTRL2_HW_AUTONOMOUS_SPEED_DISABLE", 1),
    ("LINK_STATUS_SLOT_CLOCK_CONFIG", 1),
    ("MPS_FORCE", 1),
    ("MSI_CAP_64_BIT_ADDR_CAPABLE", 1),
    ("MSI_CAP_ON", 1),
    ("MSI_CAP_PER_VECTOR_MASKING_CAPABLE", 1),
    ("MSIX_CAP_ON", 1),
    ("PCIE_CAP_ON", 1),
    ("PCIE_CAP_SLOT_IMPLEMENTED", 1),
    ("PM_CAP_D1SUPPORT", 1),
    ("PM_CAP_D2SUPPORT", 1),
    ("PM_CAP_DSI", 1),
    ("PM_CAP_ON", 1),
    ("PM_CAP_PME_CLOCK", 1),
    ("PM_CSR_B2B3", 1),
    ("PM_CSR_BPCCEN", 1),
    ("PM_CSR_NOSOFTRST", 1),
    ("RBAR_CAP_ON", 1),
    ("ROOT_CAP_CRS_SW_VISIBILITY", 1),
    ("SELECT_DLL_IF", 1),
    ("SLOT_CAP_ATT_BUTTON_PRESENT", 1),
    ("SLOT_CAP_ATT_INDICATOR_PRESENT", 1),
    ("SLOT_CAP_ELEC_INTERLOCK_PRESENT", 1),
    ("SLOT_CAP_HOTPLUG_CAPABLE", 1),
    ("SLOT_CAP_HOTPLUG_SURPRISE", 1),
    ("SLOT_CAP_MRL_SENSOR_PRESENT", 1),
    ("SLOT_CAP_NO_CMD_COMPLETED_SUPPORT", 1),
    ("SLOT_CAP_POWER_CONTROLLER_PRESENT", 1),
    ("SLOT_CAP_POWER_INDICATOR_PRESENT", 1),
    ("SSL_MESSAGE_AUTO", 1),
    ("VC_CAP_ON", 1),
    ("VC_CAP_REJECT_SNOOP_TRANSACTIONS", 1),
    ("VSEC_CAP_IS_LINK_VISIBLE", 1),
    ("VSEC_CAP_ON", 1),
    ("LL_ACK_TIMEOUT_EN", 1),
    ("LL_REPLAY_TIMEOUT_EN", 1),
    ("PM_ASPML0S_TIMEOUT_EN", 1),
    ("PM_ASPM_FASTEXIT", 1),
    ("DISABLE_LANE_REVERSAL", 1),
    ("DISABLE_SCRAMBLING", 1),
    ("ENTER_RVRY_EI_L0", 1),
    ("ALLOW_X8_GEN2", 1),
    ("PL_FAST_TRAIN", 1),
    ("UPCONFIG_CAPABLE", 1),
    ("UPSTREAM_FACING", 1),
    ("EXIT_LOOPBACK_ON_EI", 1),
    ("DISABLE_ASPM_L1_TIMER", 1),
    ("DISABLE_BAR_FILTERING", 1),
    ("DISABLE_ID_CHECK", 1),
    ("DISABLE_RX_TC_FILTER", 1),
    ("DISABLE_RX_POISONED_RESP", 1),
    ("ENABLE_RX_TD_ECRC_TRIM", 1),
    ("TL_TFC_DISABLE", 1),
    ("TL_TX_CHECKS_DISABLE", 1),
    ("TL_RBYPASS", 1),
    ("DISABLE_PPM_FILTER", 1),
    ("DISABLE_LOCKED_FILTER", 1),
    ("USE_RID_PINS", 1),
    ("DISABLE_ERR_MSG", 1),
    ("PM_MF", 1),
    ("VC0_CPL_INFINITE", 1),
    ("RECRC_CHK_TRIM", 1),
    ("TECRC_EP_INV", 1),
    ("UR_INV_REQ", 1),
    ("UR_PRS_RESPONSE", 1),
    ("UR_ATOMIC", 1),
    ("UR_CFG1", 1),
    ("TRN_DW", 1),
    ("TRN_NP_FC", 1),
    ("USER_CLK2_DIV2", 1),
]

hex_params = [
    ("AER_CAP_ID", 16),
    ("AER_CAP_VERSION", 4),
    ("AER_BASE_PTR", 12),
    ("AER_CAP_NEXTPTR", 12),
    ("AER_CAP_OPTIONAL_ERR_SUPPORT", 16),
    ("BAR0", 16),
    ("BAR1", 16),
    ("BAR2", 16),
    ("BAR3", 16),
    ("BAR4", 16),
    ("BAR5", 16),
    ("EXPANSION_ROM", 16),
    ("CAPABILITIES_PTR", 8),
    ("CARDBUS_CIS_POINTER", 16),
    ("CLASS_CODE", 16),
    ("CPL_TIMEOUT_RANGES_SUPPORTED", 4),
    ("DEV_CAP2_TPH_COMPLETER_SUPPORTED", 2),
    ("DEV_CAP2_MAX_ENDEND_TLP_PREFIXES", 2),
    ("DSN_BASE_PTR", 12),
    ("DSN_CAP_ID", 16),
    ("DSN_CAP_NEXTPTR", 12),
    ("DSN_CAP_VERSION", 4),
    ("EXT_CFG_CAP_PTR", 6),
    ("EXT_CFG_XP_CAP_PTR", 10),
    ("HEADER_TYPE", 8),
    ("INTERRUPT_PIN", 8),
    ("LAST_CONFIG_DWORD", 10),
    ("LINK_CAP_MAX_LINK_SPEED", 4),
    ("LINK_CTRL2_TARGET_LINK_SPEED", 4),
    ("MSI_BASE_PTR", 8),
    ("MSI_CAP_ID", 8),
    ("MSI_CAP_NEXTPTR", 8),
    ("MSIX_BASE_PTR", 8),
    ("MSIX_CAP_ID", 8),
    ("MSIX_CAP_NEXTPTR", 8),
    ("MSIX_CAP_PBA_OFFSET", 16),
    ("MSIX_CAP_TABLE_OFFSET", 16),
    ("MSIX_CAP_TABLE_SIZE", 11),
    ("PCIE_BASE_PTR", 8),
    ("PCIE_CAP_CAPABILITY_ID", 8),
    ("PCIE_CAP_CAPABILITY_VERSION", 4),
    ("PCIE_CAP_DEVICE_PORT_TYPE", 4),
    ("PCIE_CAP_NEXTPTR", 8),
    ("PM_BASE_PTR", 8),
    ("PM_CAP_ID", 8),
    ("PM_CAP_NEXTPTR", 8),
    ("PM_CAP_PMESUPPORT", 5),
    ("PM_DATA_SCALE0", 2),
    ("PM_DATA_SCALE1", 2),
    ("PM_DATA_SCALE2", 2),
    ("PM_DATA_SCALE3", 2),
    ("PM_DATA_SCALE4", 2),
    ("PM_DATA_SCALE5", 2),
    ("PM_DATA_SCALE6", 2),
    ("PM_DATA_SCALE7", 2),
    ("PM_DATA0", 8),
    ("PM_DATA1", 8),
    ("PM_DATA2", 8),
    ("PM_DATA3", 8),
    ("PM_DATA4", 8),
    ("PM_DATA5", 8),
    ("PM_DATA6", 8),
    ("PM_DATA7", 8),
    ("RBAR_BASE_PTR", 12),
    ("RBAR_CAP_NEXTPTR", 12),
    ("RBAR_CAP_ID", 16),
    ("RBAR_CAP_VERSION", 4),
    ("RBAR_NUM", 3),
    ("RBAR_CAP_SUP0", 16),
    ("RBAR_CAP_SUP1", 16),
    ("RBAR_CAP_SUP2", 16),
    ("RBAR_CAP_SUP3", 16),
    ("RBAR_CAP_SUP4", 16),
    ("RBAR_CAP_SUP5", 16),
    ("RBAR_CAP_INDEX0", 3),
    ("RBAR_CAP_INDEX1", 3),
    ("RBAR_CAP_INDEX2", 3),
    ("RBAR_CAP_INDEX3", 3),
    ("RBAR_CAP_INDEX4", 3),
    ("RBAR_CAP_INDEX5", 3),
    ("RBAR_CAP_CONTROL_ENCODEDBAR0", 5),
    ("RBAR_CAP_CONTROL_ENCODEDBAR1", 5),
    ("RBAR_CAP_CONTROL_ENCODEDBAR2", 5),
    ("RBAR_CAP_CONTROL_ENCODEDBAR3", 5),
    ("RBAR_CAP_CONTROL_ENCODEDBAR4", 5),
    ("RBAR_CAP_CONTROL_ENCODEDBAR5", 5),
    ("SLOT_CAP_PHYSICAL_SLOT_NUM", 13),
    ("SLOT_CAP_SLOT_POWER_LIMIT_VALUE", 8),
    ("VC_BASE_PTR", 12),
    ("VC_CAP_NEXTPTR", 12),
    ("VC_CAP_ID", 16),
    ("VSEC_BASE_PTR", 12),
    ("VSEC_CAP_HDR_ID", 16),
    ("VSEC_CAP_HDR_LENGTH", 12),
    ("VSEC_CAP_HDR_REVISION", 4),
    ("VSEC_CAP_ID", 16),
    ("VSEC_CAP_NEXTPTR", 12),
    ("VSEC_CAP_VERSION", 4),
    ("CRM_MODULE_RSTS", 7),
    ("LL_ACK_TIMEOUT", 15),
    ("LL_REPLAY_TIMEOUT", 15),
    ("PM_ASPML0S_TIMEOUT", 15),
    ("INFER_EI", 5),
    ("LINK_CAP_MAX_LINK_WIDTH", 6),
    ("LTSSM_MAX_LINK_WIDTH", 6),
    ("DNSTREAM_LINK_NUM", 8),
    ("ENABLE_MSG_ROUTE", 11),
    ("VC_CAP_VERSION", 4),
    ("VC0_RX_RAM_LIMIT", 13),
    ("RP_AUTO_SPD", 2),
    ("RP_AUTO_SPD_LOOPCNT", 5),
    ("SPARE_BYTE0", 8),
    ("SPARE_BYTE1", 8),
    ("SPARE_BYTE2", 8),
    ("SPARE_BYTE3", 8),
    ("SPARE_WORD0", 16),
    ("SPARE_WORD1", 16),
    ("SPARE_WORD2", 16),
    ("SPARE_WORD3", 16),
]

int_params = [
    ("DEV_CAP_ENDPOINT_L0S_LATENCY", 3),
    ("DEV_CAP_ENDPOINT_L1_LATENCY", 3),
    ("DEV_CAP_MAX_PAYLOAD_SUPPORTED", 3),
    ("DEV_CAP_PHANTOM_FUNCTIONS_SUPPORT", 2),
    ("DEV_CAP_RSVD_14_12", 3),
    ("DEV_CAP_RSVD_17_16", 2),
    ("DEV_CAP_RSVD_31_29", 3),
    ("LINK_CAP_ASPM_SUPPORT", 2),
    ("LINK_CAP_L0S_EXIT_LATENCY_COMCLK_GEN1", 3),
    ("LINK_CAP_L0S_EXIT_LATENCY_COMCLK_GEN2", 3),
    ("LINK_CAP_L0S_EXIT_LATENCY_GEN1", 3),
    ("LINK_CAP_L0S_EXIT_LATENCY_GEN2", 3),
    ("LINK_CAP_L1_EXIT_LATENCY_COMCLK_GEN1", 3),
    ("LINK_CAP_L1_EXIT_LATENCY_COMCLK_GEN2", 3),
    ("LINK_CAP_L1_EXIT_LATENCY_GEN1", 3),
    ("LINK_CAP_L1_EXIT_LATENCY_GEN2", 3),
    ("LINK_CAP_RSVD_23", 1),
    ("LINK_CONTROL_RCB", 1),
    ("MSI_CAP_MULTIMSG_EXTENSION", 1),
    ("MSI_CAP_MULTIMSGCAP", 3),
    ("MSIX_CAP_PBA_BIR", 3),
    ("MSIX_CAP_TABLE_BIR", 3),
    ("PCIE_CAP_RSVD_15_14", 2),
    ("PCIE_REVISION", 4),
    ("PM_CAP_AUXCURRENT", 3),
    ("PM_CAP_RSVD_04", 1),
    ("PM_CAP_VERSION", 3),
    ("SLOT_CAP_SLOT_POWER_LIMIT_SCALE", 2),
    ("USER_CLK_FREQ", 3),
    ("LL_ACK_TIMEOUT_FUNC", 2),
    ("LL_REPLAY_TIMEOUT_FUNC", 2),
    ("PM_ASPML0S_TIMEOUT_FUNC", 2),
    ("N_FTS_COMCLK_GEN1", 8),
    ("N_FTS_COMCLK_GEN2", 8),
    ("N_FTS_GEN1", 8),
    ("N_FTS_GEN2", 8),
    ("PL_AUTO_CONFIG", 3),
    ("TL_RX_RAM_RADDR_LATENCY", 1),
    ("TL_RX_RAM_RDATA_LATENCY", 2),
    ("TL_RX_RAM_WRITE_LATENCY", 1),
    ("TL_TX_RAM_RADDR_LATENCY", 1),
    ("TL_TX_RAM_RDATA_LATENCY", 2),
    ("TL_TX_RAM_WRITE_LATENCY", 1),
    ("VC0_TOTAL_CREDITS_CD", 11),
    ("VC0_TOTAL_CREDITS_CH", 7),
    ("VC0_TOTAL_CREDITS_NPH", 7),
    ("VC0_TOTAL_CREDITS_NPD", 11),
    ("VC0_TOTAL_CREDITS_PD", 11),
    ("VC0_TOTAL_CREDITS_PH", 7),
    ("VC0_TX_LASTPACKET", 5),
    ("RECRC_CHK", 2),
    ("CFG_ECRC_ERR_CPLSTAT", 2),
    ("SPARE_BIT0", 1),
    ("SPARE_BIT1", 1),
    ("SPARE_BIT2", 1),
    ("SPARE_BIT3", 1),
    ("SPARE_BIT4", 1),
    ("SPARE_BIT5", 1),
    ("SPARE_BIT6", 1),
    ("SPARE_BIT7", 1),
    ("SPARE_BIT8", 1),
]
