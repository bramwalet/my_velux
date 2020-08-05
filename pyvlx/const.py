"""Module for enum and consts."""

from enum import Enum


class Command(Enum):
    """Enum class for GW Command bytes."""

    # pylint: disable=invalid-name

    GW_ERROR_NTF = 0x0000
    GW_REBOOT_REQ = 0x0001
    GW_REBOOT_CFM = 0x0002

    GW_SET_FACTORY_DEFAULT_REQ = 0x0003
    GW_SET_FACTORY_DEFAULT_CFM = 0x0004

    GW_GET_VERSION_REQ = 0x0008
    GW_GET_VERSION_CFM = 0x0009

    GW_GET_PROTOCOL_VERSION_REQ = 0x000A
    GW_GET_PROTOCOL_VERSION_CFM = 0x000B

    GW_GET_STATE_REQ = 0x000C
    GW_GET_STATE_CFM = 0x000D

    GW_LEAVE_LEARN_STATE_REQ = 0x000E
    GW_LEAVE_LEARN_STATE_CFM = 0x000F

    GW_GET_NETWORK_SETUP_REQ = 0x00E0
    GE_GET_NETWORK_SETUP_CFM = 0x00E1
    GW_SET_NETWORK_SETUP_REQ = 0x00E2
    GE_SET_NETWORK_SETUP_CFM = 0x00E3

    GW_CS_GET_SYSTEMTABLE_DATQ_REQ = 0x0100
    GW_CS_GET_SYSTEMTABLE_DATA_CFM = 0x0101
    GW_CS_GET_SYSTEMTABLE_DATA_NTF = 0x0102

    GW_CS_DISCOVER_NODES_REQ = 0x0103
    GW_CS_DISCOVER_NODES_CFM = 0x0104
    GW_CS_DISCOVER_NODES_NTF = 0x0105

    GW_CS_REMOVE_NODES_REQ = 0x0106
    GW_CS_REMOVE_NODES_CFM = 0x0107

    GW_CS_VIRGIN_STATE_REQ = 0x0108
    GW_CS_VIRGIN_STATE_CFM = 0x0109

    GW_CS_CONTROLLER_COPY_REQ = 0x010A
    GW_CS_CONTROLLER_COPY_CFM = 0x010B
    GW_CS_CONTROLLER_COPY_NTF = 0x010C
    GW_CS_CONTROLLER_COPY_CANCEL_NTF = 0x010D

    GW_CS_RECEIVE_KEY_REQ = 0x010E
    GW_CS_RECEIVE_KEY_CFM = 0x010F
    GW_CS_RECEIVE_KEY_NTF = 0x0110

    GW_CS_PGC_JOB_NTF = 0x0111
    GW_CS_SYSTEM_TABLE_UPDATE_NTF = 0x0112
    GW_CS_GENERATE_NEW_KEY_REQ = 0x0113
    GW_CS_GENERATE_NEW_KEY_CFM = 0x0114
    GW_CS_GENERATE_NEW_KEY_NTF = 0x0115

    GW_CS_REPAIR_KEY_REQ = 0x0116
    GW_CS_REPAIR_KEY_CFM = 0x0117
    GW_CS_REPAID_KEY_NTF = 0x0118

    GW_CS_ACTIVATE_CONFIGURATION_MODE_REQ = 0x0119
    GW_CS_ACTIVATE_CONFIGURATION_MODE_CFM = 0x011A

    GW_GET_NODE_INFORMATION_REQ = 0x0200
    GW_GET_NODE_INFORMATION_CFM = 0x0201
    GW_GET_NODE_INFORMATION_NTF = 0x0210

    GW_GET_ALL_NODES_INFORMATION_REQ = 0x0202
    GW_GET_ALL_NODES_INFORMATION_CFM = 0x0203
    GW_GET_ALL_NODES_INFORMATION_NTF = 0x0204
    GW_GET_ALL_NODES_INFORMATION_FINISHED_NTF = 0x0205

    GW_SET_NODE_VARIATION_REQ = 0x0206
    GW_SET_NODE_VARIATION_CFM = 0x0207

    GW_SET_NODE_NAME_REQ = 0x0208
    GW_SET_NODE_NAME_CFM = 0x0209

    GW_SET_NODE_VELOCITY_REQ = 0x020A
    GW_SET_NODE_VELOCITY_CFM = 0x020B

    GW_NODE_INFORMATION_CHANGED_NTF = 0x020C

    GW_NODE_STATE_POSITION_CHANGED_NTF = 0x0211

    GW_SET_NODE_ORDER_AND_PLACEMENT_REQ = 0x020D
    GW_SET_NODE_ORDER_AND_PLACEMENT_CFM = 0x020E

    GW_GET_GROUP_INFORMATION_REQ = 0x0220
    GW_GET_GROUP_INFORMATION_CFM = 0x0221
    GW_GET_GROUP_INFORMATION_NTF = 0x0230

    GW_SET_GROUP_INFORMATION_REQ = 0x0222
    GW_SET_GROUP_INFORMATION_CFM = 0x0223

    GW_GROUP_INFORMATION_CHANGED_NTF = 0x0224

    GW_DELETE_GROUP_REQ = 0x0225
    GW_DELETE_GROUP_CFM = 0x0226

    GW_NEW_GROUP_REQ = 0x0227
    GW_NEW_GROUP_CFM = 0x0228

    GW_GET_ALL_GROUPS_INFORMATION_REQ = 0x0229
    GW_GET_ALL_GROUPS_INFORMATION_CFM = 0x022A
    GW_GET_ALL_GROUPS_INFORMATION_NTF = 0x022B

    GW_GET_ALL_GROUPS_INFORMATION_FINISHED_NTF = 0x022C

    GW_GROUP_DELETED_NTF = 0x022D

    GW_HOUSE_STATUS_MONITOR_ENABLE_REQ = 0x0240
    GW_HOUSE_STATUS_MONITOR_ENABLE_CFM = 0x0241

    GW_HOUSE_STATUS_MONITOR_DISABLE_REQ = 0x0242
    GW_HOUSE_STATUS_MONITOR_DISABLE_CFM = 0x0243

    GW_COMMAND_SEND_REQ = 0x0300
    GW_COMMAND_SEND_CFM = 0x0301
    GW_COMMAND_RUN_STATUS_NTF = 0x0302
    GW_COMMAND_REMAINING_TIME_NTF = 0x0303
    GW_SESSION_FINISHED_NTF = 0x0304

    GW_STATUS_REQUEST_REQ = 0x0305
    GW_STATUS_REQUEST_CFM = 0x0306
    GW_STATUS_REQUEST_NTF = 0x0307

    GW_WINK_SEND_REQ = 0x0308
    GW_WINK_SEND_CFM = 0x0309
    GW_WINK_SEND_NTF = 0x030A

    GW_SET_LIMITATION_REQ = 0x0310
    GW_SET_LIMITATION_CFM = 0x0311
    GW_GET_LIMITATION_STATUS_REQ = 0x0312
    GW_GET_LIMITATION_STATUS_CFM = 0x0313
    GW_LIMITATION_STATUS_NTF = 0x0314

    GW_MODE_SEND_REQ = 0x0320
    GW_MODE_SEND_CFM = 0x0321
    GW_MODE_SEND_NTF = 0x0322

    GW_INITIALIZE_SCENE_REQ = 0x0400
    GW_INITIALIZE_SCENE_CFM = 0x0401
    GW_INITIALIZE_SCENE_NTF = 0x0402
    GW_INITIALIZE_SCENE_CANCEL_REQ = 0x0403
    GW_INITIALIZE_SCENE_CANCEL_CFM = 0x0404
    GW_RECORD_SCENE_REQ = 0x0405
    GW_RECORD_SCENE_CFM = 0x0406
    GW_RECORD_SCENE_NTF = 0x0407

    GW_DELETE_SCENE_REQ = 0x0408
    GW_DELETE_SCENE_CFM = 0x0409

    GW_RENAME_SCENE_REQ = 0x040A
    GW_RENAME_SCENE_CFM = 0x040B

    GW_GET_SCENE_LIST_REQ = 0x040C
    GW_GET_SCENE_LIST_CFM = 0x040D
    GW_GET_SCENE_LIST_NTF = 0x040E

    GW_GET_SCENE_INFORMATION_REQ = 0x040F
    GW_GET_SCENE_INFORMATION_CFM = 0x0410
    GW_GET_SCENE_INFORMATION_NTF = 0x0411

    GW_ACTIVATE_SCENE_REQ = 0x0412
    GW_ACTIVATE_SCENE_CFM = 0x0413

    GW_STOP_SCENE_REQ = 0x0415
    GW_STOP_SCENE_CFM = 0x0416

    GW_SCENE_INFORMATION_CHANGED_NTF = 0x0419

    GW_ACTIVATE_PRODUCTGROUP_REQ = 0x0447
    GW_ACTIVATE_PRODUCTGROUP_CFM = 0x0448
    GW_ACTIVATE_PRODUCTGROUP_NTF = 0x0449

    GW_GET_CONTACT_INPUT_LINK_LIST_REQ = 0x0460
    GW_GET_CONTACT_INPUT_LINK_LIST_CFM = 0x0461

    GW_SET_CONTACT_INPUT_LINK_REQ = 0x0462
    GW_SET_CONTACT_INPUT_LINK_CFM = 0x0463

    GW_REMOVE_CONTACT_INPUT_LINK_REQ = 0x0464
    GW_REMOVE_CONTACT_INPUT_LINK_CFM = 0x0465

    GW_GET_ACTIVATION_LOG_HEADER_REQ = 0x0500
    GW_GET_ACTIVATION_LOG_HEADER_CFM = 0x0501

    GW_CLEAR_ACTIVATION_LOG_REQ = 0x0502
    GW_CLEAR_ACTIVATION_LOG_CFM = 0x0503

    GW_GET_ACTIVATION_LOG_LINE_REQ = 0x0504
    GW_GET_ACTIVATION_LOG_LINE_CFM = 0x0505

    GW_ACTIVATION_LOG_UPDATED_NTF = 0x0506

    GW_GET_MULTIPLE_ACTIVATION_LOG_LINES_REQ = 0x0507
    GW_GET_MULTIPLE_ACTIVATION_LOG_LINES_NTF = 0x0508
    GW_GET_MULTIPLE_ACTIVATION_LOG_LINES_CFN = 0x0509

    GW_SET_UTC_REQ = 0x2000
    GW_SET_UTC_CFM = 0x2001

    GW_RTC_SET_TIME_ZONE_REQ = 0x2002
    GW_RTC_SET_TIME_ZONE_CFM = 0x2003

    GW_GET_LOCAL_TIME_REQ = 0x2004
    GW_GET_LOCAL_TIME_CFM = 0x2005

    GW_PASSWORD_ENTER_REQ = 0x3000
    GW_PASSWORD_ENTER_CFM = 0x3001

    GW_PASSWORD_CHANGE_REQ = 0x3002
    GW_PASSWORD_CHANGE_CFM = 0x3003
    GW_PASSWORD_CHANGED_NTF = 0x3004


class Originator(Enum):
    """Enum class for originator."""

    USER = 1
    RAIN = 2
    TIMER = 3
    UPS = 5  # UPC unit
    SAAC = 8  # Stand Alone Automatic Controls
    WIND = 9
    LOAD_SHEDDING = 11
    LOCAL_LIGHT = 12
    UNSPECIFIC_ENVIRONMENT_SENSOR = 13
    EMERGENCY = 255


class Priority(Enum):
    """Enum class for priority."""

    PROTECTION_HUMAN = 0
    PROTECTION_ENVIRONMENT = 1
    USER_LEVEL_1 = 2
    USER_LEVEL_2 = 3
    COMFORT_LEVEL_1 = 4
    COMFORT_LEVEL_2 = 5
    COMFORT_LEVEL_3 = 6
    COMFORT_LEVEL_4 = 7


class Velocity(Enum):
    """Enum class for velocity."""

    DEFAULT = 0
    SILENT = 1
    FAST = 2
    NOT_AVAILABLE = 255


class NodeTypeWithSubtype(Enum):
    """Enum class for node type plus sub type combined values."""

    # pylint: disable=invalid-name
    NO_TYPE = 0
    INTERIOR_VENETIAN_BLIND = 0x0040
    ROLLER_SHUTTER = 0x0080
    ADJUSTABLE_SLUTS_ROLLING_SHUTTER = 0x0081
    ADJUSTABLE_SLUTS_ROLLING_SHUTTER_WITH_PROJECTION = 0x0082
    VERTICAL_EXTERIOR_AWNING = 0x00C0
    WINDOW_OPENER = 0x0100
    WINDOW_OPENER_WITH_RAIN_SENSOR = 0x0101
    GARAGE_DOOR_OPENER = 0x0140
    LINAR_ANGULAR_POSITION_OF_GARAGE_DOOR = 0x017A
    LIGHT = 0x0180
    LIGHT_ON_OFF = 0x01BA
    GATE_OPENER = 0x01C0
    GATE_OPENER_ANGULAR_POSITION = 0x01FA
    DOOR_LOCK = 0x0240
    WINDOW_LOCK = 0x0241
    VERTICAL_INTERIOR_BLINDS = 0x0280
    DUAL_ROLLER_SHUTTER = 0x0340
    ON_OFF_SWITCH = 0x03C0
    HORIZONTAL_AWNING = 0x0400
    EXTERIOR_VENETIAN_BLIND = 0x0440
    LOUVER_BLIND = 0x0480
    CURTAIN_TRACK = 0x04C0
    VENTILATION_POINT = 0x0500
    VENTILATION_POINT_AIR_INLET = 0x0502
    VENTILATION_POINT_AIR_TRANSFER = 0x0503
    VENTILATION_POINT_AIR_OUTLET = 0x0503
    EXTERIOR_HEATING = 0x0540
    SWINGING_SHUTTERS = 0x0600
    SWINGING_SHUTTER_WITH_INDEPENDENT_LEAVES = 0x0601
    BLADE_OPENER = 0x0740


class NodeType(Enum):
    """Enum class for node types."""

    NO_TYPE = 0
    VENETIAN_BLIND = 1
    ROLLER_SHUTTER = 2
    AWNING = 3
    WINDOW_OPENER = 4
    GARAGE_OPENER = 5
    LIGHT = 6
    GATE_OPENER = 7
    ROLLING_DOOR_OPENER = 8
    LOCK = 9
    BLIND = 10
    SECURE_CONFIGURATION_DEVICE = 11
    BEACON = 12
    DUAL_SHUTTER = 13
    HEATING_TEMPERATURE_INTERFACE = 14
    ON_OFF_SWITCH = 15
    HORIZONTAL_AWNING = 16
    EXTERNAL_VENETIAN_BLIND = 17
    LOUVRE_BLINT = 18
    CURTAIN_TRACK = 19
    VENTILATION_POINT = 20
    EXTERIOR_HEATING = 21
    HEAT_PUMP = 22
    INTRUSION_ALARM = 23
    SWINGING_SHUTTER = 24


class NodeVariation(Enum):
    """Enum class for node variations."""

    NOT_SET = 0
    TOPHUNG = 1
    KIP = 2
    FLAT_ROOT = 3
    SKY_LIGHT = 3
